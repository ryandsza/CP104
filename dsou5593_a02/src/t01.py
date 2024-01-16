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
# Constants
TAX_RATE = 18.5 / 100

# Inputs
sales_total = float(input("Enter the total sales: $"))

# Calculations
tax_annual = sales_total * TAX_RATE

# Outputs
print("\nProjected Tax Report")
print("--------------------------")
print(f"Total sales:   $ {sales_total:,.2f}")
print(f"Annual tax:    % {TAX_RATE * 100:.2f}")
print("--------------------------")
print(f"Tax:           $ {tax_annual:,.2f}")