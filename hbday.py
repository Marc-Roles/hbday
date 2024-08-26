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
    '\033[38;5;196m',  # Red
    '\033[38;5;202m',  # Red-Orange
    '\033[38;5;208m',  # Orange
    '\033[38;5;214m',  # Yellow-Orange
    '\033[38;5;220m',  # Yellow
    '\033[38;5;226m',  # Light Yellow
    '\033[38;5;190m',  # Pale Yellow-Green
    '\033[38;5;154m',  # Light Green
    '\033[38;5;118m',  # Green
    '\033[38;5;82m',   # Teal-Green
    '\033[38;5;46m',   # Cyan
    '\033[38;5;47m',   # Light Cyan
    '\033[38;5;48m',   # Pale Blue-Cyan
    '\033[38;5;33m',   # Light Blue
    '\033[38;5;27m',   # Blue
    '\033[38;5;21m',   # Indigo
    '\033[38;5;57m',   # Violet-Indigo
    '\033[38;5;93m',   # Violet
    '\033[38;5;129m',  # Magenta-Violet
    '\033[38;5;165m',  # Magenta
    '\033[38;5;201m',  # Pink
    '\033[38;5;198m',  # Light Pink
    '\033[38;5;197m',  # Rose
    '\033[38;5;196m'   # Red
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

        time.sleep(0.05)

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
