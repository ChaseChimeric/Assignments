"""
Program Name:   Golf Score Logger
Filename        main.py
Author:         Ryan Fong
Date:           31 October 2020
Assignment:     Assignment 9 Part 1
Description:    A program to store the golf scores and player names in a file.
Sources:        None
"""


def main_menu():
    menu_loop = True
    while menu_loop == True:
        #-----------------------Input Validation
        validation = False
        while validation == False:
            print('Golf Score Menu:')
            print('1. Enter golf scores to be saved')
            print('2. Display previously-entered golf scores')
            print('3. End the program')
            menu_choice = int(input('Please enter 1, 2, or 3: '))
            if menu_choice < 1 or menu_choice > 3:
                print('Invalid input, please enter either 1, 2, or 3: \n \n')
            elif menu_choice >= 1 and menu_choice <= 3:
                validation = True
        #---------------------------------------
        print('')  #New line
        if menu_choice == 1:
            get_records_from_user_and_write_to_file('golf.dat')
        elif menu_choice == 2:
            read_records_from_file_and_display('golf.dat')
        elif menu_choice == 3:
            menu_loop = False
    return 0


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


def read_records_from_file_and_display(filename):
    """
    Module Name:    read_records_from_file_and_display()
    Parameters:     1 String 'filename'
    Description:    Reads player names and scores from golf.dat and prints them
    """
    with open(filename, 'r') as InFile:
        LineCount = len(InFile.read().split('\n')) - 1  #Gets amount of lines with data in them
        InFile.seek(0, 0)  #Resets read position of file
        for line in range(0, LineCount):
            LineData = InFile.readline().rstrip('\n').split('#')  #reads a line, strips '\n', and splits the line on deliminator '#'
            print(LineData[0], 'had a score of: ', LineData[1], '\n')  #prints name and respective score
    return 0


def main():
    """
    Module Name:   main()
    Parameters:    None
    Description:   Main module for code
    """
    main_menu()


if __name__ == "__main__":
    main()
