# Name: Ximu.W
# Date: 11/17/2020
# Subject: Chapter7 Practice

# 7-1
# prompt = 'What kind of rental car would you want? '
# car_kind = input(prompt).title()
# print('Let me see if I can find a {}'.format(car_kind))
#
# # 7-2
# people = input("\nHow many people are in your dinner group? ")
# people = int(people)
# if people > 8:
#     print("Would you mind wait for a table?")
# else:
#     print("The table is ready.")

# 7-3
# prompt = '\nWould you like to enter a number? '
# number = input(prompt)
# number = int(number)
# if number % 10 == 0:
#     print(number, "It is a multiple of 10")
# else:
#     print(number, "is not a multiple of 10")

# 7-4
toppings = '\nWhat kind of toppings would you want? \n'
toppings += 'Enter "quit" if you are done: '
active = True
while active:
    topping = input('\n' + toppings)
    if topping == 'quit':
        active = False
    else:
        print(f"We are adding {topping} to your pizza.")

# 7-5
prompt = "\nHow old are you? "
active = True
while active:
    age = input(prompt)
    if age == 'quit':
        active = False
        continue
    age = int(age)
    if age < 3:
        print("The ticket if free for you!")
    elif age < 13:
        print("The ticket for " + str(age) + ' is $10.')
    else:
        print(f"cost for age {age} is $15.")


# 7-6
# 7-7
# while 1:
#     print('...')
#     print('....')

# 7-8 Deli
sandwich_order = ['Simple Samme', 'Happy Italian', 'Triple Trouble', 'Rancho Californian', 'Easy Breezy Capreezy', 'The Happy Belly', 'Willy\'s B.L.A.T']
finished_sandwiches = []
while sandwich_order:
    sandwich = sandwich_order.pop(0)
    sandwich = sandwich.upper()
    finished_sandwiches.append(sandwich)
    print(f'Adding {sandwich}...To the menu')
print('\n------------------Here is the full menu------------------')
for sandwich in finished_sandwiches:
    print(sandwich)

# 7-9 No Pastrami
sandwich_order = ['Simple Samme', 'Pastrami', 'Happy Italian', 'Pastrami', 'Triple Trouble', 'Rancho Californian', 'Pastrami', 'Pastrami', 'Easy Breezy Capreezy', 'Pastrami', 'The Happy Belly', 'Willy\'s B.L.A.T']
finished_sandwiches = []
out_of_order = 'Pastrami'
while sandwich_order:
    sandwich = sandwich_order.pop(0)
    if sandwich == 'Pastrami':
        continue
    sandwich = sandwich.upper()
    finished_sandwiches.append(sandwich)
print(finished_sandwiches)

# 7-10 Dream Vacation
dream_vacation = {}
active = True
while active:
    # prompt name and places for dream vacation
    name = input('\nWhat is your name: ')
    place = input("Where would you like to go on vacation: ")
    # stores the name and places for dream vacation
    dream_vacation[name] = place
    repeat = input("Would you like to ask another person? \nY/N?\n")
    if repeat == 'N':
        active = False
# result of dream_vacation
for name, place in dream_vacation.items():
    print(name.title(), "would like to go to", place)
print(dream_vacation)