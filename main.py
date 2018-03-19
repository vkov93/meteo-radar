#!/usr/bin/env python3

import argparse
from mrlibrary import MetaWeather, DarkSky
from cityregistry import CityRegistry, City

class WrongArguments(Exception):
    pass

class HTTPError(Exception):
    pass

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--city', type=str, required=True, help='Name of the city')
    return parser.parse_args()


def main():
    args = parse_args()
    name = args.city
    cities = CityRegistry('city_coordinates.json')
    city = cities.find(name)
    if city is not None:
        try:
            MetaWeather(city)
        except HTTPError:
            print('Metaweather server is unreachable')
        try:
            DarkSky(city)
        except HTTPError:
            print('DarkSky server is unreachable')
    else:
        pass


if __name__ == '__main__':
    main()