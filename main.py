#!/usr/bin/env python3

import argparse
from mrlibrary import MetaWeather, DarkSky
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
        city = args.city
        checkerror = CityRegistry('city_coordinates.json').repairname(city)
        if checkerror is not None:
            name = checkerror
            provider = MetaWeather()
            provider.get_temperature(name)

            provider = DarkSky()
            provider.get_temperature(name)
        else:
            print('Please enter a valid city name')
    except:
        raise WrongArguments


if __name__ == '__main__':
    main()