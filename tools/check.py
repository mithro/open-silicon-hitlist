#!/usr/bin/env python3
"""Lint an item document against TEMPLATE.md and GUIDELINES.md (checks L1 to L19).

Usage: python3 tools/check.py projects/<id>.md [more files] [--deny FILE] [--signoff FILE] [--fetch]
                              [--template TEMPLATE.md]

The heading set, sub-headings, bold lead-ins, workstream lines, milestone lines, First tasks
fields and Agent digest lines are read from the template, so the lint follows template changes.
The generated tail that tools/build.py appends ("Where it sits", "Resources", "Related items")
is not part of the hand-written document and is skipped.

--deny FILE     private list of strings that must never appear (one per line, # comments).
                Never commit it. Matches are reported by entry number, not by text.
--signoff FILE  private list of "(from Tim's unpublished notes)" sentences Tim has signed off.
--fetch         fetch every link (L15), caching results per day under ~/.cache/hitlist-check.

Exit status is 1 if any check fails; warnings alone exit 0.
"""
import argparse
import datetime
import glob
import json
import os
import re
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENERATED = ["Where it sits", "Resources", "Related items"]
STATUS_WORDS = {"active", "quiet", "inactive", "archived", "moved"}
PLACEHOLDERS = ["YYYY-MM-DD", "<id>", "<Title>", "<name>", "…", "TODO"]
MARKERS = [r"\(unverified\)", r"\(staging note", r"\(thin:", r"\[S\d+\]"]
STATUS_RE = re.compile(
    r"^\*Status: (draft \d+|stable draft|reviewed), \d{4}-\d{2}-\d{2}\. "
    r"AI review panel: ([^.]+)\. Human review: (none|Tim, \d{4}-\d{2}-\d{2})\. "
    r"Questions for Tim: (\d+)\. This document was drafted and reviewed with AI agents; "
    r"human review is recorded here\.\*$")
LINK_RE = re.compile(r"\]\((https?://[^)\s]+)\)")
DRIVE_RE = re.compile(r"https?://(?:docs|drive)\.google\.com/[^)\s>]+")
DRIVE_ID_RE = re.compile(r"/d/([A-Za-z0-9_-]{20,})|[?&]id=([A-Za-z0-9_-]{20,})")
DOI_RE = re.compile(r"\b10\.\d{4,9}/[^\s)\]]+")
ARXIV_RE = re.compile(r"\b(?:arXiv:)?(\d{4}\.\d{4,5})(?:v\d+)?\b")
REPO_RE = re.compile(r"https?://(?:github\.com|gitlab\.com|codeberg\.org)/([\w.-]+/[\w.-]+)")


class Report:
    def __init__(self, path):
        self.path, self.fails, self.warns = path, [], []

    def fail(self, check, line, msg):
        self.fails.append((check, line, msg))

    def warn(self, check, line, msg):
        self.warns.append((check, line, msg))

    def print(self):
        for level, rows in (("FAIL", self.fails), ("WARN", self.warns)):
            for check, line, msg in sorted(rows, key=lambda r: (r[0], r[1] or 0)):
                loc = f"{self.path}:{line}" if line else self.path
                print(f"{level} {check} {loc}: {msg}")


# ---------------------------------------------------------------- parsing

def split_sections(lines):
    """[(level, title, start_index)] for ## and ### headings, ignoring fenced code."""
    out, fence = [], False
    for n, line in enumerate(lines):
        if line.startswith("```"):
            fence = not fence
        elif not fence:
            m = re.match(r"^(#{2,3}) (.*)$", line)
            if m:
                out.append((len(m.group(1)), m.group(2), n))
    return out


def section_body(lines, heads, title, level=2):
    """Lines of a section up to the next heading of the same or higher level."""
    for k, (lv, t, start) in enumerate(heads):
        if lv == level and t.strip() == title:
            end = len(lines)
            for lv2, _, s2 in heads[k + 1:]:
                if lv2 <= level:
                    end = s2
                    break
            return start, lines[start + 1:end]
    return None, None


def is_guidance(line):
    return re.match(r"^>\s*\*", line) is not None


