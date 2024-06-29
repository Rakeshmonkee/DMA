# DMA Troubleshooting


Common Types of DMA Errors
1. VMM Init fails
2. FPGA Error: Unable to connect to USD/FT601 device
3. Tiny PCIe TLP Algo


## VMM INIT FAIL

Main Reasons why VMM INIT Failed is thrown when doing a speed test or trying to connect the DMA to VMM
1. FTDI Drivers on radar / second PC are not correctly installed / corrupted
2. Main Computer Bios Virtualisation (VMT) / IOMMU is not Disabled.
3. USB Cable is still in JTAG port, not the DATA port.
4. Bad firmware


### How to fix:
1. On the second computer, head to [FTDI3XX](https://ftdichip.com/drivers/d3xx-drivers/) website and download the latest compatible driver for your computer.

![image](https://github.com/Rakeshmonkee/DMA/assets/89455475/96935470-bd1e-4ef5-a7cc-a9f39ebb8292)

if your computer is a 64-bit operating system, download the X64 (64-Bit) driver

if your computer is a 32-bit operating system, download the X86 (32-Bit) driver


Once the folder has downloaded, extract the folder to your desktop.

Back in the folder right right-click on the `ftdibus3.inf` file and click install.

![image](https://github.com/Rakeshmonkee/DMA/assets/89455475/c10aa9c9-ecea-4653-bd6e-80eecb863578)

