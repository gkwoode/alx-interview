#!/usr/bin/python3
"""Minimum Operation"""


def minOperations(n):
    """Minimun operation function"""

    if n <= 1:
        return 0

    operations = 0
    factor = 2  # Start with copying one character

    while n > 1:
        while n % factor == 0:
            n //= factor
            operations += factor
        factor += 1

    return operations
