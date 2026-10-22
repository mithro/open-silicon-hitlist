# cell-foundry: Standard cell generation

## Goal

Automatically generate, characterise and verify complete standard-cell libraries for any PDK, supply voltage and track height. Each library should include layouts, LEF abstracts, Liberty timing and power models across corners, SPICE netlists and DRC/LVS-clean proofs. Targets run from GF180MCU at 3.3V or 1.8V to every node in the fake-PDK project.

## Why it is high value

- Every open PDK ships one or a few hand-built libraries. A new voltage, track height or node means months of manual layout and characterisation.
- The fake PDKs on this list are useless for digital design without cell libraries, so this is on their critical path.
- Cell layout, sizing and characterisation are repetitive, rule-bound and fully checkable by DRC, LVS and SPICE, which suits agents generating and fixing cells in bulk.

## State of the art

- Hand-built open libraries: the SKY130 libraries (sky130_fd_sc_hd and its siblings), the GF180MCU 7-track and 9-track libraries, the IHP SG13G2 cells, and the ASAP7 and FreePDK45 (Nangate) research libraries.
- Open generators: LibreCell (lclayout) and ASTRAN. They work for simple cells, but neither produces a complete, characterised, signoff-quality library.
- Open characterisation flows built on ngspice or Xyce exist (for example Libretto and CharLib). The commercial tools are Cadence Liberate and Synopsys SiliconSmart.
- Commercial: foundry and IP vendors (Arm, Synopsys, Cadence) build libraries with in-house automation.

## Open questions

- Which cell set and drive strengths count as "complete" for synthesis quality (a minimal set versus a full set of about 500 cells)?
- How to handle FinFET-specific rules (fin quantisation, multi-patterning colouring) at the pre-EUV node.
- What accuracy the open characterisation needs, measured against which reference.
- How cell choices feed back into the adder and multiplier exploration item.

## Sources

Tim's design doc: [Voltages and options for I/O and standard cells (GF180MCU)](https://docs.google.com/document/d/1vQCrkIvE0MdizFUSRD8Sxo-BBnwj0SztJd-1aU5nRRs/edit).

## Where it sits

Layer: **PDK**. Function: **cross-cutting**. Target: **ASIC**. The PDK's "primitives and low-level data": a cell generator rather than a hand-drawn library, which is the manual-to-automated shift.

## Resources

Loose collection of links for fleshing this item out: [resources/cell-foundry.md](../resources/cell-foundry.md).

## Related items

- [shadow-pdks](shadow-pdks.md) (Open "almost manufacturable" PDKs): Every fake PDK needs its own cell libraries.
- [arithmetic-zoo](arithmetic-zoo.md) (Adder and multiplier exploration): Arithmetic architectures are built from these cells.
- [asic-scoreboard](asic-scoreboard.md) (ASIC benchmarking): Library quality shows up in ASIC benchmarks.
- [shuttle-program](shuttle-program.md) (Open MPW tapeout programs): Shuttles prove the cells in silicon.
- [any-angle](any-angle.md) (Non-rectilinear layout tooling): Non-rectilinear cells (hexagonal footprints, enclosed-gate transistors) are a target for the generator.
