"""
Program Name:  Encrypt/Decrypt
Filename       main.py
Author:        Ryan Fong
Date:          14 November 2020
Assignment:    Assignment 11
Description:   Menu based program to encrypt or decrypt specified files based on user's choice
Sources:       None
"""


def main_menu():
    """
    Module Name:    main_menu
    Parameters:     None
    Description:    Module for displaying menu and processing user's choice.
    """
    continue_program = True
    while continue_program == True:  #Loop for continuation of program
        valid_choice = False
        while valid_choice == False:  #loop for valid selection
            print('File Encryption/Decryption:')  #Menu choices
            print('1. Encrypt a file.')
            print('2. Decrypt a file.')
            print('3. End program.')
            try:
                menu_selection = int(input())  #getting user's menu menu_selection
                if menu_selection >= 1 and menu_selection <= 3:
                    valid_choice = True
                else:
                    print('Invalid range for answer. Please enter 1, 2, or 3.\n')
            except ValueError: #Catching non integer entries
                print('Invalid type of answer. Please enter 1, 2, or 3.\n')

        if menu_selection == 1:  #menu selection logic
            encrypt_file()
        elif menu_selection == 2:
            decrypt_file()
        elif menu_selection == 3:
            continue_program = False


def encrypt_file():
    """
    Module Name:    encrypt_file()
    Parameters:     None
    Description:    Encrypts data from user given input file to specified output.
    """
    print('Please enter the name of the file to encrypt:')
    filename = input()
    print('Please enter the name of the file that the encrypted text will be saved to:')
    destination_file = input()

    in_file = open(filename, 'r')
    out_file = open(destination_file, 'w')
    for char in in_file.read():  #stepping through characters
        current_char = ord(char)  #gets the unicode number of the current character
        encryp_char = current_char + 4  #adds 4 to the unicode number
        out_file.write(chr(encryp_char))  #Writes the Uni number as a regular character
    print('File has been encrypted to: ', destination_file, '\n')
    in_file.close()
    out_file.close()


def decrypt_file():
    """
    Module Name:    decrypt_file
    Parameters:     None
    Description:    Decrypts data from user given input file to specified output.
    """
    print('Please enter the name of the file to decrypt:')
    filename = input()
    print('Please enter the name of the file that the decrypted text will be saved to:')
    destination_file = input()

    in_file = open(filename, 'r')
    out_file = open(destination_file, 'w')
    for char in in_file.read():  #stepping through characters
        current_char = ord(char)  #gets the unicode number of the current character
        encryp_char = current_char - 4  #subtracts 4 to the unicode number
        out_file.write(chr(encryp_char))  #Writes the Uni number as a regular character
    print('File has been decrypted to: ', destination_file, '\n')
    in_file.close()
    out_file.close()


def main():
    """
    Module Name:   main()
    Parameters:    None
    Description:   Main module for code
    """
    main_menu()


if __name__ == "__main__":
    main()
