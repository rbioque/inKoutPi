# -*- coding: utf-8 -*-
# @proyect inKoutPi 
# config "entity"
__author__ = 'rbioque'

import sys

class Config:

	def __init__(self, tem_min, tem_max, hum_min, hum_max):
        	self.tem_min = tem_min
        	self.tem_max = tem_max
        	self.hum_min = hum_min
        	self.hum_max = hum_max

    	def toDBCollection (self):
        	return {
            		"tem_min":self.tem_min,
            		"tem_max":self.tem_max,
            		"hum_min":self.hum_min,
            		"hum_max":self.hum_max
        	}
	
	def isTempLessRange(self, temp):
		if temp < self.tem_min:
			return True;
		return False;

	def isTempGreaterRange(self, temp):
		if temp > self.tem_max:
			return True;
		return False;

        def isTempAlertLessRange(self, temp):
                if temp < 30.0:
                        return True;
                return False;

        def isTempAlertGreaterRange(self, temp):
                if temp > 31.0:
                        return True;
                return False;
	
	def isHumAlertLessRange(self, hum):
		if hum < 70:
			return True;
		return False;

	def isDoorOpen(self, hum):
		if hum == 1.0:
			return True;
		return False;

	def getTemMin(self):
		return self.tem_min;
	
	def getTemMax(self):
		return self.tem_max;
	
	def getTemAlertMin(self):
		return 30.0;

	def getTemAlertMax(self):
		return 31.0;

	def getHumAlertMin(self):
		return 70;

    	def __str__(self):
        	return "Temp min: %s - Temp max: %s - Hum min: %s - Hum max: %s" \
               %(self.tem_min, self.tem_max, self.hum_min, self.hum_max)
