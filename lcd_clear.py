#!/usr/bin/python
# Example using a character LCD plate.
import Adafruit_CharLCD as LCD

# Initialize the LCD using the pins 
lcd = LCD.Adafruit_CharLCDPlate()

# Show some basic colors.
lcd.set_color(1.0, 0.0, 0.0)
lcd.clear()

