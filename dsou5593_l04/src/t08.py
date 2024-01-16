"""
-------------------------------------------------------
[Lab 4, Task 8]
-------------------------------------------------------
Author:  Ryan D'Souza
ID: 169065593
Email: dsou5593@mylaurier.ca
__updated__ = "2023-10-06"
-------------------------------------------------------
"""
# Imports
from functions import computer_costs

# Inputs
# TODO: Asks the user to enter the cost per computer
computer_cost = float(input("Enter the cost per computer: "))
# TODO: Asks the user to enter the number of computers bought
computers_bought = int(input("Enter the number of computers bought: "))
# TODO: Asks the user to enter the number of computers bought
commission_percent = float(input("Enter the wholesaler commission percentage: "))

# Calculations
# TODO: Calculates precommission cost and total cost after commission using the computer_costs function
pre_commission_cost, total_cost = computer_costs(computer_cost, computers_bought, commission_percent)

# Outputs
print(f"({pre_commission_cost:.2f}, {total_cost:.2f})")