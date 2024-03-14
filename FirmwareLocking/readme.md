# Artix7 Firmware Locking

> [!IMPORTANT]
> This section is a work in progress. Stuff will change over time


__What is Firmware Locking__
: Firmware locking refers to the process of securing the firmware on a device to prevent unauthorized access, modification, or copying

__How does Firmware Locking Work?__
: Firmware locking works by getting the EFUSE FUSER_DNA value of the Artix7 chip from your DMA card and running a check on system bootup to check if a hard-coded(yourDNA) value is the same as your Artix7 DNA.
If the DNA values match, the firmware will work, otherwise, the firmware won't work. This is intended to work for 1 person, and 1 person only since Artix7 chips have their own <b>Unique Identifier</b>(DNA). 

To get the Values required, we'll be using <b>Openocd</b>

Within Command Prompt

Navigate to ```Openocd/bin```

We will be using the Openocd.exe process and the `xilinx-dna.cfg` script found in `/Openocd/scripts/fpga` to get our Artix7 chip FUSER_DNA value

