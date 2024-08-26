#!/usr/bin/env python

import sys
import pyfiglet
import time

try:
    if len(sys.argv) > 2:
        print("Usage: hbday \"[message]\"")
        sys.exit()
    command = sys.argv[1]
except IndexError:
    command = None

rainbow = [
    '\033[31m',
    '\033[32m',
    '\033[33m',
    '\033[34m',
    '\033[35m',
    '\033[36m'
]

def clear_screen():
    print('\033[2J', end='')  # Clear the entire screen
    print('\033[H', end='')  # Move the cursor to the top-left corner

def move_cursor_to_top():
    print('\033[H', end='')  # Move the cursor to the top-left corner of the terminal

def shift_array(arr):
    last_item = arr.pop() 
    arr.insert(0, last_item)  
    return arr

def ascii_art(msg):
    global rainbow
    ascii_art = pyfiglet.figlet_format(msg)
    art_lines = ascii_art.splitlines()

    clear_screen()  # Clear the screen once at the beginning

    while True:
        rainbow = shift_array(rainbow)

        move_cursor_to_top()  # Move cursor to the top before printing

        for i, line in enumerate(art_lines):
            color = rainbow[i % len(rainbow)]
            print('\033[1m' + color + line)

        time.sleep(0.3)

def main():
    if command is None:
        msg = "Happy Birthday Walter!"
    else: 
        msg = command

    try:
        ascii_art(msg)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__": 
    main()
