#!/usr/bin/env python3

import argparse
import sys
from mrlibrary import MetaWeather
from cityregistry import CityRegistry

class WrongArguments(Exception):
    pass


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--city', type=str, required=True, help='Name of the city')
    return parser.parse_args()


def main():
    try:
        args = parse_args()
        citieslist = CityRegistry('city_coordinates.json')
        a = citieslist.getcity(args.city)
        name = a.name
        provider = MetaWeather()
        forecast = provider.get_temperature(name)
        forecastprint = 'Temperature in {} : {}°'.format(name, forecast)
        print(forecastprint)
    except:
        raise WrongArguments


if __name__ == '__main__':
    main()