# Transport-agnostic accelerator interface (LiteX)

## Goal

A well-lit path where an accelerator developer writes a block once and attaches it to a host over Ethernet, USB 3.0, PCIe or an on-chip bus (Wishbone, AXI) without changing it. Control registers (CSRs) and streaming endpoints are abstracted over the transport, with modes for simulation, debugging and high-performance DMA. The same interface works on an FPGA and in silicon.

## Why it is high value

- Most of the effort in building an accelerator goes into the plumbing (host link, drivers, DMA, register maps), not the compute block. A standard interface removes that cost for every open accelerator project.
- It gives the composable simulation project a standard seam: a block behind this interface can move between Renode, Verilator, FPGA and silicon without its software changing.
- Writing and testing transport back-ends, host drivers and example accelerators across many boards is broad, repetitive and testable work suited to agents.

## State of the art

- LiteX already has the pieces: Etherbone (Wishbone over Ethernet), UART and JTAG bridges, LitePCIe, LiteEth and USB cores, CSR generation and `litex_server` with remote access from host scripts.
- What is missing is one documented abstraction that hides which transport is in use, plus a high-performance streaming and DMA mode on every transport.
- Comparable approaches elsewhere: Xilinx XRT and Vitis kernels, Intel OPAE, Coyote and the RIFFA and Xillybus host links. They are vendor-specific or tied to one transport.

## Open questions

- The CSR and streaming abstraction: extend LiteX's existing CSR and stream interfaces, or define a new spec that other frameworks can implement?
- Which transports come first, and the performance target on each (latency and bandwidth for PCIe, Ethernet and USB 3.0).
- How host software is exposed (Python, a C library, Linux kernel drivers) and how it stays identical across transports.
- How it lines up with the LiteX bridge protocol used for composable simulation.

## Sources

Tim's design docs: [LiteX based interface for Hardware Accelerators](https://docs.google.com/document/d/1oiTqR-6ppiObBRFA91sxl3sgHkPHw2WK_tFD5itx9xg/edit), [LiteX Bridge Protocol](https://docs.google.com/document/d/1d_Uy6oljyYS4vZhSWomF-IWtP-vDN8qYYra6-Q8KLec/edit).
