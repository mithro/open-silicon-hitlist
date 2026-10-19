# open-links: Open high-speed connectivity IP

## Goal

Open, verified IP for high-speed links that works on FPGAs and in ASICs from one source: PCIe (and CXL), USB 3, Ethernet (10G and above), DDR and LPDDR memory interfaces, and the PHY layers (PIPE, SerDes) beneath them, with controllers portable across vendors and analog PHYs for open PDKs.

## Why it is high value

- Every serious accelerator or SoC needs these links, and today they almost always mean licensed vendor IP. That blocks fully open designs, including the LiteX accelerator interface item.
- The protocols are precisely specified and checkable against compliance tests, which suits agents writing, testing and debugging controllers in bulk.
- One codebase across FPGA and ASIC means designs can be prototyped on FPGAs and taped out without swapping IP.

## State of the art

- FPGA controllers using vendor hard blocks or transceivers: LitePCIe, LiteEth, LiteDRAM and the usb3_pipe core (LiteX); Corundum (100G NIC); Verilog Ethernet and PCIe cores from Alex Forencich.
- They usually rely on vendor transceiver and PCIe hard IP; open ASIC PHYs are almost absent (some SerDes and DDR PHY research on SKY130 and GF180MCU).
- Commercial: Synopsys, Cadence, Alphawave and others license controllers and PHYs per node.

## Open questions

- Which protocols and speeds come first for open accelerators and SoCs.
- How to split work between portable digital controllers and per-PDK analog PHYs.
- How compliance is demonstrated without paid membership of the standards bodies.
- How the PHY work lines up with the analog generator and fake-PDK items.

## Related items

- [accel-harness](accel-harness.md) (Accelerator interface and harness (FPGA and ASIC)): The accelerator interface and ASIC harness are built on these links but are a separate item.
- [sim-mosaic](sim-mosaic.md) (Composable and distributed simulation): Needs models for composable simulation.
- [shadow-pdks](shadow-pdks.md) (Open "almost manufacturable" PDKs): Analog PHYs are built per PDK.
- [shuttle-program](shuttle-program.md) (Open MPW tapeout programs): Shuttles prove PHYs in silicon.
- [hard-core](hard-core.md) (Partial hardening: ASIC core plus eFPGA and software): Partially hardened chips need these links to their hosts.
