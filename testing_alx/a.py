#!/usr/bin/python3.8
import dis
import sys

def print_defined_names(file_path):
    try:
        with open(file_path, 'rb') as file:
            code = file.read()
            instructions = dis.get_instructions(code)
            names = set()
            for instr in instructions:
                if instr.opname == 'LOAD_CONST' and isinstance(instr.argval, str) and not instr.argval.startswith('__'):
                    names.add(instr.argval)
            for name in sorted(names):
                print(name)
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    if sys.version_info >= (3, 8):
        print_defined_names('hidden_4.pyc')
    else:
        print("Please run the code in Python 3.8 or later.")