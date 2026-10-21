#!/usr/bin/env python3
"""Render every Mermaid block of markdown files to PNG, so a reviewer can look at each diagram.

Usage: python3 tools/render-diagrams.py OUTDIR FILE... [--mermaid PATH/TO/mermaid.min.js]

Writes OUTDIR/<file>-<line>.html and OUTDIR/<file>-<line>.png per ```mermaid block and prints each
diagram's size, or NO SVG with the page errors. Needs node with the playwright package, a Chromium
that playwright can find, and a local copy of mermaid.min.js (the mermaid npm package's dist/ file).
"""
import argparse
import html
import json
import os
import re
import subprocess
import sys

SHOT_JS = r"""
const { chromium } = require('playwright');
const fs = require('fs'); const path = require('path');
(async () => {
  const dir = process.argv[2];
  const names = JSON.parse(fs.readFileSync(path.join(dir, 'list.json')));
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1400, height: 900 }, deviceScaleFactor: 1 });
  const errors = [];
  page.on('pageerror', e => errors.push(String(e)));
  page.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
  for (const n of names) {
    await page.goto('file://' + path.join(dir, n + '.html'), { waitUntil: 'networkidle' });
    await page.waitForTimeout(1500);
    const el = await page.$('pre.mermaid svg');
    if (!el) { console.log(n, 'NO SVG', errors.slice(-3)); continue; }
    const box = await el.boundingBox();
    await el.screenshot({ path: path.join(dir, n + '.png') });
    console.log(n, 'ok', Math.round(box.width) + 'x' + Math.round(box.height));
  }
  await browser.close();
})();
"""

# display:block keeps the SVG at full width; with inline-block it collapses to 300 px.
PAGE = """<!doctype html><html><head><meta charset="utf-8">
<script src="file://{mjs}"></script>
<style>body{{margin:16px;background:#fff;font-family:sans-serif}} pre.mermaid{{display:block;width:1300px}}</style>
</head><body><pre class="mermaid">{graph}</pre>
<script>mermaid.initialize({{startOnLoad: true}});</script></body></html>"""


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("outdir")
    ap.add_argument("files", nargs="+")
    ap.add_argument("--mermaid", default="node_modules/mermaid/dist/mermaid.min.js")
    args = ap.parse_args()
    if not os.path.exists(args.mermaid):
        sys.exit(f"mermaid.min.js not found at {args.mermaid}; pass --mermaid")
    outdir = os.path.abspath(args.outdir)
    os.makedirs(outdir, exist_ok=True)
    names = []
    for f in args.files:
        text = open(f).read()
        for m in re.finditer(r"```mermaid\n(.*?)```", text, re.S):
            name = f"{os.path.splitext(os.path.basename(f))[0]}-{text[:m.start()].count(chr(10)) + 1}"
            with open(os.path.join(outdir, name + ".html"), "w") as out:
                out.write(PAGE.format(mjs=os.path.abspath(args.mermaid), graph=html.escape(m.group(1))))
            names.append(name)
    json.dump(names, open(os.path.join(outdir, "list.json"), "w"))
    if not names:
        print("no Mermaid blocks")
        return
    shot = os.path.join(outdir, "shot.js")
    open(shot, "w").write(SHOT_JS)
    sys.exit(subprocess.call(["node", shot, outdir]))


if __name__ == "__main__":
    main()
