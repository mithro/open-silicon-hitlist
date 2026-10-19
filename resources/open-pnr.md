# FPGA place and route (FPGA Interchange, VtR, nextpnr) — resources

Loose collection, 2026-10-19. Drive links are publicly shared (anyone with the link).

## Tim's Google Drive (public)
- [SymbiFlow - Publicly Accessible Docs (folder)](https://drive.google.com/drive/folders/1euSrrszzt3Bfz792S6Ud8Ox2w7TYUZNa) — rr_graph, arch-defs, Interchange material
- [FPGA Interchange - Architectures support and VPR status](https://docs.google.com/spreadsheets/d/1hF7-PpOpa35uik2C2-RYSpY-oFJS2SpbVJj_SF_IAF0/edit) — per-family coverage (vtr.tools shared drive)
- [Open Source (FOSS) FPGA (EDA) Tooling Interchange Formats + Toolchain parts](https://docs.google.com/document/d/1DWZ0G8vehkuZTPs5N3AQqIvZZtLMGzC8i0MWPRP54O4/edit) — flow stages and formats
- [FPGA Tooling Common Interchange Formats](https://docs.google.com/document/d/1qc-iXMv3XzU21WV1qaQLtx7658nH_xqwIdqNOjR7qQM/edit) — origin of the Interchange idea
- [SymbiFlow Interchange Format Slides](https://docs.google.com/presentation/d/1Odulf22CnW576RIPK5_x6CcOJw3WHR4THHecVht29HM/edit)
- [FPGA Interchange Testing Flow - Xilinx](https://docs.google.com/drawings/d/12SjkmrsoI-Me4feKJoUV5F_0cfH75AoWoEqyvfI2Uuw/edit) — test flow diagram
- [FPGA Interchange Testing Flow - Lattice](https://docs.google.com/drawings/d/1LJhCu1kbWKb59J-oCXq1f8OYwEG-ZtkLXCvXU1Mztic/edit) — Antmicro
- [Extend python-fpga-interchange with API to manipulate device resources data](https://docs.google.com/document/d/1JMyMzeEkX5Qhqv1x_HGlGOqQ-byF2lWgv77nwAW6kuQ/edit)
- [FPGA Interchange Static Timing Analyzer](https://docs.google.com/document/d/1IF_0xrNwdtniwfWdvGdhWJqaYxDrg2FE0aKU9D4tLog/edit) — timing gap
- [FPGA Interchange macros & chains](https://docs.google.com/document/d/1-0RF7cuNoZl2t0McTYgoXyxXa_8Tqu3JFw9ZL7bLF-I/edit) — carry chains, macros
- [NISP - Nextpnr-fpga_interchange Preprocessor](https://docs.google.com/document/d/17Z8h7ilPLeUxEOpE2ai4llPSRYKI3iV0BvChmYlbmew/edit) — Antmicro
- [nextpnr-fpga_interchange profiling](https://docs.google.com/document/d/1RbrgMjJrPBTEubNMsnTpOfkv_Nb0t7zx1bHCYSUVVZI/edit) — Antmicro, runtime hotspots
- [nextpnr "Try Hard" mode](https://docs.google.com/document/d/1o548m8mJnFTck2-i1A0sSXoe3VvL32irySqE5NBJvPY/edit) — QoR via more effort
- [VTR Roadmap](https://docs.google.com/document/d/1_iRjx-ldLZbxySe-6X13qLZYgU899mnfgJS8_WtCQQY/edit) — Vaughn Betz (U Toronto)
- [vtr_8_preliminary_2018_10_24](https://docs.google.com/presentation/d/1kyBo9lDmp5efoJC5umOEKjtqDQMQqqc7bx-cuJauUwQ/edit) — VTR 8 preview deck
- [VtR Python API Design Doc](https://docs.google.com/document/d/1Pd_ygB0PvSq_gPEYIm8sJEF-mYY2nk3kLsazLVL21uw/edit)
- [VtR -- Performance Profiling](https://docs.google.com/document/d/1JYFp9-ei36Tt_j8cYpTfgksZ3pNySMGoENTQSXCksxg/edit)
- [Building real world rr_graphs to use with VPR](https://docs.google.com/document/d/17QBzXAul8ioGL7WeTXk0awwspGIDZBZgTYUKy5oT_Gg/edit)
- [Making a VPR routing graph from prjxray](https://docs.google.com/document/d/1tigU9696M8LWO46nQBBcO1Uta7cwmXg-QylktISOc4o/edit)
- [7-series VPR routing fabric modelling](https://docs.google.com/document/d/1KwERVU2Fpdgf1O0HCJT-Ri7kZCUzR_E4Aokn-LdTyPc/edit)
- [Issues with using VPR for real FPGAs](https://docs.google.com/document/d/1hnewPcFXcXvUy7IxiiwKidr0lnimxA00ZiK9gGdxrJw/edit) — Antmicro, gap list
- [VPR Proposal for supporting equivalent placement types](https://docs.google.com/document/d/1LQ0H2C9IFnCVtSuaniCs1dDmBoMBWwBQLKAGuo_kSc0/edit)
- [SymbiFlow Architecture Definitions work](https://docs.google.com/presentation/d/1wTZowU46lKCnjKwBb5B_p0_rqfvL33PibzEND4QB0VY/edit)
- [FPGA PnR tool terminology](https://docs.google.com/document/d/1sa3xjAKJxZW8S72NU7HndPksgWhxBFv0VnfcOz0_woY/edit) — nextpnr vs VPR vs vendor terms

## Talks and presentations
- [OrConf19 - v2x - Generation of VPR Architecture from Verilog Files](https://docs.google.com/presentation/d/1KKjIJHskaowFeJR7Llllrg0Dua_DpE9BIdZTlpoVTRk/edit)

## Projects and repositories
- [nextpnr](https://github.com/YosysHQ/nextpnr) — iCE40, ECP5, Nexus, Gowin, GateMate, himbaechel
- [nextpnr-xilinx](https://github.com/gatecat/nextpnr-xilinx) — 7-series / UltraScale+ fork
- [Verilog to Routing (VTR/VPR)](https://github.com/verilog-to-routing/vtr-verilog-to-routing) — [verilogtorouting.org](https://verilogtorouting.org)
- [fpga-interchange-schema](https://github.com/chipsalliance/fpga-interchange-schema) — Cap'n Proto schema
- [python-fpga-interchange](https://github.com/chipsalliance/python-fpga-interchange) — ~40 unmerged branches
- [fpga-interchange-tests](https://github.com/chipsalliance/fpga-interchange-tests) — ~25 open PRs
- [RapidWright](https://github.com/Xilinx/RapidWright) — AMD's Interchange producer/consumer
- [f4pga-arch-defs](https://github.com/f4pga/f4pga-arch-defs) — VPR architecture definitions
- [Yosys](https://github.com/YosysHQ/yosys) — synthesis front end for all of the above

## Papers and other reading
- Murray et al., "VTR 8: High-performance CAD and customizable FPGA architecture modelling" (ACM TRETS, 2020)
- Shah et al., "Yosys+nextpnr: an open source framework from Verilog to bitstream for commercial FPGAs" (FCCM 2019)
- Lavin and Kaviani, "RapidWright: Enabling custom crafted implementations for FPGAs" (FCCM 2018)
