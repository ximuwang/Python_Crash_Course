# 9-1 Restaurant
class Restaurant():
    '''A class representing a restaurant'''
    def __init__(self, name, cuisine_type):
        '''Initialize the restaurant'''
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        '''Display a summary of the restaurant'''
        print(f"Welcome to {self.name}!")
        print(f"We have the following cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        '''Display a message indicates that the restaurant is open.'''
        print("We are open now!")

a_plus = Restaurant('A_Plus', 'Chinese Food')
a_plus.describe_restaurant()
a_plus.open_restaurant()

