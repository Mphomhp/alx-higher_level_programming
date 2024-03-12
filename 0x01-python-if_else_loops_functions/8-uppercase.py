#!/usr/bin/python3
def uppercase(str):
    for interator in str:
        temp = interator
        if ord(temp) >= 97 and ord(temp) <= 122:
            temp = chr(ord(interator) - 32)
        print("{}".format(temp), end='')
    print()
