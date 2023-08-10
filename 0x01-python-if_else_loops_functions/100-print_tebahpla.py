#!/usr/bin/python3
dat = 0
for i in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(i - dat)), end="")
    dat = 32 if dat == 0 else 0
