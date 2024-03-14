#!/usr/bin/python3
# Assigning values to variables a and b
a = 1
b = 2

# Importing the add function from add_0.py
from add_0 import add

# Printing the result of the addition
print("{} + {} = {}".format(a, b, add(a, b)))
