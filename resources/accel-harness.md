# LiteX accelerator interface (FPGA and ASIC harness) — resources

Loose collection, 2026-10-19. Drive links are publicly shared (anyone with the link). One idea, two focuses: LiteX on FPGA, and the ASIC side (Sea2sky-style harness, Caravel-type management SoC).

## Tim's Google Drive (public)
### Interface and bridges (FPGA focus)
- [LiteX based interface for Hardware Accelerators — j.mp/litex-ha-dd](https://docs.google.com/document/d/1oiTqR-6ppiObBRFA91sxl3sgHkPHw2WK_tFD5itx9xg/edit) — the core design doc
- [LiteX Bridge Protocol](https://docs.google.com/document/d/1d_Uy6oljyYS4vZhSWomF-IWtP-vDN8qYYra6-Q8KLec/edit) — transport-independent bridge proposal
- [LiteX Wishbone Bridge Infrastructure](https://docs.google.com/drawings/d/13bRFtmgb7Og6hmWEYqxPrfbshxPwuIRDJ0NzPKeBoZs/edit) — diagram
- [LiteX Bridge Stack - Wishbone Tool](https://docs.google.com/drawings/d/1yCMsro2pEJlpgMA53greWiHGTBBI2Lo4yYT16ZwY3rU/edit) — diagram
- [Renode Wishbone Bridge Infrastructure](https://docs.google.com/drawings/d/1tfDZcxK3Ui8EaOnEDisxe8_LyromUIGIFkmcP76gBdc/edit) — same seam in simulation
- [LiteEth DMA Interface](https://docs.google.com/document/d/16GfKhTI6OD07oObcxq31JeKApqx4q4YHZIcNfv63gQo/edit) — high-performance Ethernet DMA
- [Eco - Improve liteeth DMA support](https://docs.google.com/document/d/1JSMUnYNa5VeUnTwYJSekbN6CsM_FiLORUsJbN4nKJPQ/edit) — project brief
- [Making GnuRadio-like flow graphs transport agnostic (FPGA + CPU partitioning)](https://docs.google.com/drawings/d/1C_YMtqvMMmxxSDfzvcU_xfAVzsImyB_rwE7p7mEbYKU/edit) — streaming over any link
- [FPGA based PCIe switch card](https://docs.google.com/drawings/d/1jN8RX05T-oKbTXVYYRqX1Xmr4Rj7xM6iq0hjG8EaQGw/edit) — host attachment idea
- [Tileable FPGA Acceleration Card](https://docs.google.com/drawings/d/1aSf8k3cqbqkVg8b0qUEA2YsN3eglmWIUPSWf07-_HMw/edit) — hardware concept
- [LiteX: SoC builder framework](https://docs.google.com/presentation/d/1mQOWqgmyQxpjLAzFwCulqgkp0TuxmaIDYp5iUfPqqIk/edit) — Florent Kermarrec's overview deck
- [litex (liteDRAM, liteVideo, liteEth) Supported boards & Interfaces](https://docs.google.com/spreadsheets/d/1q5CUI289TjGw9c66wAesOHlvH8RVo-OK6_yJ4btzZPA/edit) — board/transport matrix
- [LiteX Soft-CPU, FPGA and Firmware Support](https://docs.google.com/spreadsheets/d/1XTHfdYXuvwoYdPXm4M6qDA0D2fZCPy220-9q6qZpTw4/edit) — support matrix
- [LiteX Ecosystem Diagram](https://docs.google.com/drawings/d/15hSX1cHwz2_Lm-CxQxlelGUuVPP4AmEEljyRb1ncjjk/edit) — marked outdated
### ASIC harness focus
- [ASIC with FPGA Harness](https://docs.google.com/drawings/d/1iXQW7JOGi_LUP37g6Y4jMcrJRuAju48vB42z3v-9pm4/edit) — test chip driven from an FPGA
- [CIIC Harness](https://docs.google.com/drawings/d/1EW_pDHeUynlbNywJdXtivPt5s8F4cmcCIHLPNi3PIzM/edit) — harness diagram
- [Caravel I/O usage and status](https://docs.google.com/drawings/d/140bSCN_eblM0X-EArHoSA6zc64pyFjdcKACfIWN_Y8E/edit) — Caravel harness pins
- [Google/Efabless - IP development to improve Caravel functionality](https://docs.google.com/document/d/1S1k-zUKafO88JBQ861PhzUVRebG8IsXTyDNsEtyBFfo/edit) — harness IP wish list
- [Renode for simulation of the Caravel (and user project) testing system](https://docs.google.com/document/d/1qhin7U1esp58NoVwrdkKkEDZb2k280YF0PKGENGgLSI/edit) — harness in simulation

## Projects and repositories
- [LiteX](https://github.com/enjoy-digital/litex) — SoC builder, CSR generation, `litex_server`, Etherbone/UART/JTAG bridges
- [LitePCIe](https://github.com/enjoy-digital/litepcie), [LiteEth](https://github.com/enjoy-digital/liteeth), [LiteDRAM](https://github.com/enjoy-digital/litedram), [LiteSATA](https://github.com/enjoy-digital/litesata) — transport and memory cores
- [wishbone-utils](https://github.com/litex-hub/wishbone-utils) — host-side Wishbone bridge tool
- [LUNA](https://github.com/greatscottgadgets/luna) — USB gateware (USB2, experimental USB3)
- [Caravel](https://github.com/efabless/caravel) and [caravel_user_project](https://github.com/efabless/caravel_user_project) — ASIC harness with management SoC (LiteX-generated VexRiscv in later versions)
- [Coyote](https://github.com/fpgasystems/Coyote) — open FPGA shell with PCIe/network services
- [RIFFA](https://github.com/KastnerRG/riffa) — PCIe host link for FPGAs
- [Xilinx XRT](https://github.com/Xilinx/XRT) and Intel OPAE — vendor accelerator runtimes for comparison
- [OpenTitan](https://github.com/lowRISC/opentitan) — TL-UL on-chip bus example in silicon

## Papers and other reading
- Kermarrec et al., "LiteX: an open-source SoC builder and library based on Migen Python DSL" (OSDA 2019, arXiv:2005.02506)
- Korolija et al., "Do OS abstractions make sense on FPGAs?" (Coyote, OSDI 2020)
- Jacobsen et al., "RIFFA 2.1: A Reusable Integration Framework for FPGA Accelerators" (ACM TRETS 2015)

## Also listed on mith.ro

- [LiteX Firmware](https://docs.google.com/document/d/11uzjWRWk9-KuBFc7chUNUluL5ajysY2qfXvt1vttl7k/edit)
- [LiteX Linux Support Random Notes](https://docs.google.com/document/d/1GfWKjrcfA27qbF8F9EtvRP5mzsaBjRzADfZTb5H8irw/edit)
- [MiSoC / LiteX HDMI refactoring - PixelBone](https://docs.google.com/document/d/1L8lz7u2uj6MrzSQv4b1Vk6Rmic26okyRklOju5IWLYA/edit)
- [Testing environments and CI for open hardware projects (Open MPW program, Caravel, LiteX, F4PGA, etc) - bit.ly/test-env-asics](https://docs.google.com/document/d/1YgJ-MUC-r9-Stl1M98xjTq8Qf-YQy6LNu38Ov5K5pt0/edit)
- [Types of "testing" in LiteX (and Migen/MiSoC)](https://docs.google.com/document/d/1SLRMCTETNKA0Cfy8dExF8QAn8j0FVbUEgorsicJmoeU/edit)
