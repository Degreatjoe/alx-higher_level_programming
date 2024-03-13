#!/usr/bin/python3
def remove_char_at(input_str, n):
    if n >= 0:
        return input_str[:n] + input_str[n+1:]
    else:
        return input_str
