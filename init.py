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


## Meausre debug
logging.debug('Wire enabled: %s. Peltier enabled: %s. Fan enabled: %s. Measure: %s',rele.isWireEnabled(), rele.isPeltierEnabled(), rele.isFanEnabled(), sensor.getMeasure())
#logging.debug('tem min peltier %s peltier Off %s', config.getTemMin(), config.isTempLessRangeByPeltier(sensor.getMeasure().getTemp())) 

# Rele control temperature
if rele.isWireEnabled() and config.isTempGreaterRangeByWire(sensor.getMeasure().getTemp()):
	rele.hotWire(False)
	rele.fan(False)

	hisDao.persist(sensor.getMeasure())
	logging.info('Heating wire disabled. Temp={0:0.1f}* <= Temp_max={1:0.1f}'.format(sensor.getMeasure().getTemp(), config.getTemMin()))

elif rele.isPeltierEnabled() and config.isTempLessRangeByPeltier(sensor.getMeasure().getTemp()):
	rele.coldPeltier(False)
	rele.fan(False)

	hisDao.persist(sensor.getMeasure())
	logging.info('Colding peltier disabled. Temp={0:0.1f}* <= Temp_min={1:0.1f}'.format(sensor.getMeasure().getTemp(), config.getTemMax()))

elif rele.isWireDisabled() and config.isTempLessRangeByWire(sensor.getMeasure().getTemp()):
        rele.hotWire(True)
        rele.fan(True)

	hisDao.persist(sensor.getMeasure())
	logging.info('Heating wire enabled. Temp={0:0.1f}* < Temp_min={1:0.1f}'.format(sensor.getMeasure().getTemp(), config.getTemMinByWire()))

elif rele.isPeltierDisabled() and config.isTempGreaterRangeByPeltier(sensor.getMeasure().getTemp()):
        rele.coldPeltier(True)
        rele.fan(True)

	hisDao.persist(sensor.getMeasure())
	logging.info('Colding peltier enabled. Temp={0:0.1f}* < Temp_max={1:0.1f}'.format(sensor.getMeasure().getTemp(), config.getTemMaxByPeltier()))


# Temp Alert control
if configAlert.isTempAlertLessRange(sensor.getMeasure().getTemp()):
	logging.debug('Send alert. Temperature slow. Temp={0:0.1f}* < Temp_alert_min={1:0.1f}'.format(sensor.getMeasure().getTemp(), configAlert.getTemAlertMin()))
	mail.Mail().send("Wargning. Temperature slow", config.__str__(), sensor.getMeasure().__str__())
elif configAlert.isTempAlertGreaterRange(sensor.getMeasure().getTemp()):
	logging.debug('Send alert. Temperature high. Temp={0:0.1f}* > Temp_alert_max={1:0.1f}'.format(sensor.getMeasure().getTemp(), configAlert.getTemAlertMax()))
	mail.Mail().send("Wargning. Temperature high", config.__str__(), sensor.getMeasure().__str__())

# Humidity alert control
if configAlert.isDoorOpen(sensor.getMeasure().getHumi()):
	logging.debug('Send alert. The door is open')
	mail.Mail().send("Wargning. The door is open", config.__str__(), sensor.getMeasure().__str__())
elif configAlert.isHumAlertLessRange(sensor.getMeasure().getHumi()):
	logging.debug('Send alert. Humidity slow. Hum={0:0.1f}* < Hum_alert_min={1:0.1f}'.format(sensor.getMeasure().getHumi(), configAlert.getHumAlertMin()))
	mail.Mail().send("Wargning. Humidity slow", config.__str__(), sensor.getMeasure().__str__())
elif configAlert.isHumAlertGreaterRange(sensor.getMeasure().getHumi()):
        logging.debug('Send alert. Humidity high. Hum={0:0.1f}* < Hum_alert_min={1:0.1f}'.format(sensor.getMeasure().getHumi(), configAlert.getHumAlertMax()))
        mail.Mail().send("Wargning. Humidity high", config.__str__(), sensor.getMeasure().__str__())



