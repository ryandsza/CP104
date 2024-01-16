"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ryan D'Souza
ID: 169065593
Email: dsou5593@mylaurier.ca
__updated__ = "2023-11-24"
-------------------------------------------------------
"""
# Imports
from functions import customer_best

fh = open(r"C:\Users\seanr\eclipse-workspace\CP104\dsou5593_l10\src\customers.txt","r")

print("Find customer by with largest balance:")

result = customer_best(fh)

fh.close()

# Outputs
print(result)