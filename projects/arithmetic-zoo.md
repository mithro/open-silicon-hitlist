# arithmetic-zoo: Adder and multiplier exploration

## Goal

Generate a wide design space of adder, multiplier and multiply-accumulate (MAC) architectures, characterise each one's power, performance and area for every open PDK and fake-PDK node, and teach open synthesis (Yosys) to map arithmetic operators onto the best one for each design's constraints automatically.

## Why it is high value

- Arithmetic dominates the area and timing of most accelerators, and open ASIC flows currently map operators to a small fixed set of implementations, which costs real quality of results.
- The space (ripple, carry-lookahead, Kogge-Stone, Brent-Kung, Han-Carlson and sparse prefix adders; Booth and non-Booth multipliers with Wallace, Dadda and compressor trees; fused MACs; number formats from integer to low-precision floating point) is large and every point is measurable, which suits agents generating and benchmarking in bulk.
- Results are directly comparable across PDKs and nodes, so the work also benchmarks the fake PDKs on this list.

## State of the art

- Yosys maps `$add`, `$mul` and related cells through techmap and `booth` passes with a limited set of architectures; ABC optimises the resulting logic but does not choose architectures.
- Research generators exist (for example prefix-adder exploration with reinforcement learning, and Wallace/Dadda tree generators), but they are not integrated into open flows or characterised per open PDK.
- Commercial synthesis (DesignWare in Synopsys Design Compiler) picks among many arithmetic implementations by constraint.

## Open questions

- Which number formats and widths matter most for AI accelerators (int8/int4, bf16, fp8, wider integer MACs)?
- Characterisation method: full place and route plus static timing per variant, or a faster model calibrated against it?
- How to package the result: a Yosys pass and library, or a separate generator that Yosys calls?

## Sources

Tim's design doc: [Improving operator mapping in Yosys for ASICs](https://docs.google.com/document/d/1N4huvzOsGuEjiBCXDKPMpWfxoxpc40XFDhyxjcdtwwg/edit).

## Related items

- [cell-foundry](cell-foundry.md) (Standard cell generation): Arithmetic quality depends on the cell library.
- [shadow-pdks](shadow-pdks.md) (Open "almost manufacturable" PDKs): Each architecture is characterised per node.
- [asic-scoreboard](asic-scoreboard.md) (ASIC benchmarking): ASIC benchmarking is the scoreboard.
- [paper-replay](paper-replay.md) (Replicating classic ASIC and FPGA papers): Classic adder and multiplier studies are replication candidates.
