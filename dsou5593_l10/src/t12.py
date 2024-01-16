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
from functions import find_shortest

fh = open(r"C:\Users\seanr\eclipse-workspace\CP104\dsou5593_l10\src\words.txt", "r")

print("File 'words.txt' open for reading.")

shortest = find_shortest(fh)

# Outputs

print(f"'{shortest}' is the shortest word.'")