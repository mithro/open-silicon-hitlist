# fpga-scoreboard: FPGA benchmarking

## Goal

A continuously running benchmark of open versus vendor FPGA toolchains: a matrix of designs × toolchains (vendor, Yosys plus vendor place and route, VPR, nextpnr) × devices × seeds, run on real boards, publishing area, fmax, slack, runtime, memory and power, with structured parsers for every tool's reports.

## Why it is high value

- Nobody can say today how far open FPGA flows trail Vivado, Quartus, Radiant or Gowin EDA on the same design and device, so effort cannot be aimed.
- Single runs mislead: place-and-route results vary by seed, so the benchmark needs statistics, which means many runs.
- Agents can only optimise what is measured; this is the scoreboard for the bitstream, place-and-route and open FPGA fabric items. Writing report parsers for each vendor tool and keeping the matrix green is wide, repetitive, checkable work.

## State of the art

- SymbiFlow/F4PGA's fpga-tool-perf compared open and Xilinx flows on 7-series but is not maintained, and its report parsing was fragile.
- Benchmark sets exist but are not tied together: VTR, Titan and Koios suites, ISCAS and EPFL circuits, open RISC-V cores and LiteX SoCs.
- Hosted board farms exist that could run the hardware side.

## Open questions

- Which designs form the core set: soft CPUs, DSP, memory-heavy designs, real LiteX SoCs?
- How to publish vendor-tool results within EULA terms.
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
- [open-fabric](open-fabric.md) (Fully open FPGA and eFPGA): Measures open fabrics against proprietary parts.
- [paper-replay](paper-replay.md) (Replicating classic ASIC and FPGA papers): Old FPGA architecture results can be re-tested here.
