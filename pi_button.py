#!/usr/bin/python
# Example using a character LCD plate.
import time
import os
import subprocess
#from time import sleep, strftime
#from datetime import datetime
import board
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd

# Modify this if you have a different sized Character LCD
lcd_columns = 16
lcd_rows = 2

# Initialise I2C bus.
i2c = board.I2C()  # uses board.SCL and board.SDA

# Initialise the LCD class
lcd = character_lcd.Character_LCD_RGB_I2C(i2c, lcd_columns, lcd_rows)

show_eth0_cmd = "ip addr show eth0 | grep inet | awk '{print $2}' | cut -d/ -f1"
show_wlan0_cmd = "ip addr show wlan0 | grep inet|grep -v inet6 | awk '{print $2}' | cut -d/ -f1"
# Show button state.
lcd.clear()
lcd.message = 'Press buttons...'
def run_cmd(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    output = p.communicate()[0]
    return output

#print('Press Ctrl-C to quit.')
while True:
    # Loop through each button and check if it is pressed.
    #for button in buttons:
    #    if lcd.is_pressed(button[0]):
    #        # Button is pressed, change the message and backlight.
    #        lcd.clear()
    #        lcd.message(button[1])
    if lcd.up_button:
        lcd.clear()
        eth0 = run_cmd(show_eth0_cmd)
        print(eth0)
        if eth0 == b'':
            lcd.message = 'eth0:None'
        else:
            lcd.message = 'eth0:\n%s' % (eth0.split()[0])
        time.sleep(5)
    elif lcd.down_button:
        lcd.clear()
        wlan0 = run_cmd(show_wlan0_cmd)
        if wlan0 == b'':
            lcd.message = 'wlan0:None'
        else:
            lcd.message = 'wlan0:\n%s' % (wlan0.split()[0])
        time.sleep(5)
    elif lcd.left_button:
        lcd.clear()
        lcd.message = 'Some Message...'
        time.sleep(5)
        #os.system("/home/marty/github/ServerPython/sub_mqtt_local_raw_lcd.py -d")
        #run_cmd("python /home/marty/github/ada-lcd/sub_mqtt_local_raw_lcd.py")
    elif lcd.right_button:
        lcd.clear()
        lcd.message = 'Play Music...'
        time.sleep(5)
        #player = subprocess.Popen(["/usr/bin/mplayer", "/home/marty/tyxg.mp3", "-ss", "30"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
        time.sleep(0.1)
        lcd.clear()
        lcd.message = "Hello World"
