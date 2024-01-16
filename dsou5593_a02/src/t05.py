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
length = float(input("Foundation length (m): "))
width = float(input("Foundation width (m): "))
height  = float(input("Foundation height (m): "))
wall_height = float(input("Wall height (m): "))
concrete_cost = float(input("Cost of concrete ($/m^3): "))
bricks_cost = float(input("Cost of bricks ($/m^2): "))

# Calculations
foundation_volume = length * width * height
foundation_cost = foundation_volume * concrete_cost
walls_area = 2 * (length * wall_height + width * wall_height)
needed_bricks = walls_area * bricks_cost
total_cost = foundation_cost + needed_bricks

# Outputs
print()
print(f"Concrete needed for foundation (m^3): {foundation_volume:.2f}")
print(f"Cost of concrete: ${foundation_cost:.2f}")
print(f"Bricks needed for walls (m^2): {walls_area:.2f}")
print(f"Cost of bricks: ${needed_bricks:,.2f}")
print(f"Total cost: ${total_cost:,.2f}")