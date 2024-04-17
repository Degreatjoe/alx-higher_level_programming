#!/usr/bin/python3
'''function to open file'''


def read_file(filename=""):
    '''Reading the content of a file
    args:
        filename: the name of the file
        '''
    try:
        with open(filename, "a+", encoding="utf-8") as file:
            file.seek(0)  # Move the cursor to the beginning of the file
            content = file.read()  # Read the content
            print(content)
    except Exception as e:
        print(f"An error occurred: {e}")
