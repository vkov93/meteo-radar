#!/usr/bin/env python3

import json
import requests


class JsonError(Exception):
    pass

class HTTPError(Exception):
    pass

class MetaWeatherException(Exception):
    pass

class DarkSkyException(Exception):
    pass

class WeatherProvider:
    def __init__(self, name):
        self.name = name

class MetaWeather(WeatherProvider):
    def __init__(self, city):
        super().__init__('MetaWeather')
        try:
            woeid = self.get_woeid(city.name)
            temperature = round(self.temperature_from_woeid(woeid), 3)
            self.result = 'Metaweather: Temperature in {} : {}°'.format(city.name, temperature)
        except:
            raise MetaWeatherException

    def get_woeid(self, city):
        url = 'https://www.metaweather.com/api/location/search/?query={}'.format(city)
        response = requests.get(url)
        if response.status_code != requests.codes.ok:
            raise HTTPError
        j = response.json()
        try:
            return j[0]['woeid']
        except:
            raise JsonError

    def temperature_from_woeid(self, woeid):
        url = 'https://www.metaweather.com/api/location/{}/'.format(woeid)
        response = requests.get(url)
        if response.status_code != requests.codes.ok:
            raise HTTPError
        j = response.json()
        try:
            return j['consolidated_weather'][0]['the_temp']
        except:
            raise JsonError


class DarkSky(WeatherProvider):
    def __init__(self, city):
        super().__init__('DarkSky')
        try:
            temperature = self.temperature_from_ds(city.latitude, city.longitude)
            self.result = 'DarkSky: Temperature in {} : {}°'.format(city.name, temperature)
        except:
            raise DarkSkyException

    def temperature_from_ds(self, latitude, longitude):
        url = 'https://api.darksky.net/forecast/051577d3ef68f75953e9c9a2247582e1/{},{}'\
            .format(latitude, longitude)
        response = requests.get(url)
        if response.status_code != requests.codes.ok:
            raise HTTPError
        j = response.json()
        try:
            return round((j['currently']['temperature']-32)/1.8, 3)       #Fahrenheit into Celsius
        except:
            raise JsonError