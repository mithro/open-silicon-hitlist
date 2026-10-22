# format-kit: Libraries for every EDA file format

## Goal

High-quality, well-tested, permissively licensed libraries that read and write every file format used in open ASIC and FPGA flows, and every proprietary format with a public description, so new tools do not reinvent parsers and designs move between tools without loss. Targets include GDSII and OASIS, LEF and DEF, Liberty, SPEF and DSPF, SDC, SDF, Verilog, SystemVerilog and VHDL netlists, SPICE dialects, rule-deck languages, FPGA Interchange, FASM and vendor bitstream and netlist formats.

## Why it is high value

- Every open tool carries its own partial, subtly different parser for the same formats, and format bugs are a leading cause of tool-to-tool mismatches.
- Shared libraries make every other item cheaper: a new DRC engine, PDK audit or benchmark harness starts from correct readers and writers.
- Format work is precisely specified and checkable by round trips (read, write, compare) and by differential testing against existing tools, which suits agents writing parsers and huge test corpora.

## State of the art

- Good pieces exist but are scattered: KLayout's database (GDS, OASIS, LEF/DEF), OpenROAD's OpenDB, gdstk and gdsfactory, the Si2 LEF/DEF parsers, Liberty parsers inside OpenSTA and Yosys, Surelog/UHDM and slang for SystemVerilog, Verible, and the FPGA Interchange schemas.
- Most libraries are tied to one tool, cover only part of a format, lack conformance tests, or are hard to use from other languages.
- Proprietary formats (Cadence OpenAccess databases, vendor netlists and constraint dialects) have little or no open support.

## Open questions

- One library per format, or a common data model with many front ends?
- Which language and bindings (C++ core with Python and Rust bindings, or pure Rust)?
- Where conformance test suites come from for formats with no public specification.
- How far to go with proprietary formats when test files must come from open tools or public examples, since no proprietary tool is run.

## Where it sits

Layer: **Tooling**. Function: **cross-cutting**. Target: **ASIC and FPGA**. Foundation of the tooling layer: shared readers and writers so every ASIC and FPGA tool speaks every format.

## Resources

Loose collection of links for fleshing this item out: [resources/format-kit.md](../resources/format-kit.md).

## Related items

- [flow-proofs](flow-proofs.md) (Toolchain verification): Round trips through every format are a core verification check.
- [open-pnr](open-pnr.md) (FPGA Interchange and open place and route): FPGA Interchange is one of the formats to support well.
- [drc-forge](drc-forge.md) (Design rule checking (DRC)): A fast DRC engine needs fast, correct GDS and OASIS readers.
- [shadow-pdks](shadow-pdks.md) (Open "almost manufacturable" PDKs): PDK consistency audits compare views stored in many formats.
- [signed-builds](signed-builds.md) (Reproducible and signed toolchain): Deterministic writers are needed for reproducible outputs.
- [any-angle](any-angle.md) (Non-rectilinear layout tooling): Readers and writers must carry non-rectangular shapes and routes.
