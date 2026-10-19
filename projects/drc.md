# Design rule checking (DRC): fast engine, exhaustive tests, explainable rules

## Goal

Make open DRC trustworthy and fast enough for full-chip signoff. Three parts:

- **Distributed engine.** A parallel, distributed DRC engine that validates a reticle-sized chip (about 26 x 33 mm, roughly 858 mm²) at an advanced node in under one hour, using a map-reduce style split of the layout across a cluster.
- **Exhaustive rule-deck test suites.** For every open PDK, one small GDS per rule with passing and failing cases, plus tests for interactions between rules, so any DRC engine and any rule deck can be checked automatically.
- **Explainable, machine-checkable rules.** Every rule states why it exists (the physical or manufacturing reason) and is fully automated, with expected-versus-measured device data where it applies.

## Why it is high value

- Full-chip DRC is a signoff bottleneck; the open tools today take far too long at this scale.
- No open PDK has a complete per-rule test suite, so nobody can show an open rule deck or engine is correct. Writing thousands of small test layouts is huge, mechanical and checkable work, a good fit for AI agents.
- Rules that carry their reasons can be reviewed, ported between nodes and generated for the fake PDKs on this list. This applies to SKY130, GF180MCU and IHP SG13G2 today.
- Fast, tested DRC is a prerequisite for the open PDKs on this list being useful for large designs.

## State of the art

- Open engines: KLayout DRC (tiled and multi-threaded, with a "deep" hierarchical mode), Magic (interactive, incremental), Netgen for LVS.
- Commercial: Siemens Calibre and Cadence Pegasus both run distributed across many hosts.
- Open PDK rule decks are tested only partly and mostly by hand; the reasons behind rules are usually not written down.

## Open questions

- Rule-deck language: stay compatible with KLayout's DRC scripts, or define a new intermediate form that carries rule reasons and that several engines can compile?
- Handling of global rules that do not tile cleanly (density, antenna, connectivity-dependent checks).
- GDS/OASIS ingestion and partitioning at multi-terabyte scale.
- Benchmark designs and reference results to prove correctness against a trusted checker (the archive of open shuttle designs is a candidate source).
- Which PDK gets the first complete test suite.

## Sources

Tim's design docs: [Design Rule Check (DRC) Testing](https://docs.google.com/document/d/18z-FBJHni6qt1WR_tF6bbRHfQydKcFMAVnuj4Ixbj90/edit), [Building a (future) open source PDK](https://docs.google.com/document/d/1Y-RbdGYOzswOI5EkUuCKZnWjdT1K9UbGQc_CbcIQ9O4/edit).
