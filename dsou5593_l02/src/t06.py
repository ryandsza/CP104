"""
-------------------------------------------------------
[Lab 2, Task 6]
-------------------------------------------------------
Author:  Ryan D'Souza
ID: 169065593
Email: dsou5593@mylaurier.ca
__updated__ = "2023-09-22"
-------------------------------------------------------
"""
# Constants
# TODO: defines the variable 'months' to the number 12
months = 12

# Inputs
# TODO: asks the user for the mortgage principal
principal = int(input("Mortgage principal ($): "))
# TODO: asks the user to input the number of years
years = int(input("Number of years: "))
# TODO: asks the user to input the yearly interest rate
annual_interest_rate = float(input("Yearly interest rate (%): "))

# Calculations
# TODO: calculate the monthly interest rate by dividing the annual interest rate by the months times 100
monthly_interest_rate = annual_interest_rate / (months * 100)
# TODO: calculates the number of payments by multiplying the years by the months
num_payments = years * months
# TODO: calculates the monthly payment by using the formula to calculate the monthly payment for a mortgage
monthly_payment = principal * (monthly_interest_rate * (1 + monthly_interest_rate) ** num_payments) / ((1 + monthly_interest_rate) ** num_payments - 1)

# Outputs
print()
print("The monthly payments are: $", monthly_payment)
