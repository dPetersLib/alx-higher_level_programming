#!/usr/bin/python3
def uppercase(str):
    for i in str:
        print(chr(ord(i) - 32), end='')
    print('')
