# ASIC benchmarking (shuttle-design corpus, PPA vs proprietary) — resources

Loose collection, 2026-10-19. Drive links are publicly shared (anyone with the link).

## Tim's Google Drive (public)
- [Open MPW Repository Descriptions](https://docs.google.com/spreadsheets/d/1vQvdCUJYlQLEy8GNejeW40l78nyi3y9FJvmltSPb2gY/edit) — every SKY130 Open MPW slot, ~360 rows
- [Open MPW Run Manifests Summaries (bit.ly/openmpw-manifest-summaries)](https://docs.google.com/spreadsheets/d/1NcoXWil-ZV8IoG6bKRmdKJUiu8JE8rPTwlNxm9Xqa1Q/edit) — per-shuttle summaries
- [Open MPW Runs folder (bit.ly/sky130-mpw-manifests)](https://drive.google.com/drive/folders/1sWcj8wWxIhtSGrlYJxBpKNhfB_B4lU3j) — tapeout manifests, one per shuttle
- [SKY130 MPW-1 tapeout manifest](https://docs.google.com/spreadsheets/d/1PrRxdMPXz41_Eq22dZU_VpVKBZ7o9DWDc6EvHnX-CpY/edit) — example manifest (repo, commit per slot)
- [SKY130 MPW-2 tapeout manifest](https://docs.google.com/spreadsheets/d/1bIUoi0Pi8wd_FtqgD99NDsCTXFIKv--RVBCv_9ekeN0/edit) — second shuttle manifest
- [GF180MCU MPW-0 (GFMPW-0) tapeout manifest](https://docs.google.com/spreadsheets/d/1vt_ix2tp1s6WedCnyz3Zf_sDZyHR49r04PWI2WMKdzM/edit) — GF180 shuttle corpus
- [gfmpw-1 projects](https://docs.google.com/spreadsheets/d/1qxy1wK-fbegUjC_IC2k6f9NfbdSS9gevUzcF7rFQnfA/edit) — GFMPW-1 project list
- [GFMPW-1 Projects Details Sourcing](https://docs.google.com/spreadsheets/d/1aArPOn0M02siCaohhP4oVotHaAFZEiCiJ15lQaskNNg/edit) — recovering GFMPW-1 project details
- [Open MPW viewer website - requirements](https://docs.google.com/document/d/1YcVW-sLxFwhEJWe4EfJhXq-fRu_f41RE3cu2z58iaD0/edit) — browsable shuttle archive spec
- [SKY130 MPW Silicon that Tim has](https://docs.google.com/spreadsheets/d/1lcQtDYKufgEPqoIMMWmtI8W6HEGA9Ofi-yBoDQcHA0E/edit) — physical silicon available for measurement
- [Inspirational Information on 130nm Process Node (j.mp/si130nm)](https://docs.google.com/document/d/1sMmoCfS5l6Uz8sl9Bk3R32XtsdZmC1Hw6bY9nm6r-PA/edit) — proprietary 130nm chips: gate density, SRAM, cores
- [Process Technologies sizes at 180nm + 130nm + 90nm](https://docs.google.com/spreadsheets/d/1kL4-_4WDMSn4z6TB4NrC2em9Kvh3i4ORAz1VXlAlLVA/edit) — proprietary node reference numbers
- [Open Source SRAM Achieved Results (SKY130 / GF180MCU / IHP SG13G2)](https://docs.google.com/spreadsheets/d/1O2FOcM8blrrgphjqfaYhFVnZL5zYIxU0w4GsqV4uyRc/edit) — open SRAM density vs targets
- [SKY130 SRAM Achieved Results](https://docs.google.com/spreadsheets/d/1TJrGuujPSOE9CAxwnf8IQg4X_veLV4QahXvGOfsVLK4/edit) — SKY130 SRAM data
- [GF180MCU SRAM Achieved Results](https://docs.google.com/spreadsheets/d/1JTLDwcyJMw908QSZAjiLUDdo_IEZ0bTUjtguaUQ9ad8/edit) — GF180MCU SRAM data
- [HD SRAM Area (and eDRAM) sizes on modern process nodes (<32nm)](https://docs.google.com/spreadsheets/d/15b4bxqCPXxfdw36X9poChlp4UzpNfYsG3nE3Ryd7Yv0/edit) — advanced-node comparison points
- [Theoretical maximums of 10mm² user space on SKY130 Open MPW](https://docs.google.com/document/d/1k3LuRPa6-7iM1gC6ocFGLlAFboFiXNTpgXEjTLBbpy4/edit) — what fits in a Caravel slot
- [Tiny Tapeout Sizing Comparisons](https://docs.google.com/spreadsheets/d/1hgfRhANt3jyG4w0tgVumoxdqkyLpXQksTHPXk9g4_NM/edit) — tile area vs logic across PDKs
- [ASIC: performance modeling dashboard of SkyWater 130nm PDK](https://docs.google.com/document/d/1X-rGRxf_rPakyVYGSDEhviJ-LhxNivNpiSR7O3mN8nk/edit) — PPA dashboard project idea
- [Improving operator (adder / multiplier / MAC) mapping in Yosys for ASICs](https://docs.google.com/document/d/1N4huvzOsGuEjiBCXDKPMpWfxoxpc40XFDhyxjcdtwwg/edit) — QoR target the benchmark would measure
- [Hardening Tiny Tapeout Projects Locally](https://docs.google.com/document/d/1aUUZ1jthRpg4QURIIyzlOaPWlmQzr-jBn3wZipVUPt4/edit) — re-running TT flows (Uri Shaked)
- [wafer.space - Getting our GF180MCU submissions to zero DRC errors](https://docs.google.com/document/d/1mENpBOgVsADHeKWgw0jVLRZUdfilxKk5kO27ZlJFP6Q/edit) — signoff status on real submissions
- [Open silicon papers: tapeout programs (Tiny Tapeout, wafer.space)](https://docs.google.com/spreadsheets/d/1FnvCsk6R_SQZfqlJ2hrF43pzV0cVuwTJ28z773s_1fI/edit) — papers with taped-out designs
- [Open silicon papers: open PDKs](https://docs.google.com/spreadsheets/d/1rnYLgN1HiMaoYCYaylvfCamYu_8skDzefw1K_RzycYw/edit) — ~300 SKY130 papers, candidate cases

## Projects and repositories
- [OpenROAD-flow-scripts](https://github.com/The-OpenROAD-Project/OpenROAD-flow-scripts) — reference designs × platforms, metrics CI
- [OpenROAD](https://github.com/The-OpenROAD-Project/OpenROAD) — open P&R
- [LibreLane](https://github.com/librelane/librelane) — successor to OpenLane, used by TT and wafer.space
- [OpenLane](https://github.com/The-OpenROAD-Project/OpenLane) — flow used for Open MPW
- [Caravel user project](https://github.com/efabless/caravel_user_project) — Open MPW harness template
- [Tiny Tapeout GitHub org](https://github.com/TinyTapeout) — shuttle repos and per-project data
- [mithro/tinytapeout-project-search](https://github.com/mithro/tinytapeout-project-search) — Tim's TT project indexer
- [EPFL combinational benchmark suite](https://github.com/lsils/benchmarks) — logic synthesis benchmarks
- [OpenABC-D](https://github.com/NYU-MLDA/OpenABC) — open synthesis dataset
- [CircuitNet](https://github.com/circuitnet/CircuitNet) — open EDA ML dataset
- [ASAP7 PDK](https://github.com/The-OpenROAD-Project/asap7) — predictive 7nm for advanced-node comparisons
- foss-eda-tools.googlesource.com — original Open MPW shuttle manifest source

## Papers and other reading
- IWLS 2005 benchmarks, ISCAS-85/89, ITC-99 — classic synthesis/test benchmark sets
- ISPD contest benchmark suites — placement/routing yardsticks
- [mithro-site design-docs preview](https://preview.mith.ro/pr-3/design-docs/) — candidate 7, mineable shuttle archive

## Also listed on mith.ro

- [Efabless open source silicon directory on siliconpr0n.org - bit.ly/sp-open-silicon](https://docs.google.com/spreadsheets/d/103-gxrBH7y1bNmWtZwifcawUAduHDoEVHBN_MyswpBE/edit?gid=0#gid=0)
- [SKY130 MPW-003 (MPW-3) tapeout manifest - bit.ly/sky130-mpw3-manifest (https://foss-eda-tools.googlesource.com/third_party/shuttle/sky130/mpw-003/foundry)](https://docs.google.com/spreadsheets/d/1sipmy_ipP3TtAd-iUZGe7RR80QGmQLt-NC9NIZPvrcg/edit#gid=1361650288)
- [SKY130 MPW-004 (MPW-4) tapeout manifest - bit.ly/sky130-mpw4-manifest (https://foss-eda-tools.googlesource.com/third_party/shuttle/sky130/mpw-004/foundry/)](https://docs.google.com/spreadsheets/d/1PkSiiD9TYDTtiqyQhsw9QQ4jE0UnMAIpTrNCmUbTqIs/edit#gid=1361650288)
- [SKY130 MPW-005 (MPW-5) tapeout manifest - bit.ly/sky130-mpw5-manifest (https://foss-eda-tools.googlesource.com/third_party/shuttle/sky130/mpw-005/foundry)](https://docs.google.com/spreadsheets/d/1K9ypJnyz8znaGCS1PwhpDaVv1TPW_F3p7N4xC9I9EVw/edit#gid=1361650288)
- [SKY130 MPW-006 (MPW-6) tapeout manifest - bit.ly/sky130-mpw6-manifest (https://foss-eda-tools.googlesource.com/third_party/shuttle/sky130/mpw-006/foundry)](https://docs.google.com/spreadsheets/d/1t8HsmLD-c8eMtjBYJvCuW_uIPi64eNzCo80k43SLdQo/edit#gid=1556261536)
- [SKY130 MPW-007 (MPW-7) tapeout manifest - bit.ly/sky130-mpw7-manifest (https://foss-eda-tools.googlesource.com/third_party/shuttle/sky130/mpw-007/foundry)](https://docs.google.com/spreadsheets/d/15YeXvmrCJ8_YMZiqr2Es2P4fUeb6ho4hAZdEfMi5KvA/edit#gid=1556261536)
- [SKY130 Maximum clock frequency (performance / speed) for DFF](https://docs.google.com/spreadsheets/d/1BTvnNFhkFqT4uqZs7uIK6D6QAJ4tRYkpU44OZFgme9Q/edit#gid=1572495657)
- [Target Designs for OpenROAD on Google Cloud Analysis](https://docs.google.com/document/d/1Sn_JL3pbOenT9GnsIKpCRTDATBys9mFvHxP2qOQQozM/edit?resourcekey=0-M-i-wLOSJF7zGoLEeFXT8w#heading=h.lkjye7lihkyi)
