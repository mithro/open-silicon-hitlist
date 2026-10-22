# fpga-scoreboard: FPGA benchmarking

## Goal

A continuously running benchmark of open FPGA toolchains against themselves: a matrix of designs × open toolchains (Yosys with VPR, nextpnr and their variants) × devices with open bitstreams × seeds, run on real boards on every tool change and release. It publishes area, fmax, slack, runtime, memory and power, with structured parsers for every tool's reports, and tracks each metric over time so regressions and gains show at once. New ideas are measured against the best earlier open result, and every run is kept as an open dataset corpus AI can learn and generalise from. No vendor toolchain runs in the matrix.

## Why it is high value

- Open FPGA tool changes are judged today on a handful of designs, so regressions slip in unseen and good ideas are hard to prove.
- Single runs mislead: place-and-route results vary by seed, so the benchmark needs statistics, which means many runs.
- Agents can only optimise what is measured; this is the scoreboard for the bitstream, place-and-route and open FPGA fabric items. Writing report parsers for each open tool and keeping the matrix green is wide, repetitive, checkable work. Every run, with its inputs, settings and results, is training and evaluation data for AI models of synthesis, placement, routing and timing.

## State of the art

- SymbiFlow/F4PGA's fpga-tool-perf compared open and Xilinx flows on 7-series but is not maintained, and its report parsing was fragile.
- Benchmark sets exist but are not tied together: VTR, Titan and Koios suites, ISCAS and EPFL circuits, open RISC-V cores and LiteX SoCs.
- Hosted board farms exist that could run the hardware side.

## Open questions

- Which designs form the core set: soft CPUs, DSP, memory-heavy designs, real LiteX SoCs?
- How to store, version and license the run corpus so others can train and evaluate on it.
- How to report seed sensitivity and run-to-run noise fairly.

## Sources

[fpga-tool-perf spec](https://j.mp/fpga-tool-perf-spec).

## Where it sits

Layer: **Tooling**. Function: **cross-cutting**. Target: **FPGA**. Measurement tooling for the FPGA side: scores the open FPGA tool and device stack.

## Resources

Loose collection of links for fleshing this item out: [resources/fpga-scoreboard.md](../resources/fpga-scoreboard.md).

## Related items

- [bitstream-atlas](bitstream-atlas.md) (FPGA bitstream documentation): Devices with open bitstreams can be benchmarked end to end.
- [open-pnr](open-pnr.md) (FPGA Interchange and open place and route): The main scoreboard for open place and route.
- [open-fabric](open-fabric.md) (Fully open FPGA and eFPGA): Measures each open fabric generation against the last.
- [paper-replay](paper-replay.md) (Replicating classic ASIC and FPGA papers): Old FPGA architecture results can be re-tested here.
