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
from functions import customer_append

fh = open(r"C:\Users\seanr\eclipse-workspace\CP104\dsou5593_l10\src\customers.txt", "a")

data = ['35612', 'David', 'Brown', 237.56, '2008-10-10']

customer_append(fh, data)

print("Data:", data)
print("Data appended to file")

fh.close()