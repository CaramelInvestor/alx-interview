#!/usr/bin/python3
"""Minimum Operations python3 challenge"""


def minOperations(n):
    """
    calculates the fewest number of
    operations needed to result in exactly n H
    characters in this file.
    Returns:
        Integer : if n is impossible to achieve, return 0
    """
    if n <= 1:
        return n

    operations = 0
    clipboard = 1  # Number of characters in the clipboard
    buffer = 1     # Number of characters currently in the text editor

    while buffer < n:
        if n % buffer == 0:  # If 'n' is divisible by current buffer size, perform Copy All
            clipboard = buffer
            operations += 1
        buffer += clipboard  # Perform Paste
        operations += 1

    return operations
