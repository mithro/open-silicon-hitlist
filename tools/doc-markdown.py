#!/usr/bin/env python3
"""Turn a repository markdown file into the markdown of its living doc (SYNC.md, Links and anchors).

Usage: python3 tools/doc-markdown.py FILE [--extra PATH=DOC_ID ...] > out.md

The H1 is dropped (the doc has its own title and byline). Links outside fenced code are rewritten:
  a mirrored file (docs.json, or --extra for one not listed yet), with or without #anchor -> its living doc
  #anchor in the same file -> the file's own doc URL plus the anchor, when it has a doc (the docs
                              engine refuses one fill that carries many in-page links), else kept
  any other repository path -> the file on GitHub's main branch
The footer "Mirrored in git as FILE." ends every doc.
"""
import argparse
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOC_URL = "https://claude.ai/code/artifact/"
GITHUB = "https://github.com/mithro/open-silicon-hitlist/blob/main/"
LINK_RE = re.compile(r"\]\(([^)\s]+)\)")


def convert(path, doc_of):
    rel = os.path.relpath(os.path.abspath(path), ROOT)
    here = os.path.dirname(rel)
    lines = open(path).read().split("\n")
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
        while lines and not lines[0].strip():
            lines = lines[1:]

    def fix(m):
        target = m.group(1)
        if target.startswith("#"):
            return "](" + doc_of[rel] + target + ")" if rel in doc_of else m.group(0)
        if re.match(r"^(https?:|mailto:)", target):
            return m.group(0)
        file, _, frag = target.partition("#")
        frag = "#" + frag if frag else ""
        repo_path = os.path.normpath(os.path.join(here, file))
        if repo_path in doc_of:
            return "](" + doc_of[repo_path] + frag + ")"
        if os.path.exists(os.path.join(ROOT, repo_path)):
            return "](" + GITHUB + repo_path + frag + ")"
        sys.stderr.write(f"unresolved link target: {target}\n")
        return m.group(0)

    parts = re.split(r"(```.*?```)", "\n".join(lines), flags=re.S)
    for k in range(0, len(parts), 2):
        parts[k] = LINK_RE.sub(fix, parts[k])
    return "".join(parts).rstrip("\n") + f"\n\nMirrored in git as [{rel}]({GITHUB}{rel}).\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file")
    ap.add_argument("--extra", action="append", default=[], help="PATH=DOC_ID for a file not yet in docs.json")
    args = ap.parse_args()
    docs = json.load(open(os.path.join(ROOT, "docs.json")))
    doc_of = {p: v["url"] for p, v in docs.items() if v.get("doc_id")}
    for e in args.extra:
        p, d = e.split("=", 1)
        doc_of[p] = DOC_URL + d
    sys.stdout.write(convert(args.file, doc_of))


if __name__ == "__main__":
    main()
