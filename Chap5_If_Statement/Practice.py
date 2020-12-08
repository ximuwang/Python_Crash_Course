# Name: Ximu.W
# Date: 11/09/2020
# Subject: Chaper5 -- Try it youself

# 5-1
# result = []
# for i in range(0,10):
#     score = int(input('What is the score you get from the test?\n>'))
#     result.append(score)
#     i += 1
# print(result)
from math import pi
print('is 1 + 1 == 2?', 'I predict\n', 1 + 1 == 2)
pizza = 'Mcdonald\'s'
print('is pizza == "Mcdonald\'s"?', "I predict\n", pizza == "Mcdonald's")
print('Is 10 ** 8 <= 1000000?', 'I predict\n', 10 ** 8 <= 1000000)
print("'ball' in 'basketball'?", 'I predict\n', 'ball' in 'basketball')
print('3.1415927 < pi?', 'I predict\n', 3.1415927 < pi)
print('Is "Python" a "language"?', 'I predict\n', 'Python' == "language")

# 5-2
car = "Mercedez"
print(car.lower() == 'mercedez')
not_in_list = list(range(0,11,2))
print(not_in_list)
for num in range(0,11):
    if num % 2 == 0:
        print(num, ' is EVEN')
    else:
        print(num, "is ODD")
odd_num = list(range(1,10,2))
num = 10
if num not in not_in_list:
    print('That\'s out of range')
else:
    print(num, 'is in the list', not_in_list)

# 5-3
# points = 0
# color = input("Choose a color: \n")
# alien_color = ['green', 'yellow', 'red']
# if color in alien_color:
#     print("You just earned 5 pts")
#     points += 5
# if color == 'blue':
#     print("...")

# 5-4
# if color == 'green':
#     points += 5
# else:
#     points += 10
# print(f'You earned {points} points')

# 5-5
# if color == 'green':
#     points += 5
# if color == "yellow":
#     points += 10
# if color == "red":
#     points += 15
#
#
# print(f'You earned {points} points')

# 5-6
# age = int(input("How old are you?\n"))
# if age < 2:
#     print("You are a baby")
# elif age < 4:
#     print("You are a toddler")
# elif age < 13:
#     print("You are a kid")
# elif age < 20:
#     print("You are a teenager")
# elif age < 65:
#     print("You are an adult")
# else:
#     print("You are an elder")
#
# # 5-7
# favorite_fruits = ['banana', 'orange', 'tangerine', 'watermelon', 'coconut']
# favorite_fruits.append('kiwi')
# for item in favorite_fruits:
#     if item == 'banana':
#         print("Bananas are sweet")
#     if item == 'coconut':
#         print("You like coconut")
#     if item == 'apple':
#         print("You don't like apples")
#     if item == 'honeydew':
#         print("HONEYDEW!")
#     if item == 'kiwi':
#         print("I like kiwis too")

# 5-8
usernames = ['admin', 'ximuwang', 'akima', 'xwang', 'helloworld']
for username in usernames:
    if username == 'admin':
        print("Hello, admin, would you like to see a status report?")
    elif usernames:
        print(f"{username}, welcome to the python generator.")
    else:
        print("Hello dude, thanks for logging in again.")

# 5-9
usernames = []
if usernames:
    if username == 'admin':
        print("Hello, admin, would you like to see a status report?")
    elif usernames:
        print(f"{username}, welcome to the python generator.")
    else:
        print("Hello dude, thanks for logging in again.")
else:
    print("We need some users!")

# 5-10
current_users = ["Wang", 'Zhao', 'Qian', 'Sun', 'Li']
new_users = ["Zhao", 'Li', 'Zhou', 'Wu', 'Zheng']
for new_user in new_users:
    if new_user in current_users:
        print(f'{new_user} already exist, please enter a new one.')
    else:
        print(f"{new_user} is available.")

# 5-11
numbers = list(range(1,10))
for num in numbers:
    if num == 1:
        print(str(num) + 'st')
    elif num == 2:
        print(str(num) + 'nd')
    elif num == 3:
        print(str(num) + 'rd')
    else:
        print(str(num) + 'th')

