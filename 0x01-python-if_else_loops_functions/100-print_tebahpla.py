#!/usr/bin/python3
for letter in range(122, 96, -1):
    if letter % 2 == 0:
        print("{}".format(chr(letter)), end="")
    else:
        letter = letter - 32
        print("{}".format(chr(letter)), end="")
