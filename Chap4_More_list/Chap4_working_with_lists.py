# Name: Ximu.W
# Date: 11/09/2020
# Subject: Working with list
'''
In Chap3_List you know how to make a simple list, and you learned to work with the individual elements in a list.
In this chapter you will learn how to loop through an entire list using just a few lines of code.
'''
name = []
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
    print(magician.title() + ', that was a great trick.')
    print('I can\'t wait to see your next trick, ' + magician.title() + '\n')
    name.append(magician.title())
print('Thank you, everyone. That was a great magic show!')
print(name)

# making numerical lists
for value in range(1,5):
    print(value)
for i in range(1,6):
    print(i)
# using range() to make a list of numbers
numbers = list(range(1,6))
print(numbers)
even_numbers = list(range(2,11,2))
print(even_numbers)
squares = list()
for value in range(1,11):
    squares.append(value ** 2)
print(squares)

# simple statistics with a list of numbers
digits = list(range(0,10))
print(max(digits))
print(min(digits))
print(sum(digits))
# list comprehension
''' 
The approach described earlier for generating the list squares consisted of using three or four lines of code. 
A list comprehension 
allow you to generate this same list in just one line of code. A list comprehension combines the for loop and 
the creation of new elements into one line, and automatically appends each new element.'''

squares = [value ** 2 for value in range(1, 11)]
print(squares)

# working with part of a list
# slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])
print('Here are the first three players on my team:')
for player in players[0:3]:
    print(player.title())

# Copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]
my_foods.append('cannoli')
friends_foods.append('ice cream')
print('My favorite foods are:')
print(my_foods)
print('\nMy friends\'s favorite foods are:')
print(friends_foods)

# Tuples
'''
Lists work well for storing sets of items that can chane throughout the life_thought of a program. 
The ability to modify lists is particularly important when you're working with a list of users on a website 
or a list of characters in a game. 
However, sometimes you will want to create a list of items that cannot change. Tuples
allow you to do just that. 
Python refers to values that cannot change as immutable, and an immutable list is called a tuple

A tuple looks just like a list except you use parentheses instead of square brackets. 
Once you define a tuple, you can access individual elements by using each item's index,
just as you would for a list
'''

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# dimensions[0] = 250
# print(dimensions)
# TypeError: 'tuple' object does not support item assignment
for dimension in dimensions:
    print(dimension)

# Writing over a tuple
print("The original dimensions: ")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
''' 
When compared with lists, tuples are simple data structures. Use them when you want to store a set of values that should 
not be changed throughout the life_thought of a program
'''

'''
                    # Styling your Code
# Write easy-to-read code
Python programmers have agreed on a number of styling conventions to ensure that everyone's code is structured in 
roughly the same way, once you have learned to write clean Python code, You should be able to understand the overall 
structure of anyone else' code

# The style Guide
When someone wants to make a change to the Python language, they write a Python Enhancement Proposal(PEP). 
PEP8 instructs Python programmers on how to style their code.

# Indentation
PEP8 recommends you use four spaces per indentation level. Use tab keys and not mix them with space
Mixing tabs and spaces in your file can cause problems that are very difficult to diagnose. 
If you think you have a mix of tabs and spaces
you can CONVERT ALL TABS IN A FILE TO SPACES IN MOST EDITORS.

# Line Length
Many Python programmers recommend that each line should be less than 80 characters
Historically, this guideline developed because most computers could fit only 79 characters on a single line
in a terminal. Professional programmers often have several files open on the same screen, 
and using the standard line length allows them to see the entire lines in two or three files that are open 
side by side on screed.
PEP8 also recommends that you limits all of your comments to 72 characters per line, because some of the tools that 
generate automatic documentation for larger projects add formatting characters at the beginning of each commented line

# Blank Lines
To group parts of your program visually, use blank lines. You should use blank lines to organize your files, 
but don't do so excessively. By followint the examples provided in this book, you should strike the right balance.
For example, if you have five lines of code that build a list, and then another three lines that do something with 
that list, it is appropriate to place a blank line between the two sections. However, you should not place three or 
four blank lines between the two sections.
Blank lines won't affect how your code runs, but they will affect the readability of your code.
The python interpreter uses horizontal indentation to interpret the meaning of your code, but it 
disregards vertical spacing.

# Other Style Guidelines
PEP8
https://www.python.org/dev/peps/pep-0008/
'''

