#!/usr/bin/python3
'''Defining a lookup function '''


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.
    """
    return dir(obj)
