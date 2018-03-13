#!/usr/bin/env python3

import argparse


def main():

    args = argparse.ArgumentParser()
    args.add_argument('city_name', type=str)
    print('Weather in {} +25, sunny'.format(args.parse_args().city_name))

if __name__ == "__main__":
    main()
