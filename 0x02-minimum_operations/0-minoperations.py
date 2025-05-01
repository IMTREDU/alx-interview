#!/usr/bin/python3
"""
Calculate the minimum number of operations needed to reach 
exactly n 'H' characters in a file beginning with one 'H'
"""


def minOperations(n):
    """
    Returns the fewest steps to get n 'H's using Copy All and Paste

    We start with one 'H'. You can:
    - Copy all the current H's
    - Paste what's copied

    Trick is: add up all prime factors of n.

    Args:
        n (int): Target number of H's

    Returns:
        int: Steps needed, or 0 if not possible
    """
    if n < 2:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    return operations


if __name__ == "__main__":

    n = 4
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
    n = 12
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
    