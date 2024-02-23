# Creation of VGK Firmware

#### Before I start this off, I want to thank my friend Movinggun for initially showing me this method/technique on how to bypass VGK 💖. I was gonna release this earlier but I wanted a go from him.

This section will be quick and easy as there aren't many things to change

1. set `HEADER_TYPE` to 80
2. set `CAPABILITIES_PTR` to 80

By changing just these 2 values to 80 within the config space, you will break the config space and allow us to bypass VGK. If you do a speed test, tiny pcie tlp algo might be selected, this is for you to fix. Go NULL some stuff out in the cfg space till tiny pcie tlp algo goes away. I also suggest you expand on this more, don't just change some values and change Header_Type and Cap_Ptr.

Now you can save $200+ just by changing 2 lines

# Creation of ACE Firmware

Ace i will release soon when i feel like it
