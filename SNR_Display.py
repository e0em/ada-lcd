#!/usr/bin/python

import Adafruit_CharLCD as LCD
import sys
import time
import json
from subprocess import *
from time import sleep, strftime
from datetime import datetime

lcd = LCD.Adafruit_CharLCDPlate()

#cmd = "ip addr show eth0 | grep inet | awk '{print $2}' | cut -d/ -f1"
#cmd = "ip addr show wlan0 | grep inet|grep -v inet6 | awk '{print $2}' | cut -d/ -f1"
cmd = "hostname -I"


def run_cmd(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output

#lcd.clear()
#ipaddr = run_cmd(cmd)
#lcd.message(datetime.now().strftime('%b %d  %H:%M:%S\n'))
#lcd.message('IP%s' % (ipaddr.split()[0]))
#print ipaddr.split()[0]

k = 0
try:
    buff = ''
    while True:
        buff += sys.stdin.read(1)
        if buff.endswith('\n'):
            json_data = buff[:-1]
            #print(json_data)
            sensor_snr = json.loads(json_data)['snr']
            sensor_rssi = json.loads(json_data)['rssi']
            sensor_mac = json.loads(json_data)['macAddr']
            sensor_count = json.loads(json_data)['frameCnt']
            print('Count:'+str(sensor_count).rjust(6) + '\tMac:'+ str(sensor_mac)[8:]+'\tSNR:'+ str(sensor_snr).rjust(4)+ '\tRSSI:' + str(sensor_rssi).rjust(4))
            lcd.clear()
            lcd.message('Mac:'+ str(sensor_mac)[8:]+'Cnt:'+str(sensor_count))
            lcd.message('\nSNR/RSSI'+ str(sensor_snr)+ '/' + str(sensor_rssi))
            buff = ''
            k = k + 1
except KeyboardInterrupt:
   sys.stdout.flush()
   pass
print k
