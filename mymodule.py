# Colors
# Bold
############
black = "\033[1;30m"  # Black
R = "\033[1;31m"  # Red
G = "\033[1;32m"  # Green
y = "\033[1;33m"  # Yellow
b = "\033[1;32m"  # Blue
P = "\033[1;35m"  # Purple
C = "\033[1;36m"  # Cyan
W = "\033[1;37m"  # White
############

import os
import socket
import time


def clear():
    os.system("clear")

def wait():
    print('Wait..')
    time.sleep(0.2)


def space():
    print('')

def banner():
    clear()
    os.system('cat banner/El_Korsan_tool.txt')


def test_connection():
    try:
        print(W + 'Checking Your Internet Connection...')
        time.sleep(2)
        socket.create_connection(("information-eg.blogspot.com", 80))
        print('\033[1;32m[+] You Are Connected')
        time.sleep(1)
        clear()
    except OSError:
        print(R + '[!] You Are Not Connected To Internet')
        exit()


