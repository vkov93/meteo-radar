#!/usr/bin/env python3

from aiohttp import web
from mrlibrary import DarkSky, MetaWeather
from cityregistry import CityRegistry, City


async def handle_temp(request):
    name = request.match_info.get('name', "enter city name")
    cities = CityRegistry('city_coordinates.json')
    city = cities.find(name)
    if city is not None:
        a = DarkSky().get_temperature(city)
        b = MetaWeather().get_temperature(city)
        text = a + '\n' + b
    else:
        text = 'Please enter valid city name - \n'
        for x in cities.cities:
            text += "'{}' ".format(x)
    return web.Response(text=text)


async def handle_api(request):
    name = request.match_info.get('name', 'City name')
    method = request.match_info.get('method', 'API')
    cities = CityRegistry('city_coordinates.json')
    city = cities.find(name)
    if city is not None:
        if method.lower() == 'darksky':
            text = DarkSky().get_temperature(city)
        elif method.lower() == 'metaweather':
            text = MetaWeather().get_temperature(city)
        else:
            pass
    else:
        text = 'Enter valid city and method name'
    return web.Response(text=text)