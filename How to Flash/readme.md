# How to Flash DMA Firmware

### 35T

Everything done here is on the second computer

> [!IMPORTANT]
> This will not work with CH347 chips.

#### Download 
-  [Open OCD](https://docs.lambdaconcept.com/screamer/_downloads/e72a9b76299cd3a4cb30e53dd62505ff/openocd-win.zip)
-  [Zadig](https://zadig.akeo.ie/)
-  [Flash_Screamer](https://docs.lambdaconcept.com/screamer/_downloads/20c4c1c1dc18e10efea198d236ac015f/flash_screamer.zip)

#### Steps

##### Zadig

1. Open Zadig as Admin
2. Click on Options > Show all devices
3. In the drop-down menu, select your device, which should be RS232 +HS(Interface 0)
4. Click on reinstall driver. This should replace the FTDI Bus Driver with WinUSB 

Let the driver install. No restart is required.

##### Open OCD and Flash_Screamer
1. Unzip both of the folders and place them onto your Desktop. There should be the OpenOCD and flash_screamer folder on your Desktop.
2. With the .bin (Firmware) file you have, place this inside of the flash_screamer folder.


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


### 75T


