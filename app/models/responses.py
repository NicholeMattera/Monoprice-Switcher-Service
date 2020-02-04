#
# This file is part of MonopriceSwitcherService. https://github.com/NicholeMattera/MonopriceSwitcherService
# Copyright (C) 2020 Nichole Mattera
#

from app.errors.checksum_error import ChecksumError
from app.errors.length_error import LengthError
from app.utils.crc import calculateCRC
from flask import Response
import json

class JSONSerializableResponse:
    def jsonEncode(self):
        return json.dumps(self.__dict__)

    def response(self, status: int):
        return Response(
            self.jsonEncode(),
            status=status,
            mimetype='application/json'
        )

class ErrorResponse(JSONSerializableResponse):
    def __init__(self, num: int, message: str):
        self.num = num
        self.message = message

class SuccessResponse(JSONSerializableResponse):
    def __init__(self, message: str):
        self.message = message

# RE'd by Josh in the Amazon Reviews. (https://amzn.to/2UqCu31)
class InfoResponse(JSONSerializableResponse):
    def __init__(self, message: bytes):
        if (len(message) != 24):
            raise LengthError
            return
        
        if (calculateCRC(message[:13]) != message[13]):
            raise ChecksumError
            return

        if (calculateCRC(message[14:18]) != message[18]):
            raise ChecksumError
            return

        if (calculateCRC(message[19:23]) != message[23]):
            raise ChecksumError
            return

        self.input = message[22]
