# @proyect inKoutPi
# sensor component
__author__ = 'rbioque'

import Adafruit_DHT

#Define sensor type (DHT22) and GPIO number
SENSOR = 22
PIN = 4

#Calibrate DHT22
DHT_CAL = 0.6

class Sensor:

        def __init__(self):
		read_retry()

        def getTemp(self):
                return self.temp;

	def getHumi(self):
		return self:humi;
	
	def read_retry(self):
		self.humi, self.temp = Adafruit_DHT.read_retry(SENSOR, PIN)
                # Calibrate
                self.temp = self.temp + DHT_CAL


