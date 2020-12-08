# Name: Ximu. W
# Date: 11/10/2020
# Subject: Chapter6 -- Dictionaries

# 6-1
information = {'first_name': 'ximu', 'last_name': 'wang', 'age': 26, 'city': 'qinhuangdao'}
print(information)
print(information['city'].capitalize())
print(information["last_name"].title())
print(information['age'])

# 6-2
favorite_number = {"ximu": 7,
                   "alex": 3,
                   "aki": 5,
                   "greg": 9,
                   'aaron': 6,
                   }
print(favorite_number['ximu'])
print(favorite_number['aki'])
print(favorite_number['greg'])

# 6-3
glossary = {'string': 'a set of data include text, numbers, and floating points',
            'list': 'represent by "[]" that collects data',
            'dictionaries': 'key-value pairs that stores date',
            'boolean': 'comparison operations that always used in conditional test',
            'variable': 'used to represent string, numbers or anything that can be further used',
            'tuple': 'a data type that stores immutable data',
            'set' : 'a method that is similar to list, but the items are unique',
            '.title()': 'a method that capitalize each first letter in strings',
            'keys': "refers to the stored information before a colon in a dictionary",
            'python': 'a high-level language used in computers',
            'random.seed()': 'often a method in random module that generates the random value within a fixed seed'
                             ' that can be further retrived',
            }
print(f'variable:'.title())
print('\t', glossary['variable'])
print("")
print(f'string:'.title())
print('\t', glossary['string'], "\n")
print(f"list:".title())
print('\t', glossary['list'])

# 6-4
for name, value in glossary.items():
    print(name.title(), "means: " + value.capitalize())

# 6-5
major_rivers = {'nile': 'Egypt',
                'euphrates': 'syria',
                'yellow river': 'china',
                'tigris': 'iraq',
                'mississipi': 'united states',
                }
for river, country in major_rivers.items():
    print('The', river.title(), 'river runs through', country.title())

for river in major_rivers.keys():
    print(river.title())
print('')
for country in major_rivers.values():
    print(country.upper())
# 6-6
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
names = ['jen', 'sarah', 'alex', 'aaron', 'kobe']
for name in names:
    if name in favorite_languages.keys():
        print(f'Hi, {name.title()}, I see your favorite language is {favorite_languages[name].title()}!')
        # print('Hi ' + name.title() + ', I see your favorite programming language is: ' +
        #       favorite_languages[name].title())
    else:
        print('Hi', name.title(), 'Please take the poll.')

# 6-7
people = []
information = {'first_name': 'ximu',
               'last_name': 'wang',
               'gender': 'male',
               'age': 26,
               'city': 'qinhuangdao'
               }
people.append(information)
information = {'first_name': 'aki',
               'last_name': 'ma',
               'age': 26,
               'gender': 'female',
               'city': 'chuzhou',
                }
people.append(information)
information = {'first_name': 'steve',
               'last_name': 'jobs',
               'gender' : 'male',
               'age': 56,
               'city': 'san francisco',
               }
people.append(information)
print(people)
for information in people:
    full_name = information['first_name'].title() + ' ' + information['last_name'].title()
    age = str(information['age'])
    city = information['city']
    if information['gender'] == 'male':
        print(full_name + ' is ' + age + ', and he lives in {}'.format(information['city'].title()))
    else:
        print(full_name + ' is ' + age + ', and she lives in {}'.format(information['city'].title()))

# 6-8
pets = []
pet = {'name': 'coke',
        'kind': 'maltipuddle',
        'owner': 'aki',
        'age': '7',
        }
pets.append(pet)
pet = {'name': 'hedwig',
          'kind': 'owl',
          'owner': 'harry potter',
          'age': '7',
          }
pets.append(pet)
pet = {'name': 'rocco',
         'kind': 'pitbull',
         'owner': 'xuzhe',
         'age': '4',
         }
pets.append(pet)
for pet in pets:
    name = pet['name'].title()
    kind = pet['kind'].title()
    owner = pet['owner']
    age = pet['age']
    message = f'{name} is a {kind} owned by {owner}. It is {age} years old.'
    print(message)

# 6-9
favorite_places = {
    'aki': ['island', 'key west', 'It is an island in the Straits of Florida, within the U.S state of Florida'],
    'ximu': ['active volcano', 'Mountain Fuji', 'It located on the island of Honshu, it is the highest mountain in Japan'],
    'katrina': ['mountain', 'himalaya', 'It spread across five countries: Bhutan, China, India, Nepal, and Pakistan']
}

for key, values in favorite_places.items():
    print('\n' + key.title() + ' likes the following places:')
    for place in values:
        print('-\t' + place.title())

# 6-10
favorite_numbers = {"ximu": [7, 11,],
                   "alex": [3, 0],
                   "aki": [17, 15],
                   "greg": [9, 8],
                   'aaron': [6,1],
                   }
for name, values in favorite_numbers.items():
    print('\n' + name.title() + ' \'s favorite numbers are:')
    for value in values:
        print('-' + " " + str(value))

# 6-11
cities = {
    '秦皇岛': {'名称起源': '秦始皇出巡到此得名',
            '面积': '7803平方公里',
            '人口': '307.32万',
            'foods': ['炸肉', '海鲜']
            },
    '全椒': {'名称起源': '高阳氏在椒陵山建立古椒国',
           '面积': '1572平方千米',
           '人口': '383885',
           'foods': ['蚌全面馆', '管坝牛肉']
           },
    '西雅图': {'名称起源': 'in honor of Chief Si\'ahl of the local Duwamish and Suquamish tribes',
            '面积': '369平方公里',
            '人口': '753675',
            'foods': ['pho', 'starbucks']}
}
for city, facts in cities.items():
    print('\n' + city.title())
    origin = facts['名称起源']
    print("-It's name originated " + origin)
    area = facts['面积']
    print(f'It has an area about {area}')
    population = facts['人口']
    print(f'and it has {population} population.')
    print('You must try the following foods!')

    foods = facts['foods']
    for food in foods:
        print(food)
