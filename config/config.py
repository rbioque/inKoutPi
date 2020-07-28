# -*- coding: utf-8 -*-
# @proyect inKoutPi 
# config "entity"
__author__ = 'rbioque'

import sys

TEMP_MIN_CAL_PEL = -0.1
TEMP_MAX_CAL_PEL = 0.1
TEMP_CAL_WIR = 0.1

class Config:

	def __init__(self, id, tem_min, tem_max, hum_min, hum_max):
		self.tem_min = float(tem_min)
		self.tem_max = float(tem_max)
		self.hum_min = float(hum_min)
		self.hum_max = float(hum_max)
		self.id = id

	def toDBCollection (self):
		return {
			"id":self.id,
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
		if temp > self.getTemMinByWire():
			return True;
		return False;

	def isTempLessRangeByPeltier(self, temp):
		if temp <= self.tem_max+TEMP_MIN_CAL_PEL:
			return True;
		return False;

	def isTempGreaterRangeByPeltier(self, temp):
		if temp >= self.tem_max+TEMP_MAX_CAL_PEL:
			return True;
		return False;


	# Info

	def getTemMin(self):
		return self.tem_min;
	
	def getTemMax(self):
		return self.tem_max;
	

	def getTemMinByWire(self):
		return self.tem_min-TEMP_CAL_WIR;

	def getTemMaxByPeltier(self):
		return self.tem_max+TEMP_MAX_CAL_PEL;

	def getId(self):
		return self.id;

	def __str__(self):
		return "Temp min: %s - Temp max: %s - Hum min: %s - Hum max: %s" \
			%(self.tem_min, self.tem_max, self.hum_min, self.hum_max)
