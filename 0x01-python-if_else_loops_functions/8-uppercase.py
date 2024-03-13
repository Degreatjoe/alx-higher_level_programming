#!/usr/bin/python3
def uppercase(s):
    new_string = ''
    for char in s:
        if ord('a') <= ord(char) <= ord('z'):
            new_string += '{}'.format(chr(ord(char) - 32))
        else:
            new_string += '{}'.format(char)
    print(new_string)
