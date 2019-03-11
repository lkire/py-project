#!/usr/bin/env python3

from subprocess import call
#intentionally blocking otherwise use popen
from glob import glob

SRC_DIR = "project"

def test():
    call_str = ["python","-m","pytest"]
    call(call_str)

def pep():
    call_str = ["autopep8","--in-place", "--aggressive", "--aggressive"]
    call_str.extend(glob(f"{SRC_DIR}/*.py"))
    call(call_str)

def lint():
    call_str = ["pylint", f"{SRC_DIR}"]

if __name__== "__main__":
    test()
    pep()
    lint()
