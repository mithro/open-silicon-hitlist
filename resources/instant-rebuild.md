# Incremental toolchains (FPGA and ASIC) — resources

Loose collection, 2026-10-19. Drive links are publicly shared (anyone with the link). Tim has no Drive design doc specifically on incremental flows; the items below are adjacent (tool interchange, partial reconfiguration, timing), which any incremental flow builds on.

## Tim's Google Drive (public)
- [SymbiFlow Partial Reconfiguration Region Use Cases](https://docs.google.com/document/d/1ptKcmD9_qHeAg7sI2HqEFfxZOvzNYfoZx_lH6gtxsUE/edit) — region-level reuse in open FPGA flows (Andrew Butt)
- [Open Source (FOSS) FPGA (EDA) Tooling Interchange Formats + Toolchain parts](https://docs.google.com/document/d/1DWZ0G8vehkuZTPs5N3AQqIvZZtLMGzC8i0MWPRP54O4/edit) — stage boundaries in the flow
- [FPGA Interchange Static Timing Analyzer](https://docs.google.com/document/d/1IF_0xrNwdtniwfWdvGdhWJqaYxDrg2FE0aKU9D4tLog/edit) — standalone STA on interchange data
- [Yosys Timing Annotation support](https://docs.google.com/document/d/1A0ceG2ltz4jttb_KS4tijJrIhxrUcB23V16Sl3StO34/edit) — timing data in synthesis
- [SymbiFlow Toolchain with Vivado Sign-Off Process](https://docs.google.com/drawings/d/18kMbl0OH-VbUbYPrFXu6euYAvD0cpuerKj6GGSucVmM/edit) — mixed open/vendor flow diagram
- [Open Source EDA - Roadmap (Nov 2024)](https://drive.google.com/file/d/1dVIi6BnwZg78IU1jd8Iq7z0UYfAnwBdW/view) — EU roadmap; names hierarchical design and incremental builds as a digital-flow gap
- [[External] Reproducible and signed silicon development environments](https://docs.google.com/presentation/d/1lX_GZo0Aw6juVbB94OMWF2HDPbmkF-5dgOFSMamiRFU/edit) — caching and determinism background

## Projects and repositories
- [Yosys](https://github.com/YosysHQ/yosys) — hierarchical synthesis; no real incremental mode
- [nextpnr](https://github.com/YosysHQ/nextpnr) — no incremental mode; placement constraints and partial reuse are possible starting points
- [VTR / VPR](https://github.com/verilog-to-routing/vtr-verilog-to-routing) — research FPGA P&R; incremental routing literature built on it
- [RapidWright](https://github.com/Xilinx/RapidWright) — pre-implemented blocks and relocatable modules for Xilinx (open Java framework)
- [FPGA Interchange schema](https://github.com/chipsalliance/fpga-interchange-schema) — stage-to-stage data format
- [OpenROAD](https://github.com/The-OpenROAD-Project/OpenROAD) — incremental timing (OpenSTA), ECO hooks, hierarchical flow work
- [OpenSTA](https://github.com/parallaxsw/OpenSTA) — incremental static timing engine
- [KLayout](https://github.com/KLayout/klayout) — DRC is full-chip only today; tiling and deep mode as a base
- [Bazel](https://bazel.build/) and [bazel_rules_hdl](https://github.com/hdl/bazel_rules_hdl) — content-addressed build caching for HDL flows
- [ccache](https://ccache.dev/) — model for caching tool outputs

## Papers and other reading
- Xilinx/AMD Vivado incremental implementation (UG904) and Intel Quartus incremental compilation / design partitions — proprietary reference
- Cadence Innovus and Synopsys Fusion Compiler ECO flows — proprietary reference
- Lavin et al., "RapidWright: Enabling Custom Crafted Implementations for FPGAs" (FCCM 2018)
