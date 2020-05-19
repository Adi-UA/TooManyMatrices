"""
basicmath.py: This module defines a few functions to perform basic discrete math
calculations. Refer to the HTML documentation for an indepth explanation.
"""

__author__ = "Aditya Banerjee"
__copyright__ = "Copyright 2020, Aditya Banerjee"
__status__ = "Development"

memo = {}  # Memoizes factorial to speed up dependent functions


def factorial(n):
    """
    This function calculates the factorial of a number n >=0.

    Arguments: n {int} -- The number whose factorial is to be calculated

    Returns: The factorial value or None if the request was invalid.
    """
    if n in memo:
        return memo[n]
    else:
        if n < 0:
            return None
        elif n == 0:
            return 1
        else:
            result = n * factorial(n - 1)
            memo[n] = result
            return result


def distinct_rPermutation_counter(n, r):
    """
    This function calculates the number of permutations possible when arranging
    n distinct objects in r places.

    Arguments: n {int} -- Number of distinct objects r {int} -- Number of places
        to arrange

    Returns: the number of rPermutations possible
    """
    numerator = factorial(n)
    denominator = factorial(n - r)
    return numerator // denominator


def distinct_rCombination_counter(n, r):
    """
    This function calculates the number of combinations possible when choosing
    r objects from n distinct objects.

    Arguments: n {int} -- Number of distinct objects r {int} -- Number of
    objects to choose

    Returns: the number of rCombinations possible
    """
    return distinct_rPermutation_counter(n, r) // factorial(r)
