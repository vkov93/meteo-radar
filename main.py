#!/usr/bin/env python3

import argparse
import json
import requests


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('city_name', type=str)

    arguments = parser.parse_args()
    str_sity=str(arguments.city_name)


    response = requests.get('https://www.metaweather.com/api/location/search/?query='+str_sity)
                                                    # knock knock here's johnny
    to_json = response.json()                       # response to json
    json_encode = json.dumps(to_json)               # json encoding
    json_decode = json.loads(json_encode)[0]        # json decoding (obj 'result_dict' type==dict)
    cityid = json_decode['woeid']                   # get city_id

    response = requests.get('https://www.metaweather.com/api/location/' + str(cityid) + '/')
                                                    # second encounter
    to_json = response.json()
    hemorragelist = to_json['consolidated_weather']
    # get object type 'list', where the elements are dict
    temperature = hemorragelist[0]['the_temp']
    # get object from first list element, then get object with key 'the_temp'

    print(temperature)


if __name__ == "__main__":
    main()
