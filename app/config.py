#
# This file is part of MonopriceSwitcherService. https://github.com/NicholeMattera/MonopriceSwitcherService
# Copyright (C) 2020 Nichole Mattera
#

import serial

config = {
    'totalNumberOfInputs': 8,
    'device': '/dev/ttyUSB0',
    'baudrate': 9600,
    'bytesize': serial.EIGHTBITS,
    'parity': serial.PARITY_NONE,
    'stopbits': serial.STOPBITS_ONE,
    'timeout': 10
}
