#!/usr/bin/env python3

import json

class CityNotFound(Exception):
    pass

class City:
    def __init__(self, name, coordinates):
        self.name = name
        self.latitude = coordinates[0]
        self.longitude = coordinates[1]


class CityRegistry:
    def __init__(self, file_name):
        self.cities = {}
        with open(file_name) as f:
            data = json.load(f)
            for name in data:
                self.cities[name.lower()] = City(name, data[name])

    def find(self,city):
        try:
            return self.cities[city.lower()]
        except:
            raise CityNotFound