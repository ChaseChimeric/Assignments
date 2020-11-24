"""
Program Name:   Ackermann's Function
Filename        main.py
Author:         Ryan Fong
Date:           21 November 2020
Assignment:     Assignment 12 Part 2
Description:    Basic program to gather input and use the Ackermann's algorithm on that input
Sources:        None
"""


def ackermann(m, n):
    """
    Module Name:    ackermann()
    Parameters:     2 integers m and n
    Description:    Uses recursion and Ackermann's algorithm to process input
    """
    if m == 0:  #Using logic provided with recursion
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n-1))


def main():
    """
    Module Name:   main()
    Parameters:    None
    Description:   Main module for code
    """
    print('Please enter a value for m: ')  #getting values for both m and n
    m = int(input())
    print('Please enter a value for n: ')
    n = int(input())
    value = ackermann(m, n)  #calling ackermann function with both initial values
    print(f'The ackermannn value for {m} , {n} is: {value}')


if __name__ == "__main__":
    main()
