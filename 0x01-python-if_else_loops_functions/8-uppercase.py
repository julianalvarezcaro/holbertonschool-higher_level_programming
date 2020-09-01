#!/usr/bin/python3
def uppercase(str):
    for pos in range(len(str)):
        aski = ord(str[pos])
        if aski > 96 and aski < 123:
            print("{}".format(chr(aski - 32)), end='')
        else:
            print("{}".format(chr(aski)), end='')
    print("")