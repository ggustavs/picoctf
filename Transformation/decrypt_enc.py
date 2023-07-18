#!/usr/bin/python3
file_path = 'enc'
with open(file_path) as infile:
	encoded_string = infile.readline()
for i in range(len(encoded_string)):
	print(chr(ord(encoded_string[i])>>8), end='')
	print(chr((ord(encoded_string[i]))-((ord(encoded_string[i])>>8)<<8)), end='')
print("")
