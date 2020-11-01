"""
Program Name:   Golf Score Logger
Filename        main.py
Author:         Ryan Fong
Date:           31 October 2020
Assignment:     Assignment 9 Part 1
Description:    A program to store the golf scores and player names in a file.
Sources:        None
"""


def read_records_from_file_and_display(filename):
    """
    Module Name:
    Parameters:
    Description:
    """
    with open(filename, 'r') as InFile:
        LineCount = len(InFile.read().split('\n')) - 1  #Gets amount of lines with data in them
        InFile.seek(0,0)  #Resets read position of file
        for line in range(0, LineCount):
            LineData = InFile.readline().rstrip('\n').split('#')  #reads a line, strips '\n', and splits the line on deliminator '#'
            print(LineData[0], 'had a score of: ', LineData[1])  #prints name and respective score
    return 0


def main():
    """
    Module Name:   main()
    Parameters:    None
    Description:   Main module for code
    """
    read_records_from_file_and_display('golfData.dat')


if __name__ == "__main__":
    main()
