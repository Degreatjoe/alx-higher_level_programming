#!/usr/bin/python3
'''Defining a class'''


def is_same_class(obj, a_class):
    """Check if obj is exactly an instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is exactly an instance of a_class, otherwise False.
    """
    return type(obj) is a_class
