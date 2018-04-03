# @proyect inKoutPi
# history dao
__author__ = 'rbioque'

import pymongo
import measure

class HistoryDao:

        def __init__(self):
                # Making connection with MongoGlient
                from pymongo import MongoClient
                client = MongoClient('localhost', 27017)
                self.db = client.inKoutPiDB

        def persist(self, measure):
        	self.db.HISTORY.insert(measure.toDBCollection())
