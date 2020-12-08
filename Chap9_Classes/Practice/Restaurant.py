# A module named restaurant
class Restaurant():
    '''A class representing a restaurant'''
    def __init__(self, name, cuisine_type):
        '''Initialize the restaurant'''
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        '''Display a summary of the restaurant'''
        print(f"Welcome to {self.name}!")
        print(f"We have the following cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        '''Display a message indicates that the restaurant is open.'''
        print("\nWe are open now!")

    def set_number_served(self, number_served):
        '''allow user to set the number of customers that have been served'''
        if self.number_served >= 0:
            self.number_served = number_served
            print('We served ' + str(self.number_served) + ' people today.')

    def increment_number_served(self, add_customers):
        '''allow user to increment the number of customers served.'''
        if add_customers >= 0:
            self.number_served += add_customers
            print('We now serve ' + str(self.number_served) + ' person')
        else:
            print('Please add a positive number.')
            
