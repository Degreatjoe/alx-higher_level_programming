#!/usr/bin/python3
if __name__ == '__main__':
# Importing the add function from add_0.py
    from add_0 import add
# Assigning values to variables a and b
    a = 1
    b = 2
    ''''import: to import module
    '''
    result = add(a, b)
# Printing the result of the addition
    print("{} + {} = {} ".format(a, b, result))
