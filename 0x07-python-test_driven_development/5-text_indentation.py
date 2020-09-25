#!/usr/bin/python3
"""
5-text_identation module

Has a function that prints a text with new lines after each '?' or '.' chars
"""


def text_indentation(text):
    """
    Prints a text with new lines afters each '?' or '.'
    """
    validate = False
    if type(text) is not str:
        raise TypeError('text must be a string')
    if not text:
        return
    for x in range(len(text)):
        if text[x] is '?' or text[x] is '.' or text[x] is ':':
            print(text[x])
            print()
            validate = True
            continue
        if text[x] is ' ' and validate:
            continue
        else:
            validate = False
            print(text[x], end='')
