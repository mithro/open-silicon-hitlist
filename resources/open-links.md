# Open high-speed connectivity IP (FPGA and ASIC) — resources

Loose collection, 2026-10-19. Drive links are publicly shared (anyone with the link).

## Tim's Google Drive (public)
- [SERDES, PIPE and protocols - Pathway to fully open source implementations — bit.ly/open-pipe-talk](https://docs.google.com/presentation/d/18cGRni3QDIsyWrTx8WWoPBjEgUObHTGIXYhfViZm7xw/edit) — the core deck
- [Pathways to high speed protocols using PIPE standard SERDES and FPGAs (generic ASIC node)](https://docs.google.com/drawings/d/15hrrSxMGCxZUWH6faZ6mEbU6uLguQcjY8Kfw3p9WV6o/edit) — roadmap diagram
- [Possible USB PIPE Development process](https://docs.google.com/presentation/d/1u_XB1Gw_mn0vz3DzbzS3hL3zjeBLwp5R5fiFPHE8cEw/edit) — staged USB3 plan
- [SERDES Protocol Table (sheet)](https://docs.google.com/spreadsheets/d/1E0WAPBxvNcp4H2Ye07xbHfzR8SwAsJX_AAhaWW1eQ0w/edit) and [(doc)](https://docs.google.com/document/d/1krIVSZw_FwjG7sroVZ3IIVIHmBZ76r8e4mBtlCwJy6k/edit) — line rates and encodings per protocol
- [When was PCIe versions supported (dates, parts & process nodes)](https://docs.google.com/document/d/1ItFfVkK6SQFjOv5kzzwCAq5x_xVZee9zKB7v0VDrYKk/edit) — which node is needed per generation
- [Gigabit SERDES Publications](https://docs.google.com/spreadsheets/d/1sWjgR6Z9eW834jEJF11yitpRn2fjAvamp9ppRNipRhE/edit) — literature list
- [SERDES Breakdown](https://docs.google.com/drawings/d/1lt_5vk8gYrMRAxI506Henf1u2FKI0kHR2L_Mas11yVQ/edit) and [USB SERDES](https://docs.google.com/drawings/d/1zv6FEv6MYc4g0jWjqLVgvHlDKSJGCjAG60fR5T9OZSU/edit) — block diagrams
- [Project X-Ray -- High Speed Transceiver bitstream documentation](https://docs.google.com/document/d/1IqMAlTdAZtSV6gyj6CR-yXLAS6ycpAfeTGwLvaCwC_U/edit) — open GTP/GTX config, needed for open PIPE on Xilinx
- [Florent - Dashio USB3.0 core to Artix-7 GTP](https://docs.google.com/document/d/1i_TmHE-AK6juNWJ5OcYvuw-Vb_PnF5WngXPLyfimWqk/edit) — USB3 on FPGA transceivers
- [Port Dashio USB3.0 core to use FPGA high speed transceivers](https://docs.google.com/document/d/1wbfhdiOPFJV1wKde0blN5f62rWpPOamCfmz2aHgz3l4/edit) — earlier plan
- [Open Source Ethernet resource usage comparison](https://docs.google.com/spreadsheets/d/1BuOLFqRWo50nIeVloMo6GxBBYMzZ9BdBOhs0iBl4IoY/edit) — open MAC cores compared
- [PCI Express Development Board Pin Mapping](https://docs.google.com/spreadsheets/d/1lWmWJ1-ANhsEsvpYTgBhPL2qnzWC2HEEkqb_Rro3W5U/edit) — board-level reference
- [FPGA based PCIe switch card](https://docs.google.com/drawings/d/1jN8RX05T-oKbTXVYYRqX1Xmr4Rj7xM6iq0hjG8EaQGw/edit) — concept
- [Building an Ethernet Switch ASIC](https://docs.google.com/document/d/1olBxU1kSvzKc-IJS-eKVHS4Ctxbb1HHAnu3S0czY_rY/edit) — Julia Desmazes, open ASIC project notes

## Projects and repositories
- [ECP5-PCIe](https://github.com/ECP5-PCIe/ECP5-PCIe) — gateware PCIe data link layer on ECP5 SerDes
- [Yumewatari](https://github.com/whitequark/Yumewatari) — PCIe PHY over ECP5 SerDes (virtual PIPE)
- [LUNA](https://github.com/greatscottgadgets/luna) — USB gateware with ECP5 SerDes USB3 PIPE work
- [LitePCIe](https://github.com/enjoy-digital/litepcie) — PCIe core on vendor hard blocks
- [LiteEth](https://github.com/enjoy-digital/liteeth) and [verilog-ethernet](https://github.com/alexforencich/verilog-ethernet) — open Ethernet MACs (1G to 25G)
- [Corundum](https://github.com/corundum/corundum) — open FPGA NIC with PCIe DMA
- [OpenFASoC](https://github.com/idea-fasoc/OpenFASOC) — generators incl. SerDes design-space exploration
- [Project X-Ray](https://github.com/f4pga/prjxray) — 7-series bitstream docs (transceiver coverage incomplete)
- [daisho USB 3.0](https://github.com/mossmann/daisho) — Dashio/Daisho USB3 core origin

## Papers and other reading
- Intel "PHY Interface for PCI Express, SATA, USB 3.x, DisplayPort and USB4 Architectures" (PIPE) specification
- PCI-SIG PCIe Base specification; USB-IF USB 3.2 specification; CXL Consortium specification
- Forencich et al., "Corundum: An Open-Source 100-Gbps NIC" (FCCM 2020)
- Not public on Drive (titles only): "Open source PCIe stack - Parts and current work" (Tim, 2025), "Multi-GHz SerDes Design Space Exploration using OpenFASOC" (UMich/ASU), SKY130 SerDes project decks (UMich)

## Also listed on mith.ro

- [OpenPOWER Summit 2021 - A fully FOSS memory controller with LPDDR4/5 support for FPGA and ASICs - https://bit.ly/ops21-litedram](https://docs.google.com/presentation/d/1QxDs5OkS0DG1trDXAbMWCQuwPmjn_qxwyGKH53CC25c/embed)
