# Analog generators (OpenFASoC, ALIGN, PCells) — resources

Loose collection, 2026-10-19. Drive links are publicly shared (anyone with the link). README candidate, not yet a full item.

## Tim's Google Drive (public)
Generators and flows
- [Example Google grant proposal - LDO on SkyWater 130nm using Open FASoC (Publicly linkable version)](https://docs.google.com/document/d/1EuRwxV8RNgPDYLSVSpPPPFYYDlnr-QGkxSf22nplWsE/edit) — LDO generator proposal, public version
- [Parametric Cells for OpenSource](https://docs.google.com/presentation/d/1WbFWVVg2Vp5ukKn7bW6Wy1NOAy03Qa4MYy3AW2KbOh4/edit) — portable PCell API proposal (LibreSilicon)
- [Tiny Tapeout Analog flow workshop](https://docs.google.com/document/d/1-VwjT0K2uktSyDMH9bQP82-1xmy0BxKJRlM2YONxb4A/edit) — open analog flow tutorial (John McMaster)
- [gdsfactory workshop march 2024](https://docs.google.com/document/d/1ws5mO-cfqK-9sXYGZQvnO9gQlWz3ztyQSG6v40dcJd0/edit) — gdsfactory workshop (J. Matres)
- [gdsfactory latchup 2025](https://docs.google.com/presentation/d/183Sl19kmizHJGHBjTrgrZoXXtciyoBQRDjcrVzDCvlk/edit) — gdsfactory talk (gdsfactory.com)
- [OpenFASOC - Cryogenic teststructures generator](https://docs.google.com/presentation/d/1oROHp4B55McL_V3XpsjWqH9fspBz7vrPsw5zF5Ex_8M/edit) — test-structure generator (UMich)
- [ Cryogenic Projects Using OpenFASOC - bit.ly/openfasoc-cryo](https://docs.google.com/presentation/d/1yuf_1Q090cqq8zNeWcDJbnsBhoUDXj1fahejubjHgMI/edit) — cryo generators (UMich)
- [GF180MCU Single-Poly "Flash-Like" Memory (UMich / OpenFASoC / Mehdi)](https://docs.google.com/document/d/1I3UOSdVONUD_IXYKU4gYSDF-LOz3-B1a-wXXivrkCnw/edit) — NVM via OpenFASoC

Analog IP catalogues and design notes
- [Index of potentially interesting Analog IP for SKY130 (SkyWater 130nm) PDK - j.mp/si130nm-analog](https://docs.google.com/document/d/10G8b1sWzGrFK1D3bVlRHSX__JLXKm9Deq-qYmblGijE/edit) — SKY130 analog IP index
- [Interesting Analog IP ](https://docs.google.com/spreadsheets/d/1e9M9ZcQ4HX5QEEJRDYPAHhfSEJZnBpTYXcMkRziyRe4/edit) — analog IP wishlist
- [Tim's steps to improve analog designs on SKY130](https://docs.google.com/document/d/1KyUGaiqpxA_8A4rt_zFXV2MELvsyJtF9OmfoPeAGrJ8/edit) — SKY130 analog improvements
- [Sky130 Analog Device Specs ](https://docs.google.com/document/d/1h9q2KUO6mLlyLCp0uvf9ulrLabgLs9_5nHcwBEjE3hI/edit) — device specs (Philipp Gühring)

SerDes and high-speed IO
- [(External Access) SERDES, PIPE and protocols - Pathway to fully open source implementations... - bit.ly/open-pipe-talk](https://docs.google.com/presentation/d/18cGRni3QDIsyWrTx8WWoPBjEgUObHTGIXYhfViZm7xw/edit) — path to open SerDes/PIPE
- [Gigabit SERDES Publications](https://docs.google.com/spreadsheets/d/1sWjgR6Z9eW834jEJF11yitpRn2fjAvamp9ppRNipRhE/edit) — publications list
- [SERDES & High Speed IO Docs](https://drive.google.com/drive/folders/1A6K2b9VFvGC5VRVsnGBQJYwM-L2GsjAI) — folder of reference docs

## Projects and repositories
- OpenFASoC (incl. gLayout): https://github.com/idea-fasoc/OpenFASOC
- OpenFASoC docs: https://openfasoc.readthedocs.io/
- ALIGN: https://github.com/ALIGN-analoglayout/ALIGN-public
- BAG (Berkeley Analog Generator): https://github.com/ucb-art/BAG_framework
- MAGICAL: https://github.com/magical-eda/MAGICAL
- gdsfactory: https://github.com/gdsfactory/gdsfactory
- KLayout PCells: https://github.com/KLayout/klayout
- Xschem: https://github.com/StefanSchippers/xschem
- ngspice: https://ngspice.sourceforge.io/ ; Xyce: https://github.com/Xyce/Xyce
- Tiny Tapeout (analog tiles): https://tinytapeout.com/
- Open PDKs: SKY130 https://github.com/google/skywater-pdk , GF180MCU https://github.com/google/gf180mcu-pdk , IHP SG13G2 https://github.com/IHP-GmbH/IHP-Open-PDK

## Papers and other reading
- Ali et al., "FASoC: A Fully Automated Synthesis of Analog and Mixed-Signal Circuits" (ICCAD 2020)
- Kunal et al., "ALIGN: Open-Source Analog Layout Automation from the Ground Up" (DAC 2019)
- Chang et al., "BAG2: A Process-Portable Framework for Generator-Based AMS Circuit Design" (CICC 2018)
- Dorrer, "From Idea to Tapeout: An Open-Source Analog Mixed-Signal Design Flow with the IHP Open-PDK" (2026)
- Arévalos, "A Topology-Independent and Scalable Methodology for Automated LDO Design Using Open PDKs" (2025)