def lead_ins(body):
    return [m.group(1) for m in (re.match(r"^\*\*([^*<]+?\.)\*\*", l) for l in body) if m]


def keys_of(block):
    return [m.group(1) for m in (re.match(r"^- ([A-Z][A-Za-z /]+?):", l) for l in block) if m]


class Template:
    def __init__(self, path):
        lines = open(path).read().splitlines()
        heads = split_sections(lines)
        self.h2 = [t for lv, t, _ in heads if lv == 2]
        self.h3, self.leads = {}, {}
        for title in self.h2:
            start, body = section_body(lines, heads, title)
            self.h3[title] = [t for lv, t, s in heads if lv == 3 and start < s < start + 1 + len(body)]
            self.leads[title] = [l for l in lead_ins(body) if not re.match(r"^(W\d|M\d)", l)]
        _, ws = section_body(lines, heads, "Workstreams", 3)
        block = ws[ws.index(next(l for l in ws if l.startswith("**W1"))):]
        keys = keys_of(block)
        self.ws_optional = [k for k in keys if any(f"- {k}" in l and "optional" in l.lower() or
                                                    f"- {k} (" in l for l in block)]
        self.ws_required = [k for k in keys if k not in self.ws_optional]
        _, ms = section_body(lines, heads, "Milestones", 3)
        self.milestones = {}
        cur = None
        for l in ms:
            m = re.match(r"^\*\*(M\d) ", l)
            if m:
                cur = m.group(1)
                self.milestones[cur] = []
            elif cur and l.startswith("- "):
                self.milestones[cur].append(l[2:].split(":")[0])
        _, ft = section_body(lines, heads, "First tasks", 3)
        self.task_fields = re.findall(r"(?:\*\*\.|\.) ([A-Z][A-Za-z ]+?):", next(l for l in ft if l.startswith("1.")))
        _, dg = section_body(lines, heads, "Agent digest", 3)
        self.digest = keys_of(dg)
        self.optional_h2 = {"Questions for Tim"}


# ---------------------------------------------------------------- checks

def words(text):
    text = re.sub(r"\]\([^)]*\)", "]", text)
    return len(text.split())


def hand_written(lines):
    """Index of the first generated heading, or len(lines)."""
    for n, line in enumerate(lines):
        if line.startswith("## ") and line[3:].strip() in GENERATED:
            return n
    return len(lines)


def load_related(item_id):
    try:
        data = json.load(open(os.path.join(ROOT, "items.json")))
    except OSError:
        return None
    return {other for other, _ in data.get("related", {}).get(item_id, [])}


def resource_text():
    return "\n".join(open(p).read() for p in glob.glob(os.path.join(ROOT, "resources", "*.md")))


def fetch_ok(url, cache):
    if url in cache:
        return cache[url]
    try:
        req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "hitlist-check"})
        try:
            code = urllib.request.urlopen(req, timeout=20).status
        except Exception:
            req = urllib.request.Request(url, headers={"User-Agent": "hitlist-check"})
            code = urllib.request.urlopen(req, timeout=20).status
        result = f"ok {code}"
    except Exception as e:
        result = f"error {getattr(e, 'code', '') or type(e).__name__}"
    cache[url] = result
    return result


