#
# This file is part of MonopriceSwitcherService. https://github.com/NicholeMattera/MonopriceSwitcherService
# Copyright (C) 2020 Nichole Mattera
#

def calculateCRC(data: bytearray):
    check = 0
    for value in data:
        b = value
        if (value < 0):
            b = value + 256
        for i in range(8):
            odd = ((b ^ check) & 1) == 1
            check >>= 1
            b >>= 1
            if (odd):
                check ^= 0x8C
    return check