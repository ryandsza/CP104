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
from functions import file_copy_n

fh1 = open(r"C:\Users\seanr\eclipse-workspace\CP104\dsou5593_l10\src\words.txt", "r")
fh2 = open(r"C:\Users\seanr\eclipse-workspace\CP104\dsou5593_l10\src\new_words.txt", "w")

print("Copying 'words.txt' to 'new_words.txt'")

numOfLines = int(input("Number of lines to copy: "))

file_copy_n(fh1, fh2, numOfLines)