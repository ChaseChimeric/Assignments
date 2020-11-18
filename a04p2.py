"""
Program Name:  Celsius to Fahrenheit table
Filename       main.py
Author:        Ryan Fong
Date:          09-17-2020
Assignment:    Assignment 04 Part 2
Description:   Prints a table of converted temperatures from 0C to 20C in Fahrenheit
Sources:       N/A
"""


#Constant for fahrenheit cenversion factor of 9/5
CONVERSION_FACTOR = 9/5


def celsius_to_fahrenheit(celsius_temp):
    """
    #Module Name:   celsius_to_fahrenheit()
    #Parameters:    One Integer, celsius temp
    #Description:   Performs the conversion of celsius to fahrenheit
    """
    fahrenheit_temp = CONVERSION_FACTOR * celsius_temp + 32
    return fahrenheit_temp


def main():
    """
    #Module Name:   main()
    #Parameters:    None
    #Description:   Main module for code
    """
    celsius_list = range(0, 21, 1)
    print("Celsius | Fahrenheit")

    for x in celsius_list:
        fahrenheit = celsius_to_fahrenheit(x)
        print("     ", x, "|", fahrenheit)


#Invoking main()
if __name__ == "__main__":
    main()
