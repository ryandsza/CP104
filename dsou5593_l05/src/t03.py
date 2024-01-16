"""
-------------------------------------------------------
[Lab 5, Task 3]
-------------------------------------------------------
Author:  Ryan D'Souza
ID: 169065593
Email: dsou5593@mylaurier.ca
__updated__ = "2023-10-10"
-------------------------------------------------------
"""
# Imports
from functions import gym_cost

# Inputs
cost = float(input("What is the base cost for the gym membership?: "))
friends = int(input("How many friends are signing up for a gym membership?: "))

# Calculations

final_cost = gym_cost(cost, friends)

# Outputs
print(f"The final cost for the gym membership after the discount is: {final_cost}")