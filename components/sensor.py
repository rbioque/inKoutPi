# @proyect inKoutPi
# sensor component
__author__ = 'rbioque'

import Adafruit_DHT
import datetime
import sys

sys.path.insert(0, '../')
from history import measure

#Define sensor type (DHT22) and GPIO number
SENSOR = 22
PIN = 4

#Calibrate DHT22
DHT_CAL = 0.6

class Sensor:

        def __init__(self):
		self.humi, self.temp = Adafruit_DHT.read_retry(SENSOR, PIN)
             	# Calibrate
           	self.temp = self.temp + DHT_CAL
		self.date = datetime.datetime.now()
		self.measure = measure.Measure(self.temp, self.humi, self.date)

	def getMeasure(self):
		return self.measure;

	#def read_retry(self):
		#self.humi, self.temp = Adafruit_DHT.read_retry(SENSOR, PIN)
                # Calibrate
                #self.temp = self.temp + DHT_CAL


