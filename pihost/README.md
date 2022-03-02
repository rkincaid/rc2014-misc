Collection of files to support Raspberry Pi as host for RC2014 as a fuly connected CP/M machine. This supports:

1. Main console on serial port 1
2. Printer port on serial port 2
3. Internet Modem on serial port 3

You need to modify port assignments in various files to match your system and disable code for serial ports you don't have.  You'll need three RC2014 serial ports for full functionality. If you only have two, then decide if you want printer output or modem connectivity. If you only have one serial port you probably don't need any of this.

cpm.sh - A shell script that starts all necessary interfaces. Just run this (or include in your .bashrc file) to bring up the fully functioning cpm system.

printproxy.py - A python program that reads print the printer serial port and forwards to your default printer. This requires you set up your Raspberry Pi to have a default printer.

reset.py - This script uses a pin on the Raspberry pi to toggle a transistor switch to force a reset on the RC2014 bus.

startup.script - A minicom script that causes a reset and commands the rom monitor to automatically start CP/M
