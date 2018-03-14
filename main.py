#!/usr/bin/env python3

import argparse


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('city_name', type=str)

    arguments = parser.parse_args()
    print('Weather in {} +25, sunny'.format(arguments.city_name))

if __name__ == "__main__":
    main()
