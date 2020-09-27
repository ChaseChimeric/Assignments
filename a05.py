"""
Program Name:  Slot Machine Game
Filename       main.py
Author:        Ryan Fong
Date:          27 September 2020
Assignment:    Assignment 5
Description:   A simple slot machine game
Sources:       N/A
"""
from random import *
from locale import *
setlocale(LC_ALL, '')

#Constants
WIN = 1
LOSE = 0
JACKPOT = 2

#List of slot names
fruits_list = ["Cherries", "Oranges", "Plums", "Melons", "Bars"]
#Declaring list to store all slot results
slots_results = []

def compare_results(slot_one, slot_two, slot_three):
    """
    Module Name:   compare_results()
    Parameters:    3 Integers, slot_one, slot_two, and slot_three
    Description:   Game logic; Compares three slots and returns a win state (WIN, LOSE, JACKPOT)
    """

    if slot_one == slot_two and slot_one == slot_three:
        return JACKPOT

    elif slot_one == slot_two or slot_one == slot_three:
        return WIN
    elif slot_two == slot_one or slot_two == slot_three:
        return WIN
    elif slot_three == slot_one or slot_three == slot_two: #Probably not needed, but here anyways
        return WIN
    else: # Else Lose
        return LOSE

def slots_run(bet):
    """
    Module Name:   compare_results()
    Parameters:    3 Integers, slot_one, slot_two, and slot_three
    Description:   Game logic; Compares three slots and returns a win state (WIN, LOSE, JACKPOT)
    """

    for i in range(0,3):    #Loop that gets three random numbers and appends them to the list
        slots_results.append(randint(0,4))

    #Print slot results and get the win state from compare_results()
    print(fruits_list[slots_results[0]], fruits_list[slots_results[1]], fruits_list[slots_results[2]])
    win_state = compare_results(slots_results[0], slots_results[1], slots_results[2])


    if win_state == 0: #Calculates amount of money won based on the win_state
        print("Number of matches:  0")
        bet *= 0
    elif win_state == 1:
        print("Number of matches:  2")
        bet *= 2
    elif win_state == 2:
        print("Number of matches:  3")
        bet *= 3
    else:
        print("Unknown ERROR in slots_run()")

    print("Amount won this round: ", currency(bet))
    return bet

def main():
    """
    Module Name:   main()
    Parameters:    None
    Description:   Sets up while loop for playing repeatedly and calls slots_run() game
    """
    total_won = 0
    total_bet = 0
    play_again = True

    while play_again:

        print("Please enter your bet:")
        current_bet = float(input())        #Gets user input and stores it in current_bet
        total_bet += current_bet           #Adds the current bet to the game bet total
        amount_won = slots_run(current_bet) #Calls the main slots game and returns into amount_won
        total_won += amount_won            #Adds amount won to the total amount won during Game
        slots_results.clear()               #Clears random slot list for next playthrough

        print("Play again (y/n)?") #Play again section, gets user input and exits if N
        user_input = input()
        if user_input == "n":
            print("Total bet: ", total_bet)
            print("Total won: ", total_won)
            break


if __name__ == "__main__":
    main()
