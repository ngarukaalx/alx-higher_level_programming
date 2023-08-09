#!/usr/bin/python3
for ansii_value in range(97, 123):
    if ansii_value != ord('q') and ansii_value != ord('e'):
        print("{}".format(chr(ansii_value)), end="")
