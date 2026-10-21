# Design rule checking (DRC) — resources

Loose collection, 2026-10-19. Drive links are publicly shared (anyone with the link).

## Tim's Google Drive (public)
- [Design Rule Check (DRC) Testing - How testing for DRC rules should be done - bit.ly/drc-testing](https://docs.google.com/document/d/18z-FBJHni6qt1WR_tF6bbRHfQydKcFMAVnuj4Ixbj90/edit) — per-rule pass/fail test design (core source)
- [Building a (future) open source process design kit (PDK) - bit.ly/build-pdk](https://docs.google.com/document/d/1Y-RbdGYOzswOI5EkUuCKZnWjdT1K9UbGQc_CbcIQ9O4/edit) — rules that state their reason
- [wafer.space - Getting our GF180MCU submissions to zero DRC errors](https://docs.google.com/document/d/1mENpBOgVsADHeKWgw0jVLRZUdfilxKk5kO27ZlJFP6Q/edit) — real-shuttle DRC clean-up experience
- [wafer.space Run #2 - DRC Settings](https://docs.google.com/document/d/1nqBgG2RUrPm5rzsmBkpo10KRJk3hDvhBW6oZ5wgq_LQ/edit) — DRC settings used for a GF180MCU run (by leomoser99)
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
- GF180MCU PDK (KLayout DRC/LVS decks): https://github.com/google/gf180mcu-pdk
- IHP SG13G2 PDK (KLayout decks): https://github.com/IHP-GmbH/IHP-Open-PDK
- open_pdks: https://github.com/RTimothyEdwards/open_pdks
- efabless mpw_precheck (shuttle DRC gate): https://github.com/efabless/mpw_precheck
- gdsfactory (programmatic GDS for test layouts): https://github.com/gdsfactory/gdsfactory
- Proprietary references: Siemens Calibre, Cadence Pegasus (distributed DRC)

Benchmark design sources
- Tiny Tapeout: https://tinytapeout.com/
- wafer.space: https://wafer.space/

## Papers and other reading
- Kim, Byun, Hwang, Park and Song, "Rule2DRC: Benchmarking LLM Agents for DRC Script Synthesis with Execution-Guided Test Generation" (2026), [arXiv:2605.15669](https://arxiv.org/abs/2605.15669): 1,000 KLayout DRC tasks (310 from the SkyWater 130 rules), scored by execution
- 2026 dataset testing whether open DRC/LVS verdicts (Magic, Netgen, KLayout) on Sky130A cells reproduce across versions (listed in the papers tracker above)
- MOSIS SCMOS design rules (rev 8): a classic example of rules written with explanations
