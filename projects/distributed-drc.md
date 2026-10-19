# Distributed DRC engine

## Goal

A parallel, distributed design-rule-checking engine that validates a reticle-sized chip (about 26 x 33 mm, roughly 858 mm²) at an advanced node in under one hour, using a map-reduce style split of the layout across a cluster.

## Why it is high value

- Full-chip DRC is a signoff bottleneck; the open tools today take far too long at this scale.
- Fast open DRC is a prerequisite for the open PDKs in item 2 being useful for large designs.
- The engine design (tiling, halos, hierarchy, global rules) is well-defined engineering that benefits from large amounts of careful implementation and testing.

## State of the art

- Open: KLayout DRC (tiled and multi-threaded, with a "deep" hierarchical mode), Magic (interactive, incremental), Netgen for LVS.
- Commercial: Siemens Calibre and Cadence Pegasus both run distributed across many hosts.

## Open questions

- Rule-deck language: stay compatible with KLayout's DRC scripts, or define a new intermediate form both can compile to?
- Handling of global rules that do not tile cleanly (density, antenna, connectivity-dependent checks).
- GDS/OASIS ingestion and partitioning at multi-terabyte scale.
- Benchmark designs and reference results to prove correctness against a trusted checker.
