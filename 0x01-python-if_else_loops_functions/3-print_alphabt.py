#!/usr/bin/python3
for letter in range(ord('a'), ord('b')):
    if chr(letter) != 'q' and chr(letter) != 'e':
        print("{}".format(chr(letter)), end='')
