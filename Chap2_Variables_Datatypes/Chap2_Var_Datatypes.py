# Name: Ximu.W
# Date: 11/6/2020
# Subject: Variables and Data types

# Variables:
message = "Hello Python World"
print(message)

message = "Hello Python Crash Course World"
print(message)

# Rules for variable
'''
1. Variable names can only contain numbers, letters, and underscore'_'
2. No space
3. Avoid using Python Keywords and built-in functions
4. Short and Descriptive
5. i/0 1/o !!!
'''

# String
'This is a string'
"This is also a string"
    # Changing Case in a string
name = 'ada lovelace'
print(name.title())
print(name.upper())
print(name.lower())
    # Combining or Concatenating Strings
first_name = 'ada'
last_name = 'lovelave'
full_name = first_name + ' ' + last_name
print(full_name)
print('Hello,' + full_name.title() + '!')
    # Adding Whitespace to Strings with Tabs and Newlines
print('Python')
print('\tPython')
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")
'''To ensure that no whitespace exists at the right end of a string, use the rstrip() method
    lstrip() works for the left whitespace
'''

favorite_language = 'Python '
print(favorite_language)
print(favorite_language.rstrip())
favorite_language = favorite_language.rstrip()
print(favorite_language)
    # Avoiding syntax error with Strings
'''
A syntax error occurs when Python doesn't recognize a section of your program as valid Python code.
'''
message = "One of Python's strength is its diverse community."
print(message)
# message = 'One of Python's strength is its diverse community.'
# print(message)
'''
File "apostrophe.py", line 1 
 message = 'One of Python's strengths is its diverse community.' 
 ^u
SyntaxError: invalid syntax
'''

# Numbers
'''
Avoiding Type Errors with the str() Function
'''
# age = 23
# message = 'Happy' + age + 'rd Birthday!'
# print(message)
'''
type error: can only concatenate str (not 'int') to str
'''
    # Integers
print(3/2)
print(3.0/2)
print(3.0/2.0)

# Comments
