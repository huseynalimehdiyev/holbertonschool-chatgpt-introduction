#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function: factorial 
    Computes the factorial of a non-negative integer using recursion.

    Parameters: n : int 
    A non-negative integer whose factorial is to be computed. 

    Returns:  int 
    The factorial of the input number n. 
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Read the argument from command line, compute factorial, and print
f = factorial(int(sys.argv[1]))
print(f)
