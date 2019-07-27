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
configAlert = cnfDao.findAlert()
rele = rele.Rele()

measure = sensor.getMeasure()

## Meausre debug
logging.debug('Wire enabled: %s. Peltier enabled: %s. Fan enabled: %s. Fan peltier enabled: %s. Measure: %s',rele.isWireEnabled(), rele.isPeltierEnabled(), rele.isFanEnabled(), rele.isFanPeltierEnabled(), measure)

# Rele control temperature
if rele.isWireEnabled() and config.isTempGreaterRangeByWire(measure.getTemp()):
	rele.hotWire(False)
	rele.fan(False)
	logging.info('Heating wire disabled. Temp={0:0.1f}* <= Temp_max={1:0.1f}'.format(measure.getTemp(), config.getTemMin()))

elif rele.isPeltierEnabled() and config.isTempLessRangeByPeltier(measure.getTemp()):
	rele.coldPeltier(False)
	rele.fan(False)
	logging.info('Colding peltier disabled. Temp={0:0.1f}* <= Temp_min={1:0.1f}'.format(measure.getTemp(), config.getTemMax()))
	time.sleep(300)
	if rele.isPeltierDisabled():
		rele.fanPeltier(False)	
		logging.info('Fan peltier disabled. Temp old={0:0.1f}. Temp new={1:0.1}'.format(measure.getTemp(), sensor.getMeasure().getTemp()))
	
elif rele.isWireDisabled() and config.isTempLessRangeByWire(measure.getTemp()):
	rele.hotWire(True)
	rele.fan(True)
	logging.info('Heating wire enabled. Temp={0:0.1f}* < Temp_min={1:0.1f}'.format(measure.getTemp(), config.getTemMinByWire()))

elif rele.isPeltierDisabled() and config.isTempGreaterRangeByPeltier(measure.getTemp()):
	rele.coldPeltier(True)
	rele.fan(True)
	rele.fanPeltier(True)
	logging.info('Colding peltier enabled. Temp={0:0.1f}* < Temp_max={1:0.1f}'.format(measure.getTemp(), config.getTemMaxByPeltier()))	

# Temp Alert control
if configAlert.isTempAlertLessRange(measure.getTemp()):
	logging.debug('Send alert. Temperature slow. Temp={0:0.1f}* < Temp_alert_min={1:0.1f}'.format(measure.getTemp(), configAlert.getTemAlertMin()))
	mail.Mail().send("Wargning. Temperature slow", configAlert, config, measure)
	measure.setMsgType('Temperatura demasiado baja! No debe ser inferior a {0:0.2f}'.format(configAlert.getTemAlertMin()), 'TEM_SLOW')

elif configAlert.isTempAlertGreaterRange(measure.getTemp()):
	logging.debug('Send alert. Temperature high. Temp={0:0.1f}* > Temp_alert_max={1:0.1f}'.format(measure.getTemp(), configAlert.getTemAlertMax()))
	mail.Mail().send("Wargning. Temperature high", configAlert, config, measure)
	measure.setMsgType('Temperatura demasiado alta! No debe ser superior a {0:0.2f}'.format(configAlert.getTemAlertMax()), 'TEM_HIGH')

# Humidity alert control
if configAlert.isDoorOpen(measure.getHumi()):
	logging.error('Get humidity error!!')
#	mail.Mail().send("Wargning. The door is open", config.__str__(), measure.__str__())

elif configAlert.isHumAlertLessRange(measure.getHumi()):
	logging.debug('Send alert. Humidity slow. Hum={0:0.1f}* < Hum_alert_min={1:0.1f}'.format(measure.getHumi(), configAlert.getHumAlertMin()))
	mail.Mail().send("Wargning. Humidity slow", configAlert, config, measure)
	measure.setMsgType('Humedad demasiado baja! No debe ser inferior a {0:0.2f}'.format(configAlert.getHumAlertMin()), 'HUM_SLOW')

elif configAlert.isHumAlertGreaterRange(measure.getHumi()):
        logging.debug('Send alert. Humidity high. Hum={0:0.1f}* < Hum_alert_min={1:0.1f}'.format(measure.getHumi(), configAlert.getHumAlertMax()))
        mail.Mail().send("Wargning. Humidity high", configAlert, config, measure)
	measure.setMsgType('Humedad demasiado alta! No debe ser superior a {0:0.2f}'.format(configAlert.getHumAlertMax()), 'HUM_HIGH')

hisDao.persist(measure)


