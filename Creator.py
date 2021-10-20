#!/usr/bin/python3

import os
import random
import argparse

VERSION = '1.0.0.0'

path = ''
OS = ''

parser = argparse.ArgumentParser()

# Information arguments
parser.add_argument('-v', '--version', action='store_true', help='Program version')
parser.add_argument('-pa', '--print-args', action='store_true')

# Optional Arguments
parser.add_argument('-p', '--path', help='Directory \'path\'', required=True, type=str)
#parser.add_argument('-os', '--operating-system' ,  choices=['Linux', 'Win', 'And', 'Mac'], help='Operating system', required=True)

args = parser.parse_args()

def Creation():
    f = open(os.path.normpath(args.path) + '/newfile_by_creator.txt', 'w')
    f.close()
    print('File is create')

def IAC(): # informational argument conditions
    if args.version == True:
        print('Software version: ' + VERSION)
    
    if args.print_args == True:
        print(args)


def main():
    IAC()

    try:
        Creation ()
    except FileNotFoundError:
        print('\nInvalid path specified!')

main()
