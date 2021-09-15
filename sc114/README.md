### OVERVIEW

This directory contains various files that might be useful to the owner of an SC114 Z80 SBC. **I make no guarantees it will work for you and consider it experimental and not thorougly tested**.

The initial collection of code is for SC114's that can run CP/M with an ACIA serial board as part
of their setup. In my own case I have a very minimal system consisting of the SC114 and Rotten Snow's #61 Missing Module. The #61
is provides an ACIA serial interface along with Compact Flash storage. With just these two boards (SC114 + #61) you can construct
a complete CP/M system with up to ~128Mb of storage. However, the default CP/M for this system ONLY implements the ACIA serial
interface to the console. So no other I/O is possible.

Based on ACIA CBIOS code kindly provided Paul Wrightson, I was able to create a modified CBIOS that implements the default CP/M LST: and PUN: devices using the built-in bitbang interface of the SC114. This should enable connection to various serial devices such as printers, a real paper tape punch (should you have one!) and any other unidirectional output device. Be aware however, that the current code is fixed at 9600 baud. If you are using some vintage gear on that port you may need to add additional delays to lower the baud rate to 300 or even 110 (say for a real Teletype). However, for routing LST: output to a host computer via USB it works fine at 9600 baud.

As proof-of-concept, I wrote a short proxy in Python to listen for output from the bitbang interface and forward it to a real printer (a Brother laster printer in my case). This enabled me to actually print directly from WordStar on the SC114 to the Brother printer (included formatted text!).

**NOTE**: All of this works fine on my system with the SC113 and Rotten Snow's "Missing Module" board and a 128MB CF card. This is all I have to test with right now, so **proceed with caution**. I plan to get a second ACIA and SIO/2 boards soon to tinker with and test this setup. But that may take some time.

### THE FILES

The files included here are as follow:

**CBIOS_ACIA_CF64_CF128_pw.asm** - Paul's original code as provided to me (with an attribution added)

**CBIOS_SC114_ACIA_BITBANG_CF64_CF128.asm** - Modified CBIOS source to implement the bitbang versions of LPT: and PUN:. I tried to make the IOBYTE work correctly between the new output and the existing two ACIA ports in the code. I only have one ACIA port available (currently), so I am unable to test whether the second port works as it should. 

**PUTSYS-SC114-ACIA-BITBANG_CFxx.hex** - A hex file suitible for loading the usual PUTSYS program into
the SC114's SCM monitor. Choose the value CFxx to match your CF card. Paste this at the "\*" prompt and execute "G8000" to write the
system tracks on your compact flash card. xx denotes the CF card size (64MB vs 128MB). Caution, I have not test the 64MB as I only have 128MB at the moment. But it should work ok...

**printproxy.py** - The printer proxy. It requires python 2.7+, a system with an LPR command and a
default printer set up on the system. It was tested on MacOS but should work on Linux and other unix-like systems. The program is pretty simple and should be easily modifiable for Windows.

### BUILDING

Building a new putsys is a two step process. Using Steve Cousins' Small Computer Workshop:
1. Load the CBIOS_SC114_ACIA_BITBANG_CF64_CF128.asm, edit if necessary to match your CF capacity (64MB vs 128MB) and assemble it. You simply need to change the #DEFINE SIZE128 or SIZE64 at the beginning of the file. This will generate a file "Intel.hex" in the SCW's Output directory. Copy this to the directory "...CPM v2.2 PutSys Plus/Includes" and rename it CBIOS_RC2014_ACIA_CFxx.HEX where xx is 64 or 128 as appropriate.
2.  Then load "PutSysPlus.asm" into SCW, edit the #define to specify your CF capacity and assemble. The new "Intel.hex" file will now be your new putsysplus. With an already formatted CF card, simply paste this into the SCM monitor and execute "G8000" to write it to your CF card. You should be able to immediately type "cpm" and start the system. If this is a new CF Card, follow the instructions at Steve Cousin's website for installing download.com and subsequent CP/M utilities.

### SETUP

You will now need two serial adapters. Presumably  you already have one (likely TTL to USB) to operate your system, and attached to some ACIA card. You can now use a SECOND adapater to connect the bitbang port to your host computer. Open terminals to both USB devices as shown on your system. Make sure to get the baudrates correct. The bitbang can ONLY do 9600 baud.

With both terminals open, in the one connected to your CP/M console type:
pip LPT:=test.txt
where test.txt can be any text file you'd like to see transferred. You should also
be able to pip to PRN: and LST: with the same effect.

You can use stat to see the current assignments and also override my default IOBYTE settings.

If you would prefer a different default setup, you can edit CBIOS_ACIA_CF64_CF128_wBB_.asm. The line that sets the default IOBYTE is near the very end of the file.
