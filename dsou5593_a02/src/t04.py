"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ryan D'Souza
ID: 169065593
Email: dsou5593@mylaurier.ca
__updated__ = "2023-10-07"
-------------------------------------------------------
"""
# Inputs
flyer_num = int(input("Number of flyers: "))
num_delivery_people = int(input("Number of delivery people: "))

# Calculations
flyers_per_person = flyer_num // num_delivery_people
flyers_left_over = flyer_num % num_delivery_people

# Outputs
print()
print("Flyers per delivery person:", flyers_per_person)
print("Flyers left over:", flyers_left_over)