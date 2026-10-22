# flow-proofs: Toolchain verification

## Goal

Per-stage checks that each open tool's output is correct, so a failure points at the tool that caused it rather than showing up as a broken chip or bitstream at the end. For FPGA flows this means bitstream to FASM to Verilog round trips, with equivalence back to the source design. For ASIC flows it means formal equivalence after each transformation (synthesis, placement and clock-tree changes, routing), LVS, and timing and parasitic correlation against reference signoff tools.

## Why it is high value

- Open flows are trusted less than proprietary ones mainly because nobody can show each stage is correct. Per-stage verification is the evidence.
- It turns every bug report from "the design doesn't work" into "this tool broke this property at this stage", which agents can then fix.
- Writing checkers, round-trip tools and large regression suites is wide, mechanical and self-checking work. It also supplies the test oracle for the other items on this list (DRC, arithmetic units, the reproducible toolchain).

## State of the art

- FPGA: F4PGA/SymbiFlow used FASM round trips and fuzzer-derived databases for checking; Yosys `equiv_*` passes and SymbiYosys allow formal equivalence for small designs.
- ASIC: Yosys and EQY for equivalence; Netgen and KLayout for LVS; OpenSTA and OpenRCX for timing and extraction, with limited cross-checks between open tools and against measured silicon.
- Proprietary (context only; never run): Cadence Conformal and Synopsys Formality for equivalence; Calibre for LVS; PrimeTime and StarRC as timing and extraction references.
- Gaps: equivalence that scales to full chips, timing correlation data, and mixed-signal verification.

## Open questions

- Which stages to cover first, and for which flows (OpenROAD/OpenLane, nextpnr/F4PGA)?
- Which independent references to check against without proprietary signoff tools: a second open tool, published results, and measured silicon from the shuttle programs.
- How to make full-chip equivalence tractable (hierarchical, incremental, or distributed in the style of the DRC engine).

## Sources

Tim's design docs: [F4PGA (SymbiFlow) Checking / Testing Approach](https://docs.google.com/document/d/11wJUvr2aVBkUiuYYsFN07jkoYr_ccWlLLLFH8YQw8uQ/edit), [Test and verification for ASIC design](https://docs.google.com/document/d/1_StmqBumyTuTNVcvutiX-INbbLG7DHoGl_fe0lvQPZ8/edit).

## Where it sits

Layer: **Tooling**. Function: **cross-cutting**. Target: **ASIC and FPGA**. Tooling quality: checks every stage of both ASIC and FPGA flows.

## Resources

Loose collection of links for fleshing this item out: [resources/flow-proofs.md](../resources/flow-proofs.md).

## Related items

- [signed-builds](signed-builds.md) (Reproducible and signed toolchain): Deterministic outputs make per-stage checks repeatable.
- [bitstream-atlas](bitstream-atlas.md) (FPGA bitstream documentation): FPGA round trips depend on accurate bitstream databases.
- [drc-forge](drc-forge.md) (Design rule checking (DRC)): DRC and LVS are verification stages.
- [open-pnr](open-pnr.md) (FPGA Interchange and open place and route): Checks each open place-and-route stage.
- [instant-rebuild](instant-rebuild.md) (Incremental toolchains): Proves incremental results equal full rebuilds.
- [format-kit](format-kit.md) (Libraries for every EDA file format): Shared, tested parsers remove a major source of mismatches.
