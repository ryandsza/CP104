"""
-------------------------------------------------------
[Lab 5, Task 7]
-------------------------------------------------------
Author:  Ryan D'Souza
ID: 169065593
Email: dsou5593@mylaurier.ca
__updated__ = "2023-10-10"
-------------------------------------------------------
"""
# Imports
from functions import get_pay

# Inputs
hourly_rate = float(input("What is the hourly rate for the employee?: "))
hours_worked = float(input("How many hours did the employee work for?: "))

# Calculations
net_payment = get_pay(hourly_rate, hours_worked)

# Outputs
print(f"The final pay after working {hours_worked} hours and their pay being ${hourly_rate}/hr is: {net_payment:.2f}")