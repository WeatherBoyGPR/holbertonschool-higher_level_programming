#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) >= 1:
        res = (len(sentence), sentence[0])
    else:
        res = (0, "None")
    return res
