#!/usr/bin/python3
"""UTF-8 validation module"""


def validUTF8(data):
    """Checks if a given list of integers represents a valid UTF-8 encoding"""
    n_bytes = 0

    for num in data:
        # Only the last 8 bits are relevant
        byte = num & 0xFF

        if n_bytes == 0:
            # Count leading 1s to determine the number of bytes in the character
            mask = 1 << 7
            while mask & byte:
                n_bytes += 1
                mask >>= 1

            if n_bytes == 0:
                continue

            # UTF-8 characters can be between 2 and 4 bytes
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # All continuation bytes must start with '10'
            if not (byte & 0b10000000 and not (byte & 0b01000000)):
                return False

        n_bytes -= 1

    return n_bytes == 0
