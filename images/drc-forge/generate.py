#!/usr/bin/env python3
"""Draw the generated figures of projects/drc-forge.md as SVG.

Usage: python3 images/drc-forge/generate.py   (writes the .svg files next to this script)
The PNGs beside them are screenshots of these SVGs (tools/render-diagrams.py's Chromium).
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
INK, MUTED, METAL, FAIL, PASS, BG = "#1f2328", "#59636e", "#8c959f", "#cf222e", "#1a7f37", "#ffffff"
FONT = 'font-family="Helvetica, Arial, sans-serif"'


def svg(w, h, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">'
            f'<rect width="{w}" height="{h}" fill="{BG}"/>{body}</svg>\n')


def text(x, y, s, size=15, fill=INK, anchor="middle", weight="normal"):
    return f'<text x="{x}" y="{y}" {FONT} font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}">{s}</text>'


def arrow_h(x1, x2, y):
    # a dimension line with arrow heads at both ends
    return (f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{INK}" stroke-width="1.5"/>'
            f'<path d="M{x1},{y} l8,-5 v10 z M{x2},{y} l-8,-5 v10 z" fill="{INK}"/>')


def three_cases():
    # One width rule, three test layouts: one grid step under the limit, at it, one step over.
    cases = [("limit − 5 nm", 92, "fails: one width marker", FAIL),
             ("limit", 110, "passes: no width marker", PASS),
             ("limit + 5 nm", 128, "passes: no width marker", PASS)]
    body, x0 = [], 40
    for i, (label, w, verdict, col) in enumerate(cases):
        cx = x0 + 120 + i * 260
        body.append(f'<rect x="{cx - w / 2}" y="70" width="{w}" height="170" fill="{METAL}" stroke="{INK}" stroke-width="1"/>')
        body.append(arrow_h(cx - w / 2, cx + w / 2, 55))
        body.append(text(cx, 40, f"width = {label}", 15))
        body.append(text(cx, 272, verdict, 16, col, weight="bold"))
        body.append(text(cx, 296, f"test layout {i + 1} of 3", 13, MUTED))
    body.append(text(400, 330, "widths exaggerated; the real step is one 5 nm grid step", 13, MUTED))
    return svg(800, 345, "".join(body))


def halo():
    # Left: a tile of edge T read with a halo of width h on every side.
    b = []
    ox, oy, T, h = 70, 80, 160, 45
    b.append(f'<rect x="{ox - h}" y="{oy - h}" width="{T + 2 * h}" height="{T + 2 * h}" fill="#eaeef2" stroke="{MUTED}" stroke-dasharray="6,4"/>')
    b.append(f'<rect x="{ox}" y="{oy}" width="{T}" height="{T}" fill="{METAL}" stroke="{INK}"/>')
    b.append(text(ox + T / 2, oy + T / 2 - 6, "tile", 16, BG, weight="bold"))
    b.append(text(ox + T / 2, oy + T / 2 + 14, "markers reported", 13, BG))
    b.append(arrow_h(ox, ox + T, oy + T + h + 22))
    b.append(text(ox + T / 2, oy + T + h + 44, "T", 15, weight="bold"))
    b.append(arrow_h(ox + T, ox + T + h, oy - h + 18))
    b.append(text(ox + T + h / 2, oy - h + 12, "h", 15, weight="bold"))
    b.append(text(ox + T / 2, oy - h - 12, "halo: read; markers clipped to the tile", 13, MUTED))
    # Right: the halo factor (1 + 2h/T)^2 against T, h = 700 um, log axis 0.5 to 30 mm.
    import math
    px, py, pw, ph = 420, 50, 340, 230
    hmm, lo, hi, ymax = 0.7, 0.5, 30.0, 20.0

    def X(t):
        return px + pw * (math.log10(t) - math.log10(lo)) / (math.log10(hi) - math.log10(lo))

    def Y(f):
        return py + ph * (1 - (math.log10(f)) / math.log10(ymax))
    b.append(f'<line x1="{px}" y1="{py + ph}" x2="{px + pw}" y2="{py + ph}" stroke="{INK}"/>')
    b.append(f'<line x1="{px}" y1="{py}" x2="{px}" y2="{py + ph}" stroke="{INK}"/>')
    for t in (0.5, 1, 2, 5, 10, 26):
        b.append(f'<line x1="{X(t)}" y1="{py + ph}" x2="{X(t)}" y2="{py + ph + 5}" stroke="{INK}"/>')
        b.append(text(X(t), py + ph + 20, f"{t:g}", 12))
    for f in (1, 2, 5, 10, 20):
        b.append(f'<line x1="{px - 5}" y1="{Y(f)}" x2="{px}" y2="{Y(f)}" stroke="{INK}"/>')
        b.append(text(px - 9, Y(f) + 4, f"{f:g}", 12, anchor="end"))
    b.append(text(px + pw / 2, py + ph + 42, "tile edge T (mm, log scale)", 13))
    b.append(f'<text x="{px - 40}" y="{py + ph / 2}" {FONT} font-size="13" fill="{INK}" text-anchor="middle" '
             f'transform="rotate(-90 {px - 40} {py + ph / 2})">work per tile ÷ work without halo (log)</text>')
    pts, t = [], lo
    while t <= hi * 1.0001:
        pts.append(f"{X(t):.1f},{Y((1 + 2 * hmm / t) ** 2):.1f}")
        t *= 1.03
    b.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{INK}" stroke-width="2"/>')
    # the factor reaches 2 at T = 2h / (sqrt(2) - 1)
    t2 = 2 * hmm / (math.sqrt(2) - 1)
    b.append(f'<line x1="{px}" y1="{Y(2)}" x2="{X(t2)}" y2="{Y(2)}" stroke="{MUTED}" stroke-dasharray="4,3"/>')
    b.append(f'<line x1="{X(t2)}" y1="{Y(2)}" x2="{X(t2)}" y2="{py + ph}" stroke="{MUTED}" stroke-dasharray="4,3"/>')
    for t, lab in ((1, "1 mm: 5.76"), (t2, "3.4 mm: 2"), (26, "26 mm: 1.11")):
        f = (1 + 2 * hmm / t) ** 2
        b.append(f'<circle cx="{X(t)}" cy="{Y(f)}" r="4.5" fill="{INK}"/>')
        b.append(text(X(t) + (10 if t < 20 else 0), Y(f) - (10 if t < 20 else 30), lab, 13, INK, anchor="start" if t < 20 else "end", weight="bold"))
    b.append(text(px + pw / 2, py - 18, "halo factor (1 + 2h/T)², h = 700 µm", 14, weight="bold"))
    return svg(800, 340, "".join(b))


for name, fn in (("generated-three-test-layouts", three_cases), ("generated-tile-halo", halo)):
    with open(os.path.join(HERE, name + ".svg"), "w") as fh:
        fh.write(fn())
    print(name)
