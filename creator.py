#!/usr/bin/python3

import os
import random
import argparse

VERSION = '1.0.0.0'

path = ''
OS = ''

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path', help='Directory path', required=True, type=str)
parser.add_argument('-os', '--operating-system' ,  choices=['Linux', 'Win', 'And', 'Mac'], help='Operating system', required=True)
parser.add_argument('-v', '--version', action='store_true', help='Program version')

args = parser.parse_args()
print(args)

def Creation():
    print('Creating along the ' + args.path + ' in the ' + args.operating_system  +  ' operating system')


def main():
    if args.version == True:
        print('Software version: ' + VERSION)
    
    Creation()

main()
