# @proyect inKoutPi
# rele component
__author__ = 'rbioque'

import wiringpi
import time

#Define GPIO relay
PIN_WIRE = 18
PIN_PELTIER = 23
PIN_FAN = 24
PIN_FAN_PELTIER = 2

#Define GPIO state
ON = 1
OFF = 0

#Define components status
STATUS_ON = 0
STATUS_OFF = 1

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

	def isWireEnabled(self):
		return wiringpi.digitalRead(PIN_WIRE) == STATUS_ON;
	
	def isWireDisabled(self):
                return wiringpi.digitalRead(PIN_WIRE) == STATUS_OFF;
	
        def coldPeltier(self, status):
                if status:
                        wiringpi.pinMode(PIN_PELTIER, ON)
                else:
                        wiringpi.pinMode(PIN_PELTIER, OFF)

        def isPeltierEnabled(self):
                return wiringpi.digitalRead(PIN_PELTIER) == STATUS_ON;

        def isPeltierDisabled(self):
                return wiringpi.digitalRead(PIN_PELTIER) == STATUS_OFF;
	
	def fanPeltier(self, status):
		if status:
			wiringpi.pinMode(PIN_FAN_PELTIER, ON)
		else:
			wiringpi.pinMode(PIN_FAN_PELTIER, OFF)

	def isFanPeltierEnabled(self):
		return wiringpi.digitalRead(PIN_FAN_PELTIER) == STATUS_ON;

	def isFanPeltierDisabled(self):
		return wiringpi.digitalRead(PIN_FAN_PELTIER) == STATUS_OFF;

	def fan(self, status, waitTime=0):
		time.sleep(waitTime)

		if status:
			wiringpi.pinMode(PIN_FAN, ON)
		else:
			wiringpi.pinMode(PIN_FAN, OFF)

	def isFanEnabled(self):
		return wiringpi.digitalRead(PIN_FAN) == STATUS_ON;

	def isFanDisabled(self):
		return wiringpi.digitalRead(PIN_FAN) == STATUS_OFF;
