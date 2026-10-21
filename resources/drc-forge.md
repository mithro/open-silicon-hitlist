# Design rule checking (DRC) — resources

Loose collection, 2026-10-19. Drive links are publicly shared (anyone with the link).

## Tim's Google Drive (public)
- [Design Rule Check (DRC) Testing - How testing for DRC rules should be done - bit.ly/drc-testing](https://docs.google.com/document/d/18z-FBJHni6qt1WR_tF6bbRHfQydKcFMAVnuj4Ixbj90/edit) — per-rule pass/fail test design (core source)
- [Building a (future) open source process design kit (PDK) - bit.ly/build-pdk](https://docs.google.com/document/d/1Y-RbdGYOzswOI5EkUuCKZnWjdT1K9UbGQc_CbcIQ9O4/edit) — rules that state their reason
- [Skywater S130 DRC Rules](https://docs.google.com/spreadsheets/d/1CfV_HhjUAwmd18YbjZIqx4D-T-h_PPBM0EovhRsn7hk/edit) — SKY130 rules in table form
- [SKY130 (SkyWater PDK) -- Layer (GDS-II / Magic / Calibre / etc) Information - (public)](https://docs.google.com/spreadsheets/d/1oL6ldkQdLu-4FEQE0lX6BcgbqzYfNnd1XA8vERe0vpE/edit) — layer map across Magic/KLayout/Calibre
- [(Open Source) PDK Python Tooling - bit.ly/python-pdk](https://docs.google.com/document/d/1VZIpYx0FN1oMd2KW_oWL1gsQbssSM8JEJjRJVLamNI0/edit) — generated docs, incl. rule docs
- [Test and verification for ASIC designs options exploration - bit.ly/test-asics](https://docs.google.com/document/d/1_StmqBumyTuTNVcvutiX-INbbLG7DHoGl_fe0lvQPZ8/edit) — verification gap map (DRC/LVS/equivalence)
- [ASIC - Develop a web-app/apis for layout editing for Magic ](https://docs.google.com/document/d/19QggoAzZNRfmZivzbPWcjnxjhU8WOjfFSPn39mVEmMw/edit) — Magic layout tooling idea
- [Flip flop layout for combinational cells testing (OpenROAD and friends) (public / external)](https://docs.google.com/drawings/d/1Eoudc5e_taZ3p89ekMXDwyGZuj86M8T_Nj7q1vHG1UE/edit) — test layout pattern for OpenROAD
- [Open silicon papers: open PDKs (SKY130, GF180MCU, IHP SG13G2, ICsprout 55nm, ASAP7)](https://docs.google.com/spreadsheets/d/1rnYLgN1HiMaoYCYaylvfCamYu_8skDzefw1K_RzycYw/edit) — papers tracker; source of benchmark designs and DRC reproducibility work

## Talks and presentations
- Tim's design docs index (public): https://preview.mith.ro/pr-3/design-docs/

## Projects and repositories
Engines and decks
- KLayout (DRC/LVS scripting, tiled and deep modes): https://github.com/KLayout/klayout
- Magic: https://github.com/RTimothyEdwards/magic
- Netgen (LVS): https://github.com/RTimothyEdwards/netgen
- SKY130 PDK (rules docs): https://github.com/google/skywater-pdk
- GF180MCU PDK (KLayout DRC/LVS decks): https://github.com/google/gf180mcu-pdk — archived 2026-09-23
- IHP SG13G2 PDK (KLayout decks): https://github.com/IHP-GmbH/IHP-Open-PDK
- open_pdks: https://github.com/RTimothyEdwards/open_pdks
- efabless mpw_precheck (shuttle DRC gate): https://github.com/efabless/mpw_precheck — inactive; continued at chipfoundry/mpw_precheck
- chipfoundry/mpw_precheck (live SKY130 and GF180MCU precheck decks; `src/cf_precheck/drc_scripts/`): https://github.com/chipfoundry/mpw_precheck — active, Apache-2.0 (deck headers GPL-3.0)
- fossi-foundation/mpw_precheck (the fork open_pdks pins for SKY130): https://github.com/fossi-foundation/mpw_precheck
- fossi-foundation gf180mcu_fd_pv (live GF180MCU KLayout deck `gf180mcu.drc`, pytest harness; pinned by open_pdks): https://github.com/fossi-foundation/globalfoundries-pdk-libs-gf180mcu_fd_pv — active, Apache-2.0
- efabless gf180mcu_fd_pv (older GF180MCU deck with per-table tests): https://github.com/efabless/globalfoundries-pdk-libs-gf180mcu_fd_pv — inactive since 2023-11, Apache-2.0
- Tiny Tapeout support tools (precheck: Magic plus KLayout): https://github.com/TinyTapeout/tt-support-tools — active, Apache-2.0
- wafer.space GF180MCU project template: https://github.com/wafer-space/gf180mcu-project-template — active, Apache-2.0
- wafer.space GF180MCU precheck: https://github.com/wafer-space/gf180mcu-precheck — active, Apache-2.0
- OpenDRC (GPU research engine, four check types): https://github.com/opendrc/opendrc — inactive since 2023-09, MIT
- Rule2DRC benchmark code: https://github.com/snu-mllab/Rule2DRC — active, MIT (dataset licence unknown)
- gdsfactory (programmatic GDS for test layouts): https://github.com/gdsfactory/gdsfactory
- Proprietary references: Siemens Calibre, Cadence Pegasus (distributed DRC)

Benchmark design sources
- Tiny Tapeout: https://tinytapeout.com/
- wafer.space: https://wafer.space/

## Papers and other reading
- Kim, Byun, Hwang, Park and Song, "Rule2DRC: Benchmarking LLM Agents for DRC Script Synthesis with Execution-Guided Test Generation" (2026), [arXiv:2605.15669](https://arxiv.org/abs/2605.15669): 1,000 KLayout DRC tasks (310 from the SkyWater 130 rules), scored by execution
- Chamalet 2026, "Reproduction Records and Sources for Reproducibility of Open-Source DRC and LVS Verdicts for Public Sky130A Layout Cells" (dataset), [doi:10.5281/zenodo.23137757](https://doi.org/10.5281/zenodo.23137757): whether open DRC/LVS verdicts (Magic, Netgen, KLayout) on Sky130A cells reproduce across versions
- He et al. 2023, "OpenDRC", DAC, [doi:10.1109/dac56929.2023.10247734](https://doi.org/10.1109/dac56929.2023.10247734): GPU-accelerated open design rule checking
- MOSIS SCMOS design rules (rev 8): a classic example of rules written with explanations
