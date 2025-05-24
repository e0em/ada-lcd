#!/bin/bash
# Install Poetry
curl -sSL https://install.python-poetry.org | python3 -
# Add Path 
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
# sudo apt install python-dev
# sudo pip install Adafruit-GPIO Adafruit-PureIO Adafruit-CharLCD
sudo pip3 install adafruit-circuitpython-charlcd
