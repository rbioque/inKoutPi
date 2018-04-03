# -*- coding: utf-8 -*-
# @proyect inKoutPi
# measure for history
__author__ = 'rbioque'

import sys

class Measure:

    def __init__(self, tem, hum, date):
        self.tem = tem
        self.hum = hum
        self.date = date

    def toDBCollection (self):
        return {
            "tem":self.tem,
            "hum":self.hum,
            "date":self.date,
        }

    def __str__(self):
        return "Temperatura: %s - Humedad: %s - Fecha: %s" \
	 %(self.tem, self.hum, self.date)
