#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        control = True
        if i % 3 == 0:
            print("Fizz", end='')
            control = False
        if i % 5 == 0:
            print("Buzz", end='')
            control = False
        if control:
            print(i, end='')
        print(" ", end='')
