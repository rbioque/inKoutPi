#!/usr/bin/python

# @proyect inKoutPi
# init
__author__ = 'rbioque'

import sys
import logging
import time

from config import configDao, config
from history import historyDao, measure
from components import sensor, rele
from alerts import mail

#Define log file
logging.basicConfig(filename='/var/log/inkoutpi.log',
                    level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s: %(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S')

# DAO define
cnfDao = configDao.ConfigDao()
hisDao = historyDao.HistoryDao()

# Obtain measure and configuration
sensor = sensor.Sensor()
config = cnfDao.find()
rele = rele.Rele()

# Rele control temperature
if rele.isWireDisabled() and config.isTempLessRange(sensor.getMeasure().getTemp() ):
	# Store measure
	hisDao.persist(sensor.getMeasure())
	
	# Enable wire/fan
	logging.debug('Heating wire enabled Temp={0:0.1f}* < Temp_min={1:0.1f}'.format(sensor.getMeasure().getTemp(), config.getTemMin()))
	rele.hotWire(True)
	rele.fan(True)

	# Alert control
	if config.isTempAlertLessRange(sensor.getMeasure().getTemp()):
        	logging.debug('Send alert. Temperature slow. Temp={0:0.1f}* < Temp_min={1:0.1f}'.format(sensor.getMeasure().getTemp(), config.getTemAlertMin()))
        	mail.Mail().send("Wargning. Temperature slow", config.__str__(), sensor.getMeasure().__str__())

elif rele.isWireEnabled() and config.isTempGreaterRange(sensor.getMeasure().getTemp()):
	# Store measure
        hisDao.persist(sensor.getMeasure())

	# Disable wire/fan
	logging.debug('Heating wire disabled Temp={0:0.1f}* > Temp_max={1:0.1f}'.format(sensor.getMeasure().getTemp(), config.getTemMax()))
        rele.hotWire(False)
	rele.fan(False, 240)

	# Alert control
	if config.isTempAlertGreaterRange(sensor.getMeasure().getTemp()):
        	logging.debug('Send alert. Temperature high. Temp={0:0.1f}* > Temp_max={1:0.1f}'.format(sensor.getMeasure().getTemp(), config.getTemAlertMax()))
        	mail.Mail().send("Wargning. Temperature high", config.__str__(), sensor.getMeasure().__str__())

# Rele control humidity
if config.isDoorOpen(sensor.getMeasure().getHumi()):
        logging.debug('Send alert. The door is open')
        mail.Mail().send("Wargning. The door is open", config.__str__(), sensor.getMeasure().__str__())
elif config.isHumAlertLessRange(sensor.getMeasure().getHumi()):
	logging.debug('Send alert. Humidity slow. Hum={0:0.1f}* < Hum_min={1:0.1f}'.format(sensor.getMeasure().getHumi(), config.getHumAlertMin()))
  	mail.Mail().send("Wargning. Humidity slow", config.__str__(), sensor.getMeasure().__str__())

logging.debug(sensor.getMeasure())
