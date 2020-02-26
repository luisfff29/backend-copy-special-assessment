#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import re
import os
import sys
import shutil
import subprocess
import argparse

# This is to help coaches and graders identify student assignments
__author__ = "luisfff29"


# Write functions and modify main() to call them
def get_special_paths(dirname):
    """Fin all special files and list them"""
    paths = []
    for p, d, f in os.walk(dirname):
        for files in f:
            if "/." not in p and re.findall(r'\w*__\w+__\w*.\w*', files):
                paths.append(os.path.join(p, files))
    return paths


def copy_to(paths, dirname):
    """Copy all special files into the given directory"""
    for files in paths:
        shutil.copy(files, dirname)


def main():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser(
        description="Take a directory as an argument")
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('dir', help='dir path')
    # TODO need an argument to pick up 'from_dir'
    args = parser.parse_args()
    print(args)

    if args.dir == ".":
        args.dir = os.getcwd()

    # TODO you must write your own code to get the cmdline args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation.  If something is wrong (or missing) with any
    # required args, the general rule is to print a usage message and exit(1).

    if not args:
        parser.print_usage()
        sys.exit(1)
    # Call your functions

    if args.dir:
        try:
            if os.path.exists(args.todir):
                copy_to(get_special_paths(args.dir), args.todir)
            else:
                os.makedirs(args.todir)
                copy_to(get_special_paths(args.dir), args.todir)
        except shutil.Error:
            print('Oops! {} was already created'.format(args.todir))
            sys.exit(1)
    else:
        for files in get_special_paths(args.dir):
            print(files)


if __name__ == "__main__":
    main()
