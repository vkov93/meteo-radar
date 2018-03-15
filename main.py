#!/usr/bin/env python3

import argparse
import json
import sys
import requests

class GetWoeidErr(Exception):
    pass

class GetTmpErr(Exception):
    pass


def parse_args():
    parser=argparse.ArgumentParser()
    parser.add_argument('-c','--city', type=str, required=True, help='Name of the city')
    return parser.parse_args()

def get_woeid(city):
    url='https://www.metaweather.com/api/location/search/?query={}'.format(city)
    response=requests.get(url)
    if response.status_code != 200:
        raise Exception
    j=response.json()
    try:
        return j[0]['woeid']
    except:
        raise GetWoeidErr

def get_temperature(city):
    url='https://www.metaweather.com/api/location/{}/'.format(city)
    response=requests.get(url)
    if response.status_code != 200:
        raise Exception
    j=response.json()
    try:
        return j['consolidated_weather'][0]['the_temp']
    except:
        raise GetTmpErr

def main():
    arguments=parse_args()
    woeid=get_woeid(arguments.city)
    temperature=get_temperature(woeid)

    print(temperature)

if __name__=='__main__':
    main()