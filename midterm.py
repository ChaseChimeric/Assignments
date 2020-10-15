"""
Program Name: CISP300 Midterm
Filename:     main.py
Author:       Ryan Fong
Date:         2020-10-08
Assignment:   Midterm Exam
Description:  Complete the program per the specifications
Sources:      None
"""
from random import *

MIN_OPERANDS = 0
MAX_OPERANDS = 999

def main():
    # Accumulators
    total_questions = 0
    total_correctly_answered = 0

    # Loop as long as the player wishes to keep playing
    keep_playing = True;
    while keep_playing:
        # Get 2 random numbers
        num_one = get_random_number()
        num_two = get_random_number()

        # Display the math problem
        display_addition_operation(num_one, num_two)

        # Get the user's
        user_attempt = get_user_answer_validated()

        # Calculate the correct answer
        correct_answer = num_one + num_two

        # Determine if the user answered correctly
        if (get_comparison_result(correct_answer, user_attempt)):
            # Implement Me: track total_correctly_answered
            total_correctly_answered += 1
            print("Correct!")
        else:
            print("Sorry, the correct answer is: ", correct_answer)
        total_questions += 1

        keep_playing = player_wishes_to_play()

    display_final_results(total_questions, total_correctly_answered)

def get_random_number():
  """
  Module Name:  get_random_number
  Parameters:   None
  Description:  Returns a random integer in the range specified by the global constants
  """
  return randint(MIN_OPERANDS,MAX_OPERANDS)

def display_addition_operation(number_one, number_two):
  """
  Module Name:  display_addition_operation
  Parameters:   Two parameters, both integers
  Description:  Displays the math problem in a friendly way
  """
  print(f"  {number_one:>3d}")
  print(f"+ {number_two:>3d}")
  print("-"*5)

def player_wishes_to_play():
    """
    Module Name:    player_wishes_to_play
    Parameters:     None
    Description:    Asks the user if they want to play again, with input validation
                    returns Boolean
    """
    print("Do you wish to go again? (y/n)")
    user_input = input().lower()
    while user_input != "y" and user_input != "n": #Input Validation
        print("Incorrect input, please enter y or n:")
        user_input = input().lower()
    if user_input == "y":
        keep_playing = True
    elif user_input == "n":
        keep_playing = False
    else:
        print("ERROR from player_wishes_to_play()")
    return keep_playing

def get_user_answer_validated():
  """
  Module Name:    get_user_answer_validated
  Parameters:     None
  Description:    Validates for correct input, integer returns value
  """
  user_input = int(input())
  while user_input < 0: #Input Validation
      print("Incorrect input, please enter a value above zero:")
      user_input = int(input())
  return user_input

def get_comparison_result(correct_result, attempt):
    """
    Module Name:    get_comparison_result
    Parameters:     2 integers, correct_result, attempt
    Description:    compares user answer with the correct result. returns boolean
    """
    if correct_result == attempt:
        return True
    else:
        return False

def display_final_results(number_of_questions, number_correctly_answered):
    """
    Module Name:    display_final_results
    Parameters:     2 integers, number_of_questions, number_correctly_answered
    Description:    Finds percentage correct, Displays total attempted, number correct, and percentage
    """
    percentage_correct = round(number_correctly_answered/number_of_questions, 2) * 100 #Finding percentage correct
    print("Total number of math problems attempted: ", number_of_questions)
    print("Number of correct answers:               ", number_correctly_answered)
    print("Percentage correct:                      ", percentage_correct, "%")


main()
