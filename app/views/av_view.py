#
# This file is part of MonopriceSwitcherService. https://github.com/NicholeMattera/MonopriceSwitcherService
# Copyright (C) 2020 Nichole Mattera
#

from app.config import config
from app.errors.checksum_error import ChecksumError
from app.errors.length_error import LengthError
from app.models.serial_requests import switchInput
from app.models.responses import ErrorResponse, SuccessResponse, InfoResponse
from app.views.serial_method_view import SerialMethodView
from flask import request
import serial

class AVView(SerialMethodView):
    def get(self):
        try:
            s = self.connect()
            # RE'd by Josh in the Amazon Reviews. (https://amzn.to/2UqCu31)
            s.write(bytearray.fromhex("20 3F 00 00 F1 20 08 00 00 55 20 07 00 00 0A"))
            return InfoResponse(s.readline()).response(200)
        except ChecksumError as e:
            return ErrorResponse(4, 'One or more invalid checksums in message.').response(500)
        except LengthError as e:
            return LengthError(3, 'Invalid length of message.').response(500)
        except serial.serialutil.SerialException as e:
            return ErrorResponse(0, 'Device not available.').response(500)

    def post(self):
        data = request.json

        if 'input' not in data:
            return Error(1, 'Input field is required.').response(400)
        if data['input'] < 1 or data['input'] > config['totalNumberOfInputs']:
            return Error(2, 'Input field is out of range.').response(400)

        try:
            s = self.connect()
            s.write(switchInput(data['input']))
            return SuccessResponse('Success!').response(200)
        except serial.serialutil.SerialException as e:
            return ErrorResponse(0, 'Device not available.').response(500)
