"""
Program Name:  Sales Tax Calculator *REFORMATTED*
Filename       main.py
Author:        Ryan Fong
Date:          09/04/2020
Assignment:    CISP 300 - Assignment 02 Part 1
Description:   Reformatted program to use modules
Sources:       See \/
https://stackoverflow.com/questions/52796600/typeerror-can-only-concatenate-str-not-float-to-str
https://appdividend.com/2020/05/13/how-to-convert-python-string-to-float/
https://stackoverflow.com/questions/20457038/how-to-round-to-2-decimals-with-python
https://docs.python.org/3/library/stdtypes.html?highlight=format#str.format
"""


#declaring tax rates at top so they aren't locked later in code
STATE_TAX = 0.04
COUNTY_TAX = 0.02


def get_amount():
    """
    Module Name: get_amount
    Parameters:  None
    Desription:  Declaring need for input then gathering input
    """
    print("Enter the purchase amount for sales tax calculation")
    return float(input())


def calculate_state_sales_tax(sale_amount):
    """
    Module Name: calculate_state_sales_tax
    Parameters:  1 float, sale_amount
    Desription:  calculating state tax and returning value
    """
    return sale_amount * STATE_TAX


def calculate_county_sales_tax(sale_amount):
    """
    Module Name: calculate_county_sales_tax
    Parameters:  1 float, sale_amount
    Desription:  calculating county tax and returning value
    """
    return sale_amount * COUNTY_TAX


def calculate_total_sales_tax(state_sales_tax_amount, county_sales_tax_amount):
    """
    Module Name: calculate_total_sales_tax
    Parameters:  2 floats, state_sales_tax_amount and county_sales_tax_amount
    Desription:  calculating total tax amount and returning it
    """
    return state_sales_tax_amount + county_sales_tax_amount


def calculate_total_sale(sale_amount, sales_tax_amount):
    """
    Module Name: calculate_total_sale
    Parameters:  2 floats, sale_amount and sales_tax_amount
    Desription:  calculates total sale by adding user data with total tax amount
    """
    return sale_amount + sales_tax_amount


def main():
    """
    Module Name: main
    Parameters:  None
    Desription:  prints and formats data while calling required modules
    """
    user_input = get_amount()
    state_sales_tax = calculate_state_sales_tax(user_input)
    county_sales_tax = calculate_county_sales_tax(user_input)
    total_sales_tax = calculate_total_sales_tax(state_sales_tax, county_sales_tax)
    total_purchase = calculate_total_sale(user_input, total_sales_tax)

    print("State sales tax is: {:.2f}".format(state_sales_tax))
    print("County sales tax is: {:.2f}".format(county_sales_tax))
    print("Total sales tax is: {:.2f}".format(total_sales_tax))
    print("\nTotal purchase amount is: {:.2f}".format(total_purchase))


if __name__ == "__main__":
    main()
