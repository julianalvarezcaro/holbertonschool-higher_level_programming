#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    result = 0
    nargs = len(args)
    for pos in range(1, nargs):
        result += int(args[pos])
    print(result)
