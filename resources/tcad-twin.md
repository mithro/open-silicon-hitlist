# Open TCAD stack — resources

Loose collection, 2026-10-19. Drive links are publicly shared (anyone with the link). Includes test structures, measurement and model extraction.

## Tim's Google Drive (public)
TCAD and the characterisation loop
- [(Open Source Silicon) TCAD Flows](https://docs.google.com/presentation/d/1lMfMHNLSb8cuPYUNfC6DerJhv1ddvy7ec7QQRA_eJcc/edit) — loop diagram, "TCAD on cloud"
- [Open source process characterization flow (test structures / simulation / test data collection)](https://docs.google.com/drawings/d/1uPqgGqe4tB0qG-bMLlaYzMi9ILhh217VeVVLWLFBLDY/edit) — flow diagram
- [Open source TCAD Market Overview - bit.ly/pg-tcad](https://docs.google.com/spreadsheets/d/1dK1GxGl1C7v3rhWKw3RcbeZsRre66HPAOPFbgYni74A/edit) — survey of open TCAD tools (by Philipp Gühring)
- [SKY130 (SkyWater PDK) -- Stackup Capacitance Data (public)](https://docs.google.com/spreadsheets/d/1N9To-xTiA7FLfQ1SNzWKe-wMckFEXVE9WPkPPjYkaxE/edit) — stack-up for calibration
- [SKY130 Cross sections](https://docs.google.com/drawings/d/1gbpWye9Gmi4Es-IaQQ0azpaUYSnrT6se4ogGDGroEBE/edit) — process cross-section drawings

Test structures and measured data
- [SKY130 MPW-I Manufacturing Test Tiles Random Notes and Documentation - https://bit.ly/sky130-mpw1-testtile-notes](https://docs.google.com/document/d/16xyYe0Xu4ScDvNsoOG2TUB5iSQCWn7VryFxZxZh4ihI/edit) — SKY130 e-test tile notes
- [Pad documentation for SKY130 MPW Manufacturing E-Test Tile -- https://bit.ly/sky130-testtile-edit](https://docs.google.com/spreadsheets/d/1LSINFWJRTvHEC7PzT-Y1yHR9Nuz75gVvBY0e7oAhnCg/edit) — pad map for the test tile
- [SKY130 MPW-I Manufacturing Test Tiles - Rough Layout](https://docs.google.com/drawings/d/1xT8TNkyBl7OrmVIX1EdhABbqLkIqfXeoydMHigG7tII/edit) — test tile layout sketch
- [OpenFASOC - Cryogenic teststructures generator](https://docs.google.com/presentation/d/1oROHp4B55McL_V3XpsjWqH9fspBz7vrPsw5zF5Ex_8M/edit) — OpenFASoC test-structure generator (UMich)
- [Document on running the cryo generators on OpenFASOC](https://docs.google.com/document/d/1VHELepRUYkY2U0N4onNoNQCNoquZsgFYK8X87PpOnaY/edit) — how to run the cryo generators (UMich)
- [ Cryogenic Projects Using OpenFASOC - bit.ly/openfasoc-cryo](https://docs.google.com/presentation/d/1yuf_1Q090cqq8zNeWcDJbnsBhoUDXj1fahejubjHgMI/edit) — cryogenic projects overview (UMich)
- [UMich + NIST Inductor Characterization Progress](https://docs.google.com/presentation/d/1GCBY3_LZzK186IWdLkqmY3F6wRBatrKWzQwUdeFaI3Q/edit) — passive device measurement (UMich + NIST)
- [Inductor Characterization](https://docs.google.com/document/d/1Cn8WTY5fIF-mAvHUjeXas9V7WYKpNWQhRHMLXbrM5e8/edit) — inductor measurement notes
- [GF180 IO and Std Cell Library Measurements](https://docs.google.com/document/d/1xY8Bs1hBnGedHV0iPN5M4tmC3i43jlTyGoMgv24C3to/edit) — measured GF180 cell and IO data (Tiny Tapeout)

## Projects and repositories
Device and process simulation
- DEVSIM: https://github.com/devsim/devsim
- ViennaPS (process/topography): https://github.com/ViennaTools/ViennaPS
- ViennaTS, Charon (Sandia), FLOOXS (Univ. of Florida), Genius (names only)
- Archimedes: https://www.gnu.org/software/archimedes/

Test structures, measurement, extraction
- gdsfactory (incl. gplugins for DEVSIM): https://github.com/gdsfactory/gdsfactory
- OpenFASoC (test-structure and cryo generators): https://github.com/idea-fasoc/OpenFASOC
- LibreSilicon (Danube River test structures): https://libresilicon.com/
- pyuscope (automated probing/imaging, Labsmore): https://github.com/Labsmore/pyuscope
- SKY130 raw device measurements: https://github.com/google/skywater-pdk-sky130-raw-data
- OpenVAF (Verilog-A compiler): https://github.com/pascalkuthe/OpenVAF
- DMT-core model extraction (SemiMod) (name only)
- ngspice: https://ngspice.sourceforge.io/ ; Xyce: https://github.com/Xyce/Xyce
- BSIM models: https://bsim.berkeley.edu/

PDKs to reproduce
- IHP SG13G2: https://github.com/IHP-GmbH/IHP-Open-PDK
- SKY130: https://github.com/google/skywater-pdk
- GF180MCU: https://github.com/google/gf180mcu-pdk

## Papers and other reading
- Beall, "DC Cryogenic Modeling of Open-Source SkyWater 130 nm MOSFETs at 77 K Using BSIM4" (2026)
- Singh, "BSIM3v3 to EKV2.6 Model Parameter Extraction and Optimisation using LM Algorithm on 0.18µm" (2018)
- Ayed, "A Conversion of Empirical MOS Transistor Model Extracted from 180 nm Technology to EKV3.0" (2016)
- Grabiński, "Advanced compact modeling of the deep submicron technologies" (2000)
- Luo, "MOSFET characterization and modeling at cryogenic temperatures" (2018)
- Buckland, "TCAD simulations of High-Voltage-CMOS Pixel structures for the CLIC vertex detector" (2016)
