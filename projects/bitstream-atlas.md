# bitstream-atlas: FPGA bitstream documentation

## Goal

Complete, machine-readable bitstream documentation (bit-to-function databases, routing graphs, tile grids, timing data) for every commercial off-the-shelf FPGA family, good enough for a fully open toolchain (synthesis, place and route, bitstream generation) to target each device.

## Why it is high value

- Vendor toolchains are the only way to use almost all FPGAs; open documentation unlocks open toolchains, research, auditing and long-term preservation.
- The work is huge, repetitive and well-specified: fuzz the vendor tools, diff the bitstreams, infer the encoding, verify on hardware. That is a good fit for AI agents running at scale.

## State of the art

- Fully or largely documented: Lattice iCE40 (Project IceStorm), ECP5 (Project Trellis), Nexus (Project Oxide); Xilinx 7-series (Project X-Ray, partial coverage of hard blocks); Gowin (Project Apicula); Intel Cyclone V (Mistral); Cologne Chip GateMate (vendor-open).
- Partial: Xilinx UltraScale/UltraScale+ (Project U-Ray, prjcombine); many older Xilinx and Altera families in prjcombine.
- Largely undocumented: AMD Versal, Intel Agilex/Stratix 10, Microchip PolarFire, Efinix, most hard IP (transceivers, PCIe, DDR controllers) on every family.

## Open questions

- Legal posture per vendor (EULA terms on reverse engineering, DMCA considerations) and which families are safe to target first.
- Coverage definition: is "documented" every bit, or enough for a working open flow plus timing?
- Vendor tool licences and compute needed to fuzz the largest devices.
- Hardware-in-the-loop verification: which boards, and who hosts them.

## Related items

- [open-pnr](open-pnr.md) (FPGA Interchange and open place and route): Open place and route needs these databases to target each family.
- [fpga-scoreboard](fpga-scoreboard.md) (FPGA benchmarking): Scores open toolchains on the documented devices.
- [flow-proofs](flow-proofs.md) (Toolchain verification): Bitstream round trips check the databases are right.
- [open-fabric](open-fabric.md) (Fully open FPGA and eFPGA): An open fabric needs no reverse engineering at all.
