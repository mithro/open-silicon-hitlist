# hard-core: Partial hardening

## Goal

A flow for chips where only the most important, highest-performance core of a design is hardened as an ASIC block, the rest goes into an embedded FPGA (eFPGA), and control and slow paths run as software on on-chip CPUs. The flow decides the split from profiling and benchmarks, generates the interfaces between the three parts, and lets the soft parts keep changing after tapeout.

## Why it is high value

- Full custom ASICs are expensive and frozen at tapeout; FPGAs are flexible but slow and large. Hardening only the hot core gets most of the ASIC performance while keeping most of the design changeable.
- It makes advanced accelerators feasible on small budgets and open shuttles, where die area and respins are the limiting cost.
- Choosing the split, generating glue logic and verifying all three parts together is a large, measurable design-space search that suits agents.

## State of the art

- Proprietary SoCs pair hard cores with eFPGA (for example devices built with Flex Logix, Achronix Speedcore or QuickLogic eFPGA IP), and FPGA vendors ship hard DSP, AI engines and CPUs inside programmable fabric.
- Open pieces exist separately: open eFPGA generators (FABulous, OpenFPGA), open CPU cores, LiteX SoC integration and high-level synthesis tools, but no open flow chooses the split or generates the boundaries.
- Hardware/software co-design and partitioning research has a long history but little open, end-to-end tooling.

## Open questions

- How the split is chosen: profiling on FPGA prototypes, cost models, or search with the benchmarking items as the scoreboard?
- What the standard interface between hard block, eFPGA and CPUs looks like, and whether it is the same one the accelerator interface item defines.
- How to verify the combined system before tapeout, using composable simulation.
- Which first demonstrator design and which PDK and shuttle to target.

## Where it sits

Layer: **IP**. Function: **computation**. Target: **ASIC**. Embodies the deck's criticality scale in one chip: performance-critical hard core, flexibility-critical eFPGA, non-critical software.

## Resources

Loose collection of links for fleshing this item out: [resources/hard-core.md](../resources/hard-core.md).

## Related items

- [open-fabric](open-fabric.md) (Fully open FPGA and eFPGA): The eFPGA holds the parts that stay programmable.
- [sim-mosaic](sim-mosaic.md) (Composable and distributed simulation): Composable simulation verifies the hard, eFPGA and software parts together.
- [accel-harness](accel-harness.md) (Accelerator interface and harness): The same accelerator interface can join the hard block, eFPGA and CPUs.
- [open-links](open-links.md) (Open high-speed connectivity IP): Connectivity IP links the chip to its host.
- [arithmetic-zoo](arithmetic-zoo.md) (Adder and multiplier exploration): Arithmetic-heavy cores are prime candidates for hardening.
- [open-airwaves](open-airwaves.md) (Open wireless with eFPGA and SDR): Radios are a natural partial-hardening case.
