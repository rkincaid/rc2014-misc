#
# This program serves as a printer proxy for CP/M computers
# using a second serial port as a LST: or PUN: device.
# It was written specifically for my SC114 board using the built-in
# bit-bang interface as the LST: device. All input is sent directly
# to the default lpr printer without processing.
#
# This *should* work for other serial LST: devices if you change
# the serial device name and appropriate baud rate.
#
# The host computer I use is MacOS, but it should probably work
# as well for Linux. The main requirement is the host computer needs
# the lpr command and a default printer assignment.
#
# It can probably be modified to print with other means for Windows.
# 
# Note that if Wordstar (or other software) has drivers for the
# printer you are using, then it will send the appropriate formatted
# codes for more-or-less full formatted print functionality supported
# by your WordStar/printer combination.
#
import serial
import sys
import os
import time

#
# Change serialport and baudrate to match your setup
#
serialport = "/dev/cu.usbserial-141420"
baudrate = 9600
timeout = 2 # timeout in secs to guess end of print, change as needed

if __name__ == '__main__':
    ser = serial.Serial(serialport, baudrate, timeout=0)
    while (True):
        # open the spool file
        # CP/M is a single task system, so we don't expect multiple
        # input streams. One file will do.
        f = open('spool.txt', 'w+')
        lasttime=sys.maxint
        while (True):
            if ser.inWaiting() > 0:
                c = ser.read(1)
                lasttime = time.time()
                f.write(c)
            else:
                #if we're idling, check for timeout
                time.sleep(.5)
                thistime = time.time()
                if (thistime-lasttime)>timeout:
                    break
        f.close()

        # if the spool file is not tiny, go ahead and print
        # hack to get around suprious chars after resets, etc.
        # print some output to the console to track what's
        # happeing
        size = os.stat('spool.txt').st_size
        if size>10:
            print ('spooling %d byte file' % size)
            os.system('lpr spool.txt')
        else:
            print 'skipping tiny file'
    
    # we shouldn't actually get here...
    ser.close()


