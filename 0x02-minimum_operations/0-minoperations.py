#!/usr/bin/python3
"""
Your text editor can execute only two operations in this file:
Copy All and Paste. Given a number n, write a method that
calculates the fewest number of operations needed to
result in exactly n H characters in the file
"""


def minOperations(n):
    """Calculates the fewest number of operations"""
    if n == 1:
        return 0

    operations = 0
    current_h = 1
    clipboard = 0

    while current_h < n:
        if n % current_h == 0:
            clipboard = current_h
            current_h *= 2
            operations += 2
        else:
            current_h += clipboard
            operations += 1

    return operations if current_h == n else 0
