#!/usr/bin/python

# @proyect inKoutPi
# init
__author__ = 'rbioque'
import sys

from config import configDao
from history import historyDao, measure
from components import *

# DAO define
cnfDao = configDao.ConfigDao()
hisDao = historyDao.HistoryDao()

# Obtener medida

# Insertar

# Obtener limites

# Cable/Ventilador


print("historico")
m = measure.Measure(30, 80, '1/1/2001')
hisDao.persist(m)


