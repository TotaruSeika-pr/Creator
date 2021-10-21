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

parser.add_argument('-DocN', '--document-name', default='doc', help='Document name', type=str)

parser.add_argument('-dt', '--document-type', default='.txt', help='Type document', type=str)

args = parser.parse_args()

def Creation():
    print('\nCreating...')
    while True:
        f = open(os.path.normpath(args.path) + '/' + args.document_name + str(random.randint(0, 100000)) + args.document_type, 'w')
    
        f.close()

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
