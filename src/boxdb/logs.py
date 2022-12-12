import contextlib
from boxdb.core import reader,writer
import logging
from colorama import init , Fore , Style
from boxdb.settings import (ERRORLOGS,
INFOLOGS,
WARNINGLOGS
)
init(convert=True)

def logWarning(table,message):
    """
    write logs into the file
    """
    with contextlib.suppress(Exception):
        writer(WARNINGLOGS(table),f'WARNING:{message}\n','a')
    print(f'{Fore.YELLOW}{message}{Style.RESET_ALL}')
    logging.basicConfig(format='%(asctime)s %(message)s')

def logerror(table,message):
    """
    write logs into the file
    """
    with contextlib.suppress(Exception):
        writer(ERRORLOGS(table),f'ERROR:{message}\n','a')
    print(f'{Fore.RED}{message}{Style.RESET_ALL}')
    logging.basicConfig(format='%(asctime)s %(message)s')

def loginfo(table,message):
    """
    write logs into the file
    """
    with contextlib.suppress(Exception):
        writer(INFOLOGS(table),f'SUCCESS:{message}\n','a')

    print(f'{Fore.GREEN}{message}{Style.RESET_ALL}')
    logging.basicConfig(format='%(asctime)s %(message)s')

def showlogs(table,
            error=False,
            warnings=False,
            info=False):
    """
    display log file in Terminal
    """
    if error:
        print(f"{Fore.RED}['ERROR']")
        print(reader(ERRORLOGS(table)))
    if warnings:
        print(f"{Fore.YELLOW}[WARNING]")
        print(reader(WARNINGLOGS(table)))
    if info:
        print(f"{Fore.GREEN}['SUCCESS']")
        print(reader(INFOLOGS(table)))
    print(Style.RESET_ALL)
