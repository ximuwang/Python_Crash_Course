# Name: Ximu.W
# Date: 11/09/2020
# Subject: Chapter 5 -- If statement
'''
Programming often involves examining a set of conditions and deciding which action to take based on those conditions.
Python's if statement allows you to examine the current state of a program and respond appropriately to that state.
'''

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# Conditional test
'''
At the heart of every if statement is an expression that can be evaluated as True of False and is called a conditional 
test. Python uses the values True and False to decide whether the code in an if statement should be executed. If a 
conditional test evaluates to True, Python executes the code following the if statement. If the test evaluates to False
Python ignores the code following the if statement
'''

# >>> car = 'bmw'
# >>> car == 'bmw'
# True

# >>> car = 'audi'
# >>> car == 'bmw'
# False

# >>> car = 'Audi'
# >>> car == 'audi'
# False

# >>> car = 'Audi'
# >>> car.lower() == 'audi'
# True
# >>> car
# 'Audi'

# Checking for inequality
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print('Hold the anchovies')

# Numerical Comparisons
# >>> age = 18
# >>> age == 18
# True

answer = 17

if answer != 43:
    print("That is not the correct answer. Please try again!")

# >>> age = 19
# >>> age < 21
# True
# >>> age <= 21
# True
# >>> age > 21
# False
# >>> age >= 21
# False

# Checking Multiple Conditions
# >>> age_0 = 22
# >>> age_1 = 18
# >>> age_0 >= 21 and age_1 >= 21
# False
# >>> age_1 = 22
# >>> age_0 >= 21 and age_1 >= 21
# True

# >>> age_0 = 22
# >>> age_1 = 18
# >>> age_0 >= 21 or age_1 >= 21
# True
# >>> age_0 = 18
# >>> age_0 >= 21 and age_1 >= 21
# False

# Checking whether a value is in a list
requested_toppings = ['mushrooms', 'onions', 'pineapples']
for topping in requested_toppings:
    if topping == 'mushrooms':
        print('True')
    if topping == 'peperoni':
        print('True')
    else:
        print('False')

# >>> requested_toppings = ['mushrooms', 'onions', 'pineapples']
# >>> 'mushrooms' in requested_toppings
# True
# >>> 'pepperoni' in requested_toppings
# False

# Checking whether a value is not in a list
banner_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banner_users:
    print(user.title() + ", you can post a response if you wish.")

# Boolean Expressions
game_active = True
can_edit = False

# if statements
# The simplest kind of if statement has one test and one action
# if conditional_test:
#     do something
age = 19
if age >= 18:
    print('You are old enough to vote!')
    print('Have you registered to vote yet?')

# if-else Statements
age = 17
if age >= 18:
    print('You are old enough to vote!')
    print('Have you registered to vote yet?')
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

# if-elif-else chain
age = 12
if age < 4:
    print("Your admission cost is 0$")
elif age < 18:
    print("Your admission cost is 5$")
else:
    print("Your admission cost is 10$")
# revised code
age = 3
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print(f"Your admission cost is {price}$.")

# Testing multiple conditions
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print('Adding mushrooms')
if 'pepperoni' in requested_toppings:
    print('Adding pepperoni')
if 'extra cheese' in requested_toppings:
    print('Adding extra cheese')

print("\nFinished making your pizza!")

# Using if statements with list
# Checking for special items
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
print(requested_toppings)
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print('Adding ' + requested_topping + '.')
print("\nFinished making your pizza!")

# Checking that a list is not empty
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print('Adding ' + requested_topping + '.')
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
''' 
Python returns True if the list contains at lease one item;
An empty list evaluates to False
'''

# Using multiple lists
available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print('Adding ' + requested_topping + '.')
    else:
        print("Sorry, we don't have " + requested_topping + '.')
print("Finished making pizza!")

# Styling if statement
''' 
use a single space around comparison operators
'''
