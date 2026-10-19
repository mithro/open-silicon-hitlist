# Toolchain verification — resources

Loose collection, 2026-10-19. Drive links are publicly shared (anyone with the link).

## Tim's Google Drive (public)
- [F4PGA (SymbiFlow) Checking / Testing Approach](https://docs.google.com/document/d/11wJUvr2aVBkUiuYYsFN07jkoYr_ccWlLLLFH8YQw8uQ/edit) — per-stage FPGA checks
- [F4PGA Bitstream Verification Process](https://docs.google.com/drawings/d/1NJlN-cPLNx4nULHiL4938RD-H14izpayqtNSQ4XRjfA/edit) — bitstream to FASM to Verilog round trip
- [Data Flow in F4PGA Arch Defs for Xilinx Series 7 Testing + Verification](https://docs.google.com/drawings/d/1-FmukrW4YtreRwkA4JKkYd-siscC3OvDTq8rKreOVHE/edit)
- [SymbiFlow Toolchain with Vivado Sign-Off Process](https://docs.google.com/drawings/d/18kMbl0OH-VbUbYPrFXu6euYAvD0cpuerKj6GGSucVmM/edit) — vendor tool as oracle
- [SymbiFlow Toolchain with Vivado Interchange](https://docs.google.com/drawings/d/1chipxEMaLllGfYSxgpY0cW46nn2Y1Xd4_zdJ-UkGhkc/edit) — mixed open/vendor flows
- [7-series testing status](https://docs.google.com/spreadsheets/d/1RlSiC9RJrrswtYfE5DnPGegpP2v7pautYixhwMAKyN0/edit) — primitive test coverage
- [SymbiFlow Testing Examples Breakdown (Where to add a test?)](https://docs.google.com/document/d/1ZQp8D_Jp1C2kmJR9WOYwis8U5N0xIUB0RFLnvyLlNH8/edit)
- [Test and verification for ASIC designs options exploration](https://docs.google.com/document/d/1_StmqBumyTuTNVcvutiX-INbbLG7DHoGl_fe0lvQPZ8/edit) — ASIC gap map
- [Tapeout Sign-off and Tools Qualification](https://drive.google.com/file/d/1uall0VbcQiPrt8zBZn5_w4ACAMrqQVH3/view) — what qualifying a tool means
- [Design Rule Check (DRC) Testing - How testing for DRC rules should be done](https://docs.google.com/document/d/18z-FBJHni6qt1WR_tF6bbRHfQydKcFMAVnuj4Ixbj90/edit) — per-rule test method
- [Flip flop layout for combinational cells testing (OpenROAD and friends)](https://docs.google.com/drawings/d/1Eoudc5e_taZ3p89ekMXDwyGZuj86M8T_Nj7q1vHG1UE/edit)
- [Yosys Timing Annotation support](https://docs.google.com/document/d/1A0ceG2ltz4jttb_KS4tijJrIhxrUcB23V16Sl3StO34/edit) — timing correlation input
- [SystemVerilog flows (for OpenTitan and other SV designs) using open tools](https://docs.google.com/drawings/d/1GEjCoLwY57bsuZoj5ymyXoToIEOC0H4j2SEYsqQupM8/edit) — SV front-end map
- [SystemVerilog - Synthesis & Testing Prioritization Diagram (BlackParrot)](https://docs.google.com/drawings/d/1zdOuH2YZzFLb0n5M-q9LPti64Wnsh9c6eqmfqO1ypkQ/edit)
- [BlackParrot Module Status (Surelog / Verilator / Yosys / Renode)](https://docs.google.com/spreadsheets/d/18okLCMcx55yZ67i5rda6f3ymgqcChlK0-fWjWcqSkeU/edit) — per-module tool support
- [OpenTitan Peripheral Status (Surelog / Verilator / Yosys / Renode)](https://docs.google.com/spreadsheets/d/1g7R3xjYnI83_cLagv-Bv23CCkycRbcUFUgz1CtSIsL8/edit)
- [Types of "testing" in LiteX (and Migen/MiSoC)](https://docs.google.com/document/d/1SLRMCTETNKA0Cfy8dExF8QAn8j0FVbUEgorsicJmoeU/edit)

## Talks and presentations
- [OrConf19 - SystemVerilog Test Suite](https://docs.google.com/presentation/d/1ytlKMWrt4XYk-JVxCn1pN4bAojBsT1oWuKu3KRJtbZU/edit) — sv-tests origin
- [UHDM](https://docs.google.com/presentation/d/1evu8aBWMFwi_UrK-DfWXowfsXM4Bp9knQuHV24lwkPc/edit) — Alain Dargelas
- [ORConf 2026: Closing in on full SystemVerilog support in Verilator (PDF)](https://drive.google.com/file/d/1Na523Hf0XgPsJwr8LuvAuYcQh0sYMANP/view) — four-state, UVM, SVA

## Projects and repositories
- FPGA: [FASM](https://github.com/chipsalliance/fasm), [Project X-Ray](https://github.com/f4pga/prjxray) (fasm2frames, bit2fasm), [f4pga-arch-defs](https://github.com/f4pga/f4pga-arch-defs) (simulation models), fasm2bels
- Formal: [SymbiYosys](https://github.com/YosysHQ/sby), [EQY](https://github.com/YosysHQ/eqy), [MCY](https://github.com/YosysHQ/mcy), [riscv-formal](https://github.com/YosysHQ/riscv-formal)
- SV front ends: [sv-tests](https://github.com/chipsalliance/sv-tests) ([results](https://chipsalliance.github.io/sv-tests-results/)), [Surelog](https://github.com/chipsalliance/Surelog), [UHDM](https://github.com/chipsalliance/UHDM), [Synlig](https://github.com/chipsalliance/synlig), [slang](https://github.com/MikePopoloski/slang), [yosys-slang](https://github.com/povik/yosys-slang), [sv2v](https://github.com/zachjs/sv2v), [Verilator](https://github.com/verilator/verilator)
- VHDL: [GHDL](https://github.com/ghdl/ghdl) and [ghdl-yosys-plugin](https://github.com/ghdl/ghdl-yosys-plugin)
- ASIC: [OpenROAD](https://github.com/The-OpenROAD-Project/OpenROAD), [OpenSTA](https://github.com/parallaxsw/OpenSTA), [Netgen](https://github.com/RTimothyEdwards/netgen) (LVS), [KLayout](https://github.com/KLayout/klayout)
- Test harnesses: [cocotb](https://github.com/cocotb/cocotb), [openFPGALoader](https://github.com/trabucayre/openFPGALoader) for on-hardware checks

## Papers and other reading
- Wolf, "Yosys Open SYnthesis Suite" manual — `equiv_*` passes for post-synthesis checks
- Commercial references for correlation: Cadence Conformal, Synopsys Formality, Siemens Calibre, Synopsys PrimeTime/StarRC
