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



def calculate_paint_gallons_required(total_wall_space):
    """
    Module Name:   calculate_paint_gallons_required
    Parameters:    1 float, total_wall_space
    Desription:    Multiplies square_feet and GALLONS_PER_FOOT to get number of gallons
    """
    return total_wall_space * GALLONS_PER_FOOT


def calculate_labor_hours_required(total_wall_space):
    """
    Module Name:   calculate_labor_hours_required
    Parameters:    1 float, total_wall_space
    Desription:    Multiplies square_feet and LABOR_PER_FOOT to get number of hours
    """
    return total_wall_space * LABOR_PER_FOOT


def calculate_cost_of_paint(paint_gallons_required, paint_price_per_gallon):
    """
    Module Name:   calculate_cost_of_paint
    Parameters:    2 floats, paint_gallons_required and paint_price_per_gallon
    Desription:    Multiplies calculate_paint_gallons_required() and paint_price
    """
    return paint_gallons_required * paint_price_per_gallon


def calculate_cost_of_labor(labor_hours_required, labor_cost_per_hour):
    """
    #Module Name:   calculate_cost_of_labor
    #Parameters:    2 floats, labor_hours_required and labor_cost_per_hour
    #Desription:    Multiplies calculate_labor_hours_required() and the LABOR_COST
    """
    return labor_hours_required * labor_cost_per_hour


def calculate_total_job_cost(cost_of_paint, cost_of_labor):
    """
    Module Name:   calculate_total_job_cost
    Parameters:    2 floats, cost_of_paint and cost_of_labor
    Desription:    Adds calculate_cost_of_paint() and calculate_cost of labor together and returns that value
    """
    return cost_of_paint + cost_of_labor


def main():
    """
    Module Name:   main
    Parameters:    None
    Desription:    Gathers input from user, and calls all required modules and prints output
    """
    print("Enter the square footage of the area to be painted: ")
    square_feet = float(input())
    print("Enter the price of paint (per gallon) to be used: ")
    paint_price = float(input())

    paint_gallons_required = calculate_paint_gallons_required(square_feet)
    labor_hours_required = calculate_labor_hours_required(square_feet)
    cost_of_paint = calculate_cost_of_paint(paint_gallons_required, paint_price)
    cost_of_labor = calculate_cost_of_labor(labor_hours_required, LABOR_COST)
    total_job_cost = calculate_total_job_cost(cost_of_paint, cost_of_labor)

    print("Gallons of paint required:   | {:.2f} Gallons".format(paint_gallons_required))
    print("Labor hours required:        | {:.2f} Hours".format(labor_hours_required))
    print("Cost of paint:               | ${:.2f}".format(cost_of_paint))
    print("Cost of labor:               | ${:.2f}".format(cost_of_labor))
    print("Total job cost is:           | ${:.2f}".format(total_job_cost))

#Run Program
if __name__ == "__main__":
    main()
