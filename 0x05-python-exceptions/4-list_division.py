#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    pos = 0
    result = []
    while(pos < list_length):
        try:
            result.append(my_list_1[pos] / my_list_2[pos])
        except TypeError:
            result.append(0)
            print("wrong type")
        except ZeroDivisionError:
            result.append(0)
            print("division by 0")
        except IndexError:
            result.append(0)
            print("out of range")
            return result
        pos += 1
    return result
