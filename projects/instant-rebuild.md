# instant-rebuild: Incremental toolchains for FPGA and ASIC

## Goal

Open FPGA and ASIC flows in which a small design change costs a small amount of work: synthesis, placement, routing, timing and checks reuse everything that did not change, so edit-compile-test loops drop from hours to minutes, and results stay identical to a full rebuild.

## Why it is high value

- Long rebuild times are a main cost of hardware development and a main reason AI agents iterate slowly on hardware; incremental flows multiply the speed of every other effort on this list.
- Vendor tools offer incremental compile and partial reconfiguration; open tools almost entirely rebuild from scratch.
- Making each stage incremental and proving it equals a full rebuild is precise, testable engineering well suited to agents, especially combined with the reproducible toolchain and toolchain verification items.

## State of the art

- Vendor: Vivado incremental implementation and Quartus incremental compilation with design partitions; Cadence and Synopsys ECO flows for ASICs.
- Open: Yosys and OpenROAD run each stage as a batch; OpenROAD has some ECO support and incremental timing in OpenSTA; nextpnr and VPR have no general incremental mode. Research exists on incremental synthesis and placement but is not in open flows.

## Open questions

- The unit of reuse: hierarchy-based partitions, content-addressed caching of stage outputs, or fine-grained incremental algorithms?
- How to guarantee results identical to a full rebuild, and how that ties to deterministic builds.
- Which stage gives the biggest win first (synthesis, placement, routing or timing).

## Where it sits

Layer: **Tooling**. Function: **cross-cutting**. Target: **ASIC and FPGA**. Tooling speed for both ASIC and FPGA flows.

## Resources

Loose collection of links for fleshing this item out: [resources/instant-rebuild.md](../resources/instant-rebuild.md).

## Related items

- [signed-builds](signed-builds.md) (Reproducible and signed toolchain): Incremental results must match a reproducible full build.
- [flow-proofs](flow-proofs.md) (Toolchain verification): Verification proves the incremental result is correct.
- [open-pnr](open-pnr.md) (FPGA Interchange and open place and route): Place and route is the slowest FPGA stage to make incremental.
