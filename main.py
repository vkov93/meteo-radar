#!/usr/bin/env python3

import argparse
import json
import sys
import requests

class GetWoeidErr(Exception):
    pass

class GetTmpErr(Exception):
    pass

class GetUrlErr(Exception):
    pass

class WeatherProvider():
    def __new__(cls,city):
        woeid=WeatherProvider.get_woeid(city)
        temperature=WeatherProvider.get_temperature(woeid)
        return temperature

    def get_woeid(city):
        url = 'https://www.metaweather.com/api/location/search/?query={}'.format(city)
        response = requests.get(url)
        if response.status_code != 200:
            raise GetUrlErr
        j = response.json()
        try:
            return j[0]['woeid']
        except:
            raise GetWoeidErr

    def get_temperature(city):
        url = 'https://www.metaweather.com/api/location/{}/'.format(city)
        response = requests.get(url)
        if response.status_code != 200:
            raise GetUrlErr
        j = response.json()
        try:
            return j['consolidated_weather'][0]['the_temp']
        except:
            raise GetTmpErr

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--city', type=str, required=True, help='Name of the city')
    return parser.parse_args()

def main():
    args=parse_args()
    city=args.city
    a = WeatherProvider(city)
    print(a)

if __name__ == '__main__':
        main()