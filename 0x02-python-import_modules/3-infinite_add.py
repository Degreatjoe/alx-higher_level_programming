#!/usr/bin/python3

import sys


def main():
    args = sys.argv[1:]

    result = sum(int(arg) for arg in args)

    print(result)


if __name__ == "__main__":
    main()
