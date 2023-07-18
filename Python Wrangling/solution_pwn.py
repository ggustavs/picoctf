#!/usr/bin/env python3
import pwn
target = pwn.process('python3 ende.py -d flag.txt.en',shell=True)
with open('pw.txt','r') as infile:
    pw = infile.readlines()[0].encode('ascii')
    target.sendline(pw)
    print(target.recvline())

