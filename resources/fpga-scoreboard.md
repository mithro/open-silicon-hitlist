# FPGA benchmarking (open vs vendor) — resources

Loose collection, 2026-10-19. Drive links are publicly shared (anyone with the link).

## Tim's Google Drive (public)
- [SymbiFlow FPGA Tool Performance (Xilinx Performance)](https://docs.google.com/document/d/16L50pyS3RjYStvRKRoWyVac7NoZKyu45fpPQXJqeKYo/edit) — fpga-tool-perf spec, seed study
- [FPGA Tool Perf Rework Needed](https://docs.google.com/document/d/1sgWYXiyrHawk0i5ymUTBA6QP6YnD9m5YHbreA3wAogg/edit) — what broke in the old harness
- [Soft Processor (RISC-V) Performance on modern FPGAs](https://docs.google.com/document/d/1AXImPy8gu668WqMP_dKUdVTMNTH35udxiFH-wzBFUzk/edit) — soft-CPU PPA targets
- [Benchmarking FPGA CPU Designs](https://docs.google.com/document/d/1Z_FAfFPszk8nreLSvssLmDGayXmF4hmh6R8fMxUEZPM/edit) — method (with IBM/OpenPOWER input)
- [LiteX Soft-CPU, FPGA and Firmware Support](https://docs.google.com/spreadsheets/d/1XTHfdYXuvwoYdPXm4M6qDA0D2fZCPy220-9q6qZpTw4/edit) — CPU x board matrix
- [Yosys May 30 vs. July 02 on PRflow Rosetta Leaves](https://docs.google.com/spreadsheets/d/1oMg5nAcfRzRGFXAD9--0_ACCpKyl-tr25DeC3Z_dgMM/edit) — UPenn regression comparison
- [VtR -- Data Collection and Analysis](https://docs.google.com/document/d/1wrc6jBPw8f0v4o8ENuQuSGm1yXEJwAqRAiN-1uhzDCU/edit) — metrics collection
- [VtR -- Performance Profiling](https://docs.google.com/document/d/1JYFp9-ei36Tt_j8cYpTfgksZ3pNySMGoENTQSXCksxg/edit) — runtime profiling
- [CI system with Arty hardware for FPGA Tooling](https://docs.google.com/document/d/1H3x34bdztWy-uN8EYe-FxJL2YojIjd-0feL9d8BMtN4/edit) — hardware-in-the-loop CI
- [Testing environments and CI for open hardware projects](https://docs.google.com/document/d/1YgJ-MUC-r9-Stl1M98xjTq8Qf-YQy6LNu38Ov5K5pt0/edit) — CI landscape
- [NeTV2 for fpgas.online](https://docs.google.com/document/d/13G_kHRMXtH4D2gqP0eD5F9i5Kb42xDtPgQAccq0Migo/edit) — board farm addition
- [Arty + RPi High Level Wiring Diagram (fpgas.online)](https://docs.google.com/drawings/d/1N-UI958MvaZnchtrwlIlQ1Z8vxTZb-JY3wyjCGp2_8k/edit) — farm node design
- [Tiny Tapeout Online like fpgas.online](https://docs.google.com/document/d/1nxh9IU4fiWmDl0Qpxg611UzboF1wI374F7qQg6SPS3s/edit) — same farm for ASIC boards

## Projects and repositories
- [fpga-tool-perf](https://github.com/chipsalliance/fpga-tool-perf) — open vs Vivado benchmark harness (unmaintained)
- [fpgas.online](https://fpgas.online) — remote FPGA board farm
- [edalize](https://github.com/olofk/edalize) — tool launcher where report parsers belong
- [LiteX](https://github.com/enjoy-digital/litex) and [linux-on-litex-vexriscv](https://github.com/litex-hub/linux-on-litex-vexriscv) — realistic SoC benchmark designs
- [VTR benchmarks](https://github.com/verilog-to-routing/vtr-verilog-to-routing) — VTR, Titan and Koios suites ship with VTR
- [EPFL combinational benchmark suite](https://github.com/lsils/benchmarks)
- [Yosys](https://github.com/YosysHQ/yosys), [nextpnr](https://github.com/YosysHQ/nextpnr) — open flows under test

## Papers and other reading
- Murray et al., "Titan: Enabling large and complex benchmarks in academic CAD" (FPL 2013)
- Arora et al., "Koios: A deep learning benchmark suite for FPGA architecture and CAD research" (FPL 2021)
- Amarú et al., "The EPFL combinational benchmark suite" (IWLS 2015)

## Also listed on mith.ro

- [Carl's Arty CI for Tim - Pictures and Links - bit.ly/carl-arty](https://docs.google.com/document/d/1jyodwCNK-9mokDAe6X1AMhEDPW-qPeqPTHI-z9aUGVg/edit)
