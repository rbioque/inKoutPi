# -*- coding: utf-8 -*-
# @proyect inKoutPi 
# config "entity"
__author__ = 'rbioque'

import sys

TEMP_CAL = 0.1
TEMP_STOP_CAL = 0.01

class Config:

	def __init__(self, tem_min, tem_max, hum_min, hum_max):
		self.tem_min = float(tem_min)
		self.tem_max = float(tem_max)
		self.hum_min = float(hum_min)
		self.hum_max = float(hum_max)

	def toDBCollection (self):
		return {
			"tem_min":self.tem_min,
			"tem_max":self.tem_max,
			"hum_min":self.hum_min,
			"hum_max":self.hum_max
		}

	
	# Components control

	def isTempLessRangeByWire(self, temp):
		if temp <= self.getTemMinByWire():
			return True;
		return False;

	def isTempGreaterRangeByWire(self, temp):
		if temp >= self.getTemMin()-TEMP_STOP_CAL:
			return True;
		return False;

	def isTempLessRangeByPeltier(self, temp):
		if temp <= self.getTemMax()+TEMP_STOP_CAL:
			return True;
		return False;

	def isTempGreaterRangeByPeltier(self, temp):
		if temp >= self.getTemMaxByPeltier():
			return True;
		return False;


	# Info

	def getTemMin(self):
		return self.tem_min;
	
	def getTemMax(self):
		return self.tem_max;
	

	def getTemMinByWire(self):
		return self.tem_min-TEMP_CAL;

	def getTemMaxByPeltier(self):
		return self.tem_max+TEMP_CAL;

	def __str__(self):
		return "Temp min: %s - Temp max: %s - Hum min: %s - Hum max: %s" \
			%(self.tem_min, self.tem_max, self.hum_min, self.hum_max)
