#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
import subprocess

# the serial port that is serving as your console
console = '/dev/ttyUSB0'

# the Pi pin that will invoke the /reset on the Z80 bus
ResetPin = 12

# set the CPIO mode
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ResetPin, GPIO.OUT)
# set the toggle the reset circuit holding high for a brief moment
GPIO.output(ResetPin,GPIO.HIGH)
time.sleep(0.2)
GPIO.output(ResetPin,GPIO.LOW)
# do some housekeeping
GPIO.cleanup()

# we have to wait briefly for the initial system to boot up
time.sleep(0.5)

# this is specific to SCM Bios. We inovke the cpm command to
# automatically bootup CPM from the SCM monitor
# if you are just booting without CPM you could change this to
# start BASIC or use othe commands on your style of ROM
with open(console,'w') as f:
	subprocess.Popen(['echo','-e','cpm\r'], stdout=f)
