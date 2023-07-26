#!/usr/bin/python3
"""UTF-8 validator"""


def validUTF8(data):
    """
    Check that a sequence of byte values follows the UTF-8 encoding
    rules.  Does not check for canonicalization (i.e. overlong encodings
    are acceptable).
    """

    # Helper function to check if a number has the '10' prefix
    def is_10_prefix(num):
	"""Prefix"""

        return (num & 0b11000000) == 0b10000000

    # Number of bytes remaining for the current character
    remaining_bytes = 0

    for num in data:
        # If no remaining bytes, check the starting byte of a new character
        if remaining_bytes == 0:
            if (num & 0b10000000) == 0:
                continue  # 1-byte character, move to the next number
            elif (num & 0b11100000) == 0b11000000:
                remaining_bytes = 1
            elif (num & 0b11110000) == 0b11100000:
                remaining_bytes = 2
            elif (num & 0b11111000) == 0b11110000:
                remaining_bytes = 3
            else:
                return False  # Invalid starting byte for UTF-8 character
        else:
            # If it's not a continuation byte, it's an invalid character
            if not is_10_prefix(num):
                return False
            remaining_bytes -= 1

    # All bytes have been checked and no incomplete characters are left
    return remaining_bytes == 0

# Test case
if __name__ == "__main__":
    data_set = [197, 130, 1]
    print(validUTF8(data_set))  # Output should be True
