#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        return length, None
    elif length > 0:
        for first in sentence:
            return length, first
