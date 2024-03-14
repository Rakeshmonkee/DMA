# Frequently Asked DMA Questions

__which DMA card should I get?__
: If you want to save money, 35T. If you don't mind spending more for a faster and new DMA card, I suggest the 75T.

__What Firmware do I need for my DMA card?__
: 35T - Squirrel,  75T - EnigmaX1.

__If I have a 35T, and I buy a new card E.g(cap DMA 4th Gen), is it fine to flash the same FW?__
: Yes, both 35T and 4th gen cap DMA share the same prototype chip (squirrel).

__What are the minimum specs I need for my second computer?__
: USB 3.0, at least 6GB RAM, 

__Why do I get Tiny PCIe TLP Algorithm when running a speed test?__
: This happens due to the motherboard in the main PC not liking the config space of the DMA FW.

__How do I flash my FW?__
: If you are using 35T, use Open OCD to [program](https://docs.lambdaconcept.com/screamer/programming.html) and [to upgrade](https://docs.lambdaconcept.com/screamer/openocd.html) or visit [How to Flash](https://github.com/Rakeshmonkee/DMA/tree/main/How%20to%20Flash)

__What donor board do I need?__
: Any PCIe Device technically can be used as a donor board. I wouldn't recommend using the values from an already existing PCIe Device you have on your computer. E.g. (GPU). I use an Intel Wifi 6 Ax200 card. You don't need to use this, you can use devices such as video capture cards, USB extensions, Sound Cards, SATA Expansion Cards, and so on.

__What is Firmware Locking__
: Firmware locking refers to the process of securing the firmware on a device to prevent unauthorized access, modification, or copying

__How does Firmware Locking Work?__
: Firmware locking works by getting the EFUSE FUSER_DNA value of the Artix7 chip from your DMA card and running a check on system bootup to check if a hard-coded(yourDNA) value is the same as your Artix7 DNA.
If the DNA values match, the firmware will work, otherwise, the firmware won't work. This is intended to work for 1 person, and 1 person only since Artix7 chips have their own <b>Unique Identifier</b>(DNA). 



More coming soon
