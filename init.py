#!/usr/bin/python

# @proyect inKoutPi
# init
__author__ = 'rbioque'

import sys

from config import configDao, config
from history import historyDao, measure
from components import sensor, rele
from alerts import mail

# DAO define
cnfDao = configDao.ConfigDao()
hisDao = historyDao.HistoryDao()

# Obtain measure and configuration
sensor = sensor.Sensor()
config = cnfDao.find()
rele = rele.Rele()

# Store measure
hisDao.persist(sensor.getMeasure())

mail.Mail().send("prueba")

# Rele control
if config.isTempLessRange(sensor.getMeasure().getTemp()):
	rele.hotWire(True)
	rele.fan(True)
elif config.isTempGreaterRange(sensor.getMeasure().getTemp()):
        rele.hotWire(False)
#	rele.fan(False, 240)

