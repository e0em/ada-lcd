#!/bin/bash
echo "dtparam=i2c_arm=on
dtparam=i2c1=on" >> /boot/config.txt
echo "i2c-bcm2708
i2c-dev" >> /etc/modules
pip install Adafruit-GPIO Adafruit-PureIO Adafruit-CharLCD
