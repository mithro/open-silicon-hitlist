# paper-replay: Replicating classic ASIC and FPGA papers

## Goal

Reproduce the results of important past papers in ASIC and FPGA design, architecture and EDA with open tools, then test whether their conclusions still hold now that AI agents and very cheap, very fast compute can search far larger design spaces than the original authors could.

## Why it is high value

- Many design rules of thumb (FPGA LUT size and cluster size, routing architecture choices, placement and routing heuristics, adder and multiplier trade-offs, standard-cell library composition) rest on studies from the 1990s and 2000s run on small benchmarks with limited compute. Some conclusions may no longer hold.
- Reproduction is well defined and checkable: match the published numbers first, then rerun with modern nodes, larger benchmarks and exhaustive search.
- Replications become regression tests and benchmark cases for the tools on this list, and overturned results point to where open tools can beat the conventional choices.

## State of the art

- Reproducibility in EDA and architecture research is poor: code, benchmarks and tool versions are often unavailable, and results depend on closed vendor tools.
- Some groups publish open artefacts (VTR architecture studies, OpenROAD and ISPD contest flows), and conferences have started artefact evaluation, but nothing systematically re-tests the classic results.
- Open PDKs, open tools and open shuttle designs now make full reproduction possible for the first time.

## Open questions

- Which papers to start with: a ranked list of influential, checkable results in FPGA architecture, EDA algorithms and circuit design.
- How to report a replication (matched, partly matched, overturned) and where to publish it.
- How to handle papers whose results depend on vendor tools or proprietary processes.
- How this connects to the benchmarking and open MPW items for silicon-backed checks.

## Related items

- [fpga-scoreboard](fpga-scoreboard.md) (FPGA benchmarking): FPGA architecture papers are re-tested on the FPGA benchmark.
- [asic-scoreboard](asic-scoreboard.md) (ASIC benchmarking): ASIC papers are re-tested on the ASIC benchmark.
- [arithmetic-zoo](arithmetic-zoo.md) (Adder and multiplier exploration): Arithmetic trade-off papers are prime candidates.
- [open-fabric](open-fabric.md) (Fully open FPGA and eFPGA): Classic FPGA architecture studies inform the open fabric.
