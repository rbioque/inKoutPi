#!/usr/bin/python
# @proyect inKoutPi
# @autor rbioque
# Temperature control by DHT22 and Relay Module

import sys
import Adafruit_DHT
import logging
import wiringpi

#Define sensor type (DHT22) and GPIO number
SENSOR = 22
PIN = 4

#Define GPIO relay
PIN_WIRE = 18
OUTPUT = 1

wiringpi.wiringPiSetup()
wiringpi.pinMode(PIN_WIRE, OUTPUT)

#Define log file
logging.basicConfig(filename='/var/log/inkoutpi.log', 
                    level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)s: %(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S')

# Define temperature/humidity range
TEMP_MAX = 27.0
TEMP_MIN = 26.0
HUMI_MIN = 70.0


# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(SENSOR, PIN)

# Enable heating wire
def hot_wire(enable):
    if enable:
        logging.info('Heating wire enabled Temp={0:0.1f}* < Temp_min={1:0.1f}'.format(temperature, TEMP_MIN))
	wiringpi.digitalWrite(PIN_WIRE, 1)
    else:
        logging.info('Heating wire disabled Temp={0:0.1f}* > Temp_max={1:0.1f}'.format(temperature, TEMP_MAX))
	wiringpi.digitalWrite(PIN_WIRE, 0)
    return;

# Enable fan
def fan(enable):
    if enable:
        logging.info('fan enabled')
    else:
        logging.info('fan disabled')
    return;

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
# If this happens try again!
if temperature is not None and humidity is not None:
    logging.info('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
else:
    logging.error('Failed to get reading. Try again!')

if temperature is not None:
    if temperature < TEMP_MIN:
        hot_wire(True)
        fan(True)
    elif temperature > TEMP_MAX:
        hot_wire(False)
        fan(False)
else:
        logging.error('Failed to get reading. Try again!')

if humidity is not None and humidity < HUMI_MIN:
    logging.info('Send notice Humidity={0:0.1f}* < Humidity_min={1:0.1f}'.format(humidity, HUMI_MIN))





