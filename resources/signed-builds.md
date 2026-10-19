# Reproducible and signed toolchain — resources

Loose collection, 2026-10-19. Drive links are publicly shared (anyone with the link).

## Tim's Google Drive (public)
- [Trillian applied to Integrated Circuits (IC) — bit.ly/trillian-ic](https://docs.google.com/document/d/1SQHC3eQ4n-VchxuOmgY5JXy0T6rR7LpX9uZckc6UCLQ/edit) — transparency logs for designs, PDKs, tools
- [[External] Reproducible and signed silicon development environments — bit.ly/goog-secure-silicon](https://docs.google.com/presentation/d/1lX_GZo0Aw6juVbB94OMWF2HDPbmkF-5dgOFSMamiRFU/edit) — the main deck
- [State of Reproducible Builds in Chromium](https://docs.google.com/document/d/1KtKauRHBYnno29MOJNEoGw496m9xt9sqcyUIF3s6ekY/edit) — Tim's Chromium determinism work
- [EDDA - Conda based system for FPGA and ASIC Dev](https://docs.google.com/document/d/1BZcSzU-ur0J02uO5FSGHdJHYGnRfr4n4Cb7PMubXOD4/edit) — conda packaging design
- [EDDA Package Status (EDA Tools Conda Packages) — j.mp/edda-status](https://docs.google.com/spreadsheets/d/1d-o_udk4mZkeOL7ZqffPcIKCExhV9ZpmGyjP4kFcfjI/edit) — per-tool package tracker
- [SymbiFlow, LiteX & TimVideos Conda Packages](https://docs.google.com/document/d/1fWV259IbgnenwjRswE9dqCMBfyg8NC2Ily3pGQcw5ck/edit) — earlier packaging plan
- [conda package stages](https://docs.google.com/document/d/1cj4pnacf6Vh3DySiAM3h3v6XOHUIA9WXVy7esuUyRAg/edit) — build/test/upload pipeline
- [Next Conda Work](https://docs.google.com/document/d/11XFnJ0ExBgE1pMQksw0rQerAZo3F83AVIu2YK1pbg1k/edit) — 2021 follow-up tasks
- [conda notes](https://docs.google.com/document/d/1AaL460Uf_8_9v8EIy4pAZYTFOFXbv5O4RRU7Jv4t_Z4/edit) — working notes
- [Eco - Conda packages](https://docs.google.com/document/d/1SPYTBfLBCIlsvw6aGDlqxbtlSuaVkRZYpHiGY-lpl3A/edit) — project brief
- [Open Source EDA: building, packaging, installing](https://docs.google.com/document/d/10_MqFjTIYVVuOJlusJydsp4KOcmrrHk03__7ME5thOI/edit) — Unai Martinez-Corral survey
- [EDA integration: managing projects for simulation and implementation](https://docs.google.com/document/d/1qThGGqSVQabts-4imn5zY5BMptp1-Q2rGiNKHDH1Pbk/edit) — Unai Martinez-Corral
- [edalize.autosetup](https://docs.google.com/document/d/1IMVrSmMO5wqTV3W22Bv2PeKtMHO3WSyCwHm3N-Wkwbk/edit) — automatic tool setup in Edalize
- [Tim's suggestions for a edalize v2](https://docs.google.com/document/d/1VakRJV0Pv4eM_hJnCCfh2l3bCMD3y07p6hFpc7z2Kg4/edit) — 2026 tool-launch API ideas
- [EDAlize usage in F4PGA (SymbiFlow)](https://docs.google.com/drawings/d/104n5VIRmLOIs6pQlMCrssxZXFQbEM1bk1vpki02Ckd0/edit) — diagram

## Projects and repositories
- [Reproducible Builds](https://reproducible-builds.org/) — practice, tools (diffoscope, SOURCE_DATE_EPOCH)
- [diffoscope](https://diffoscope.org/) — deep diff of build outputs
- [Sigstore](https://www.sigstore.dev/) and [Rekor](https://github.com/sigstore/rekor) — signing and transparency log
- [Trillian](https://github.com/google/trillian) — verifiable log backend
- [in-toto](https://in-toto.io/) and [SLSA](https://slsa.dev/) — supply-chain attestations and levels
- [Nix](https://nixos.org/) and [GNU Guix](https://guix.gnu.org/) — bit-for-bit package builds
- [hdl/conda-eda](https://github.com/hdl/conda-eda) — conda recipes for open EDA tools (litex-hub channel)
- [OSS CAD Suite](https://github.com/YosysHQ/oss-cad-suite-build) — nightly binary builds of open EDA tools
- [IIC-OSIC-TOOLS](https://github.com/iic-jku/IIC-OSIC-TOOLS) — pinned Docker image of open ASIC tools
- [Edalize](https://github.com/olofk/edalize) and [FuseSoC](https://github.com/olofk/fusesoc) — tool launching and core packaging (signing targets)
- [OpenLane 2](https://github.com/efabless/openlane2) — Nix-based flow
- Determinism targets: [Yosys](https://github.com/YosysHQ/yosys), [OpenROAD](https://github.com/The-OpenROAD-Project/OpenROAD), [KLayout](https://github.com/KLayout/klayout), [Magic](https://github.com/RTimothyEdwards/magic), [nextpnr](https://github.com/YosysHQ/nextpnr)

## Papers and other reading
- Certificate Transparency, RFC 6962 / RFC 9162
- Lamb and Zacchiroli, "Reproducible Builds: Increasing the Integrity of Software Supply Chains" (IEEE Software, 2022)
- Ken Thompson, "Reflections on Trusting Trust" (1984); David A. Wheeler, "Diverse Double-Compiling" (2009)
