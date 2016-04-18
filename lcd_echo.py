#!/usr/bin/python

import Adafruit_CharLCD as LCD
import sys
from subprocess import *
from time import sleep, strftime
from datetime import datetime

lcd = LCD.Adafruit_CharLCDPlate()

lcd.clear()
lcd.message(str(sys.argv[1])+str(sys.argv[2]))
