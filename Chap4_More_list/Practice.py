# Name: Ximu. W
# Date: 11/09/2020
# Subject: Chap4_More_list -- Try it yourself

# 4-1
pizzas = ['cheese', 'meatlover', 'crispy']
for pizza in pizzas:
    print(f'I like {pizza.title()} pizza\n')
print('I love pizza, pizza loves me')

# 4-2
animals = ['dogs', 'cats', 'parrots']
for animal in animals:
    print(animal)
    print(f'{animal} would make a great company!\n')
print('all of the animals are friends with us'.capitalize())

# 4-3
numbers = [value for value in range(1, 21)]
print(numbers)

# 4-4
# numbers = list(range(1,1000001))
# for value in numbers:
#     print(value)

# 4-5
numbers = [value for value in range(1, 1000001)]

print(max(numbers))
print(min(numbers))
print(sum(numbers))

# 4-6
odd_numbers = [i for i in range(1, 20, 2)]
print(odd_numbers)

# 4-7
numbers = []
for value in range(3, 31):
    if value % 3 == 0:
        numbers.append(value)
print(numbers)

# 4-8
numbers = [i ** 3 for i in range(1, 10)]
print(numbers)
for number in numbers:
    print(number)

# 4-9
print(len(numbers))
numbers = [i ** 3 for i in range(1, 11)]
print(numbers)
print('The first {} cubes are: {}'.format(len(numbers), numbers))

# 4-10
print(numbers)
print('The first three cubes from 1 to 10 is: ')
print(numbers[:3])
print('The middle three cubes from 1 to 10 is: ')
print(numbers[3:6])
print('The last four cubes from the list are: ')
print(numbers[6:])

# 4-11
print(pizzas)
friends_pizza = pizzas[:]
friends_pizza.append('peperoni')
pizzas.append('hawaii')
print('My favorite pizzas are:')
for pizza in pizzas:
    print(pizza.title(), end='\\')

print('\nMy friends favorite pizzas are:')
for friend_favorite in friends_pizza:
    print(friend_favorite.title(), end='|')

# 4-12
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
print('Here are my favorite foods:')
for my_food in my_foods:
    print(my_food.title())
print('\nHere are my friends\'s favorite foods:')
for friend_food in friend_foods:
    print(friend_food.replace('pizza', 'rice'))
print(friend_foods)

# 4-13
print('The orignal menu: ')
foods = ('Burgers', 'Pizza', 'Beer', 'Wine', 'Beef')
for food in foods:
    print(food)
# foods[0] = 'Cheerios'
# print(foods)
print('\nThe revised menu: ')
foods = ('Cheerios', 'Pho', 'Beer', 'Wine', 'Beef')
for food in foods:
    print(food)

# 4-14
# https://www.python.org/dev/peps/pep-0008/
# 4-15