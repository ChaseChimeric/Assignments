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

#Module Name: get_amount
#Parameters:  None
#Desription:  Declaring need for input then gathering input
def get_amount():
  print("Enter the purchase amount for sales tax calculation")
  return  float(input())


#Module Name: calculate_state_sales_tax
#Parameters:  1 float, sale_amount
#Desription:  calculating state tax and returning value
def calculate_state_sales_tax(sale_amount):
  return sale_amount * STATE_TAX


#Module Name: calculate_county_sales_tax
#Parameters:  1 float, sale_amount
#Desription:  calculating county tax and returning value
def calculate_county_sales_tax(sale_amount):
  return sale_amount * COUNTY_TAX


#Module Name: calculate_total_sales_tax
#Parameters:  2 floats, state_sales_tax_amount and county_sales_tax_amount
#Desription:  calculating total tax amount and returning it
def calculate_total_sales_tax(state_sales_tax_amount, county_sales_tax_amount):
  return state_sales_tax_amount + county_sales_tax_amount


#Module Name: calculate_total_sale
#Parameters:  2 floats, sale_amount and sales_tax_amount
#Desription:  calculates total sale by adding user data with total tax amount
def calculate_total_sale(sale_amount, sales_tax_amount):
  return sale_amount + sales_tax_amount


#Module Name: main
#Parameters:  None
#Desription:  prints and formats data while calling required modules
def main():
  user_input = get_amount()
  print("State sales tax is: {:.2f}".format(calculate_state_sales_tax(user_input)))
  print("County sales tax is: {:.2f}".format(calculate_county_sales_tax(user_input)))
  print("Total sales tax is: {:.2f}".format(calculate_total_sales_tax(calculate_state_sales_tax(user_input), calculate_county_sales_tax(user_input))))
  print("\nTotal purchase amount is: {:.2f}".format(calculate_total_sale(user_input, calculate_total_sales_tax(calculate_state_sales_tax(user_input), calculate_county_sales_tax(user_input)))))

main()
