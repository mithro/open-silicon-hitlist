# Partial hardening — resources

Loose collection, 2026-10-21. Drive links are publicly shared (anyone with the link).

## Tim's Google Drive (public)
- [Interface / Computation / Storage -- Complete (Open) Silicon Ecosystem ("Way of thinking")](https://docs.google.com/presentation/d/1LD-dE5ID98Kfb1dc6jWuprDgtSDS5p8-BL8j6nobjqk/edit) — performance-critical, flexibility-critical and non-critical split
- [Partial "sea of gates" with FPGA ASIC for cheaper / faster custom designs?](https://docs.google.com/drawings/d/1hO_vX0DC1GOOrL0gFCCeaXAXhqpA_AFCJ7mnqZZJIbM/edit) — hybrid hard and programmable die idea
- [ASIC with FPGA Harness](https://docs.google.com/drawings/d/1iXQW7JOGi_LUP37g6Y4jMcrJRuAju48vB42z3v-9pm4/edit) — ASIC block paired with FPGA logic
- [SKY130 FPGA / eFPGA Tapeouts](https://docs.google.com/spreadsheets/d/1DVIkQgD9HWo5R26ULP5lPq6iadIxdeXA1CpPbhjOINo/edit) — eFPGA fabrics already proven on open shuttles
- [Open source FPGA generators and opportunity with ReRAM references](https://docs.google.com/document/d/19vSZ2pC5gxm7_j6NhX7hes4hmHZy4vYofzJCjyA6GFo/edit) — eFPGA generator survey, non-volatile configuration
- [LiteX based interface for Hardware Accelerators — j.mp/litex-ha-dd](https://docs.google.com/document/d/1oiTqR-6ppiObBRFA91sxl3sgHkPHw2WK_tFD5itx9xg/edit) — candidate interface between hard block, fabric and CPU
- [Soft Processor (RISC-V) Performance on modern FPGAs](https://docs.google.com/document/d/1AXImPy8gu668WqMP_dKUdVTMNTH35udxiFH-wzBFUzk/edit) — cost of logic left soft versus hardened
- [wafer.space - GF180MCU Gate Array (bit.ly/ws-gatearray-v1)](https://docs.google.com/document/d/1fs6V-7rEOaixsN88ZM_rbp1WFtheEz0K0Ui6tlUtnBk/edit?tab=t.0) — another middle ground between full custom and programmable (listed on mith.ro)

## Projects and repositories
- [FABulous](https://github.com/FPGA-Research/FABulous) — eFPGA generator with integrated CAD flow
- [OpenFPGA](https://github.com/lnis-uofu/OpenFPGA) — eFPGA IP generator
- [OpenROAD](https://github.com/The-OpenROAD-Project/OpenROAD) — open hardening of the ASIC core
- [LiteX](https://github.com/enjoy-digital/litex) and [VexRiscv](https://github.com/SpinalHDL/VexRiscv) — SoC integration and CPUs for the software part
- [ESP](https://github.com/sld-columbia/esp) — heterogeneous SoC platform with accelerator integration flow
- [Chipyard](https://github.com/ucb-bar/chipyard) — RISC-V SoC generator with accelerators
- [CFU Playground](https://github.com/google/CFU-Playground) — profile-driven custom instructions, a small-scale version of the split
- [PandA-bambu](https://github.com/ferrandi/PandA-bambu) — high-level synthesis for moving software hot spots to hardware
- [Tiny Tapeout](https://tinytapeout.com) and [wafer.space](https://wafer.space) — cheap shuttles for test chips

## Papers and other reading
- [Gupta and De Micheli, "Hardware-software cosynthesis for digital systems" (IEEE Design & Test, 1993)](https://doi.org/10.1109/54.232470) — classic hardware/software partitioning
- [Whatmough et al., "A 16nm 25mm2 SoC with a 54.5x Flexibility-Efficiency Range from Dual-Core Arm Cortex-A53 to eFPGA and Cache-Coherent Accelerators" (VLSI Symposium 2019)](https://doi.org/10.23919/vlsic.2019.8778002) — CPU, eFPGA and hard accelerators on one die
- [Schiavone et al., "Arnold: An eFPGA-Augmented RISC-V SoC for Flexible and Low-Power IoT End Nodes" (IEEE TVLSI, 2021)](https://doi.org/10.1109/tvlsi.2021.3058162) — RISC-V SoC with eFPGA in silicon
- [Davidson et al., "The Celerity Open-Source 511-Core RISC-V Tiered Accelerator Fabric" (IEEE Micro, 2018)](https://doi.org/10.1109/mm.2018.022071133) — tiered general, manycore and specialised compute
- [Giri et al., "Accelerator Integration for Open-Source SoC Design" (IEEE Micro, 2021)](https://doi.org/10.1109/mm.2021.3073893) — generating the glue for accelerators
- [Koch et al., "FABulous: An Embedded FPGA Framework" (FPGA 2021)](https://doi.org/10.1145/3431920.3439302) — open eFPGA generator
- [Tang et al., "OpenFPGA: An Open-Source Framework for Agile Prototyping Customizable FPGAs" (IEEE Micro, 2020)](https://doi.org/10.1109/mm.2020.2995854) — open eFPGA generator
- [Baungarten-Leon et al., "Comprehensive RTL-to-GDSII Workflow for Custom Embedded FPGA Architectures Using Open-Source Tools" (Electronics, 2025)](https://doi.org/10.3390/electronics14193866) — fully open eFPGA hardening
- [Kuga et al., "An eFPGA Generation Suite with Customizable Architecture and IDE" (IEICE Trans., 2022)](https://doi.org/10.1587/transfun.2022vlp0008) — another eFPGA generator
- [Bhandari et al., "Not All Fabrics Are Created Equal: Exploring eFPGA Parameters for IP Redaction" (IEEE TVLSI, 2023)](https://doi.org/10.1109/tvlsi.2023.3301334) — choosing which logic goes into the fabric
