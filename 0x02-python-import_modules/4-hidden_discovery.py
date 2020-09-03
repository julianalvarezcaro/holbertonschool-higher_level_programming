#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    for pos in range(len(names)):
        if names[pos][0] == '_' and names[pos][0] == '_':
            pass
        else:
            print(names[pos])
