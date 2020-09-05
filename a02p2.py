#Program Name:  Paint Job Calculator
#Filename       main.py
#Author:        Ryan Fong
#Date:          09/04/2020
#Assignment:    Assignment 02 | part 2
#Description:   A tool that gathers user data of square footage and paint price and calculates total job price based on input.
#Sources:       


#Declaring constants: fixed labor cost, gallons of paint per ^2 foot, and the hours of labor per ^2 foot
LABOR_COST = 20.00
#Gallons per foot is 1/115
GALLONS_PER_FOOT = 0.00869565217391304347826086956522
#Labor per foot is 8/115
LABOR_PER_FOOT = 0.06956521739130434782608695652174

#Multiplies square_feet and GALLONS_PER_FOOT to get number of gallons
def calculate_paint_gallons_required(total_wall_space):
    return total_wall_space * GALLONS_PER_FOOT

#Multiplies square_feet and LABOR_PER_FOOT to get number of hours
def calculate_labor_hours_required(total_wall_space):
    return total_wall_space * LABOR_PER_FOOT

#Multiplies calculate_paint_gallons_required() and paint_price
def calculate_cost_of_paint(paint_gallons_required, paint_price_per_gallon):
    return paint_gallons_required * paint_price_per_gallon

#Multiplies calculate_labor_hours_required() and the LABOR_COST
def calculate_cost_of_labor(labor_hours_required, labor_cost_per_hour):
    return labor_hours_required * labor_cost_per_hour

#Adds calculate_cost_of_paint() and calculate_cost of labor together and returns that value
def calculate_total_job_cost(cost_of_paint, cost_of_labor):
    return cost_of_paint + cost_of_labor

def main():

    #Gathers input from user
    print("Enter the square footage of the area to be painted: ")
    square_feet = float(input())
    print("Enter the price of paint (per gallon) to be used: ")
    paint_price = float(input())

    #Calls all required modules and prints output
    print("Gallons of paint required:   ", calculate_paint_gallons_required(square_feet))
    print("Labor hours required:        ", calculate_labor_hours_required(square_feet))
    print("Cost of paint:               ", calculate_cost_of_paint(calculate_paint_gallons_required(square_feet), paint_price))
    print("Cost of labor:               ", calculate_cost_of_labor(calculate_labor_hours_required(square_feet), LABOR_COST))
    print("Total job cost is:           ", calculate_total_job_cost(calculate_cost_of_paint(calculate_paint_gallons_required(square_feet), paint_price), calculate_cost_of_labor(calculate_labor_hours_required(square_feet), LABOR_COST)))
#Run Program
main()
