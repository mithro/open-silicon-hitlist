# Fully reproducible and signed toolchain and build space

## Goal

Bit-identical builds of the open EDA tools and of everything they produce (GDS, bitstreams, netlists, reports) from pinned inputs, with every tool binary, PDK release and design artefact signed and recorded in a public transparency log, so anyone can verify exactly what went into a chip.

## Why it is high value

- Chips are trusted largely through obscurity today. Reproducible builds plus a verifiable log give an alternative: anyone can rebuild and compare.
- Determinism also makes everything else on this list easier: regressions become diffs, benchmarks become repeatable and AI-generated changes can be checked bit for bit.
- Finding and fixing every source of nondeterminism (timestamps, hash-map ordering, threading, floating point, file paths) across Yosys, OpenROAD, KLayout, Magic and nextpnr is wide, painstaking work well suited to agents.

## State of the art

- Software has mature practice: the Reproducible Builds project, Debian and Nix/Guix bit-for-bit builds, Chromium's deterministic builds, Sigstore signing and Certificate Transparency or Trillian logs.
- Open EDA has partial pinning (Nix and conda packages, Docker images, OpenLane releases), but tool outputs are often not bit-identical across runs, threads or machines, and nothing is logged or signed end to end.

## Open questions

- Scope of "reproducible": the same bits on the same machine, across thread counts, or across machines and operating systems?
- What gets logged: tool binaries, PDK releases, source designs, intermediate and final outputs?
- Which signing and log stack to adopt (Sigstore, Trillian-based, in-toto attestations, SLSA levels)?
- How to handle vendor tools in mixed flows, where only the open parts can be reproduced.

## Sources

Tim's design docs: [Trillian applied to Integrated Circuits](https://docs.google.com/document/d/1SQHC3eQ4n-VchxuOmgY5JXy0T6rR7LpX9uZckc6UCLQ/edit?resourcekey=0-nQtazqnEVI0OSF7LVq0Hnw), [State of Reproducible Builds in Chromium](https://docs.google.com/document/d/1KtKauRHBYnno29MOJNEoGw496m9xt9sqcyUIF3s6ekY/edit), [edalize.autosetup](https://docs.google.com/document/d/1IMVrSmMO5wqTV3W22Bv2PeKtMHO3WSyCwHm3N-Wkwbk/edit).
