#!/usr/bin/env python3

import argparse
import json
import sys
import requests

class CityDoesNotExist(Exception):
    pass

class JsonError(Exception):
    pass

class HTTPError(Exception):
    pass

class MetaWeatherException(Exception):
    pass

class WeatherProvider:
    def __init__(self, name):
        self.name = name

    def get_temperature(self, city):
            raise NotImplementedError


class MetaWeather(WeatherProvider):
    def __init__(self):
        super().__init__('MetaWeather')

    def get_woeid(self, city):
        url = 'https://www.metaweather.com/api/location/search/?query={}'.format(city)
        response = requests.get(url)
        if response.status_code != 200:
            raise HTTPError
        j = response.json()
        try:
            return j[0]['woeid']
        except:
            raise JsonError

    def temperature_from_woeid(self, woeid):
        url = 'https://www.metaweather.com/api/location/{}/'.format(woeid)
        response = requests.get(url)
        if response.status_code != 200:
            raise HTTPError
        j = response.json()
        try:
            return j['consolidated_weather'][0]['the_temp']
        except:
            raise JsonError

    def get_temperature(self, city):
        try:
            woeid = self.get_woeid(city)
            temperature = self.temperature_from_woeid(woeid)
            return temperature
        except:
            raise MetaWeatherException