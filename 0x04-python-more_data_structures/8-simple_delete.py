#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    Deletes the key from the dictionary if it exists.

    Args:
    a_dictionary (dict): The dictionary from which to delete the key.
    key (str): The key to delete from the dictionary.

    Returns:
    None. The function modifies the dictionary in place.
    """
    if a_dictionary is None:
        return
    else:
        if key in a_dictionary:
            del a_dictionary[key]
        return a_dictionary