def check(path, tpl, args):
    r = Report(os.path.relpath(path, os.getcwd()))
    all_lines = open(path).read().splitlines()
    end = hand_written(all_lines)
    lines = all_lines[:end]
    tail = all_lines[end:]
    heads = split_sections(lines)
    item_id = os.path.splitext(os.path.basename(path))[0]
    text = "\n".join(lines)

    # L1: heading set and order; generated tail only at the end, once each, in order.
    if not all_lines or not re.match(r"^# [a-z0-9-]+: \S", all_lines[0]):
        r.fail("L1", 1, "line 1 must be the title '# <id>: <Title>'")
    h2 = [t for lv, t, _ in heads if lv == 2]
    expected = [t for t in tpl.h2 if t in h2 or t not in tpl.optional_h2]
    if h2 != expected:
        r.fail("L1", None, f"## headings {h2} do not match the template order {expected}")
    for lv, t, n in heads:
        if t != t.rstrip():
            r.fail("L1", n + 1, "heading ends in whitespace")
    gen = [l[3:].strip() for l in tail if l.startswith("## ")]
    if gen and (len(gen) != len(set(gen)) or gen != [g for g in GENERATED if g in gen]):
        r.fail("L1", end + 1, f"generated sections duplicated or out of order: {gen}")
    if any(l.startswith("## ") and l[3:].strip() not in GENERATED for l in tail):
        r.fail("L1", end + 1, "hand-written heading after the generated tail")

    # L2: ### sub-headings per section.
    for title in tpl.h2:
        start, body = section_body(lines, heads, title)
        if body is None:
            continue
        got = [t for lv, t, s in heads if lv == 3 and start < s <= start + len(body)]
        if got != tpl.h3[title]:
            r.fail("L2", start + 1, f"'{title}' sub-headings {got} do not match {tpl.h3[title]}")

    # L3: guidance lines and placeholders. L12: working-draft markers.
    for n, line in enumerate(lines):
        if is_guidance(line):
            r.fail("L3", n + 1, "template guidance line left in")
        for p in PLACEHOLDERS:
            if p in line:
                r.fail("L3", n + 1, f"placeholder {p!r}")
        for m in MARKERS:
            if re.search(m, line):
                r.fail("L12", n + 1, f"working-draft marker {re.search(m, line).group(0)!r}")
    # Guidance lines are reported once, above; blank them so later checks do not count them.
    lines = ["" if is_guidance(l) else l for l in lines]
    text = "\n".join(lines)

    # L4: status line and question count.
    status = [(n, l) for n, l in enumerate(lines) if l.startswith("*Status:")]
    qstart, qbody = section_body(lines, heads, "Questions for Tim")
    entries = [l for l in (qbody or []) if re.match(r"^\d+\. ", l)]
    if len(status) != 1:
        r.fail("L4", None, f"expected one status line, found {len(status)}")
    else:
        n, l = status[0]
        m = STATUS_RE.match(l)
        if not m:
            r.fail("L4", n + 1, "status line does not match the GUIDELINES.md 4.1 grammar")
        elif int(m.group(4)) != len(entries):
            r.fail("L4", n + 1, f"status says {m.group(4)} questions, section has {len(entries)}")

    # L5: bold lead-ins, exact words, in each section.
    for title, wanted in tpl.leads.items():
        start, body = section_body(lines, heads, title)
        if body is None or not wanted:
            continue
        got = lead_ins(body)
        for w in wanted:
            if w not in got:
                r.fail("L5", start + 1, f"'{title}' is missing the lead-in **{w}**")

    # L6: workstream blocks and summary table.
    start, ws = section_body(lines, heads, "Workstreams", 3)
    blocks = []
    if ws is not None:
        for n, l in enumerate(ws):
            m = re.match(r"^\*\*(W\d+) ", l)
            if m:
                blocks.append([m.group(1), start + 2 + n, [l]])
            elif blocks and l.startswith("- "):
                blocks[-1][2].append(l)
        if not 3 <= len(blocks) <= 8:
            r.fail("L6", start + 1, f"{len(blocks)} workstreams; three to eight required")
        for wid, n, block in blocks:
            if "Produces:" not in block[0] or "Needed because:" not in block[0]:
                r.fail("L6", n, f"{wid} header needs 'Produces:' and 'Needed because:'")
            have = keys_of(block[1:])
            for k in tpl.ws_required:
                if k not in have:
                    r.fail("L6", n, f"{wid} is missing '{k}:'")
            if have and not re.search(r"\b[A-D]\b", next((l for l in block if l.startswith("- Fit:")), "")):
                r.fail("L6", n, f"{wid} Fit must be A, B, C or D")
    start, tbl = section_body(lines, heads, "Summary table", 3)
    if tbl is not None:
        rows = [re.match(r"^\|\s*(W\d+)\s*\|", l).group(1) for l in tbl if re.match(r"^\|\s*W\d+\s*\|", l)]
        if rows != [b[0] for b in blocks]:
            r.fail("L6", start + 1, f"summary rows {rows} do not match workstreams {[b[0] for b in blocks]}")

    # L7: milestone ladder.
    start, ms = section_body(lines, heads, "Milestones", 3)
    if ms is not None:
        found, cur = {}, None
        for n, l in enumerate(ms):
            m = re.match(r"^\*\*(M\d) ", l)
            if m:
                cur = m.group(1)
                found[cur] = (start + 2 + n, [], l)
            elif cur and l.startswith("- "):
                found[cur][1].append(l[2:].split(":")[0])
        for mid, wanted in tpl.milestones.items():
            if mid not in found:
                if not (mid == "M4" and re.search(r"Not applicable \(", "\n".join(ms))):
                    r.fail("L7", start + 1, f"{mid} missing")
                continue
            n, have, head = found[mid]
            if mid == "M4" and "Not applicable (" in head + "".join(have):
                continue
            for k in wanted:
                if k not in have:
                    r.fail("L7", n, f"{mid} is missing '{k}:'")

    # L8: length.
    body = [l for l in lines[1:] if not re.match(r"^\|[\s:|-]+\|$", l)]
    total = words("\n".join(body))
    if total > 7000:
        r.fail("L8", None, f"{total} words; the limit is 7,000")
    elif total > 6000 or total < 3000:
        r.warn("L8", None, f"{total} words; the band is 3,000 to 6,000")
    first_h2 = next((s for lv, _, s in heads if lv == 2), len(lines))
    summary = [l for l in lines[1:first_h2] if l.strip() and not l.startswith("*Status:")]
    sw = words(" ".join(summary))
    if not 60 <= sw <= 120:
        r.fail("L8", 2, f"summary is {sw} words; 60 to 120 required")
    if qbody is not None:
        qw = words("\n".join(qbody))
        if qw > 300 or len(entries) > 5:
            r.fail("L8", qstart + 1, f"Questions for Tim has {len(entries)} entries and {qw} words; max 5 and 300")

    # L9: Drive links must be in a resources file.
    res = resource_text()
    for n, line in enumerate(all_lines):
        for url in DRIVE_RE.findall(line):
            m = DRIVE_ID_RE.search(url)
            key = (m.group(1) or m.group(2)) if m else url
            if key not in res:
                r.fail("L9", n + 1, f"Drive link not in any resources/*.md: {url}")

    # L10: deny list (private). Report the entry number only.
    if args.deny:
        deny = [d.strip() for d in open(args.deny) if d.strip() and not d.startswith("#")]
        for n, line in enumerate(all_lines):
            for k, d in enumerate(deny, 1):
                if d.lower() in line.lower():
                    r.fail("L10", n + 1, f"matches deny-list entry {k}")

    # L11: Needs first / Unlocks on this list ids are in related.
    related = load_related(item_id)
    start, sbody = section_body(lines, heads, "What success unlocks")
    if sbody is not None and related is not None:
        cur = None
        for n, l in enumerate(sbody):
            m = re.match(r"^\*\*([^*]+?)\.\*\*", l)
            if m:
                cur = m.group(1)
            elif cur in ("Needs first", "Unlocks on this list"):
                for other in re.findall(r"^- \[([a-z0-9-]+)\]", l):
                    if other not in related:
                        r.fail("L11", start + 2 + n, f"{other} is not in items.json related for {item_id}")

    # L13: as-of months and status vocabulary.
    for title, level in (("State of the art", 2), ("Projects and code", 3)):
        start, b = section_body(lines, heads, title, level)
        if b is None:
            continue
        if not re.search(r"\bas of \d{4}-\d{2}\b", "\n".join(b)):
            r.fail("L13", start + 1, f"'{title}' has no 'as of YYYY-MM'")
        sub = b
        if title == "State of the art":
            s2, sub = section_body(lines, heads, "Open tools and projects", 3)
            sub = sub or []
        for l in sub:
            m = re.match(r"^- (?:\*\*[^*]+\*\* \(\[link\]\([^)]*\)\)|\[[^\]]+\]\([^)]*\)): (\w+)", l)
            if m and m.group(1).lower() not in STATUS_WORDS:
                r.fail("L13", None, f"status {m.group(1)!r} is not one of {sorted(STATUS_WORDS)}")

    # L14: Key papers identifiers; duplicates across the document.
    start, kp = section_body(lines, heads, "Key papers", 3)
    for n, l in enumerate(kp or []):
        if l.startswith("- ") and not (DOI_RE.search(l) or ARXIV_RE.search(l)):
            r.fail("L14", start + 2 + n, "Key papers entry without a DOI or arXiv identifier")
    seen = {}
    for n, line in enumerate(lines):
        ids = {d.rstrip(".,;").lower() for d in DOI_RE.findall(line)} | set(ARXIV_RE.findall(line))
        ids |= {"repo:" + m.lower().removesuffix(".git") for m in REPO_RE.findall(line)}
        for i in ids:
            if i in seen and seen[i] != n:
                r.fail("L14", n + 1, f"{i} also appears on line {seen[i] + 1}")
            seen.setdefault(i, n)

    # L15: fetch links.
    if args.fetch:
        cache_dir = os.path.expanduser("~/.cache/hitlist-check")
        os.makedirs(cache_dir, exist_ok=True)
        cache_path = os.path.join(cache_dir, f"{datetime.date.today()}.json")
        cache = json.load(open(cache_path)) if os.path.exists(cache_path) else {}
        for n, line in enumerate(lines):
            for url in LINK_RE.findall(line):
                result = fetch_ok(url, cache)
                if not result.startswith("ok"):
                    r.fail("L15", n + 1, f"{url}: {result}")
        json.dump(cache, open(cache_path, "w"), indent=1)

    # L16: First tasks fields.
    start, ft = section_body(lines, heads, "First tasks", 3)
    for n, l in enumerate(ft or []):
        if re.match(r"^\d+\. ", l):
            for f in tpl.task_fields:
                if f + ":" not in l:
                    r.fail("L16", start + 2 + n, f"First task is missing '{f}:'")
            if not re.search(r"Fit: A\b", l):
                r.fail("L16", start + 2 + n, "First task must be Fit: A")

    # L17: Agent digest.
    start, dg = section_body(lines, heads, "Agent digest", 3)
    if dg is not None:
        have = keys_of(dg)
        for k in tpl.digest:
            if k not in have:
                r.fail("L17", start + 1, f"Agent digest is missing '{k}:'")
        dw = words("\n".join(l for l in dg if l.startswith("- ")))
        if dw > 150:
            r.fail("L17", start + 1, f"Agent digest is {dw} words; max 150")

    # L18: unpublished-notes sentences need sign-off.
    marker = "(from Tim's unpublished notes)"
    signed = set()
    if args.signoff:
        signed = {" ".join(l.split()) for l in open(args.signoff) if l.strip()}
    for n, line in enumerate(lines):
        if marker in line:
            for sentence in re.split(r"(?<=[.!?])\s+", line):
                if marker in sentence and " ".join(sentence.lstrip("-* ").split()) not in signed:
                    r.fail("L18", n + 1, "unpublished-notes sentence not in the sign-off file")

    # L19: long sentences; heading case.
    for n, line in enumerate(lines):
        if line.startswith(("#", "|")):
            continue
        for sentence in re.split(r"(?<=[.!?])\s+", re.sub(r"\]\([^)]*\)", "]", line)):
            if len(sentence.split()) > 60:
                r.warn("L19", n + 1, f"sentence of {len(sentence.split())} words")
    template_words = {w for h in tpl.h2 + sum(tpl.h3.values(), []) for w in h.split()}
    for lv, t, n in heads:
        for w in t.split()[1:]:
            if w[0].isupper() and not w.isupper() and not any(c.isdigit() for c in w) and w not in template_words:
                r.warn("L19", n + 1, f"heading not in sentence case: {t!r}")
                break
    return r


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="+")
    ap.add_argument("--deny")
    ap.add_argument("--signoff")
    ap.add_argument("--fetch", action="store_true")
    ap.add_argument("--template", default=os.path.join(ROOT, "TEMPLATE.md"))
    args = ap.parse_args()
    tpl = Template(args.template)
    failed = False
    for path in args.files:
        rep = check(path, tpl, args)
        rep.print()
        failed |= bool(rep.fails)
        print(f"{rep.path}: {len(rep.fails)} failures, {len(rep.warns)} warnings")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
