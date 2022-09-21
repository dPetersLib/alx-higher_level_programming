#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) in range(32, 91):
            order = ord(i)
        else:
            order = ord(i) - 32
        print("{}".format(chr(order)), end='')
    print('')
