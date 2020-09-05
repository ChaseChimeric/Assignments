#Program Name:  Sales Tax Calculator *REFORMATTED*
#Filename       main.py
#Author:        Ryan Fong
#Date:          09/04/2020
#Assignment:    CISP 300 - Assignment 02 Part 1
#Description:   Reformatted program to use modules
#Sources:       See \/
#https://stackoverflow.com/questions/52796600/typeerror-can-only-concatenate-str-not-float-to-str
#https://appdividend.com/2020/05/13/how-to-convert-python-string-to-float/
#https://stackoverflow.com/questions/20457038/how-to-round-to-2-decimals-with-python
#https://docs.python.org/3/library/stdtypes.html?highlight=format#str.format

#declaring tax rates at top so they aren't locked later in code
STATE_TAX = 0.04
COUNTY_TAX = 0.02

#declaring need for input then gathering input
def get_amount():
  print("Enter the purchase amount for sales tax calculation")
  return  float(input())

#calculating state tax and returning value
def calculate_state_sales_tax(sale_amount):
  return sale_amount * STATE_TAX

#calculating county tax and returning value
def calculate_county_sales_tax(sale_amount):
  return sale_amount * COUNTY_TAX

#calculating total tax amount and returning it
def calculate_total_sales_tax(state_sales_tax_amount, county_sales_tax_amount):
  return state_sales_tax_amount + county_sales_tax_amount

#calculates total sale by adding user data with total tax amount
def calculate_total_sale(sale_amount, sales_tax_amount):
  return sale_amount + sales_tax_amount

#prints and formats data while calling required modules
def main():
  user_input = get_amount()
  print("State sales tax is: {:.2f}".format(calculate_state_sales_tax(user_input)))
  print("County sales tax is: {:.2f}".format(calculate_county_sales_tax(user_input)))
  print("Total sales tax is: {:.2f}".format(calculate_total_sales_tax(calculate_state_sales_tax(user_input), calculate_county_sales_tax(user_input))))
  print("\nTotal purchase amount is: {:.2f}".format(calculate_total_sale(user_input, calculate_total_sales_tax(calculate_state_sales_tax(user_input), calculate_county_sales_tax(user_input)))))

main()
