# 9-14 Dice
from random import randint

class Die():
    '''Make a class Die, represent a die, which can be rolled.'''
    def __init__(self, sides=6):
        '''Initialize the Die'''
        self.sides = sides

    def roll_die(self):
        '''Return a number between 1 and 6'''
        output = randint(1, self.sides)
        return output

d6 = Die()
result = []
for i in range(10):
    result.append(d6.roll_die())
print('10 rolls of 6-side dice: ')
print(result)

result = []
d10 = Die(10)
for i in range(20):
    result.append(d10.roll_die())
print('\n20 rolls of 10 sides dice: ')
print(result)
