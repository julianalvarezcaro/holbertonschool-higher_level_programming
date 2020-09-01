#!/usr/bin/python3
def uppercase(str):
    for pos in range(len(str)):
        aski = ord(str[pos])
        if aski > 96 and aski < 123:
            upaski = chr(aski - 32)
        else:
            upaski = chr(aski)
        print("{}".format(upaski), end='')
    print("")
