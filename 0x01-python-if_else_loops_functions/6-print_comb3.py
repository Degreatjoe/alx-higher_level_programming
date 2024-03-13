#!/usr/bin/python3
for tens in range(10):
    for ones in range(tens + 1, 9):
        print("{:d}{:d}, ".format(tens, ones), end='')
print("89")
