#!/usr/bin/python
# @proyect inKoutPi
# @autor rbioque
# Temperature control by DHT22 and Relay Module

import sys
import Adafruit_DHT
import logging
import wiringpi
import time

#Define sensor type (DHT22) and GPIO number
SENSOR = 22
PIN = 4

#Define GPIO relay
PIN_WIRE = 18
PIN_FAN = 23
ON = 1
OFF = 0

#Calibrate DHT22
DHT_CAL = 0.6

wiringpi.wiringPiSetupGpio()
wiringpi.pullUpDnControl(PIN_FAN, OFF)  
wiringpi.pullUpDnControl(PIN_WIRE, OFF)

#Define log file
logging.basicConfig(filename='/var/log/inkoutpi.log', 
                    level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)s: %(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S')

# Define temperature/humidity range
TEMP_MAX = 32.10
TEMP_MIN = 32.00
HUMI_MIN = 70.00


# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(SENSOR, PIN)

# Calibrate
temperature = temperature + DHT_CAL

# Enable heating wire
def hot_wire(enable):
    if enable:
        logging.info('Heating wire enabled Temp={0:0.1f}* < Temp_min={1:0.1f}'.format(temperature, TEMP_MIN))
	wiringpi.pinMode(PIN_WIRE, ON)
	logging.debug(wiringpi.digitalRead(PIN_WIRE))
    else:
        logging.info('Heating wire disabled Temp={0:0.1f}* > Temp_max={1:0.1f}'.format(temperature, TEMP_MAX))
	wiringpi.pinMode(PIN_WIRE, OFF)
	logging.debug(wiringpi.digitalRead(PIN_WIRE))
    return;

# Enable fan
def fan(enable):
    if enable:
        logging.info('fan enabled')
	wiringpi.pinMode(PIN_FAN, ON)
	logging.debug(wiringpi.digitalRead(PIN_FAN))
	time.sleep(240)
	logging.info('fan disabled')
	wiringpi.pinMode(PIN_FAN, OFF)
	logging.debug(wiringpi.digitalRead(PIN_FAN))
    else:
	logging.info('fan disabled')
	wiringpi.pinMode(PIN_FAN, OFF)
	logging.debug(wiringpi.digitalRead(PIN_FAN))
    return;

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
# If this happens try again!

if temperature is not None and humidity is not None:
    logging.info('Temp={0:0.11f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
else:
    logging.error('Failed to get reading. Try again!')

if temperature is not None:
    if temperature <= TEMP_MIN:
        hot_wire(True)
        fan(True)
    elif temperature >= TEMP_MAX:
        hot_wire(False)
#        fan(False)
else:
        logging.error('Failed to get reading. Try again!')

if humidity is not None and humidity < HUMI_MIN:
    logging.info('Send notice Humidity={0:0.1f}* < Humidity_min={1:0.1f}'.format(humidity, HUMI_MIN))





