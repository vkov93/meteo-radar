#!/usr/bin/env python3

import argparse
import sys
from mrlibrary import WeatherProvider

class WrongArguments(Exception):
    pass

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--city', type=str, required=True, help='Name of the city')
    return parser.parse_args()


def main():
    try:
        args = parse_args()
        provider = WeatherProvider()
        temperature = WeatherProvider.get_temperature(provider, args.city)

        TempetarurePrint = 'Temperature in {} : {}'.format(args.city, temperature)
        print(TempetarurePrint + chr(176))
    except:
        raise WrongArguments

if __name__ == '__main__':
    main()