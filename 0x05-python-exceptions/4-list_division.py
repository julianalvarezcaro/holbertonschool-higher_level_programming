#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for pos in range(list_length):
        div = 0
        try:
            div = my_list_1[pos] / my_list_2[pos]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            result.append(div)
    return result