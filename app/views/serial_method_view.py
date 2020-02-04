#
# This file is part of MonopriceSwitcherService. https://github.com/NicholeMattera/MonopriceSwitcherService
# Copyright (C) 2020 Nichole Mattera
#

from app.config import config
from flask.views import MethodView
import serial

class SerialMethodView(MethodView):
    def connect(self):
        return serial.Serial(
            config['device'],
            baudrate=config['baudrate'],
            bytesize=config['bytesize'],
            parity=config['parity'],
            stopbits=config['stopbits'],
            timeout=config['timeout']
        )
