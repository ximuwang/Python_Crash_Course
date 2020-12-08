# Name: Ximu. W
# Date: 11/10/2020
# Subject: Chaper 6 -- Dictionaries
'''
In this chapter you'll learn how to use Python's dictionaries, which allow you to
connect pieces of related information. You will learn how to access the information
once it's in a dictionary and how to modify that information. Because dictionaries can
store an almost limitless amount of information, I will show you how to loop through the
data in a dictionary. Additionally, you will learn to nest dictionaries inside lists,
lists inside dictionaries, and even dictionaries inside other dictionaries.
'''

# a simple dictionaries
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# working with dictionaries: key-value pairs
''' 
A dictionary in Python is a collection of key-value pairs. Each key is connected to a value,
and you can use the key to access the value associated with that key.
A key value can be a number, a string, a list, or even another dictionary.
Dictionary is wrapped in {} with a series of key-value pairs inside the braces.
'''
#alien_0 = {'color': 'blue'}
# accesing values in a dictionary
print(alien_0['color'])
print(alien_0)
new_points = alien_0["points"]
print("You just earned {} points!".format(new_points))

# Adding new Key-Value pairs
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
# Starting with an empty dictionary
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
# Modifying Values in a Dictionary
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f'The alien color now is {alien_0["color"]}.')
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3
# the new position is the old position plus the increment.
alien_0['x_position'] = alien_0["x_position"] + x_increment
print("New x-position: " + str(alien_0['x_position']))
alien_0['speed'] = 'fast'
print(alien_0['x_position'])
print(alien_0)
# removing key_value pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)
# a dictionary of similar objects
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print(favorite_languages)
print("Sarah's favorite language is " + favorite_languages['sarah'].title() + '.')
for name, language in favorite_languages.items():
    print('\nName: ', name.title())
    print('Favorite language: ', language.title())
    print(name.title() + "'s favorite language is " + language.title() + '.')
# looping through a dictionary
# looping through all key-value pairs
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)
print(favorite_languages)
for language in favorite_languages.values():
    print(language.title())
for name in favorite_languages.keys():
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print("\tHi " + name.title() + ", I see your favorite language is " +
              favorite_languages[name].title() + '!')
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# looping through a dictionary's keys in order
for name in sorted(favorite_languages.keys()):
    print(name.title() + ', thank you for taking the poll')

# looping through all values in a dictionary
print("The following languages have been mentioned: ")
for language in favorite_languages.values():
    print(language.title())
'''
This approach pulls all the values from the dictionary without checking for repeats. That might work fine with a 
small number of values, but not so efficient with a large number of respondents.
To see each language chosen without repetition, we can use a set.
A set is similar to a list except that each item in the set must be unique:
'''
print('')
for language in set(favorite_languages.values()):
    print(language.title())

# A list of Dictionaries
''' 
Sometimes you'll want to store a set of dictionaries in a list or a list of items as a value
in a dictionary. This is called nesting
'''

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
print(aliens)
# we pack each of these dictionaries into a list called aliens, and loop
# through the list and print out each alien
for alien in aliens:
    print(alien)
    print(alien['color'].title())
# a more realistic example would involve more than three aliens with code that automatically generates
# each alien. In the following example we use range() to create a fleet of 30 aliens:

# Make an empty list for storing aliens:
aliens = []
# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
# Show the first 5 aliens:
for alien in aliens[:5]:
    print(alien)
print('...')
# show how many aliens have been created.
print('Total number of aliens: ' + str(len(aliens)))
'''
This example begins with an empty list to hold all of the aliens that will be created.
At range() returns a set of numbers, which just tells Python how many times we want the loop to repeat. Each
time the loop turns we create a new alien and then append each new alien to the list aliens. We 
use a slice to print the first five aliens, and then we print the length of the list to prove we've actually
generated the full fleet of 30 aliens:
'''
# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
# Change the first 3 aliens to a different set of values
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
# Show the first 5 aliens:
for alien in aliens[0:5]:
    print(alien)
print('...')

# A list in a Dictionary
# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }
# Summarize the order
print("You ordered a " + pizza['crust'] + '-crust pizza ' +
      "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

favorite_languages = {'jen': ['python', 'ruby'],
                      'sarah': ['c'],
                      'edward': ['ruby', 'go'],
                      'phil': ['python', 'haskell'],
                      }
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print('\t' + language.title())

# A dictionary in a dictionary
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())

