"""
Program Name:   Golf Score Logger
Filename        main.py
Author:         Ryan Fong
Date:           31 October 2020
Assignment:     Assignment 9 Part 1
Description:    A program to store the golf scores and player names in a file.
Sources:        None
"""


def get_records_from_user_and_write_to_file(filename):
    """
    Module Name:
    Parameters:
    Description:
    """
    with open(filename, 'a') as OutputFile:
        go_again = True
        while go_again == True:
            print('Please enter the player\'s name:')
            name_temp = input()  #Puts player name into variable for now
            print('Please enter ', name_temp, '\'s score:')
            score_temp = input()  #Puts score in variable
            OutputFile.write(name_temp + '#' + score_temp + '\n')  #Writes name and score into file and adds new line '#' is deliminator
            print('Would you like to add another record (y/n)?')
            user_input = input().lower()
#---------------------------------------------------- Input Validation / Exit Script
            correct_input = False
            while correct_input == False:
                if user_input != 'n' and user_input != 'y':
                    print("Please enter Yes('y') or No('n')")
                    user_input = input().lower()
                elif user_input == 'n':
                    go_again = False
                    correct_input = True
                elif user_input == 'y':
                    correct_input = True
#-----------------------------------------------------
    return 0


def main():
    """
    Module Name:   main()
    Parameters:    None
    Description:   Main module for code
    """
    get_records_from_user_and_write_to_file('golf.dat')


if __name__ == "__main__":
    main()
