# open-fabric: Fully open, better FPGA and eFPGA

## Goal

A fully open FPGA architecture, as a standalone chip and as an embedded FPGA (eFPGA) block, that is designed, verified and hardened entirely with open tools on open PDKs, ships with its own open toolchain from day one, and is competitive with commercial parts of the same class on density and performance.

## Why it is high value

- It is the one FPGA whose bitstream, architecture and toolchain are open by construction, so no reverse engineering is needed.
- An eFPGA block lets open SoCs add post-silicon flexibility, and makes FPGA-to-ASIC migration paths possible.
- Exploring the architecture space (LUT size, cluster size, routing channel width, switch box patterns, DSP and memory blocks) is a large search over measurable designs, a strong fit for agents with the FPGA benchmarking item as the scoreboard.

## State of the art

- Generators: FABulous (Manchester) and OpenFPGA (Utah) generate fabrics with matching VPR or nextpnr flows; both have been taped out on SKY130 and GF180MCU through open shuttles.
- Most past open-shuttle eFPGA tapeouts relied on proprietary tools for at least part of the hardening.
- Commercial eFPGA IP exists (QuickLogic, Flex Logix, Menta); QuickLogic has open-sourced toolchain support for some parts.

## Open questions

- What "better" means first: density, performance, power, or ease of use for open toolchains?
- Which PDKs and process nodes to target, including the fake PDKs.
- Standalone chip, eFPGA IP, or both, and what interfaces the eFPGA exposes to its host SoC.
- How to fund and run the silicon validation.

## Where it sits

Layer: **IP**. Function: **computation**. Target: **ASIC and FPGA**. An IP generator for the deck's flexibility-critical computation: an eFPGA block in ASICs and a standalone FPGA.

## Resources

Loose collection of links for fleshing this item out: [resources/open-fabric.md](../resources/open-fabric.md).

## Related items

- [open-pnr](open-pnr.md) (FPGA Interchange and open place and route): Uses VPR and nextpnr as its toolchain.
- [fpga-scoreboard](fpga-scoreboard.md) (FPGA benchmarking): Benchmarked against commercial FPGAs.
- [shuttle-program](shuttle-program.md) (Open MPW tapeout programs): Taped out on open shuttles.
- [accel-harness](accel-harness.md) (Accelerator interface and harness (FPGA and ASIC)): An eFPGA can host accelerators behind the same interface.
- [hard-core](hard-core.md) (Partial hardening: ASIC core plus eFPGA and software): Partial hardening uses an eFPGA for everything outside the hard core.
- [open-airwaves](open-airwaves.md) (Open wireless with eFPGA and SDR): Wireless basebands are a flagship eFPGA use.
