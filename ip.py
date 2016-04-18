#!/usr/bin/python
# Example using a character LCD plate.
import time

import Adafruit_CharLCD as LCD


# Initialize the LCD using the pins 
lcd = LCD.Adafruit_CharLCDPlate()
from subprocess import *
cmd = "ip addr show wlan0 | grep inet|grep -v inet6 | awk '{print $2}' | cut -d/ -f1"
def run_cmd(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output

# Show some basic colors.
lcd.set_color(1.0, 0.0, 0.0)
lcd.clear()
ipaddr = run_cmd(cmd)
lcd.message('IP: %s' % (ipaddr))
time.sleep(3.0)

