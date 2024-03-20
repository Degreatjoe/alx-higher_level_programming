#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorts = sorted(a_dictionary)
    for key in sorts:
        print(f"{key}: {a_dictionary[key]}")
