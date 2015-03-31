#!/usr/bin/env python
# coding=utf-8
# which.py
# Copyright 2015.03.30 Xu.rongzhong 
# http://automationtesting.sinaapp.com
# python 2.7.* linux　and windows 7
import sys
import os
import os.path
import argparse

# deal with arguments
parser = argparse.ArgumentParser()
parser.add_argument("command", nargs='+', help="command name") 
parser.add_argument("-a", "--all", dest='all', action="store_true",
    help="echo the string you use here")
args = parser.parse_args()


def which(name, all):
    for path in os.getenv("PATH").split(os.path.pathsep):
        full_path = path + os.sep + name
        if os.path.exists(full_path):
            print(full_path)
            if not all:
                break

def main():    
    for name in args.command:
        which(name, False)

if "__main__" == __name__:
    main()