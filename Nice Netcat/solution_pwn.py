#!/usr/bin/env python3
import pwn
target = pwn.remote('mercury.picoctf.net','43239')
for i in range(200):
    try:

        recv = target.recvline()
        print(chr(int(recv)),end='')
    except:
        break
