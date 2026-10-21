# Adder and multiplier exploration — resources

Loose collection, 2026-10-19. Drive links are publicly shared (anyone with the link).

## Tim's Google Drive (public)
- [Improving operator (adder / multiplier / multiply-accumulate) mapping in Yosys for ASICs](https://docs.google.com/document/d/1N4huvzOsGuEjiBCXDKPMpWfxoxpc40XFDhyxjcdtwwg/edit) — Tim's design doc, the core source
- [Tim's rework of Teo's Adder slides](https://docs.google.com/presentation/d/1amfSPuLVciFnsExunL_Ch0vYU8hU6XmElnPCdg268Kw/edit) — prefix adder exploration deck
- [SKY130 Adder performance](https://docs.google.com/spreadsheets/d/1pTGzZo5XYU7iuUryxorfzJwNuE9rM3le5t44wmLohy4/edit) — measured PPA per adder type (Teodor Ene)
- [adder_implementation.ipynb](https://colab.research.google.com/drive/1bqAWs2To8suxx5acmCYp10iWlKI-Qsn4) — Colab notebook generating adders (Teodor Ene)
- [Design Document on 16bit Floating Point](https://docs.google.com/document/d/1684Tn4aeWxeelCvrJ5maKJoShtlIRolC2oq0c4_4A7k/edit) — fp16 unit design (external author)

## Projects and repositories
- [Yosys](https://github.com/YosysHQ/yosys) — `techmap`, `booth`, `alumacc` passes; target for operator mapping
- [ABC](https://github.com/berkeley-abc/abc) — logic optimisation after mapping
- [OpenROAD](https://github.com/The-OpenROAD-Project/OpenROAD) and [OpenROAD-flow-scripts](https://github.com/The-OpenROAD-Project/OpenROAD-flow-scripts) — PPA characterisation per PDK
- synth_opt_adders (Teodor Ene, GitHub user tdene) — constraint-driven prefix adder generator
- [FloPoCo](https://gitlab.com/flopoco/flopoco) — arithmetic core generator (FPGA-focused, many formats)
- [Berkeley HardFloat](https://github.com/ucb-bar/berkeley-hardfloat) — IEEE floating-point units
- [CIRCT](https://github.com/llvm/circt) — `comb`/`arith` lowering, relevant to datapath generation
- [ASAP7](https://github.com/The-OpenROAD-Project/asap7), [SKY130](https://github.com/google/skywater-pdk), [GF180MCU](https://github.com/google/gf180mcu-pdk) PDKs — characterisation targets

## Papers and other reading
- Roy et al., "PrefixRL: Optimization of Parallel Prefix Circuits using Deep Reinforcement Learning" (NVIDIA, DAC 2021)
- Kogge and Stone (1973); Brent and Kung (1982); Han and Carlson (1987) — classic prefix adder papers
- Wallace (1964) and Dadda (1965) — multiplier reduction trees
- Synopsys DesignWare Building Block IP — proprietary reference for constraint-driven arithmetic selection
- Papers in Tim's papers corpus (Drive copies not public): Ledoux, "Progressive Arithmetic Lowering from Tensor Kernels to Synthesizable Datapaths" (2026); Rizos, "Designing Approximate Reduced Complexity Wallace Multipliers" (2025); Hu, "A datapath compiler with technology portability"; Barbe, "Reconfigurable constant multipliers" (2026)

## Also listed on mith.ro

- [OrConf - Yosys Synthesis Improvements](https://docs.google.com/presentation/d/1lyIW8OLNznzongp_njMGiEq-t7tlyDXnlNR13tUmK7w)
