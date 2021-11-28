#!/usr/bin/python3

import os
import random
import time
import argparse
import shutil

VERSION = '1.0.1.0'


def CreateAndGetArgs():
    global args

    parser = argparse.ArgumentParser()


    # Information arguments:
    parser.add_argument('-a', '--about', action='store_true', help='Information about the program')
    parser.add_argument('-pa', '--print-args', action='store_true')


    # Optional Arguments:
    parser.add_argument('-p', '--path', help='Path to create files', required=True, type=str)
    parser.add_argument('-os', '--operating-system', required=True, choices=['Win', 'Linux'], help='Affects the separator between folders')
    parser.add_argument('-DocN', '--document-name', default='doc', help='The name of the document to be created (not including the distinguished number)', type=str)
    parser.add_argument('-DocT', '--document-type', default='.txt', help='The type of document being created', type=str)
    parser.add_argument('-r', '--range', nargs=2, help='A certain distinctive number of documents created', default=[0, 1000000], type=int)
    parser.add_argument('-ctf', '--copy-text-file', help='Accepts the path to the file, the text of which will be copied', default='N')
    parser.add_argument('-cf', '--copy-file', help='Accepts the path to the file to be copied', default='N')
    parser.add_argument('-d', '--delay', type=float, default=0.0, help='Delay between file creation')
    parser.add_argument('-q', '--quantity', default=-1, type=int, help='Number of files created')
    parser.add_argument('-t', '--text', default='', help='Text in generated documents', type=str)

    args = parser.parse_args()


def PrintStats():
    DateEnd = time.time()
    print('\nFiles created: ' + str(NumbeFilesCreated))
    ProgramWorked = round(float(DateEnd)-float(DateStart), 3)
    print('Program worked: ' + str(ProgramWorked) + ' sec')
    if args.delay == 0.0:
        print('Average Crafting Speed: ' + str(round(int(float(NumbeFilesCreated)/float(ProgramWorked)), 3)) + '/sec')

    else:
        print('Average Crafting Speed: ' + '1/' + str(args.delay) + ' sec')


def Creation():
    global iterations_var, DateStart, NumbeFilesCreated
    iterations_var = args.quantity
    NumbeFilesCreated = 0
    
    if args.operating_system == 'Win':
        separator = '\\'
    elif args.operating_system == 'Linux':
        separator = '/'

    print('\nCreated...')

    DateStart = time.time()

    while iterations_var != 0:

        new_file = os.path.normpath(args.path) + separator + args.document_name + str(random.randint(args.range[0], args.range[1]))
        
        if args.copy_text_file == 'N' and args.copy_file == 'N':
            f = open(new_file + args.document_type, 'w')
            f.write(args.text)
            f.close()
        else:
            if args.copy_text_file != 'N':
                
                shutil.copy(os.path.normpath(args.copy_text_file), new_file + args.document_type)

            elif args.copy_file != 'N':

                file_type = os.path.splitext(args.copy_file)[1]
                
                if args.operating_system == 'Win':
                    os.system(f'copy {args.copy_file} {new_file + file_type}')

                elif args.operating_system == 'Linux':
                    os.system(f'cp {args.copy_file} {new_file + file_type}')

        NumbeFilesCreated += 1              
        iterations_var -= 1

        time.sleep(args.delay)

    print('\nCompleted')

    PrintStats()


def IAC(): # informational argument conditions
    
    if args.about == True:
        print('\n\tSoftware version: ' + VERSION)
        print('\tGitHub: https://github.com/TotaruSeika-pr')
        print('\tTwitter: https://twitter.com/TotaruS\n')
    
    if args.print_args == True:
        print(args)


def main():
    CreateAndGetArgs()
    IAC()

    try:

        Creation ()
    
    except FileNotFoundError:
       print('\nInvalid path specified!')

    except KeyboardInterrupt:
        PrintStats()

main()
