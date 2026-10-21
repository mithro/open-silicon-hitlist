# Open wireless with eFPGA and SDR — resources

Loose collection, 2026-10-21. Drive links are publicly shared (anyone with the link).

## Tim's Google Drive (public)
- [Interface / Computation / Storage -- Complete (Open) Silicon Ecosystem ("Way of thinking")](https://docs.google.com/presentation/d/1LD-dE5ID98Kfb1dc6jWuprDgtSDS5p8-BL8j6nobjqk/edit) — wireless as interface IP: analog front end plus flexible logic
- [Index of potentially interesting Analog IP for SKY130 (SkyWater 130nm) PDK - j.mp/si130nm-analog](https://docs.google.com/document/d/10G8b1sWzGrFK1D3bVlRHSX__JLXKm9Deq-qYmblGijE/edit) — open analog blocks a front end could reuse
- [Interesting Analog IP](https://docs.google.com/spreadsheets/d/1e9M9ZcQ4HX5QEEJRDYPAHhfSEJZnBpTYXcMkRziyRe4/edit) — PLL and other analog IP list
- [SKY130 FPGA / eFPGA Tapeouts](https://docs.google.com/spreadsheets/d/1DVIkQgD9HWo5R26ULP5lPq6iadIxdeXA1CpPbhjOINo/edit) — open fabrics that could hold a baseband
- [Intro to Software Radio (PyCon AU 2017)](https://docs.google.com/presentation/d/1uFZ-IcqT5cuVVbqTguRfnmERH3wC0SZisqPJ9WIV_ro/edit) — SDR basics (Jim Mussared)

## Projects and repositories
- [openwifi](https://github.com/open-sdr/openwifi) — open 802.11 baseband in FPGA with Linux driver
- [srsRAN Project](https://github.com/srsran/srsRAN_Project) — open 5G CU/DU software (this repository is archived)
- [OpenAirInterface](https://gitlab.eurecom.fr/oai/openairinterface5g) — open LTE and 5G stack
- [LiteX M2SDR](https://github.com/enjoy-digital/litex_m2sdr) — LiteX-based SDR board with open gateware
- [HackRF](https://github.com/greatscottgadgets/hackrf) — open hardware SDR
- [Ubertooth](https://github.com/greatscottgadgets/ubertooth) — open Bluetooth radio hardware and firmware
- [Proxmark3 (RRG)](https://github.com/RfidResearchGroup/proxmark3) — FPGA-based NFC/RFID reader and emulator
- [FABulous](https://github.com/FPGA-Research/FABulous) and [OpenFPGA](https://github.com/lnis-uofu/OpenFPGA) — eFPGA generators for the reprogrammable baseband
- [IHP SG13G2 open PDK](https://github.com/IHP-GmbH/IHP-Open-PDK) — open BiCMOS PDK aimed at RF
- [SKY130](https://github.com/google/skywater-pdk) and [GF180MCU](https://github.com/google/gf180mcu-pdk) (archived; development continues in its forks) — open PDKs for lower-frequency front ends

## Papers and other reading
- [Jiao et al., "openwifi: a free and open-source IEEE802.11 SDR implementation on SoC" (VTC 2020)](https://doi.org/10.1109/vtc2020-spring48590.2020.9128614) — WiFi baseband in FPGA plus CPU
- [Gomez-Miguelez et al., "srsLTE: An Open-Source Platform for LTE Evolution and Experimentation" (2016)](https://arxiv.org/abs/1602.04629) — open LTE stack
- [Kaltenberger et al., "OpenAirInterface: Democratizing innovation in the 5G Era" (Computer Networks, 2020)](https://doi.org/10.1016/j.comnet.2020.107284) — open 5G stack
- [Ruiz et al., "HELIX: High-speed Real-Time Experimentation Platform for 6G Wireless Networks" (MobiSys 2025)](https://doi.org/10.1145/3711875.3729152) — FPGA and software split for a real-time PHY
- [Fath, "Towards a practical open source RF SoC design flow: Lessons from a 40 GHz tapeout in IHP SG13G2" (2026)](https://doi.org/10.5281/zenodo.21508491) — open RF flow on an open PDK
- [Gilo and Brito Filho, "A 2.4 GHz Wireless Temperature Sensor with 0.93 C precision designed in 130 nm CMOS technology for Internet of Things applications" (IEEE Latin America Trans., 2025)](https://doi.org/10.1109/tla.2025.10974372) — 2.4 GHz radio at 130 nm
- [Yuan et al., "A Temperature-Compensated BLE Beacon and 802.15.4-to-BLE Translator on a Crystal-Free Mote" (EuMC 2022)](https://doi.org/10.23919/eumc50147.2022.9784300) — minimal BLE radio on a research chip
- [Lovell et al., "SCμM-V23: Towards A Crystal-Free System-On-Chip For IoT In 16nm" (CrystalFreeIoT 2024)](https://doi.org/10.1109/crystalfreeiot62484.2024.00008) — single-chip radio SoC from academia
- ["A Digital Twin Platform Enabling Monolithic Crystal-Free Bluetooth Low Energy Single-Chip Sensor Motes" (2026)](https://arxiv.org/abs/2605.24277) — simulating a BLE radio chip before silicon
- ["ProtO-RU: An O-RAN Split-7.2 Radio Unit using SDRs" (2025)](https://arxiv.org/abs/2512.02398) — open cellular radio unit on SDRs and CPUs
