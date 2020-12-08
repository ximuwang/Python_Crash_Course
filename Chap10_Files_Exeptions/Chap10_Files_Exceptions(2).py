# Name: Ximu.W
# Date: 12/1/2020
# Subject: Chapter 10 -- Files and Exceptions

# Storing Data
''':key
Many of your programs will ask users to input certain kinds of information.
You might allow users to store preferences in a game or provide data for a
visualization. Whatever the focus of your program is, you will store the info
users proide in data structures such as lists and dictionaries. When users close
a program, you will almost always want to save the info they entered. A simple
way to do this involves storing your data using the json module.
'''
''':key
The json module allows you to dump simple Python data structures into a file and 
load the data from that file the next time the program runs. You can also use json 
to share data between different Python programs. Even better, the JSON data format is 
not specific to Python, so you can share data you store in the JSON format with people
who works in many other programming languages. It is a useful and portable format, and
it is easy to learn
'''
''':key
The JSON (JavaScript Object Notation) format was originally developed for JavaScript. 
However, it has since become a common format used by many languages, including Python.
'''
# Using json.dump() and json.load()
''':key
Let's write a short program that stores a ser of numbers and another program that reads 
these numbers back into memory. The first program will use json.dump() to store the set
of numbers, and the second program will use json.load()
The json.dump() function takes two arguments: a piece of data to store and a file object
it can use to store the data. Here is how you can use json.dump() to store a list of numbers
'''

import json

numbers = [2, 3, 5, 7, 11, 13]
filename = r'texts_file\numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

with open(filename) as f_obj:
    numbers = json.load(f_obj)
    print(numbers)

# Saving and Reading User-Generated Data
''':key
Saving data with json is useful when you are working with user-generated data, because if you 
don't store your user's information somehow, you will lose it when the program stops running.
'''
# username = input('What is your name...\n')
# filename = f'texts_file\{username}.json'
# with open(filename, 'w') as f_obj:
#     json.dump(username, f_obj)
#     print("We will remember you when you come back, " + username + '!')

# with open(filename) as f_obj:
#     username = json.load(f_obj)
#     print(f"welcome back {username}!")

''':key
We need to combine these two programs into one file. When someone runs remember me to retrieve 
their username from memory if possible; therefore, we will start with a try block that attempts
to recover the username. If the username.json doesn't exist, we will have the except block prompt
for a username and store it in username.json for next time.
'''

import json
# Load the username, if it has not been stored prviously
# Otherwise, prompt for the username and store it.
# filename = f'texts_file\{username}.json'
# try:
#     with open(filename) as f_obj:
#         username = json.load(f_obj)
# except FileNotFoundError:
#     username = input('What is your name? ')
#     with open(filename, 'w') as f_obj:
#         json.dump(username, f_obj)
#         print("We will remember you when you come back! " + username + '!')
# else:
#     print('Welcome back, ' + username + '!')

# Refactoring
''':key

Often, you will come to a point where your code will work, but you will recognize that you 
could improve the code by breaking it up into a series of functions that have specific jobs.
This process is called refactoring, Refactoring makes your code cleaner, easier to understand,
and easier to extend.
We can refactor remember me by moving the bulk of its logic into one or more functions. The 
focus of remember me is on greeting the user, so let's move all of our existing code into a 
function called greet_user():
'''

import json
# username = input("Tell me the username so that I can retrieve the file for you: ")
# def greet_user():
#     '''Great the user by name.'''
#     filename = r'username.json'
#     try:
#         with open(filename) as f_obj:
#             username = json.load(f_obj)
#     except FileNotFoundError:
#         username = input("What is your name? ")
#         with open(filename, 'w') as f_obj:
#             json.dump(username, f_obj)
#             print("We will remember you when you come back, " + username + '!')
#     else:
#         print("Welcome back " + username + '!')
# greet_user()
''':key
Because we are using a function now, we update the comments with a docstring that 
reflects how the program currently works. This file is a little cleaner, but the
function greet_user() is doing more than just greeting the user--it is also retrieving 
a stored username if one exists and prompting for a new username if one does not exist. 
Let's refactor greet_user() so it is not doing so many different tasks. We will start by moving
the code for retrieving a stored username to a separate function. 
'''
import json

def get_stored_username():
    '''Get stored username if available.'''
    filename = r'texts_file\username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    '''Prompt for a new username.'''
    username = input("What is your name? ")
    filename = r'texts_file\username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        return username
def greet_user():
    '''Great the user by name.'''
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + '!')
    else:
        username = get_new_username()
        print("We will remember you when you come back, " + username + '!')
greet_user()

# Summary
''':key
In this Chapter, you learned how to work with files. You learned to read an entire file at once
and read through a file's contents one line at a time. You learned to write to a file and append 
text onto the end of a file. You read about exceptions and how to handle the exceptions you are 
likely to see in your programs. Finally, you laerned how to store Python data structures so you 
can save information your users provide, preventing them from having to start over each time they 
run a program.
In Chap 11 You will learn efficient ways to test your code. This will hep you trust that the code you develop is 
correct, and it will help you identify bugs that are introduced as yo continue to build on the program
you have written.
'''