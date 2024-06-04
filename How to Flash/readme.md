# How to Flash DMA Firmware

> [!NOTE]
> This is a WIP (WORK IN PROGRESS), not everything is finished


TODO:
- 100T flashing


Finished:
- [X] CaptainDMA
- [X] GhostDMA


# Content
- 35T
  - [CaptainDMA]()
    - 3rd Gen(squirrel)
    - 4th Gen
    - 4.1th Gen
    - 5th Gen
    
  - [Leet]()
  - [MVP]()
  - [HackDMA]()
  - [GhostDMA](https://github.com/Rakeshmonkee/DMA/blob/main/How%20to%20Flash/readme.md#ghostdma-35t)
- 75T
  - [CaptainDMA]()
  - [MVP]()
- 100T
  - [Lightingz]()





# CaptainDMA 35T

Everything done here is on the second computer. Make sure your cable on the DMA is connected to the JTAG port

#### Download 
-  [Open OCD](https://github.com/Rakeshmonkee/DMA/tree/main/How%20to%20Flash/OpenOCD)
-  [Zadig](https://zadig.akeo.ie/)
-  [Flash_Screamer](https://docs.lambdaconcept.com/screamer/_downloads/20c4c1c1dc18e10efea198d236ac015f/flash_screamer.zip)

#### Steps

##### Zadig

1. Open Zadig as Admin
2. Click on Options > Show all devices
3. In the drop-down menu, select your device, which should be RS232 +HS(Interface 0)
4. Click on reinstall driver. This should replace the FTDI Bus Driver with WinUSB 

Let the driver install it. You don't need to restart.

##### Open OCD and Flash_Screamer
1. Unzip both of the folders and place them on your Desktop. There should be the OpenOCD and flash_screamer folder on your Desktop.
2. With your .bin (Firmware) file, place this inside the flash_screamer folder.


##### Flashing Firmware

Before Flashing, make sure the USB is connected to the JTAG slot on your DMA board

1. Open the command prompt as a user and cd to `Desktop/flash_screamer`
2. Once you are in the flash_screamer folder, on a new command line type in `..\openocd\bin\openocd.exe -f flash_screamer_squirrel.cfg`
3. Your Firmware should flash and show something like

```
Info : sector 0 took 113 ms
Info : sector 1 took 108 ms
Info : sector 2 took 113 ms
Info : sector 3 took 116 ms
Info : sector 4 took 125 ms
Info : sector 5 took 114 ms
Info : sector 6 took 110 ms
Info : sector 7 took 98 ms
Info : sector 8 took 122 ms
Info : sector 9 took 118 ms
Info : sector 10 took 117 ms
Info : sector 11 took 114 ms
Info : sector 12 took 108 ms
```

Will go up to sector 23 or 24

Once it shows something like

```
Info : Found flash device 'issi is25lp256d' (ID 0x0019609d)
Warn : device needs paging or 4-byte addresses - not implemented
shutdown command invoked
``` 

This means the Firmware has successfully flashed onto your DMA board.

You will now need to restart your Main PC. (It is necessary to restart your Main PC after flashing)


# GhostDMA 35T

#### Download 

Download the OpenOCD and CH341PAR folders provided above.

- [OpenOCD](https://github.com/Rakeshmonkee/DMA/tree/main/How%20to%20Flash/OpenOCD)
- [CH341PAR](https://github.com/Rakeshmonkee/DMA/tree/main/How%20to%20Flash/CH341PAR)

#### Steps
1. Put the cable into the JTAG / CFG / UPDATE port on the dma
2. Open the CH341PAR folder and once open, right-click on the `CH341WDM.inf` file and click install
3. Open the OpenOCD folder and place your firmware (.bin) file inside and rename the file to `firmware.bin` instead of the original `pcileech_squirrel_top.bin`
4. In the OpenOCD folder, type `cmd.exe` into the search address and hit enter

![image](https://github.com/Rakeshmonkee/DMA/assets/89455475/016a29e6-b432-4429-aa74-806b57d914c3)

![image](https://github.com/Rakeshmonkee/DMA/assets/89455475/7ec678b1-094a-4f52-9721-2b12c855a552)

5. in command prompt type in `openocd.exe -f flash.cfg` and hit enter

![image](https://github.com/Rakeshmonkee/DMA/assets/89455475/660e5f2e-3a5f-4261-baf4-2fae8812de2c)

Command prompt should spit out sector information, let this run. After its flashed, it will say something like `Close CH347`, once this is shown your firmware has been flashed. Restart Main pc to see the changes





# 75T and 35T CH347

#### Download 
-  [Ch347 FPGA Flash tool](https://github.com/WCHSoftGroup/ch347/tree/main/CH347FPGATool)

#### Chip Info

35T - XC7A35T

75T - XC7A75T


#### Steps

1. Run the executable
2. Chose the FPGA chip you have (look at chip info above)
3. Change from bit to bin in the drop-down
4. leave the clock speed as the default
5. Select the .bin file (firmware)
6. Download

Hitting download should then begin the flashing phase

Once it says something like; Close the ch347 ..... This means the firmware has been flashed

