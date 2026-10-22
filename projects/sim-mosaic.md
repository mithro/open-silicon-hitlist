# sim-mosaic: Composable and distributed simulation and emulation

## Goal

One SoC model in which each block can run in the engine that gives the accuracy it needs: Renode for fast functional models, Verilator for cycle-accurate RTL, or FPGA emulation for speed at RTL accuracy, all joined by standard bridges and swappable per block. The same model then scales out across a cluster for full-chip or many-instance runs.

## Why it is high value

- Today a team picks one engine for the whole SoC and pays for it: functional simulation misses RTL bugs, full RTL simulation is too slow to boot software, and FPGA emulation needs the whole design to fit.
- Mixing engines lets software run at near-functional speed while the block under test runs at RTL accuracy, which shortens verification and makes hardware CI practical.
- Writing missing Renode peripheral models, bridge adapters and one test matrix across Renode, Verilator, FPGA and silicon is bulk model-writing work agents can do.

## State of the art

- Renode co-simulates with Verilator through its integration layer, and has been used to model the Caravel test harness.
- LiteX provides bridges (for example Etherbone over Ethernet and UART) that connect host software to FPGA designs; Tim's LiteX bridge protocol proposes a common interface.
- Hardware in the loop: [fpgas.online](https://fpgas.online) is a public farm of Artix-7 and iCE40 boards with bitstream upload and serial access, usable to check simulation results against real boards.
- Proprietary: hybrid emulation from Cadence (Palladium with virtual platforms) and Synopsys (ZeBu with Virtualizer). Open distributed RTL simulation is limited (Verilator multithreading, research work on partitioned simulation).

## Open questions

- The bridge standard: extend the LiteX bridge protocol, adopt an existing one (TLM-2.0, SystemC, PCIe/AXI transactors), or define a new one?
- How time synchronises between engines running at very different speeds.
- How a model is partitioned across a cluster, and what "distributed" targets first (one big chip, or many instances for regression).
- Which reference SoC to prove it on.

## Sources

Tim's design docs: [Renode for simulation of the Caravel testing system](https://docs.google.com/document/d/1qhin7U1esp58NoVwrdkKkEDZb2k280YF0PKGENGgLSI/edit), [Testing environments (and CI) for open hardware projects](https://docs.google.com/document/d/1YgJ-MUC-r9-Stl1M98xjTq8Qf-YQy6LNu38Ov5K5pt0/edit), [LiteX Bridge Protocol](https://docs.google.com/document/d/1d_Uy6oljyYS4vZhSWomF-IWtP-vDN8qYYra6-Q8KLec/edit), [LiteX based interface for Hardware Accelerators](https://docs.google.com/document/d/1oiTqR-6ppiObBRFA91sxl3sgHkPHw2WK_tFD5itx9xg/edit).

## Where it sits

Layer: **Tooling**. Function: **cross-cutting**. Target: **ASIC and FPGA**. Verification and simulation tooling that cuts across interface, computation and storage blocks.

## Resources

Loose collection of links for fleshing this item out: [resources/sim-mosaic.md](../resources/sim-mosaic.md).

## Related items

- [accel-harness](accel-harness.md) (Accelerator interface and harness (FPGA and ASIC)): Shares the bridge seam between simulation, FPGA and silicon.
- [open-links](open-links.md) (Open high-speed connectivity IP): Connectivity IP needs models at every accuracy level.
- [flow-proofs](flow-proofs.md) (Toolchain verification): Mixed-engine runs cross-check each other.
- [hard-core](hard-core.md) (Partial hardening: ASIC core plus eFPGA and software): Partially hardened chips need hard, eFPGA and software parts simulated together.
