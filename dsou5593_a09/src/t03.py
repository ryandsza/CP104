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
from functions import file_statistics

file_handle = open("addresses.txt", "r", encoding="utf-8")
ucount, lcount, dcount, wcount, rcount = file_statistics(file_handle)
print(f"{ucount},{lcount},{dcount},{wcount},{rcount}")

file_handle.close()