#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure both tuples have at least two elements
    a = tuple_a[:2] + (0, 0)
    b = tuple_b[:2] + (0, 0)
    
    # Return a tuple containing the element-wise sum of the input tuples
    return (a[0] + b[0], a[1] + b[1])
