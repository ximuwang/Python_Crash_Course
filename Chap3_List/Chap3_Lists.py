# Name: Ximu.W
# Date: 11/08/2020
# Subject: Chap3_List Lists

# A list is a collection of items in a particular order
# You can make a list that includes the letters of the alphabet, the digits, or the names of all.
# In Python, square bracket([]) indicate a list, and individual elements in the list are separated by commas.

bicycles = ['trek', 'cannondale', 'redline', 'specialized',]
print(bicycles)

# Accessing Elements in a list
print(bicycles[0:3])
print(bicycles[0].title())

# Index Positions Start at 0, Not 1
# You can get any element you want from a list by subtracting one from its position in the list.
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])
bicycles.reverse()
# Reverse the list: Using the “ [::-1] ” list slicing trick to create a reversed copy.
print(bicycles)
print(bicycles[::-1])
print(bicycles)
# Using Individual Values from a list
bicycles.reverse()
message = 'My first bicycles was a ' + bicycles[0].title() + '.'
print(message)
# Changing Elements
motorcycles = ['Honda', 'Yamaha', 'Suzuki']
print(motorcycles)

motorcycles[0] = 'Ducati'
print(motorcycles)
# Adding Elements to a list
motorcycles.append('Honda')
print(motorcycles)
# Inserting Elements into a List
motorcycles = ['Honda', 'Yamaha', 'Suzuki']
motorcycles.insert(0, 'Ducati')
print(motorcycles)
# Removing Elements from a list
del motorcycles[0]
print(motorcycles)
del motorcycles[1]
print(motorcycles)
# Removing an item using the pop() Method
'''
Sometimes you will want to use the value of an item after you remove it from a list. For example,
you might want to get the x and y position of an alien that was just shot down, so you can draw an explosion at the 
position. In a web application, you might want to remove a user from a list of active members and then add that user to a list of 
inactive members
The pop() method removes the last item in a list, but it lets you work with that item after removing it.
The term pop comes from thinking of a list as a stack of items and popping one item off the top of the stack. 
'''
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)   # the last item is stored

motorcycles.append('suzuki')
last_owned = motorcycles.pop()
print('The last motorcycle I owned was a ' + last_owned.title() + '.')
# Popinf items from any Position in a list
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')
print(motorcycles)
'''
If you are unsure whether to use the del statement or the pop() method, here's a simple way to decide: when you want to delete an item from a list
and not use that item in any way, use the del statement; if you want to use an item as you remove it, use the pop() method.
'''

# Removing an item by value
# Sometimes you won't know the position of the value you want to remove from a list. If you only know the value of the item you want to remove, you can use the remove() method

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
# You can also use the remove() method to work with a value that's being removed from a list
motorcycles.insert(3, 'ducati')
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + ' is too expensive for me.')
'''
The remove() method deletes only the first occurrence of the value you specify. If there's a possibility the value appears more than once in the list,
you'll need to use a loop to determine if all occurrences of the value have been removed. 
'''


# sorting a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print('Here is the original list:')
print(cars)
print('\nHere is the sorted list:')
print(sorted(cars))
print('\nHere is the original again:')
print(cars)
print('\nHere is the reversed list:')
b = cars.copy()
b.sort(reverse=True)
print(b)
''' 
Sorting a list alphabetically is a bit more complicated when all the values are not in lowercase. 
There are several ways to interpret capital letters when you are deciding on a sort order, and specifying
the exact order can be more complex than we want to deal with at this time. However, most approaches to sorting
will build directly on what you learned in this section
'''

# Printing a list in reverse order
print(cars)
cars.reverse()
print(cars)
print(len(cars))

# Avoid index errors when working with lists
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles[3])
# IndexError: list index out of range
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[-1])
'''
If an index error occurs and you can't figure out how to resolve it, try printing your list or just printing the length of your list. Your list might look much different
than you thought it did, especially if it has been managed dynamically by your program.
seeing the actual list, or the exact number of items in your list, can help you sort out such logical errors.
'''