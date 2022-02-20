#!/usr/bin/python3

import os
import random
import time
import argparse
import shutil

VERSION = '1.0.2.0'


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
    parser.add_argument('-l', '--logging', type=int, choices=[1, 2, 3], default= 0,  help='Logs the work of the program')
    parser.add_argument('-t', '--text', default='', help='Text in generated documents', type=str)
    parser.add_argument('-m', '--mode', choices=[1, 2, 3], default=1, help='Selecting the program operation mode (1 - documents, 2 - folders, 3 - mixed)', type=int)
    parser.add_argument('-tw', '--time-work', default=None, type=float, help='Specifies the program running time in seconds.')
    
    args = parser.parse_args()


def GetStats():
    DateEnd = time.time()
    Files_created = str(NumbeFilesCreated)
    ProgramWorked = round(float(DateEnd)-float(DateStart), 3)
    if args.delay == 0.0:
        Average_Crafting_Speed = str(round(int(float(NumbeFilesCreated)/float(ProgramWorked)), 3)) + '/sec'

    else:
        Average_Crafting_Speed = '1/' + str(args.delay) + ' sec'

    return [Files_created, ProgramWorked, Average_Crafting_Speed]

def PrintStats(values):
    if log_file_write == False:
        if args.logging > 1:
            answer = GetStats()
            log_file.write('\nFiles created: ' + str(answer[0]) + '\nProgram worked: ' + str(answer[1]) + ' sec\nAverage Crafting Speed: ' + str(answer[2]))
            log_file.close()
        
    print('\nCreated: ' + str(values[0]))
    print('Program worked: ' + str(values[1]) + ' sec')
    print('Average Crafting Speed: ' + str(values[2]))

def CreatingDocument():
    global f

    try:
    
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
    
    except FileExistsError:
        pass

def CreatingFolders():

    try:
        os.mkdir(new_file)

    except FileExistsError:
        pass



def Creation():
    global iterations_var, DateStart, NumbeFilesCreated, log_file, new_file, f, log_file_write
    iterations_var = args.quantity
    NumbeFilesCreated = 0
    log_file_write = False

    if args.operating_system == 'Win':
        separator = '\\'
    elif args.operating_system == 'Linux':
        separator = '/'

    print('\nCreated...')

    if args.logging > 0:
        log_file = open('log'+ str(time.time())+'.txt', 'w')
        log_file.write('Arguments:' + str(args)+'\n')

    DateStart = time.time()

    while iterations_var != 0:

        file_name = args.document_name + str(random.randint(args.range[0], args.range[1]))
        new_file = os.path.normpath(args.path) + separator + file_name
        
        if args.mode == 1:
            CreatingDocument()
        elif args.mode == 2:
            CreatingFolders()
        elif args.mode == 3:
            if random.randint(0, 1) == 0:
                CreatingDocument()
            else:
                CreatingFolders()

        if args.time_work != None:
            if time.time()-DateStart >= args.time_work:
                break


        if args.logging == 3:
            log_file.write('Created -> ' + file_name + '\n')


        NumbeFilesCreated += 1              
        iterations_var -= 1

        time.sleep(args.delay)

    print('\nCompleted')

    if args.logging > 1:
        answer = GetStats()
        log_file.write('\nFiles created: ' + str(answer[0]) + '\nProgram worked: ' + str(answer[1]) + ' sec\nAverage Crafting Speed: ' + str(answer[2]))
        log_file_write = True

    PrintStats(GetStats())


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
        PrintStats(GetStats())

main()
