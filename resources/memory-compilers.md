# Memory compilers (SRAM, ROM, register file) — resources

Loose collection, 2026-10-19. Drive links are publicly shared (anyone with the link). README candidate, not yet a full item.

## Tim's Google Drive (public)
Results and sizing
- [Open Source SRAM Achieved Results (SKY130 / GF180MCU / IHP SG13G2)](https://docs.google.com/spreadsheets/d/1O2FOcM8blrrgphjqfaYhFVnZL5zYIxU0w4GsqV4uyRc/edit) — open SRAM results across three PDKs
- [SKY130 SRAM Achieved Results](https://docs.google.com/spreadsheets/d/1TJrGuujPSOE9CAxwnf8IQg4X_veLV4QahXvGOfsVLK4/edit) — SKY130 results
- [GF180MCU SRAM Achieved Results](https://docs.google.com/spreadsheets/d/1JTLDwcyJMw908QSZAjiLUDdo_IEZ0bTUjtguaUQ9ad8/edit) — GF180MCU results
- [GF180MCU SRAM Sizing - bit.ly/ws-gf180mcu-sram](https://docs.google.com/spreadsheets/d/1fW5ecBsLSec4hXBMaOjMUHQGslm4y-QUILgrxqS8MpA/edit) — GF180MCU sizing
- [wafer.space - GF180MCU SRAM Maximizer](https://docs.google.com/document/d/1hk0WXCmQ8LYNhn8gIVs8vHymR2MleQx2ro_hQlyOYKU/edit) — fitting max SRAM per die
- [HD SRAM Area (and eDRAM) sizes on modern process nodes (<32nm)](https://docs.google.com/spreadsheets/d/15b4bxqCPXxfdw36X9poChlp4UzpNfYsG3nE3Ryd7Yv0/edit) — bit-cell sizes at advanced nodes
- [Memory Data (DFF / OpenRAM) and Caraval Sizing Data](https://docs.google.com/spreadsheets/d/1W0Z418xObi-EeCeD1f-5tYnxRaPcE4w-26hiB8ZLP3k/edit) — DFF RAM vs OpenRAM area (AUC)
- [OpenRAM - RAM Sizing Info for Block RAMs and "Mega LUTs"](https://docs.google.com/document/d/1VDK0x1ycj7ll9d2gzku8INaz3qmunZ-D8DGjG2lBloA/edit) — FPGA-style block RAM sizes

SKY130 SRAM bit cells and layouts
- [SKY130 SRAM Random Collection of stuff - https://bit.ly/sky130-sram](https://docs.google.com/document/d/1-QEdqZBav24ErLHDvifSMAtMSjWEsVCopgWU4R0Ueq4/edit) — SKY130 SRAM hub doc
- [sky130_fd_bd_sram - Cell Descriptions](https://docs.google.com/spreadsheets/d/12Kt2uZm0Y6nPVJzsgFgXD4rUI-8B5EqG7_3S7c26jo4/edit) — foundry bit-cell descriptions
- [SKY130 - SRAM Build Space Layout](https://docs.google.com/drawings/d/1PdwTmAd2Fwto8LxhFZUt1OGUCfWWr5m_AFJadNSmRbI/edit) — build-space layout
- [Previous SKY130 SRAM Layouts](https://docs.google.com/drawings/d/1PSGVa1UpmpH4u62BLWoSMNJe9FWkHbDR_UBjBBqi1pg/edit) — earlier layouts
- [Weirdness with the SRAM Ram Layouts diagrams...](https://docs.google.com/drawings/d/1PmNi_MjYJvLOZOSoIZbfWBW4JhGEsuGe2l4CRIdV8xs/edit) — layout oddities
- [SKY130 SRAM - Cross Section of SRAM with Diodes for Correct Biasing](https://docs.google.com/drawings/d/1yuje6JPUadbIDWujNHbhZ1Zu6hYH0p_LO94fJfI_9wA/edit) — biasing cross-section
- [Adding SRAM + Flash capacity to SKY130 using SkyWater Florida](https://docs.google.com/document/d/1OLJEzrN7mEfAuc7UV9E6zYYmp0FDNONU0jh_3LkZ6xE/edit) — more SRAM/flash capacity

Compilers and requirements
- [OpenRAM: FOSSI Dial-Up 2020](https://docs.google.com/presentation/d/1ckh14Kd_LTkIzIH7cYkVAQ1VcKiIM6_6vEB7dw_d0Qc/edit) — OpenRAM talk (UCSC)
- [OpenRAM Documentation](https://docs.google.com/presentation/d/10InGB33N51I6oBHnqpU7_w9DXlx-qe9zdrlco2Yc5co/edit) — OpenRAM docs deck
- [shared OpenRAM documentation](https://docs.google.com/document/d/1wLjU6hkAoYvSWNBAyTj8HmIV70eJWU3apa9_OEpsd3Y/edit) — OpenRAM community docs (Matt Venn)
- [Soft Multiport OpenRAM](https://docs.google.com/document/d/1J34yF8EtjfdsN5xz68y1tZo54Ojh0Jnld1IRYjjTQqM/edit) — multiport / register-file design (UCSC)
- [Things Google needs in DFFRAM yesterday](https://docs.google.com/document/d/13xGaMWR9dCPwgX7FOtE4pgiMtufbjAU54tSNVca1th0/edit) — DFFRAM requirements
- [GF180MCU Single-Poly "Flash-Like" Memory (UMich / OpenFASoC / Mehdi)](https://docs.google.com/document/d/1I3UOSdVONUD_IXYKU4gYSDF-LOz3-B1a-wXXivrkCnw/edit) — NVM on GF180MCU
- [Inspirational Information on 130nm Process Node - j.mp/si130nm](https://docs.google.com/document/d/1sMmoCfS5l6Uz8sl9Bk3R32XtsdZmC1Hw6bY9nm6r-PA/edit) — 130nm bit-cell targets (~2.45 µm²)

## Projects and repositories
- OpenRAM: https://github.com/VLSIDA/OpenRAM
- SKY130 SRAM macros from OpenRAM: https://github.com/VLSIDA/sky130_sram_macros
- SKY130 SRAM build space: https://github.com/google/skywater-pdk-libs-sky130_fd_bd_sram
- GF180MCU SRAM IP: https://github.com/google/globalfoundries-pdk-ip-gf180mcu_fd_ip_sram
- DFFRAM (standard-cell RAM/register files): https://github.com/AUCOHL/DFFRAM
- bsg_fakeram (placeholder macros for flow testing): https://github.com/bsg-external/bsg_fakeram
- OpenFASoC (alt. memory generators): https://github.com/idea-fasoc/OpenFASOC
- AMC asynchronous memory compiler (name only)

## Papers and other reading
- Guthaus et al., "OpenRAM: An Open-Source Memory Compiler" (ICCAD 2016)
- P, "Design-Space Exploration for Macro-Based SRAM Configuration on the SKY130 PDK" (2026)
- Baungarten-Leon, "Macro Memory Cell Generator for SKY130 PDK" (2024)
- Pai, "Ankhdjet: An Open-Source Compiler for Mask-Programmed Ternary Compute-in-ROM on an Open PDK" (2026)
