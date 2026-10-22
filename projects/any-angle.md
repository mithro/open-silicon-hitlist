# any-angle: Non-rectilinear layout tooling

## Goal

An open ASIC layout stack that is not tied to the Manhattan grid: design rules, cells, placement, routing, extraction and checking that work with hexagonal, octagonal, diagonal and curved geometry. The aim is to find out, with real tools and real numbers, what the industry gave up by optimising everything around right angles, and to make the alternatives usable: more pin access points per cell, any-angle or X/Y-direction wiring, and circular or enclosed-gate transistors with more margin for manufacturing error.

## Why it is high value

- Today's flows assume square grids and horizontal and vertical wires because that is what the previous flows assumed. Rules, cell libraries, routers and file formats all reinforce each other, so nobody can try anything else without rebuilding the whole stack. That feedback loop, not physics, is the main reason layouts are rectilinear.
- Pin access is a real limit. A pin on a square grid has four neighbours, and in a standard-cell row the power rails above and below usually block two of them. A hexagonal grid gives six and an octagonal (with diagonals) eight, which could ease the routing congestion that limits cell density.
- Waves dislike right angles. Sharp corners cause reflections and current crowding in high-speed and RF lines, and field crowding that hurts reliability; RF and photonic layouts already use mitred bends, octagonal inductors and curves, with tools that sit outside the digital flow.
- Circular and enclosed-gate (annular) transistors have no gate ends and no gate edge over the isolation oxide, so line-end shortening, misalignment and edge leakage matter less. They are already used for radiation hardness; with tools that handle them, they could trade a little area for far more manufacturing margin.
- The work is a stack of checkable generators (rules, cells, routers, checkers) where every result can be compared against a Manhattan baseline on the same designs, which suits agents doing large amounts of careful, measurable work.

## State of the art

- Diagonal wiring: the X Architecture (Simplex, then Cadence, with Toshiba and others, early 2000s) added 45-degree wires on upper metal layers and reported shorter total wirelength; academic work followed with X-architecture routers and the hexagonal 0/60/120-degree Y-architecture. None of it survived into today's mainstream or open flows.
- Enclosed-gate transistors: used for radiation tolerance (CERN's deep-submicron work and later rad-hard libraries), with known costs in minimum size, area and asymmetric source and drain, and with compact models that assume rectangular devices.
- Masks are already curved: at advanced nodes, inverse lithography and multi-beam mask writers produce curvilinear masks, even though the drawn layout stays rectilinear and, below about 28nm, is forced onto unidirectional gridded metal.
- Open tools: GDS and OASIS can carry any polygon and KLayout handles all-angle geometry and DRC on it; Magic supports Manhattan plus 45-degree shapes; OpenROAD's placers and routers, LEF and DEF and most extraction assume rectangles on preferred-direction tracks. gdsfactory handles curved photonic layout but not digital place and route.
- Proprietary: analog and RF layout editors draw octagons and curves by hand, and topological PCB routers route at any angle; no widely used digital ASIC flow, open or proprietary, is built around non-Manhattan geometry today.

## Open questions

- Which nodes allow it: older nodes (180/130nm) print 45-degree and other angles on many layers, while FinFET nodes restrict geometry to gridded, one-direction patterns. Is this mainly a 200mm-node opportunity?
- Where to start for the clearest result: diagonal routing on upper layers with today's cells, hexagonal cell rows with six-way pin access, or enclosed-gate transistors in a cell library.
- How much of the gain survives square vias, the manufacturing grid (off-grid vertices snap to it), power grids, extraction and timing, measured against a Manhattan baseline on the same designs.
- How to model circular and enclosed-gate transistors well enough for characterisation and signoff when standard compact models assume a rectangular width and length.
- Which foundry rule decks would accept the shapes, and what a fake PDK should allow so the tools can be developed before a foundry signs off.

## Sources

Tim's description of the idea in the project thread (2026-10-21). It is not yet written up in his notes or Drive.

## Where it sits

Layer: **Tooling and PDK**. Function: **cross-cutting**. Target: **ASIC**. Tooling layer, with the PDK's rules and cells beneath it: a layout stack not tied to the Manhattan grid. Breaks the loop where rules, cells and tools only support right angles because that is all anyone has built for.

## Resources

Loose collection of links for fleshing this item out: [resources/any-angle.md](../resources/any-angle.md).

## Related items

- [cell-foundry](cell-foundry.md) (Standard cell generation): Hexagonal cells and enclosed-gate transistors need a cell generator, not hand layout.
- [drc-forge](drc-forge.md) (Design rule checking (DRC)): All-angle geometry needs rules and a checker that handle more than 45-degree edges.
- [shadow-pdks](shadow-pdks.md) (Open "almost manufacturable" PDKs): A fake PDK can define non-Manhattan rules before any foundry signs off on them.
- [tcad-twin](tcad-twin.md) (Open TCAD stack): Device simulation measures what circular and enclosed-gate transistors gain.
- [format-kit](format-kit.md) (Libraries for every EDA file format): LEF, DEF and tool databases must carry shapes and routes that are not rectangles.
- [asic-scoreboard](asic-scoreboard.md) (ASIC benchmarking): Benchmarks show whether non-Manhattan layouts beat Manhattan ones on the same designs.
- [paper-replay](paper-replay.md) (Replicating classic ASIC and FPGA papers): The X- and Y-architecture results can be re-tested with today's tools.
- [shuttle-program](shuttle-program.md) (Open MPW tapeout programs): Test structures on shuttles measure what the new geometries buy in silicon.
