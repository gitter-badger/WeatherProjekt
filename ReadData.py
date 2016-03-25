#read data from a BME280 Sensor and write it into a LOG<date>.txt file
#
#author Benjamin Koderisch
#version 1.0 25.03.16

from time import *
import time
from Adafruit_BME280 import *

sensor = BME280(mode=BME280_OSAMPLE_8)

temp = sensor.read_temperature()
pascals = sensor.read_pressure()
press = pascals / 100
hum = sensor.read_humidity()

def writeDATA():
        #write year, month and day in the title
	f = open('LOG' + strftime("%Y%m%d", time.localtime())'.txt', 'a')
	f.write(time.strftime("%Y%m%d%H%M%S", time.localtime()) + '\n' + 
                'TEMP {0:0} | PRESS {} | HUM {} \n'.format(temp, press, hum))
	f.close()

	
while True:
	writeDATA()
	#900 = 15 min
	time.sleep(2)
