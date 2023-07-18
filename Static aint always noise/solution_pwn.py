#!/usr/bin/env python3
import pwn
pwn.log.info('Opening static file')
bash = pwn.ELF('static')
pwn.log.success('Yay! Got the flag: {}'.format(bash.string(list(bash.search(b'picoCTF'))[0]).decode('utf-8')))



