# shuttle-program: Open MPW tapeout programs

## Goal

Run recurring, open multi-project wafer (MPW) shuttles on open PDKs, and on fake-PDK-equivalent real nodes where a foundry allows, so the community keeps taping out real silicon. Every design, its PDK and tool versions, flow results and measured silicon status are archived as one public corpus that grows into a library of proven open IP and a benchmark set.

## Why it is high value

- Silicon is the only final proof that open PDKs, tools and IP work. Regular shuttles turn the rest of this list from simulation into measured results.
- Each shuttle adds proven blocks (standard cells, SRAM, IO, analog, connectivity PHYs, eFPGA fabrics) and real designs for the ASIC benchmarking item.
- Agents can do much of the work around a shuttle: precheck and fix submissions, re-run flows on every archived design when tools change, and collate test results into the corpus.

## State of the art

- Past and current programs: Google and Efabless Open MPW on SKY130 and GF180MCU (Efabless has since shut down, and many project links are dead), Tiny Tapeout (thousands of small designs on shared dies), wafer.space on GF180MCU, IHP's free open-source shuttles on SG13G2, and Europractice and Chipathon-style programs.
- Results are scattered: designs live in individual repositories, flow and silicon status are rarely recorded, and nothing re-runs old designs against new tools.

## Open questions

- Who funds and operates the shuttles, on which PDKs, and how often.
- What every submission must include (tests, documentation, licence) so it becomes reusable IP and a benchmark case.
- How measured silicon results are collected and published (shared test boards, bring-up harnesses).
- How to rescue and mirror the archives of past programs before more links are lost.

## Where it sits

Layer: **Proof in silicon**. Function: **cross-cutting**. Target: **ASIC**. Sits outside the three layers: real silicon is the proof that the PDK, tooling and IP layers work.

## Resources

Loose collection of links for fleshing this item out: [resources/shuttle-program.md](../resources/shuttle-program.md).

## Related items

- [asic-scoreboard](asic-scoreboard.md) (ASIC benchmarking): Every shuttle design joins the benchmark corpus.
- [shadow-pdks](shadow-pdks.md) (Open "almost manufacturable" PDKs): Validates the open PDKs.
- [cell-foundry](cell-foundry.md) (Standard cell generation): Proves cell libraries in silicon.
- [open-links](open-links.md) (Open high-speed connectivity IP): Proves connectivity PHYs in silicon.
- [tcad-twin](tcad-twin.md) (Open TCAD stack): Measured silicon validates TCAD.
- [drc-forge](drc-forge.md) (Design rule checking (DRC)): Every shuttle submission passes the design rule check precheck.
