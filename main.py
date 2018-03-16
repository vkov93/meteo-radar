#!/usr/bin/env python3

import argparse
import sys
from mrlibrary import MetaWeather
from cityregistry import CityChecker

class WrongArguments(Exception):
    pass


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--city', type=str, required=True, help='Name of the city')
    return parser.parse_args()


def main():
    try:
        args = parse_args()
        citieslist = CityChecker()
        citieslist.checkcity(args.city)
        provider = MetaWeather()
        forecast = provider.get_temperature(args.city)
        forecastprint = 'Temperature in {} : {}°'.format(args.city, forecast)
        print(forecastprint)
    except:
        raise WrongArguments


if __name__ == '__main__':
    main()