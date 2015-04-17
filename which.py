#!/usr/bin/env python
# coding=utf-8
"""which.py -- "Similar function like Linux which!"
Answer of the following question:
(http://www.yl1001.com/group_article/1341427686200575.htm)
Copyright 2015.03.30 Xu.rongzhong
http://automationtesting.sinaapp.com
python 2.7.* linux　and windows 7
"""
import os
import os.path
import argparse

# deal with arguments
PARSER = argparse.ArgumentParser()
PARSER.add_argument("command", nargs='+', help="command name")
PARSER.add_argument("-a", "--all", dest='all', action="store_true",
                    help="echo the string you use here")
ARGS = PARSER.parse_args()


def which(name, all_flag):
    """
    'which' for single command.
    """
    for path in os.getenv("PATH").split(os.path.pathsep):
        full_path = path + os.sep + name
        if os.path.exists(full_path):
            print(full_path)
            if not all_flag:
                break


def main():
    """
    call function 'which'
    """
    for name in ARGS.command:
        which(name, False)

if "__main__" == __name__:
    main()
