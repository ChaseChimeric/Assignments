#Program Name:  Sales Tax Calculator
#Filename       a01.py
#Author:        Ryan Fong
#Date:          8/27/2020
#Assignment:    CISP 300 - Assignment 01 Programming Exercise #06
#Description:   A quick program to calculate sales tax based on given rates and user input
#Sources:       See \/
#https://stackoverflow.com/questions/52796600/typeerror-can-only-concatenate-str-not-float-to-str
#https://appdividend.com/2020/05/13/how-to-convert-python-string-to-float/
#https://stackoverflow.com/questions/20457038/how-to-round-to-2-decimals-with-python
#https://docs.python.org/3/library/stdtypes.html?highlight=format#str.format

#declaring tax rates at top so they aren't locked later in code
STATE_TAX = 0.04
COUNTY_TAX = 0.02

#declaring need for input then gathering input
print("Enter the purchase amount for sales tax calculation")
purchase_amount = float(input())

#calculating state tax and county tax, then adding them together for total
state_tax_calculated = purchase_amount * STATE_TAX
county_tax_calculated = purchase_amount * COUNTY_TAX
total_tax = state_tax_calculated + county_tax_calculated

#printing out all calculated data (formatting to display two decimal places)
print("\nState Sales Tax: {:0.2f}".format(state_tax_calculated))
print("\nCounty Sales Tax: {:0.2f}".format(county_tax_calculated))
print("\n>>> Total Sales Tax: {:0.2f} <<<".format(total_tax))