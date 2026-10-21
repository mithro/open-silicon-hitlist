# asic-scoreboard: ASIC benchmarking

## Goal

A public, re-runnable ASIC benchmark: designs from every open shuttle (Open MPW, Tiny Tapeout, wafer.space, Chipathon) and from published open-PDK papers, run through open flows per PDK and fake PDK, with power, performance, area, runtime and signoff results tracked over time and compared with historical commercial results at the same node.

## Why it is high value

- Open flows lack a shared yardstick, so tool changes are judged on a handful of designs.
- Thousands of real taped-out designs exist with known silicon status, but links rot (many Efabless Open MPW links are already dead) and nobody re-runs them.
- Reproducing each design's flow and keeping the corpus current is large, mechanical work where each design's own tests are the check. It is the scoreboard for the arithmetic, standard-cell, PDK and toolchain items.

## State of the art

- Open MPW produced about 360 SKY130 project slots with manifests; Tiny Tapeout has thousands of taped-out designs; wafer.space runs on GF180MCU.
- OpenROAD's flow scripts publish metrics on a small design set; academic contest suites (ISPD, ICCAD) and EPFL circuits cover single stages.
- Published industry figures at mature nodes (gate density, SRAM bit-cell area, known core area and clock) give targets to compare against.

## Open questions

- Which metrics are canonical (area, fmax, power, DRC/LVS clean, runtime)?
- Where the corpus lives and who pays for compute.
- How it shares designs with the DRC item's benchmark needs and the open MPW programs item.

## Where it sits

Layer: **Tooling**. Function: **cross-cutting**. Target: **ASIC**. Measurement tooling for the ASIC side: scores PDKs, tools and IP together.

## Resources

Loose collection of links for fleshing this item out: [resources/asic-scoreboard.md](../resources/asic-scoreboard.md).

## Related items

- [shuttle-program](shuttle-program.md) (Open MPW tapeout programs): Shuttle designs form the benchmark corpus.
- [shadow-pdks](shadow-pdks.md) (Open "almost manufacturable" PDKs): Compares PPA across real and fake PDKs.
- [arithmetic-zoo](arithmetic-zoo.md) (Adder and multiplier exploration): Scoreboard for arithmetic choices.
- [cell-foundry](cell-foundry.md) (Standard cell generation): Scoreboard for cell libraries.
- [paper-replay](paper-replay.md) (Replicating classic ASIC and FPGA papers): Replicated results become benchmark cases.
- [drc-forge](drc-forge.md) (Design rule checking (DRC)): Fast, tested design rule checks gate every scored design.
