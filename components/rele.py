# @proyect inKoutPi
# rele component
__author__ = 'rbioque'

import wiringpi
import time

#Define GPIO relay
PIN_WIRE = 18
PIN_FAN = 23

#Define GPIO state
ON = 1
OFF = 0

class Rele:

	def __init__(self):
		wiringpi.wiringPiSetupGpio()
		wiringpi.pullUpDnControl(PIN_FAN, OFF)
		wiringpi.pullUpDnControl(PIN_WIRE, OFF)

	def hotWire(self, status):
		if status:
			wiringpi.pinMode(PIN_WIRE, ON)
		else:
			wiringpi.pinMode(PIN_WIRE, OFF)
	
	def fan(self, status, waitTime=0):
		time.sleep(waitTime)

		if status:
			wiringpi.pinMode(PIN_FAN, ON)
		else:
			wiringpi.pinMode(PIN_FAN, OFF)

