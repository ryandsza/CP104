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
from functions import append_increment

fh = open(r"C:\Users\seanr\eclipse-workspace\CP104\dsou5593_l10\src\numbers.txt", "r+")

print("File 'numbers.txt' open for reading and writing.")
result = append_increment(fh)

fh.close()

print(f"{result} is appended.")