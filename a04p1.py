"""
Program Name: Buggy Code to Display 1-60 and then "Time's up!"
Filename:     main.py
Author:       Edited by Ryan Fong
Date:         2020-09-17
Assignment:   Assignment04 Part 1 of 2
Description:  Troubleshooting while loop
Sources:      N/A
"""


TIME_LIMIT = 60


def main():
    """
    # Module Name:  main
    # Parameters:   None
    # Description:  The program's entry point
    """
    counter = 1
                 #\/ Changed [<] to [<=] so it counts till TIME_LIMIT == 60
    while counter <= TIME_LIMIT:
        print(counter)
        counter = counter + 1
    print("Time's up!")


# Invoke the main module
if __name__ == "__main__":
    main()
