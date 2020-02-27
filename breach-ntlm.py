#!/usr/bin/python3
import hashlib
import fileinput
import subprocess

for line in fileinput.input():
    line=line.rstrip()
    
    ntlmhash=line
    hits=0

    #check 1
    process = subprocess.Popen(['./sgrep', '-i',ntlmhash,'./allbreach.txt'],stdout=subprocess.DEVNULL)
    process.communicate()
    return_code = process.poll()
    if return_code is not None:
        if return_code == 0:
            print("Found '"+line+"' in breach list")

