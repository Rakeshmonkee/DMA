# DMA Troubleshooting


Common Types of DMA Errors
1. [VMM Init fails](https://github.com/Rakeshmonkee/DMA/tree/main/DMA%20Troubleshooting#vmm-init-fail)
2. [FPGA Error: Unable to connect to USB/FT601 device](https://github.com/Rakeshmonkee/DMA/blob/main/DMA%20Troubleshooting/readme.md#fpga-error-unable-to-connect-to-usbft601-device)
3. [Tiny PCIe TLP Algo]()


## VMM INIT FAIL

Main reasons why VMM INIT failed is thrown when doing a speed test or trying to connect the DMA to VMM

1. FTDI Drivers on radar / second PC are not correctly installed / corrupted
2. Main Computer Bios Virtualisation (VMT) / IOMMU is not Disabled.
3. USB Cable is still in JTAG port, not the DATA port.
4. Bad firmware

### How to fix:

## 1. FTDI Drivers

On the second computer, head to [FTD3XX](https://ftdichip.com/drivers/d3xx-drivers/) website and download the latest compatible driver for your computer.

![image](https://github.com/Rakeshmonkee/DMA/assets/89455475/96935470-bd1e-4ef5-a7cc-a9f39ebb8292)

if your computer is a 64-bit operating system, download the X64 (64-Bit) driver

if your computer is a 32-bit operating system, download the X86 (32-Bit) driver

Once the folder has been downloaded, extract the folder to your desktop.

Back in the folder right right-click on the `ftdibus3.inf` file and click install.

![image](https://github.com/Rakeshmonkee/DMA/assets/89455475/c10aa9c9-ecea-4653-bd6e-80eecb863578)

## 2. Disabling Virtualisation / IOMMU

The following steps are within the BIOS


### MSI Click BIOS:
OC > Advanced CPU Configuration > SVM Mode > Disabled

### ASUS BIOS:

Advanced Mode[F7] > Advanced > CPU Configuration > Intel [VMX] Virtualisation Technology > Disabled

### Gigabyte BIOS:

Advanced Mode[F2] > Tweaker > Advanced CPU Settings > SVM Mode > Disabled

### ASRock:

Advanced > CPU Configuration > SVM MODE > Disabled

### Biostar:

Advanced > CPU Settings and Information > Intel Virtualisation > Disabled




## FPGA Error: Unable to connect to USB/FT601 device

Main reasons why FPGA Error: Unable to connect to USB/FT601 device

1. Faulty USBC-USB3.0 cable
2. USB Cable is still in JTAG port, not the DATA port.
3. FTDI Drivers on radar / second PC are not correctly installed / corrupted

### How to fix:

1. Buying a new USB-C to USB A cable. I recommend this USB Cable from [AMAZON](https://www.amazon.com.au/CableCreation-Transfer-10Gbps-Charging-External/dp/B09QKHPT35/ref=sr_1_2_sspa?dib=eyJ2IjoiMSJ9.Gf0JIfmmFhmI5TU_Hx-PfacNeAkKjmOlBeBQaKN5Xhblz2OF36mS3-0MK8Wo29I3qt4ENT1PMhz4ZhaDJQyAi7vufKb8VNex0zjJ616vM7wSm3wKbycBQEFiLNzK2PVC7A8DuTQ_7t5peKKf9irUWh5YSKGkPlv0IJKr99c34lmWqUjXwH7ywQFE7-XH27eh5WNilpeUUhX0VNogKm3mMVq_955BqxYOTdbvLpAnQPbrXCMZ37pyfRKBtHUP0OoQz9Qof_LYDRD8ePw5jf-yNQKIZQJvFSh25MHzqA-2c-I.JHVF_jJx0q260kYEsskiyps3NBXaqnXc8__Cn4lgsHc&dib_tag=se&keywords=usb%2Bc%2Bto%2Busb%2Ba%2B3.2&qid=1719671885&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1)

![image](https://github.com/Rakeshmonkee/DMA/assets/89455475/10bf26d1-ccb2-4b6c-9819-8353482959de)


2. Change the cable from the JTAG port to DATA Port

3. See [FTDI DRIVERS](https://github.com/Rakeshmonkee/DMA/tree/main/DMA%20Troubleshooting#1-ftdi-drivers)


## Tiny PCIe TLP Algo

Main reasons why Tiny PCIe TLP Algo is chosen

1. Faulty Firmware
2. Bad / faulty USB Cable.





