#!/usr/bin/python

# @proyect inKoutPi
# init
__author__ = 'rbioque'

import sys
sys.path.insert(0, r'/config/')
from config import configDao

cnfDao = configDao.ConfigDao()

print("prueba metodo")
cnfDao.find_config()

