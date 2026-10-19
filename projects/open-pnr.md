# open-pnr: FPGA Interchange and open FPGA place and route

## Goal

Revive the FPGA Interchange format as the common exchange layer between open FPGA tools and device databases, and substantially improve the open place-and-route tools (VPR from Verilog-to-Routing, and nextpnr) so they produce results competitive with vendor tools on every family the bitstream documentation project covers.

## Why it is high value

- Bitstream documentation is only useful if open tools can place and route for the documented devices with good quality of results.
- A single interchange format means each new device database works with every tool, instead of one hand-written back-end per tool per family.
- Place-and-route quality (timing-driven placement, routing congestion, packing) is measurable on the FPGA benchmarking item and improves through many careful, testable changes, which suits agents.

## State of the art

- FPGA Interchange (device resources, logical and physical netlists in Cap'n Proto) was developed by AMD, Antmicro and Google with RapidWright and nextpnr support; nextpnr's `fpga_interchange` architecture was removed in 2024 and a backlog of test and tool pull requests was never merged.
- nextpnr supports iCE40, ECP5, Nexus, Gowin, GateMate, Cyclone V (Mistral) and Xilinx (nextpnr-xilinx, out of tree).
- VPR is highly configurable and strong for architecture research, with Xilinx 7-series support through F4PGA; quality and runtime trail vendor tools on large devices.

## Open questions

- Revive FPGA Interchange as it was, or define a lighter successor?
- Which families and devices to target first for competitive quality of results.
- Whether to invest mainly in nextpnr, VPR or both, and how to share algorithms between them.
- Timing models: where accurate delay data comes from for each family.

## Related items

- [bitstream-atlas](bitstream-atlas.md) (FPGA bitstream documentation): Needs the bitstream databases for each family.
- [fpga-scoreboard](fpga-scoreboard.md) (FPGA benchmarking): Benchmarked against vendor place and route.
- [instant-rebuild](instant-rebuild.md) (Incremental toolchains): Incremental place and route is a key speed-up.
- [open-fabric](open-fabric.md) (Fully open FPGA and eFPGA): Open fabrics ship with these tools as their flow.
- [format-kit](format-kit.md) (Libraries for every EDA file format): Builds on shared format libraries.
