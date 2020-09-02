#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 != 0:
        askii = i - 32
    else:
        askii = i
    print("{}".format(chr(askii)), end='')
