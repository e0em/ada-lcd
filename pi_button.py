#!/usr/bin/python
# Example using a character LCD plate.
#import time
import os
import Adafruit_CharLCD as LCD
import subprocess
#from time import sleep, strftime
#from datetime import datetime

# Initialize the LCD using the pins
lcd = LCD.Adafruit_CharLCDPlate()
show_eth0_cmd = "ip addr show eth0 | grep inet | awk '{print $2}' | cut -d/ -f1"
show_wlan0_cmd = "ip addr show wlan0 | grep inet|grep -v inet6 | awk '{print $2}' | cut -d/ -f1"
# Show button state.
lcd.clear()
lcd.message('Press buttons...')
def run_cmd(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
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
	if eth0 == '':
            lcd.message('eth0:None')
        else:
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
        lcd.message('LoRa Message...')
        os.system("/home/marty/github/ServerPython/sub_mqtt_local_raw_lcd.py -d")
        #run_cmd("python /home/marty/github/ada-lcd/sub_mqtt_local_raw_lcd.py")
    if lcd.is_pressed(LCD.RIGHT):
        lcd.clear()
        lcd.message('Play Music...')
        player = subprocess.Popen(["/usr/bin/mplayer", "/home/marty/tyxg.mp3", "-ss", "30"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        while True:
            if lcd.is_pressed(LCD.SELECT):
                lcd.clear()
                lcd.message('Stop Music')
                player.stdin.write("q")
                break
