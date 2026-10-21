# Sign-off correlation (open PEX, STA, LVS, IR/EM vs proprietary) — resources

Loose collection, 2026-10-19. Drive links are publicly shared (anyone with the link). README candidate, not yet a full item.

## Tim's Google Drive (public)
- [Open Source ASIC CAD tooling and file formats relationships — bit.ly/cad-ff](https://docs.google.com/spreadsheets/d/14f1R7LdGAmY7LGJOmKO0c3akV7ctFelNITSxVAIg7Q0/edit) — per sign-off function: proprietary tool vs open counterpart
- [Test and verification for ASIC designs options exploration — bit.ly/test-asics](https://docs.google.com/document/d/1_StmqBumyTuTNVcvutiX-INbbLG7DHoGl_fe0lvQPZ8/edit) — gate-level/SDF sim and verification gaps
- [Open Source EDA - Roadmap (Nov 2024)](https://drive.google.com/file/d/1dVIi6BnwZg78IU1jd8Iq7z0UYfAnwBdW/view) — EU roadmap (FOSSi et al.); PEX, LVS, reliability, rule-format gaps
- [Timing Closure](https://docs.google.com/document/d/13J1AY1zhzxur8vaFs3rRW9ZWX113rSDs63LezOOoXZ8/edit) — Jeff DiCorpo (Efabless), timing closure in open flows
- [Heuristic Flow in OpenLane for Signoff Hold Timing Fixes](https://docs.google.com/document/d/1RYWNeVjQpBkMhN1LGLOyMwwtLzFAENI-veqsfWg-5v8/edit) — UMich (Mehdi Saligane's group)
- [SymbiFlow Toolchain with Vivado Sign-Off Process](https://docs.google.com/drawings/d/18kMbl0OH-VbUbYPrFXu6euYAvD0cpuerKj6GGSucVmM/edit) — FPGA analogue: open flow, vendor sign-off

## Projects and repositories
- [OpenSTA](https://github.com/parallaxsw/OpenSTA) — static timing (multi-corner, SPEF)
- [OpenROAD](https://github.com/The-OpenROAD-Project/OpenROAD) — OpenRCX extraction, PDNSim IR drop, OpenSTA integration
- [Magic](https://github.com/RTimothyEdwards/magic) — extraction (`ext2spice`, `ext2spef`)
- [Netgen](https://github.com/RTimothyEdwards/netgen) — LVS
- [KLayout](https://github.com/KLayout/klayout) — LVS and device extraction, DRC
- [ngspice](https://ngspice.sourceforge.io/) and [Xyce](https://github.com/Xyce/Xyce) — post-layout SPICE
- [FasterCap / FastFieldSolvers](https://www.fastfieldsolvers.com/) — field-solver capacitance reference
- [SymbiYosys](https://github.com/YosysHQ/sby) and [EQY](https://github.com/YosysHQ/eqy) — formal and equivalence checking
- [OpenLane 2](https://github.com/efabless/openlane2) and [OpenROAD-flow-scripts](https://github.com/The-OpenROAD-Project/OpenROAD-flow-scripts) — flows with sign-off steps
- [IHP SG13G2 PDK](https://github.com/IHP-GmbH/IHP-Open-PDK), [SKY130](https://github.com/google/skywater-pdk), [GF180MCU](https://github.com/google/gf180mcu-pdk) — correlation targets with real tapeouts

## Papers and other reading
- Kahng et al., OpenROAD project papers (e.g., "Toward an Open-Source Digital Flow: First Learnings from the OpenROAD Project", DAC 2019)
- Proprietary golden references: Synopsys PrimeTime / StarRC, Cadence Tempus / Quantus / Voltus, Siemens Calibre xRC / nmLVS, Ansys RedHawk
- Tim's papers corpus (Drive copy not public): Rodriguez, "CapBench: A Multi-PDK Dataset for Machine-Learning-Based Post-Layout Capacitance Extraction" (2026)
