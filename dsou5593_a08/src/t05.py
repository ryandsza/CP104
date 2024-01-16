"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ryan D'Souza
ID: 169065593
Email: dsou5593@mylaurier.ca
__updated__ = "2023-11-25"
-------------------------------------------------------
"""
# Imports
from functions import has_word_chain

result1 = has_word_chain(['camel', 'leopard', 'dog', 'giraffe', 'elephant'])
result2 = has_word_chain(['cat', 'alligator', 'monkey', 'cow', 'tiger'])
result3 = has_word_chain(['gorilla', 'kitten', 'puppy', 'frog', 'snake'])

print(result1)
print(result2)
print(result3)