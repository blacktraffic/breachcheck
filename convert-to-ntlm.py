#!/usr/bin/python3
import hashlib
import fileinput

for line in fileinput.input():
    line=line.rstrip()
    try:
      ntlmhash=hashlib.new('md4', line.encode('utf-16le')).hexdigest()
      print(ntlmhash)
    except:
      a=1
    
