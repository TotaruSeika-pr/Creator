#!/usr/bin/python3

import os
import random
import argparse
import shutil

VERSION = '1.0.0.0'

# ---------------------------------------------------------------------------

parser = argparse.ArgumentParser()


# Information arguments:
parser.add_argument('-a', '--about', action='store_true', help='About the program and author')


# Optional Arguments:
parser.add_argument('-p', '--path', help='Path of files created', required=True, type=str)

parser.add_argument('-os', '--operating-system', required=True, choices=['Win', 'Linux'], help='Select the operating system in which the program will work')

parser.add_argument('-DocN', '--document-name', default='doc', help='The name of the documents being created', type=str)

parser.add_argument('-DocT', '--document-type', default='.txt', help='Type of documents created', type=str)

parser.add_argument('-r', '--range', nargs=2, help='[Beginning of range] [end of range]', default=[0, 1000000], type=int)

parser.add_argument('-cf', '--copy-file', help='The path to the contents of which will be copied', default='N')

parser.add_argument('-q', '--quantity', default=-1, type=int, help='Number of files created')

parser.add_argument('-t', '--text', default='', help='Text in the created files', type=str)

args = parser.parse_args()

# ---------------------------------------------------------------------------

def Creation():
    global iterations_var
    iterations_var = args.quantity
    
    if args.operating_system == 'Win':
        separator = '\\'
    elif args.operating_system == 'Linux':
        separator = '/'

    print('\nCreated...')
    while iterations_var != 0:

        new_file_str = os.path.normpath(args.path) + separator + args.document_name + str(random.randint(args.range[0], args.range[1])) + args.document_type
        
        if args.copy_file == 'N':
            f = open(new_file_str, 'w')
            f.write(args.text)
            f.close()
        else:
            shutil.copy(os.path.normpath(args.copy_file), new_file_str)

        iterations_var -= 1

    print('\nCompleted')

def IAC(): # informational argument conditions
    
    if args.about == True:
        print('\n\tSoftware version: ' + VERSION)
        print('\tGitHub: https://github.com/TotaruSeika-pr')
        print('\tTwitter: https://twitter.com/TotaruS\n')

def main():
    IAC()

    try:

        Creation ()
    
    except FileNotFoundError:
       print('\nInvalid path specified!')

    except KeyboardInterrupt:
        print('\nCreation stopped')
        print('Files created: ' + str((iterations_var+1)*-1))

main()
