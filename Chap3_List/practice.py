# Name: Ximu.W
# Date: 11/08/2020
# Subject: Try it yourself

# 3-1
# friends = []
# for i in range(0, 5):
#     names = input('Enter the names: ')
#     friends.append(names)
#     i += 1
# print(friends)
#
# for items in friends:
#     print(items)

# 3-2
# message1 = friends[0] + ' is the most beautiful thing in the world'
# print(message1)
# print(type(message1))
# message2 = 'Hello ' +  friends[1]
# print(message2)
# message3 = friends[2] + ' ' + 'Give my MONEY back!'
# print(message3)
# message4 = 'Gym on Saturday at 7pm' + ' ' + friends[3]
# print(message4)
# message5 = 'Hands up!', friends[4]
# print(message5)
# print(type(message5))

# 3-3
# list = []
#
# a = input('What is your favorite car?\n: ')
# b = input('What is the brand of the car you are driving?\n: ')
# c = input('What is your first car?\n: ')
# list.append(a)
# list.append(b)
# list.append(c)
# print(list)
#
# sentence_1 = 'I would like to have a {} in the future'.format(list[0])
# print(sentence_1)
# sentence_2 = "My current transpotation method is " + list[1]
# print(sentence_2)
# sentence_3 = 'I drive' + ' ' + list[2] + 'when I was in high school'
# print(sentence_3)

# 3-4
# guest = []
# guest.append('Larry')
# guest.append('Aaron')
# guest.append('Fred')
# guest.append('Lamelo')
# print(guest)
# message = 'Would you like to come to dinner?'
# print(message + ' ' + guest[0])
# print(message + ' ' + guest[1])
# print(message + ' ' + guest[2])
# print(message + ' ' + guest[3])
#
#
# # 3-5
# absence = 'Larry'
# guest.remove(absence)
# print(absence + ' cannot come to dinner tonight.')
# guest.insert(0, 'Aki')
# print(message + ' ' + guest[0])
# print(message + ' ' + guest[1])
# print(message + ' ' + guest[2])
# print(message + ' ' + guest[3])
#
# # 3-6
# guest.insert(0, "alex")
# guest.insert(2, 'greg')
# guest.append('branden')
# guest[6].title()
# print(guest)
#
# # 3-7
# print('Deeply sorry to say that there are only two spot to sit around the table.')
# print(len(guest))
# a = guest.pop()
# print('sorry', a)
# b = guest.pop(4)
# print('sorry', b)
# c = guest.pop(2)
# print('sorry', c)
# d = guest.pop(1)
# print('sorry', d)
# e = guest.pop()
# print('sorry', e)
# print(guest)
#
# print(guest, 'are still in the table')
# del guest[1], guest[0]
# print(guest)

# 3-8
# locations = ['Seattle', 'Japan', 'Tibet', 'Antarctica', 'South Africa']
# print(locations)
# print(sorted(locations))
# print(locations)
# print(sorted(locations, reverse=True))
# print(locations)
# locations.reverse()
# print(locations)
# locations.reverse()
# print(locations)
# locations.sort()
# print(locations)
# locations.sort(reverse=True)
# print(locations)
#
# # 3-9
# print(len(locations))
# print('There are {} places that I want to travel in the next few years'.format(len(locations)))

# 3-10
foods = ['Omelet']
print(foods)
foods.append('Milk')
foods.append('Steak')
foods.append('Pizza')
foods.append('Burgers')
print(foods)
a = sorted(foods)
print(a)
b = sorted(foods, reverse=True)
print(b)
print(foods)
breakfast = 'I would like to have ' + foods[0] + ' for breakfast'
print(breakfast)
in_stomach = 'Omelet'
foods.remove(in_stomach)
print(foods)
lunch = foods.pop()
print('I had ' + lunch + ' for lunch' )
print(foods)
foods.sort()
print(foods)

# 3-11
foods.append(lunch)
foods.append(in_stomach)
print(foods)
foods.insert(5, 'Ham')
print(foods[5])