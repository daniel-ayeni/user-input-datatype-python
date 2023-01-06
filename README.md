# user-input-datatype-python
This code is a program that checks the data type of a user-inputted value in Python. 
It does this by using regular expressions to match the value against a series of patterns, each corresponding to a specific data type. 
The code first imports the re module, which provides functions for working with regular expressions.
The user is then prompted to input a value, which is stored in the value variable. 
The code then defines a series of patterns for identifying different data types, including float, list, tuple, complex, set, dictionary, and unknown.
The code then uses the match function from the re module to check if the user-inputted value matches any of these patterns. 
If a match is found, the code prints out a message indicating the data type of the value. 
If no match is found, the code uses a try-except statement to catch any ValueError exceptions that may be raised if the value cannot be cast to a specific data type.
