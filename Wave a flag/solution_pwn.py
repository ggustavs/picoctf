#!/usr/bin/env python3
import pwn
import re

#the pwn tools way - trying to get used to processes and shit
target = pwn.process('strings warm | grep picoCTF',shell=True)
ans = re.search('picoCTF+\{[^}]*\}',str(target.recvline()))
print(ans.group(0)) 

# the proper python way

