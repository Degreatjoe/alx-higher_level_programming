#!/usr/bin/python3
'''function to open file'''


def read_file(filename=""):
    '''Reading the content of a file
    args:
        filename: the name of the file
        '''
    with open(filename, "r+", encoding="utf-8") as file:
        content = file.read()  # Read the content
        print(content)

read_file('AUTHORS')
