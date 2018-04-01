# @proyect inKoutPi 
# config "entity"
__author__ = 'rbioque'

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
            "hum_min": self.hum_min,
            "hum_max":self.hum_max
        }

    def __str__(self):
        return "Temperatura mínima: %s - Temperatura máxima: %s - Humedad mínima: %i - Humedad máxima: %s" \
               %(self.tem_min, self.tem_max, self.hum_min, self.hum_max)
