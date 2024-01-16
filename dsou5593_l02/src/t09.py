"""
-------------------------------------------------------
[Lab 2, Task 9]
-------------------------------------------------------
Author:  Ryan D'Souza
ID: 169065593
Email: dsou5593@mylaurier.ca
__updated__ = "2023-09-22"
-------------------------------------------------------
"""
# Constants
# TODO: define 
PI = 3.14

# Inputs
# TODO: asks the user for the diameter of the container base
diameter_base = float(input("Diameter of container base (cm): "))
# TODO: asks the user for the height of container
container_height = float(input("Height of container (cm): "))
# TODO: asks the user for the cost of the material
material_cost = float(input("Cost of material ($/cm^2): "))
# TODO: asks the user for the number of containers
containers_numbers = int(input("Number of containers: "))

#Calculations
# TODO: calculates the radius of the base by dividing the diameter by 2
radius_base = diameter_base / 2

# TODO: calculates the surface area of the side
side_surface_area = 2 * PI * radius_base * container_height

# TODO: calculates the area of the base
base_area = PI * radius_base ** 2

# TODO: calculates the total surface area of the cylinder
one_container = side_surface_area + base_area

# TODO: calculates the total cost of one container
total_cost_one_container = one_container * material_cost

# TODO: calculates the total cost of all container
total_cost_all_containers = total_cost_one_container * containers_numbers

#Outputs 
print()
print("The total cost of one containers is $", total_cost_one_container)
print("The total cost of all containers is $", total_cost_all_containers)