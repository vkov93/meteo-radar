#!/usr/bin/env python3

import ast

class CityNotFound(Exception):
    pass

class CityChecker():
    def __init__(self):
        with open('coordinates.txt', 'r') as file:
            data = file.read().replace('\n','')
        data = str(data)
        data = data.lower()
        self.cities = ast.literal_eval(data)
        file.close()


    def checkcity(self,city):
        city = city.lower()
        if city in self.cities:
            return self.cities[city]
        else:
            raise CityNotFound

