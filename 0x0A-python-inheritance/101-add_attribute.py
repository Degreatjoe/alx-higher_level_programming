#!/usr/bin/python3
'''add attribute module'''


def add_attribute(obj, attr, value):
    """Add a new attribute to an object if possible.

    Args:
        obj: The object to which the attribute will be added.
        attr: The name of the attribute to add.
        value: The value of the attribute to add.

    Raises:
        TypeError: If the object cannot have new attributes.
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
