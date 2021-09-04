**OVERVIEW**

This directory contains various files that might be useful to the owner of an SC114 Z80 SBC.

The initial collection of code is for SC114's that can run CP/M with an ACIA serial board as part
of their setup. In my own case I have a very minimal system consisting of the SC114 and Rotten Snow's #61 Missing Module. The #61
is provides an ACIA serial interface along with Compact Flash storage. With just these two boards (SC114 + #61) you can construct
a complete CP/M system with up to ~128Mb of storage. However, the default CP/M for this system ONLY implements the ACIA serial
interface to the console. So no other I/O is possible.

Based on ACIA CBIOS code kindly provided Paul Wrightson, I was able to create a modifie CBIOS that implements the built-in bitbang interface of the SC114 as the default CP/M LST: and PUN: devices. This should enable connection to various serial devices such as printers, a real paper tape punch (should you have one!) and any other unidirectional output device.

As proof-of-concept, I wrote a short proxy in Python to listen for output from the bitbang interface and forward it to a real printer (a Brother laster printer in my case). This enabled me to actually print directly from WordStar on the SC114 to the Brother printer (included formatted text!).


