# Reproduce important ASIC and FPGA papers — resources

Loose collection, 2026-10-19. Drive links are publicly shared (anyone with the link).

## Tim's Google Drive (public)
- [Open silicon papers: open PDKs (SKY130, GF180MCU, IHP SG13G2, ICsprout 55nm, ASAP7)](https://docs.google.com/spreadsheets/d/1rnYLgN1HiMaoYCYaylvfCamYu_8skDzefw1K_RzycYw/edit) — main tracker, ~300 SKY130 papers
- [Open silicon papers: tapeout programs (Tiny Tapeout, wafer.space)](https://docs.google.com/spreadsheets/d/1FnvCsk6R_SQZfqlJ2hrF43pzV0cVuwTJ28z773s_1fI/edit) — papers from shuttle designs
- [Open silicon papers: base data for the Stats tabs](https://docs.google.com/spreadsheets/d/1uRbEzLtt_iosz4ateQ4kq5m2VGajCRTdYipNQfk-xDs/edit) — raw data behind the trackers
- [180nm processes papers](https://docs.google.com/spreadsheets/d/1iPfSN9yspyovaxq8oBqSr12wQNFDHGDdvTnJ6tjuwDA/edit) — 180nm paper set
- [Benchmarking FPGA CPU Designs](https://docs.google.com/document/d/1Z_FAfFPszk8nreLSvssLmDGayXmF4hmh6R8fMxUEZPM/edit) — soft-CPU comparison method
- [vtr_8_preliminary_2018_10_24](https://docs.google.com/presentation/d/1kyBo9lDmp5efoJC5umOEKjtqDQMQqqc7bx-cuJauUwQ/edit) — VTR 8 results deck
- [Tim's rework of Teo's Adder slides](https://docs.google.com/presentation/d/1amfSPuLVciFnsExunL_Ch0vYU8hU6XmElnPCdg268Kw/edit) — adder architecture trade-offs
- [Improving operator mapping in Yosys for ASICs](https://docs.google.com/document/d/1N4huvzOsGuEjiBCXDKPMpWfxoxpc40XFDhyxjcdtwwg/edit) — re-testing arithmetic choices

Note: the "Open Silicon Papers" folder (with its Papers and Topics subfolders, ~350 PDFs) is domain-only, not public.

## Projects and repositories
- [fpgas.online](https://fpgas.online) ([source](https://github.com/fpgas-online)) — real Artix-7 boards for replaying FPGA papers
- [Verilog-to-Routing (VTR)](https://github.com/verilog-to-routing/vtr-verilog-to-routing) — FPGA architecture studies, VTR/Titan/Koios benchmarks
- [ABC](https://github.com/berkeley-abc/abc) — logic synthesis research baseline
- [Yosys](https://github.com/YosysHQ/yosys) — open synthesis
- [OpenROAD-flow-scripts](https://github.com/The-OpenROAD-Project/OpenROAD-flow-scripts) — open ASIC flow for re-runs
- [DREAMPlace](https://github.com/limbo018/DREAMPlace) — GPU placement; example of compute changing old answers
- [RePlAce](https://github.com/The-OpenROAD-Project/RePlAce) — analytic placement
- [TILOS MacroPlacement](https://github.com/TILOS-AI-Institute/MacroPlacement) — model public reproduction of an influential paper
- [Circuit Training](https://github.com/google-research/circuit_training) — the code being reproduced above
- [ASAP7](https://github.com/The-OpenROAD-Project/asap7) — predictive PDK for advanced-node replication

## Papers and other reading
- Kuon & Rose, "Measuring the Gap Between FPGAs and ASICs" (IEEE TCAD 2007) — classic, worth re-measuring
- Ahmed & Rose, "The Effect of LUT and Cluster Size on Deep-Submicron FPGA Performance and Density" (2004) — LUT-size study
- Betz & Rose, "VPR: A New Packing, Placement and Routing Tool for FPGA Research" (1997)
- Mirhoseini et al., "A graph placement methodology for fast chip design" (Nature 2021) — and Cheng et al., "Assessment of Reinforcement Learning for Macro Placement" (ISPD 2023)
- DAC / ICCAD / FPGA / ISPD best-paper lists — source of "important" papers
