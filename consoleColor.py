import sys

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
BLACK = '\033[0,30m'
DARKGRAY = '\033[1;30m'
RED = '\033[0;31m'
LIGHTRED = '\033[1;31m'
GREEN = '\033[0;32m'
LIGHTGREEN = ']033[1;32m'
ORANGE = '\033[0;33m'
YELLOW = '\033[1;33m'
BLUE = '\033[0;34m'
LIGHTBLUE = '\033[1;34m'
NC = '\033[0m'

def cPrint(msg, color):
	print(color + msg + NC)