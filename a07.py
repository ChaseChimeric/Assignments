"""
Program Name:   Rainfall Logging Program
Filename        main.py
Author:         Ryan Fong
Date:           18-10-2020
Assignment:     Assignment 7
Description:    A program that collects user data for rainfall in the months of
                a year and calculates various data off of it
                (e.g. Average rainfall, total rainfall)
Sources:        None
"""
MONTH_NAMES = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
               'August', 'September', 'October', 'November', 'December']
MONTHS_AMOUNT = 12

rainfall_array = []


def get_rainfall_data():
    """
    Module Name:   get_rainfall_data()
    Parameters:    None
    Description:   Loops through rainfall_array[] and fills it with data
    """
    for iter in range(0, MONTHS_AMOUNT):  #For loop to gather input in rainfall_array
        print("Please enter the rainfall for", MONTH_NAMES[iter])
        rainfall_array.append(float(input()))


def get_total_rainfall(rainfall_array, months_len):
    """
    Module Name:   get_total_rainfall()
    Parameters:    1 Array 'rainfall_array' 1 Integer 'months_len'
    Description:   Returns the total sum of all elements in rainfall_array[]
    """
    total = 0
    for iter in range(0, months_len):  #Calculating the total amount
        total += rainfall_array[iter]
    return total


def get_average_monthly_rainfall(total_rainfall, months_len):
    """
    Module Name:   get_average_monthly_rainfall()
    Parameters:    2 Integers 'total_rainfall, months_len'
    Description:   Calculates the average rainfall
    """
    average = total_rainfall/months_len
    return average


def get_month_with_highest_rainfall(rainfall_array, months, months_len):
    """
    Module Name:   get_month_with_highest_rainfall()
    Parameters:    2 Arrays 'rainfall_array, months', 1 Integer 'months_len'
    Description:   Finds the highest rainfall amount and returns the
                   corresponding month as a string
    """
    highest = rainfall_array[0]
    for iter in range(0, months_len):  #Finds the lowest rainfall amount by looping through
        if rainfall_array[iter] > highest:
            highest = rainfall_array[iter]
    flag = False
    index = 0
    while flag == False:  #Finds the corresponding month from the data
        if highest == rainfall_array[index]:
            flag = True
        else:
            index += 1
    return months[index]


def get_month_with_lowest_rainfall(rainfall_array, months, months_len):
    """
    Module Name:   get_month_with_lowest_rainfall()
    Parameters:    2 Arrays 'rainfall_array, months', 1 Integer 'months_len'
    Description:   Finds the lowest rainfall amount and returns the
                   corresponding month as a string
    """
    lowest = rainfall_array[0]
    for iter in range(0, months_len):  #Finds the lowest rainfall amount by looping through
        if rainfall_array[iter] < lowest:
            lowest = rainfall_array[iter]
    flag = False
    index = 0
    while flag == False:  #Finds the corresponding month from the data
        if lowest == rainfall_array[index]:
            flag = True
        else:
            index += 1
    return months[index]


def main():
    """
    Module Name:   main()
    Parameters:    None
    Description:   calls all needed functions and prints the collected data out
    """

    get_rainfall_data()
    total_rainfall = get_total_rainfall(rainfall_array, MONTHS_AMOUNT)
    average_rainfall = get_average_monthly_rainfall(total_rainfall, MONTHS_AMOUNT)
    highest_rainfall = get_month_with_highest_rainfall(rainfall_array, MONTH_NAMES, MONTHS_AMOUNT)
    lowest_rainfall = get_month_with_lowest_rainfall(rainfall_array, MONTH_NAMES, MONTHS_AMOUNT)
    print("Total Rainfall:              ", total_rainfall)
    print("Average Monthly Rainfall:    ", average_rainfall)
    print("Month with highest rainfall: ", highest_rainfall)
    print("Month with lowest_rainfall   ", lowest_rainfall)


if __name__ == "__main__":
    main()
