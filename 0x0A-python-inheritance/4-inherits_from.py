#!/usr/bin/python3
'''Defining a module'''


def inherits_from(obj, a_class):
    """Check if obj is an instance of a class that inherited
    (directly or indirectly)
    from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a subclass of a_class, otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
