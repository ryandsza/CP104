"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ryan D'Souza
ID: 169065593
Email: dsou5593@mylaurier.ca
__updated__ = "2023-12-02"
-------------------------------------------------------
"""
# Imports
from functions import read_integers

file_path = "numbers.txt"
with open(file_path, "r") as file_handle:
    numbers = read_integers(file_handle)
    print(numbers)