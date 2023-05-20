#!/usr/bin/env python3
"""
Validate utf-8 for data
"""
def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data: A list of integers representing the data set.

    Returns:
        True if data is a valid UTF-8 encoding, else False.
    """
    num_bytes = 0

    for num in data:
        # Check if the current byte is a continuation byte
        if num >> 6 == 0b10:
            # If num_bytes is 0, then there's no corresponding starting byte
            if num_bytes == 0:
                return False
            num_bytes -= 1
        else:
            # Check the number of bytes in the current character
            if num_bytes != 0:
                return False
            if num >> 7 == 0b0:
                num_bytes = 0
            elif num >> 5 == 0b110:
                num_bytes = 1
            elif num >> 4 == 0b1110:
                num_bytes = 2
            elif num >> 3 == 0b11110:
                num_bytes = 3
            else:
                return False

    # If num_bytes is not 0 at the end, it means there's an incomplete character
    return num_bytes == 0
