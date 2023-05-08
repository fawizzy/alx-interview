#!/usr/bin/python3
"""
method to determine if a given
data set represents a valid UTF8
"""

def validUTF8(data: list) -> bool:
    for i in data:
        print(i >> 4)
    
    return True