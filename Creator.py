from args import Argument
from ClassCreator import Creator
import traceback

VERSION = '1.0.2.1'

def main():
    try:
        argument = Argument()
        creator = Creator(argument.args, VERSION)
        creator.Creation()
    except KeyboardInterrupt:
        creator.GetStats()
        creator.PrintStats()
    except FileNotFoundError:
        print('\nInvalid path specified!')
    except Exception as e:
        print(f'Unknown error! The program is stopped. The error was written to the log file.\nError: {e}')
        creator.LoggingError(error=str(traceback.format_exc()))



if __name__ == '__main__':
    main()
