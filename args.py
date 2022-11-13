import argparse


class Argument:
    
    def __init__(self):
        self.args = None
        self.parser = None
        Argument.CreateAndGetArgs(self)

    def CreateAndGetArgs(self):
        self.parser = argparse.ArgumentParser()

        Argument.InitializingArguments(self)

        self.args = self.parser.parse_args()

    def InitializingArguments(self):
        Argument.InitializingInformationArguments(self)
        Argument.InitializingEffectiveArguments(self)


    def InitializingInformationArguments(self):
        
        self.parser.add_argument(
            '-a', '--about',
            action='store_true', required=False,
            help='Information about the program')

        self.parser.add_argument(
            '-pa', '--print-args',
            action='store_true', required=False,
            help='A function for debugging. Outputs all arguments.')

    def InitializingEffectiveArguments(self):

        self.parser.add_argument(
            '-p', '--path',
            required=False, type=str, default=None,
            help='Path to create files')

        self.parser.add_argument(
            '-dn', '--document-name',
            required=False, type=str, default='doc',
            help='The name of the document to be created (not including the distinguished number)')

        self.parser.add_argument(
            '-dt', '--document-type',
            required=False, type=str, default='.txt',
            help='The type of document being created')

        self.parser.add_argument(
            '-r', '--range',
            required=False, nargs=2, default=[0, 1000000],
            help='A certain distinctive number of documents created')

        self.parser.add_argument(
            '-ctf', '--copy-text-file',
            required=False, default=None,
            help='Accepts the path to the file, the text of which will be copied')
        
        self.parser.add_argument(
            '-cf', '--copy-file',
            required=False, default=None,
            help='Accepts the path to the file to be copied')

        self.parser.add_argument(
            '-d', '--delay',
            required=False, type=float, default=0.0,
            help='Delay between file creation')
        
        self.parser.add_argument(
            '-q', '--quantity', 
            required=False, default=None, type=int,
            help='Number of files created')
        
        self.parser.add_argument(
            '-l', '--logging',
            required=False, choices=[1, 2, 3], type=int, default=0,
            help='Logs the work of the program')

        self.parser.add_argument(
            '-t', '--text',
            required=False, type=str, default='',
            help='Text in generated documents')

        self.parser.add_argument(
            '-m', '--mode',
            required=False, type=int, default=1,
            help='Selecting the program operation mode (1 - documents, 2 - folders, 3 - mixed)')

        self.parser.add_argument(
            '-tw', '--time-work',
            required=False, type=float, default=None,
            help='Specifies the program running time in seconds')