# Name: Ximu.W
# Date: 11/16/2020
# Subject: Chapter-7 User input and while loop

'''
Most programs are written to solve an end user's problem. To do so,
you usually need to get some information from the user. In this chapter you
will learn how to accept user input so your program can then work with it.
You will also learn how to keep programs running as long as users want them.
So they can enter as much information.
'''

## Writing clear prompts
# name = input('Please enter your name:\n ')
# print("Hello", name.title() + '!')
#
# prompt = 'If you tell us who you are, we can personalize the messages you see.'
# prompt += "\nWhat is your first name? "
#
# name = input(prompt)
# print('Hello', name.title() + '!')

## Use int() to Accept Numerical Input
# age = input("How old are you? ")
# print(age)
# age = int(age)
# print(age >= 18)
# height = input('How tall are you, in centimeters?\n')
# height = int(height)
#
# if height >= 180:
#     print('\nYou are tall enough to ride!')
# else:
#     print('\nYou will be able to ride when you are a little older')
'''
Be sure to convert the input value to a numerical representation first.
'''

## The Modulo Operator
'''
A useful tool for working with numerical information is the modulo operator(%),
which divides one number by another number and returns the remainder:
'''
# print(4 % 3)
# print(5 % 3)
# print(6 % 3)
# print(7 % 3)
# number = input("Enter a number, and I will tell you if it's even or odd: ")
# number = int(number)
#
# if number % 2 == 0:
#     print("\nThe number " + str(number) + ' is even.')
# else:
#     print('\nThe number ' + str(number) + ' is odd.')

## introducing while loop
## The while loop in action
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
print('')
for number in range(1, 6):
    print(number)

## Letting user choose when to quit
# prompt = '\nTell me something, and I will repeat it back to you:'
# prompt += "\nEnter 'quit' to end the program."
# prompt += '\n:'
# message = ''
# while message != 'quit':
#     message = input(prompt)
#
#     if message != 'quit':
#         print(message)

## Using a flag
'''
If there are many different events that can cause the program to stop
running, you can define one variable that determines whether or not the 
entire program is active. This variable called a flag, acts as a signal
to the program. We can write our programs so they run while the flag is set to
True, and stop running when any of several events sets the value of the 
flag to False.
As a result, the while statement needs to check only one condition: Whether
or not the flag is currently True.
'''
# prompt = '\nTell me something, and I will repeat it back to you:'
# prompt += "\nEnter 'quit' to end the program."
# prompt += '\n:'
# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)

## Using break to Exit a Loop
'''
To exit a while loop immediately without running any remaining code in the loop, regardless
of the results of any conditional test, use the break statement. It controls which lines of 
code are executed and which aren't
'''
# prompt = '\nPlease enter the name of a city you have visited:'
# prompt += "\n(Enter 'quit' when you are finished.)"
# prompt += '\n:'
# places = []
# while True:
#     city = input(prompt)
#     places.append(city)
#     if city == '1' or 'quit':
#         places.remove('quit' and '1')
#         break
#     else:
#         print('I\'d love to go to ' + city.title() + '!')
# print(places)

## Using continue in a loop
'''
Rather than breaking out of a loop entirely without executing the rest of its code,
you can use the continue statement to return to the beginning of the loop bsed on the 
result of a conditional test.
'''
print('\n')
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

## Avoiding infinite loops
'''
Every programmer accidentally writes an infinite while loop from time to time, especially when a 
program's loops have subtle exit conditions. Try CTRL-C to stop

To avoid writing infinite loops, test every while loop and make sure the loop stops when you expect it to.
If you want your program to end when the user enters a certain input value, run the program and enter that 
value. Make sure at least one part of the program can make the loop's condition False or cause it to reach 
a break statement.
'''

## Using a while loop with lists and dictionaries
# Moving items from one list to another
# start with users that need to be verified,
# and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# verify each user until there are no more unconfirmed users.
# move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user.title())
    confirmed_users.sort()
# Display all confirmed users.
print('\nThe following users have been confirmed:')
for confirmed_user in confirmed_users:
    print('\t' + confirmed_user)

## Removing all instances of specific values from a list
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
remove_item = 'cat'
count = 0
while remove_item in pets:
    pets.remove(remove_item)
    count += 1
    print(f'We are removing {count} \'cat\' in the list')
print(pets)

## Filling a dictionary with User Input
responses = {}
# Set a flag to indicate that polling is active.
polling_active = True
while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Store the response in the dictionary
    responses[name] = response

    # Find out if anyone else is going to take the poll
    repeat = input("Would you like to let another person respond? (Y/N) ")
    if repeat == 'N':
        break
# Polling is complete. Show the results.
print('\n--- Poll Results ---')
for name, response in responses.items():
    print(name.title(), 'would like to climb', response,'.')
