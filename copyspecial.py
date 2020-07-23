#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "Gabrielle Morrow/demo"

import re
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    # your code here
    # get list of files in directory
    paths = os.listdir(dirname)
    special_paths = []
    # identify "special" files -- "_w_"
    for filename in paths:
        match = re.search(r'_\w+_', filename)
        if match:
            special_paths.append(os.path.abspath(os.path.join(dirname, filename)))
    #return absolute path to special files
    print(special_paths)        
    return special_paths


def copy_to(path_list, dest_dir):
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)
    for dest_dir in path_list:
      filename = os.path.basename(path_list)
      shutil.copy(dest_dir, filename)      
    return


def zip_to(path_list, dest_zip):
    cmd = ['zip-j', 'dest_zip']
    cmd.extend(path_list)
    print("command im going to do:")
    print(' '.join(cmd))
    subprocess.check_output(cmd)
    return


def main(args):
    print(args)
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('from_dir', help='dest zipfile for special files')

    # TODO: add one more argument definition to parse the 'from_dir' argument
    ns = parser.parse_args(args)
    print(ns)

    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).

    special_paths = get_special_paths(ns.from_dir)

    if ns.tozip:
        zip_to(special_paths, ns.tozip)
    else:
        print('\n'.join(special_paths))
    # Your code here: Invoke (call) your functions


if __name__ == "__main__":
    main(sys.argv[1:])
