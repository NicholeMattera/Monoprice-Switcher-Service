#
# This file is part of MonopriceSwitcherService. https://github.com/NicholeMattera/MonopriceSwitcherService
# Copyright (C) 2020 Nichole Mattera
#

from app.utils.crc import calculateCRC

# RE'd by Josh in the Amazon Reviews. (https://amzn.to/2UqCu31)
def switchInput(input: int):
    audio = bytearray(b'\x20\x02\x01')
    audio.append(input)
    audio.append(calculateCRC(audio))

    audioUnknown = bytearray(b'\x20\x08\x01\x00')
    audioUnknown.append(calculateCRC(audioUnknown))

    video = bytearray(b'\x20\x01\x01')
    video.append(input)
    video.append(calculateCRC(video))

    videoUnknown = bytearray(b'\x20\x07\x01\x00')
    videoUnknown.append(calculateCRC(videoUnknown))
    
    return audio + audioUnknown + video + videoUnknown
