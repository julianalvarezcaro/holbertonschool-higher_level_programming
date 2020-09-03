#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv  # I save the args from the command line to this variable
    narg = len(args)  # I get the len of that list. AKA # of elements
    if narg == 1:
        sep = "."
    else:
        sep = ":"
    if narg == 2:
        argstr = "argument"
    else:
        argstr = "arguments"
    print("{} {}{}".format(narg - 1, argstr, sep))
    for pos in range(1, narg):
        print("{}{} {}".format(pos, sep, args[pos]))
