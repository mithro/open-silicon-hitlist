#!/usr/bin/env python3
"""Regenerate the README list, the "How the items connect" section, each
project's id-prefixed title and its "Where it sits", "Resources" and "Related
items" sections, and docs.json, all from items.json.

Usage: python3 tools/build.py [--doc-sections OUT.json]
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOC_URL = "https://claude.ai/code/artifact/"
REPO_URL = "https://github.com/mithro/open-silicon-hitlist/blob/main/"
LAYERS = [("pdk", "PDK"), ("tooling", "Tooling"), ("ip", "IP"), ("silicon", "Proof in silicon")]
FUNCTIONS = [("interface", "Interface"), ("computation", "Computation"), ("storage", "Storage"), ("all", "Cross-cutting")]
TARGETS = [("asic", "ASIC"), ("fpga", "FPGA"), ("both", "ASIC and FPGA")]


def load():
    with open(os.path.join(ROOT, "items.json")) as f:
        return json.load(f)


def related_md(data, item_id, for_doc):
    items = {i["id"]: i for i in data["items"]}
    me = items[item_id]
    lines = ["## Related items", ""]
    for other, note in data["related"].get(item_id, []):
        o = items[other]
        if for_doc:
            link = DOC_URL + o["doc"]
        else:
            link = os.path.relpath(o["path"], os.path.dirname(me["path"]))
        lines.append(f"- [{other}]({link}) ({o['title']}): {note}.")
    return "\n".join(lines)


def layers_of(item):
    return item["layer"] if isinstance(item["layer"], list) else [item["layer"]]


def frame_md(data, item_id, for_doc):
    """The "Where it sits" and "Resources" sections."""
    items = {i["id"]: i for i in data["items"]}
    me = items[item_id]
    layer = " and ".join(dict(LAYERS)[l] for l in layers_of(me))
    out = ["## Where it sits", "",
           f"Layer: **{layer}**. Function: **{me['function'].replace('all', 'cross-cutting')}**. Target: **{dict(TARGETS)[me['target']]}**. {me['frame']}"]
    if me.get("resources"):
        link = REPO_URL + me["resources"] if for_doc else os.path.relpath(me["resources"], os.path.dirname(me["path"]))
        out += ["", "## Resources", "", f"Loose collection of links for fleshing this item out: [{me['resources']}]({link})."]
    return "\n".join(out)


def strip_section(text, heading):
    """Remove a "## heading" section, including an empty one at the end of the file."""
    return re.sub(r"\n## " + re.escape(heading) + r"[ \t]*(?:\n.*?)?(?=\n## |\Z)", "", text, flags=re.S)


def heading(item, text):
    """The file's H1 without any id prefix."""
    h1 = text.split("\n", 1)[0][2:]
    return h1.split(": ", 1)[1] if h1.startswith(item["id"] + ": ") else h1


def update_project(data, item):
    path = os.path.join(ROOT, item["path"])
    with open(path) as f:
        text = f.read().rstrip("\n")
    title = heading(item, text)
    text = f"# {item['id']}: {title}\n" + text.split("\n", 1)[1]
    for h in ("Where it sits", "Resources", "Related items"):
        text = strip_section(text, h)
    text = text.rstrip("\n") + "\n\n" + frame_md(data, item["id"], for_doc=False)
    text += "\n\n" + related_md(data, item["id"], for_doc=False) + "\n"
    with open(path, "w") as f:
        f.write(text)
    return f"{item['id']}: {title}"


def list_md(data, for_doc):
    rows = ["| Id | Project | One-line goal |", "| --- | --- | --- |"]
    for i in data["items"]:
        link = DOC_URL + i["doc"] if for_doc else i["path"]
        title = i["title"] if for_doc else f"{i['title']} ([doc]({DOC_URL + i['doc']}))"
        rows.append(f"| [{i['id']}]({link}) | {title} | {i['goal']} |")
    return "\n".join(rows) + "\n\nIds are stable names for each item; the order of the table carries no meaning."


def groups_md(data, for_doc):
    def ids(pred):
        found = [i["id"] for i in data["items"] if pred(i)]
        return ", ".join(found) if for_doc else ", ".join(f"[{x}](projects/{x}.md)" for x in found)

    out = ["## How the items connect", "",
           "Each item lists its closest neighbours under \"Related items\". At a higher level, the items sit in the layers you need to make a chip, with FPGA work alongside ASIC work:", "",
           "| Layer | ASIC | FPGA | Both |", "| --- | --- | --- | --- |"]
    for lk, ln in LAYERS:
        cells = [ids(lambda i, t=tk: lk in layers_of(i) and i["target"] == t) for tk, _ in TARGETS]
        out.append(f"| {ln} | " + " | ".join(cells) + " |")
    out += ["", "For FPGAs the analogy is direct: the device database (bitstream-atlas) plays the PDK's role.", "",
            "By what a chip does, the same items cover:", "",
            "| Layer | " + " | ".join(fn for _, fn in FUNCTIONS) + " |", "| --- |" + " --- |" * len(FUNCTIONS)]
    for lk, ln in LAYERS:
        cells = [ids(lambda i, f=fk: lk in layers_of(i) and f in i["function"]) for fk, _ in FUNCTIONS]
        out.append(f"| {ln} | " + " | ".join(cells) + " |")
    out += ["", "What the grid shows:", ""] + [f"- {g}" for g in data["gaps"]]
    return "\n".join(out)


def update_readme(data):
    path = os.path.join(ROOT, "README.md")
    with open(path) as f:
        text = f.read()
    text = re.sub(r"(## The list\n\n).*?(?=\n## )", lambda m: m.group(1) + list_md(data, False) + "\n", text, flags=re.S)
    text = strip_section(text, "How the items connect")
    text = text.replace("\n## Candidates", "\n" + groups_md(data, False) + "\n\n## Candidates", 1)
    with open(path, "w") as f:
        f.write(text)


def write_docs_json(data):
    docs = {data["overview"]["path"]: {"doc_id": data["overview"]["doc"], "body_node_id": data["overview"]["doc_node"],
                                       "url": DOC_URL + data["overview"]["doc"]}}
    for i in data["items"]:
        docs[i["path"]] = {"id": i["id"], "doc_id": i["doc"], "body_node_id": i["doc_node"], "url": DOC_URL + i["doc"]}
    # Non-item documents (GUIDELINES.md, TEMPLATE.md, PROCESS.md, ...): carried in docs.json only,
    # never rewritten by update_project. An entry without a doc yet is skipped.
    for d in data.get("docs", []):
        if d.get("doc"):
            docs[d["path"]] = {"doc_id": d["doc"], "body_node_id": d.get("doc_node"), "url": DOC_URL + d["doc"]}
    with open(os.path.join(ROOT, "docs.json"), "w") as f:
        json.dump(docs, f, indent=2)
        f.write("\n")


def main():
    data = load()
    titles = {i["id"]: update_project(data, i) for i in data["items"]}
    update_readme(data)
    write_docs_json(data)
    if len(sys.argv) == 3 and sys.argv[1] == "--doc-sections":
        out = {i["id"]: {"title": titles[i["id"]], "related": related_md(data, i["id"], for_doc=True),
                        "frame": frame_md(data, i["id"], for_doc=True)} for i in data["items"]}
        out["_list"] = list_md(data, True)
        out["_groups"] = groups_md(data, True)
        with open(sys.argv[2], "w") as f:
            json.dump(out, f, indent=1, ensure_ascii=False)


if __name__ == "__main__":
    main()
