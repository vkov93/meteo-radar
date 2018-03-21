#!/usr/bin/env python3

import server
import argparse
from aiohttp import web
from mrlibrary import MetaWeather, DarkSky
from cityregistry import CityRegistry, City

class WrongArguments(Exception):
    pass

class HTTPError(Exception):
    pass

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--city', type=str, help='Name of the city')
    parser.add_argument('--ip', type=str, help='ip for connection')
    parser.add_argument('--port', type=str, help='port')
    return parser.parse_args()


def main():
    args = parse_args()
    name = args.city
    cities = CityRegistry('city_coordinates.json')
    if args.ip is None and args.port is None:
        city = cities.find(name)
        if city is not None:
            try:
                print(MetaWeather(city).result)
            except HTTPError:
                print('Metaweather server is unreachable')
            try:
                print(DarkSky(city).result)
            except HTTPError:
                print('DarkSky server is unreachable')
        else:
            pass
    else:
        app = web.Application()
        app.add_routes([web.get('/{name}', server.handle_temp),
                        web.get('/', server.handle_temp),
                        web.get('/{name}/{method}', server.handle_api)])
        web.run_app(app, host=args.ip, port=args.port)


if __name__ == '__main__':
    main()