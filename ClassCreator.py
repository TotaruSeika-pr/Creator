from fileinput import filename
import time
from LogIt import LogIt
import shutil
import random
import os.path
from sys import platform

class Creator():
    
    def __init__ (self, args, VERSION):
        self.args = args
        self.VERSION = VERSION
        self.session_name = str(round(time.time()))

        LEVELS = {'INFO': 'INFO', 'ERROR': 'ERROR'}
        self.log = LogIt(levels=LEVELS)
        self.log.Format(text_format='[{session_name}] {date} !{level}! -> {message}', date_format='%Y-%m-%d', data={'session_name': round(time.time())})

    def LoggingError(self, error):
        self.log.Logging(message=error, level='ERROR')

    def CreateDocument(self):
        try:
            if self.args.copy_text_file == None and self.args.copy_file == None:
                f = open(self.new_file + self.args.document_type, 'w')
                f.write(self.args.text)
                f.close()
            else:
                if self.args.copy_text_file != None:
                        
                    shutil.copy(os.path.normpath(self.args.copy_text_file), self.new_file + self.args.document_type)

                elif self.args.copy_file != None:

                    self.file_type = os.path.splitext(self.args.copy_file)[1]
                        
                    if self.os == 'win32':
                        os.system(f'copy {self.args.copy_file} {self.new_file +self.file_type}')

                    elif self.os == 'linux' or self.os == 'linux2':
                        os.system(f'cp {self.args.copy_file} {self.new_file + self.file_type}')
        
        except FileExistsError:
            pass


    def CreateFolder(self):
        try:
            os.mkdir(self.args.path + self.separator + self.file_name)
        
        except FileExistsError:
            pass

    def OSDefinition(self):
        self.os = platform
        if self.os == 'linux' or self.os == 'linux2':
            self.separator = '/'
        elif self.os == 'win32':
            self.separator = '\\'
    
    def PrintStats(self):
        print(f'\nCreated: {self.files_creation}')
        print(f'Program worked: {self.program_worked}')
        print(f'Average Crafting Speed: {self.average_crafting_speed}')

    def GetStats(self):
        self.time_end = time.time()
        self.program_worked = round(float(self.time_end)-float(self.time_start), 5)
        if self.args.delay == 0.0:
            self.average_crafting_speed = str(round(int(float(self.files_creation)/float(self.program_worked)), 3)) + '/sec'
        else:
            self.average_crafting_speed = '1/' + str(self.args.delay) + ' sec'

        if self.args.logging > 1:
            self.log.Logging(message=f'Created: {self.files_creation} | Program worked: {self.program_worked} sec | Average crafting speed: {self.average_crafting_speed}', level='INFO')

    def ModeDefinition(self):
        if self.args.mode == 1:
            Creator.CreateDocument(self)
        elif self.args.mode == 2:
            Creator.CreateFolder(self)
        elif self.args.mode == 3:
            if random.randint(0, 1) == 0:
                Creator.CreateDocument(self)
            else:
                Creator.CreateFolder(self)

    def TimeWorkCheck(self):
        if self.args.time_work != None:
            if time.time() - self.time_start >= self.args.time_work:
                return True
    
    def InformationalArgumentConditions(self):
        if self.args.about == True:
            print('\n\tSoftware version: ' + self.VERSION)
            print('\tGitHub: https://github.com/TotaruSeika-pr')
            print('\tReddit: https://www.reddit.com/user/Totaru_Seika\n')
    
        if self.args.print_args == True:
            print(self.args)
    
    def WriteInLog(self):
        if self.args.logging > 0:
            self.log.Logging(message=f'args: {str(self.args)}', level='INFO')

    def Creation(self):
        Creator.InformationalArgumentConditions(self)

        self.iterations = self.args.quantity
        self.files_creation = 0
        
        Creator.OSDefinition(self)
        Creator.WriteInLog(self)
        
        self.time_start = time.time()

        print('Creation...')
        

        while self.iterations != 0:

            if Creator.TimeWorkCheck(self):
                break
                
            if self.args.quantity != None:
                if self.args.quantity <= self.files_creation:
                    break
            
            self.file_name = self.args.document_name + str(random.randint(int(self.args.range[0]), int(self.args.range[1])))
            self.new_file = os.path.normpath(self.args.path) + self.separator + self.file_name

            Creator.ModeDefinition(self)

            self.files_creation += 1
            if self.iterations != None:
                self.iterations -= 1
            
            if self.args.logging == 3:
                self.log.Logging(message=f'created {self.file_name}', level='INFO')

            time.sleep(self.args.delay)

        print('\nCompleted')

        Creator.GetStats(self)
        Creator.PrintStats(self)