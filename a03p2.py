#Program Name:  Dollar Change Game
#Filename       main.py
#Author:        Ryan Fong
#Date:          9/14/2020
#Assignment:    Assignment 03 Part 2
#Description:   A game that takes user integer input converts number of coins to actual values,
#               adds them up and judges whether or not they equal one dollar.
#Sources:       N/A
#gittest


#Module Name:   get_user_input()
#Parameters:    None
#Description:   gets user input in local variables and returns them as a list
def get_user_input():
    print("Step 1: enter the number of pennies (integer values only):")
    number_of_pennies = int(input())
    print("Step 2: enter the number of nickels (integer values only):")
    number_of_nickels = int(input())
    print("Step 3: enter the number of dimes (integer values only):")
    number_of_dimes = int(input())
    print("Step 4: enter the number of quarters (integer values only):")
    number_of_quarters = int(input())
    return number_of_pennies, number_of_nickels, number_of_dimes, number_of_quarters

#Module Name:   coin_calculation()
#Parameters:    4 integers| pennies, nickels, dimes, and quarters
#Description:   converts integers to actual coin values and adds them while returning them
def coin_calculation(pennies, nickels, dimes, quarters):
    pennies *= 0.01
    nickels *= 0.05
    dimes *= 0.10
    quarters *= 0.25
    return pennies + nickels + dimes + quarters

#Module Name:   main()
#Parameters:    None
#Description:   Intros game, calls both modules, and performs if/else logic to display win/lose situations
def main():
    print("How to Play: enter the number of coins required to make exactly one dollar.")
    user_input = get_user_input()
    coin_total = coin_calculation(user_input[0], user_input[1], user_input[2], user_input[3])

    if coin_total == 1.0:
        print("Congratulations - your total is $1.00.  You Win!")
    elif coin_total > 1.0:
        print("Your total was more than $1.00 ($ {:.2f})".format(coin_total))
    elif coin_total < 1.0:
        print("Your total was less than $1.00 ($ {:.2f} )".format(coin_total))

if __name__ == "__main__":
    main()
