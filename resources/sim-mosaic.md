# Composable and distributed simulation — resources

Loose collection, 2026-10-19. Drive links are publicly shared (anyone with the link).

## Tim's Google Drive (public)
- [Renode for simulation of the Caravel (and user project) testing system — bit.ly/caravel-renode](https://docs.google.com/document/d/1qhin7U1esp58NoVwrdkKkEDZb2k280YF0PKGENGgLSI/edit) — full-rig Caravel model
- [Efabless Nucleo SKY130 Open MPW Tester Infrastructure: Renode and FPGA based Testing](https://docs.google.com/drawings/d/11wgA2bEIODewvWDxn2f5CLxW6vCnkb9Yxu5HM2M0XT4/edit) — diagram
- [Testing environments and CI for open hardware projects (Open MPW, Caravel, LiteX, F4PGA)](https://docs.google.com/document/d/1YgJ-MUC-r9-Stl1M98xjTq8Qf-YQy6LNu38Ov5K5pt0/edit) — sim/FPGA/silicon test matrix
- [CI system with Arty hardware for FPGA Tooling — bit.ly/ci-arty](https://docs.google.com/document/d/1H3x34bdztWy-uN8EYe-FxJL2YojIjd-0feL9d8BMtN4/edit) — hardware-in-the-loop CI
- [Carl's Arty CI for Tim - Pictures and Links — bit.ly/carl-arty](https://docs.google.com/document/d/1jyodwCNK-9mokDAe6X1AMhEDPW-qPeqPTHI-z9aUGVg/edit) — built rig (fpgas.online precursor)
- [LiteX Bridge Protocol](https://docs.google.com/document/d/1d_Uy6oljyYS4vZhSWomF-IWtP-vDN8qYYra6-Q8KLec/edit) — candidate bridge standard
- [LiteX based interface for Hardware Accelerators — j.mp/litex-ha-dd](https://docs.google.com/document/d/1oiTqR-6ppiObBRFA91sxl3sgHkPHw2WK_tFD5itx9xg/edit) — transport-agnostic seam
- [Renode bridge examples](https://docs.google.com/drawings/d/108zuiInqsXV_MeTDhsdB-bx5khhFz3tvpm0lLTDyKis/edit) — diagram
- [Renode Wishbone Bridge Infrastructure](https://docs.google.com/drawings/d/1tfDZcxK3Ui8EaOnEDisxe8_LyromUIGIFkmcP76gBdc/edit) — diagram
- [Tim's (incomplete) map of Renode ecosystem / parts](https://docs.google.com/drawings/d/196_WW3gu095bS7Y-kkOuKgs9lOSJwGPZsSqb8_OuiyM/edit) — diagram
- [Renode public presentation](https://docs.google.com/presentation/d/1j0gjI4pVkgF9CWvxaxr5XuCKakEB25YX2n-iFxlYKnE/edit) — Antmicro overview deck
- [OpenTitan Peripheral Status (Surelog / Verilator / Yosys / Renode)](https://docs.google.com/spreadsheets/d/1g7R3xjYnI83_cLagv-Bv23CCkycRbcUFUgz1CtSIsL8/edit) — per-block engine support
- [BlackParrot Module Status (Surelog / Verilator / Yosys / Renode)](https://docs.google.com/spreadsheets/d/18okLCMcx55yZ67i5rda6f3ymgqcChlK0-fWjWcqSkeU/edit) — same for BlackParrot
- [OpenTitan Earl Grey - Peripherals supported in Renode](https://docs.google.com/drawings/d/1XyRMs2FfyAO76Ns4hcwZQLdXlQu4NVjuOeAZ37oSZyo/edit) — marked obsolete
- [Eco - Support for 64-bit LiteX in Renode](https://docs.google.com/document/d/1JUqffuu0v_edmwB7oJYelAw7QFPZ8OIfjsZrPpATzYI/edit) — project brief
- [Interactively controlling an STM32F4 simulation in Renode from Colab](https://colab.research.google.com/drive/1pz2XqlqPdqWmomA1B6XgjH0UZs-gICCu) — notebook demo
- [Simulation via treating x86 like a strange FPGA to techmap to](https://docs.google.com/document/d/1gXAhvLjidhGVQeL9b5wACanlExDOVxO551xabUoYuoE/edit) — fast-RTL-sim idea
- [Types of "testing" in LiteX (and Migen/MiSoC)](https://docs.google.com/document/d/1SLRMCTETNKA0Cfy8dExF8QAn8j0FVbUEgorsicJmoeU/edit) — test taxonomy
- [LiteX QEmu Simulation support Random Notes](https://docs.google.com/document/d/1x3YDNqg1xUiLKl85YVvVBWTwHOq1hSWyyRMO-eKLBeQ/edit) — 2017 notes
- [ASIC -- Improving OpenROAD CI integration with Google Cloud Platform](https://docs.google.com/document/d/1QutVnDU8Cytnn2MfXxkh1hydG8x__pwm_wLB2VXVhik/edit) — cloud CI
- [Skywater-pdk Continuous integration](https://docs.google.com/document/d/14RDmAdGrVVn2ArA8pz6RAYGS5Cv4OEGB340wbnXzwmc/edit) — Rob Taylor

## Talks and presentations
- [fpgas.online](https://fpgas.online/) — hosted FPGA board farm for hardware CI

## Projects and repositories
- [Renode](https://github.com/renode/renode) — functional SoC simulator ([renode.io](https://renode.io/)); Verilator co-simulation integration
- renode-verilator-integration (Antmicro) — co-simulation examples
- [Verilator](https://github.com/verilator/verilator) — cycle-accurate RTL simulation, multithreaded
- [cocotb](https://github.com/cocotb/cocotb) — Python testbenches across simulators
- [LiteX](https://github.com/enjoy-digital/litex) — `litex_sim`, Etherbone/UART bridges, `litex_server`
- [Caravel](https://github.com/efabless/caravel) — SKY130 harness modelled in Renode
- [OpenTitan](https://github.com/lowRISC/opentitan) — reference SoC with Verilator and FPGA targets
- [Chipyard FireSim](https://github.com/firesim/firesim) — FPGA-accelerated, distributed cycle-exact simulation
- [ESSENT](https://github.com/ucsc-vama/essent) and RepCut — research on fast and partitioned parallel RTL simulation
- [QEMU](https://www.qemu.org/) and [SystemC / TLM-2.0](https://systemc.org/) — virtual platform and bridge standards
- [GHDL](https://github.com/ghdl/ghdl), [Icarus Verilog](https://github.com/steveicarus/iverilog), [CXXRTL in Yosys](https://github.com/YosysHQ/yosys) — other engines

## Papers and other reading
- Karandikar et al., "FireSim: FPGA-Accelerated Cycle-Exact Scale-Out System Simulation in the Public Cloud" (ISCA 2018)
- Wang and Beamer, "RepCut: Superlinear Parallel RTL Simulation with Replication-Aided Partitioning" (ASPLOS 2023)
- Beamer and Donofrio, "Efficiently Exploiting Low Activity Factors to Accelerate RTL Simulation" (ESSENT, DAC 2020)
- Cadence Palladium hybrid and Synopsys ZeBu + Virtualizer — proprietary hybrid emulation
