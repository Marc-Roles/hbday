#!/usr/bin/env python

import sys

try:
    command = sys.argv[1]
except IndexError:
    command = None

def main():

    if command == None:
        print("Happy Birthday Walter!")
    else: 
        print(command)
