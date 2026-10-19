# FPGA bitstream documentation — resources

Loose collection, 2026-10-19. Drive links are publicly shared (anyone with the link).

## Tim's Google Drive (public)
- [Project U-Ray - Extending Project X-Ray to 7 Series, UltraScale and UltraScale+ Parts](https://docs.google.com/document/d/1y_9tFoLzVC_PrZA2YIej__7LsgiXgrTN3oitTcsXEF8/edit) — UltraScale/US+ plan
- [Project X-Ray -- High Speed Transceiver bitstream documentation](https://docs.google.com/document/d/1IqMAlTdAZtSV6gyj6CR-yXLAS6ycpAfeTGwLvaCwC_U/edit) — GTP/GTX hard-IP gap
- [Project X-Ray - DSP Fuzzer](https://docs.google.com/document/d/15MBYkL7FOoK4U5pxx7L1DLZZ_V70OdugjUZCgz5lx5I/edit) — DSP48 fuzzing plan
- [Project X-Ray -- Improve FASM speed (by rewriting in C++)](https://docs.google.com/document/d/1F-balyceXOyuV9TdWooZexWUaP1Y2wyrS7CHV0GVrS0/edit) — fasm2frames performance
- [Project X-Ray - File Diagram](https://docs.google.com/drawings/d/1eqP44TDeaLLEO0CaEjn_bxorOV3iAXmelFsyzMi4yVI/edit) — database layout
- [SymbiFlow Grid + Connectivity Database](https://docs.google.com/document/d/1UcDoX51WGP4Ov5s0fMRjZzn-BtFiJaHk-VHwjuqt6Xs/edit) — tile grid / routing DB design
- [FASM Database Specification](https://docs.google.com/document/d/1NUVo-k_TYDZvH8EKcL7c-q30rMhPSeVA2DaHzT4zSLE/edit) — bit-to-feature DB format
- [FPGA ASM (FASM) File Format Requirements](https://docs.google.com/document/d/13ubzrxcfU0TUVIIRpmZt0aMwaMFm_HsjNlzRK0uvNhI/edit) — FASM design rationale
- [FASM "Metadata Comment" Formats](https://docs.google.com/document/d/1wbYiZQLTrUQ67Vl2gLmI954PrsAJmSbnETCDm9UYT9w/edit) — FASM annotations
- [iCE40 FASM Format](https://docs.google.com/document/d/1waqO7CYT5d9sbTKBU1-2GvFIlgRRWsusPZTYY2EfC4c/edit) — FASM for a second family
- [Importing FASM into Vivado](https://docs.google.com/document/d/1oAISSfNaOlb5c1PTrWhG5XfmMmG667cEQWhTLlm2NHA/edit) — vendor cross-check path
- [Xilinx Series 7 BitStream Sizes](https://docs.google.com/spreadsheets/d/1Ym8VYGhPbtnjxdPOFiYoerwxTileuB0zkZohpDWMDRE/edit) — per-part sizes
- [SymbiFlow Parts Encyclopedia](https://docs.google.com/document/d/1ngck6LGVTXm6HDrVqWeEGdEELrKPWXVaeejkXurgfl4/edit) — family/part catalogue
- [SymbiFlow Name Mapping (Xilinx, Lattice, Altera/Intel)](https://docs.google.com/spreadsheets/d/1pWjU8RujiGdlr-8iG66O1rvognNHgtnNVvCjSfksH-4/edit) — cross-vendor terminology
- [FPGA Internal RAM Types (SymbiFlow)](https://docs.google.com/document/d/1kviDz-KiaXVTXqA9qvQWeEZhQznK38nnKsSsPX4zoS4/edit) — BRAM/LUTRAM across families
- [Example grant proposal - BYU Sensitive Bits SymbiFlow Proposal (public version)](https://docs.google.com/document/d/13rFZ1dKrWLdZTJnUrXX5hse3iIuzWjADU1DXLUaeAGQ/edit) — bitstream security research
- [Openness in FPGAs - Stages Diagram](https://docs.google.com/drawings/d/1f9wEtbZ5yWQsPG1lxRiBFv_4x-XyfI5GONvi3bUn-as/edit) — levels of openness
- [Open FPGA Ecosystem](https://docs.google.com/presentation/d/1RlOPCLYUmtRTCkiuVoWcpJLZ16ldXngDGlA-q4AvkuU/edit) — legacy Xilinx (Spartan-3/6, Virtex-5) still ISE-only

## Talks and presentations
- [SymbiFlow - Xilinx Series 7 FPGAs now have a fully Open Source toolchain! (Hackaday Supercon 2019)](https://docs.google.com/presentation/d/1YQZELnTiVDw7GGsNk-h_ojh-vMDLk23WXathY7sPudQ/edit)
- [SymbiFlow - Finally the GCC of FPGAs! (35C3)](https://docs.google.com/presentation/d/18HM63VXKigypJy6vniqfk6a7QaTu4Yj8YdmyqVBVYtY/edit)
- [SymbiFlow - Finally the GCC of FPGAs! (LCA 2019)](https://docs.google.com/presentation/d/1mIrmFpAtgkGCKa5nMawT_pBeOVps4VuxmHJHEP6VaBc/edit)
- [An update on SymbiFlow - a multiplatform FPGA project](https://docs.google.com/presentation/d/1GZrZCDr59AObbs6rtPOdraIlhRz1YNychQ8M0NbOQlQ/edit)
- [OrConf19 - Status of Artix 7 support in SymbiFlow](https://docs.google.com/presentation/d/1EBpThE64ci4nNbQaO5n_Uc7QmDGpcb1Rm-iNAyd7fUw/edit)

## Projects and repositories
- [Project X-Ray](https://github.com/f4pga/prjxray) and [prjxray-db](https://github.com/f4pga/prjxray-db) — Xilinx 7-series
- [Project U-Ray](https://github.com/f4pga/prjuray) — UltraScale/US+ (partial)
- [prjcombine](https://github.com/prjunnamed/prjcombine) — many Xilinx/Altera/Lattice families incl. legacy
- [Project IceStorm](https://github.com/YosysHQ/icestorm) — Lattice iCE40
- [Project Trellis](https://github.com/YosysHQ/prjtrellis) — Lattice ECP5
- [Project Oxide](https://github.com/gatecat/prjoxide) — Lattice Nexus
- [Project Apicula](https://github.com/YosysHQ/apicula) — Gowin
- [Mistral](https://github.com/Ravenslofty/mistral) — Intel Cyclone V
- [FASM](https://github.com/chipsalliance/fasm) — FPGA assembly format and tools
- [F4PGA](https://f4pga.org) and [f4pga-arch-defs](https://github.com/f4pga/f4pga-arch-defs) — consumer of the databases
- [openFPGALoader](https://github.com/trabucayre/openFPGALoader) — open programming for hardware checks
- Project Peppercorn (Cologne Chip GateMate) — vendor-open bitstream docs

## Papers and other reading
- [Reverse-engineering the first FPGA chip, the XC2064](https://www.righto.com/2020/09/reverse-engineering-first-fpga-chip.html) (Ken Shirriff) — legacy pilot target
- Wolf and Lasser, "Project IceStorm" — first fully documented COTS FPGA

## Also listed on mith.ro

- [ERI Panel - SymbiFlow + POSH/IDEA](https://docs.google.com/presentation/d/13VzMFyAJVCZivpYNk_D4HyMPbM5xVacpFLlPFzQiiEM)
- [F4PGA (SymbiFlow) Checking / Testing Approach](https://docs.google.com/document/d/11wJUvr2aVBkUiuYYsFN07jkoYr_ccWlLLLFH8YQw8uQ/edit)
- [SymbiFlow Target Designs](https://docs.google.com/document/d/163Vxde2vLeQCR0V2RJDsxFERbC2P5n0VzwkALtC-OTY/edit#heading=h.932aic2njsrd)
