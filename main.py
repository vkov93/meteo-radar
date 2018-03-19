#!/usr/bin/env python3

import argparse
from mrlibrary import MetaWeather, DarkSky
from cityregistry import CityRegistry, City

class WrongArguments(Exception):
    pass


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--city', type=str, required=True, help='Name of the city')
    return parser.parse_args()


def main():
    args = parse_args()
    name = args.city
    cities = CityRegistry('city_coordinates.json')
    try:
        city = cities.find(name)
    except KeyError:
        print('fuck your mom')
    try:
        MetaWeather(city)
    except Exception:
        print('Metaweather server is unreachable')
    try:
        DarkSky(city)
    except Exception:
        print('DarkSky server is unreachable')


if __name__ == '__main__':
    main()