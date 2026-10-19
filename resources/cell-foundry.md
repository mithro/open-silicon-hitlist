# Standard cell generation — resources

Loose collection, 2026-10-19. Drive links are publicly shared (anyone with the link). Includes IO cells.

## Tim's Google Drive (public)
Standard cells
- [wafer.space - Notes around voltages and options for I/O and standard cells - bit.ly/ws-gf180mcu-stdcells](https://docs.google.com/document/d/1vQCrkIvE0MdizFUSRD8Sxo-BBnwj0SztJd-1aU5nRRs/edit) — voltage/track options for GF180MCU (core source)
- [wafer.space - GF180MCU Standard Cell um sizing](https://docs.google.com/spreadsheets/d/1__CaMhJ88QpAhJFrScrBWYnRrFHs8kl6nTi9r7uFDIw/edit) — GF180MCU cell dimensions
- [wafer.space - GF180MCU metal to standard cell sizing comparison](https://docs.google.com/drawings/d/1SaiOaU_0zsvS1woV1bmsTb6vF3R0fk8iL3YWnFGUV0g/edit) — metal pitch vs cell size
- [wafer.space - GF180MCU Random Small Things (like new standard cells)](https://docs.google.com/document/d/1mgT8xbG41T9sk0-hP0JaGTUg8b9GmdSfF66FsgRUBuo/edit) — missing GF180MCU cells
- [3 metal layer standard cell design](https://docs.google.com/drawings/d/14ce1bUE655Hvn_o3eGN1v4xwxl89xPFZppUj3WwRad0/edit) — 3-metal cell idea
- [Standard Cell Library Generator - LibreSilicon / Philipp Gühring](https://docs.google.com/presentation/d/1cG3p8pvLDLercdtif88P7D9Le48mxK67Q3UXDyKnKyA/edit) — LibreSilicon generator talk
- [Open-Source Standard Cell Characterization](https://docs.google.com/document/d/11C_-Z9wbetNNtIjxXg8M3MSLq2Lh861kUaBmmaKOt_0/edit) — open characterisation (Teo Ene)
- [Standard Cell List for DTCO / Pathfinding](https://docs.google.com/document/d/1ByKOMY7ENfotWeb_D52MB5mCHcxQSvJWbd_pPfhmoOA/edit) — cell list for DTCO (UCSD, A. Kahng)
- [SKY130 (SkyWater PDK) -- Standard Cells in libraries Index (public)](https://docs.google.com/spreadsheets/d/1KMZ215M_7YQb0l-vCyVdzSsRzaSJN4VVGsTwf4wFK3k/edit) — SKY130 cell index
- [SKY130 (SkyWater PDK) -- Standard Cell Library Cell sizing Comparison (public)](https://docs.google.com/spreadsheets/d/1il_87E5sJ2WKciwEPlG8IymWsnheIlpBkUOxmTkHWyA/edit) — SKY130 library comparison
- [(needs work?) ASIC -- Automatic datasheet generation from standard cell libraries in Sphinx](https://docs.google.com/document/d/1Uw59pAHFCRA5p3qoV6QInFSwDkosuthec7oQAjOFboM/edit) — generated cell datasheets
- [ASIC Intern Project -- Automatic datasheet generation from standard cell libraries in Sphinx](https://docs.google.com/document/d/1ipsA0do27OIwNCo_XVxx43FXAZXhJlyQ7A09MrO-42g/edit) — same, intern scope
- [SkyWater PDK Data Improvement Project](https://docs.google.com/document/d/1Dlb1ihhIgsCmUzM0pHo7BV2UQb1zsRoaLqhSSd_JYrc/edit) — SPICE-to-Liberty and per-cell docs gaps
- [Inspirational Information on 130nm Process Node - j.mp/si130nm](https://docs.google.com/document/d/1sMmoCfS5l6Uz8sl9Bk3R32XtsdZmC1Hw6bY9nm6r-PA/edit) — gate-density targets at 130nm
- [GF180 IO and Std Cell Library Measurements](https://docs.google.com/document/d/1xY8Bs1hBnGedHV0iPN5M4tmC3i43jlTyGoMgv24C3to/edit) — measured GF180 cells and IO (Tiny Tapeout)

IO cells and pad rings
- [Breakdown of files available per cell in the IO library](https://docs.google.com/spreadsheets/d/1ViVg0UHxYHS1964M8TkCkpVxvlV7ocJoWgPB8Mmh6Gc/edit) — SKY130 IO library views (AUC)
- [PADFrame - Chipathon 2023](https://docs.google.com/presentation/d/12w4WBoleFAE4UePdoUf-bxsZR_BttwY3wknBPPJrEHE/edit) — padframe generator (UMich)
- [TT GF180 padframe](https://docs.google.com/spreadsheets/d/1sZCpz6yy-bHGaV2BVG4IZOLBWn--WIddM9pkCQm_Vyc/edit) — Tiny Tapeout GF180 pad ring
- [LVDS IO Pad Random Notes](https://docs.google.com/document/d/1P_EXnUtjxKO571Z1ogq4waMygobbG6v7jpaJnG6-7uw/edit) — LVDS IO notes

## Projects and repositories
Existing libraries
- sky130_fd_sc_hd: https://github.com/google/skywater-pdk-libs-sky130_fd_sc_hd
- GF180MCU 7-track: https://github.com/google/globalfoundries-pdk-libs-gf180mcu_fd_sc_mcu7t5v0
- GF180MCU 9-track: https://github.com/google/globalfoundries-pdk-libs-gf180mcu_fd_sc_mcu9t5v0
- IHP SG13G2 cells (in the PDK): https://github.com/IHP-GmbH/IHP-Open-PDK
- ASAP7 cells: https://github.com/The-OpenROAD-Project/asap7
- Nangate/FreePDK45 Open Cell Library (name only)

IO libraries
- sky130_fd_io: https://github.com/google/skywater-pdk-libs-sky130_fd_io
- gf180mcu_fd_io: https://github.com/google/globalfoundries-pdk-libs-gf180mcu_fd_io

Generators and characterisation
- LibreCell / lclayout, ASTRAN, Libretto (names only)
- CharLib (open Liberty characterisation): https://github.com/stineje/CharLib
- ngspice: https://ngspice.sourceforge.io/ ; Xyce: https://github.com/Xyce/Xyce
- OpenROAD (consumer of the libraries): https://github.com/The-OpenROAD-Project/OpenROAD
- Commercial: Cadence Liberate, Synopsys SiliconSmart

## Papers and other reading
- Ghani, "IO Pad Integrity in Energy-Efficient Neuromorphic Chips" (2026)
- Wang, "A Compact Model with Self-Heating Effect Applying to the SCR Device for ESD Protection" (2025)
