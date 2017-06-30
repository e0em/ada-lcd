#!/usr/bin/python
# Example using a character LCD plate.
import time

import Adafruit_CharLCD as LCD
from subprocess import *
from time import sleep, strftime
from datetime import datetime

# Initialize the LCD using the pins
lcd = LCD.Adafruit_CharLCDPlate()
show_eth0_cmd = "ip addr show eth0 | grep inet | awk '{print $2}' | cut -d/ -f1"
show_wlan0_cmd = "ip addr show wlan0 | grep inet|grep -v inet6 | awk '{print $2}' | cut -d/ -f1"
# Show button state.
lcd.clear()
lcd.message('Press buttons...')
def run_cmd(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output
# Make list of button value, text, and backlight color.
buttons = ( (LCD.SELECT, 'Select'),
            (LCD.LEFT,   'Left'  ),
            (LCD.UP,     'Up'    ),
            (LCD.DOWN,   'Down'  ),
            (LCD.RIGHT,  'Right' ) )

#print('Press Ctrl-C to quit.')
while True:
    # Loop through each button and check if it is pressed.
    #for button in buttons:
    #    if lcd.is_pressed(button[0]):
    #        # Button is pressed, change the message and backlight.
    #        lcd.clear()
    #        lcd.message(button[1])
    if lcd.is_pressed(LCD.UP):
        lcd.clear()
        eth0 = run_cmd(show_eth0_cmd)
        lcd.message('eth0:\n%s' % (eth0.split()[0]))
    if lcd.is_pressed(LCD.DOWN):
        lcd.clear()
        wlan0 = run_cmd(show_wlan0_cmd)
	if wlan0 == '':
            lcd.message('wlan0:None')
        else:
            lcd.message('wlan0:\n%s' % (wlan0.split()[0]))
    if lcd.is_pressed(LCD.LEFT):
        lcd.clear()
        lcd.message('Rebooting')
        run_cmd("reboot")
