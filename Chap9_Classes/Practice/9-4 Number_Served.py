# 9-4 Number_Served
class Restaurant():
    '''Set up a class for restaurant.'''
    def __init__(self, name, crusine_type):
        '''Initialize the restaurant class.'''
        self.name = name
        self.crusine_type = crusine_type
        self.number_served = 0

    def describe_restaurant(self):
        '''Display the information of a restaurant.'''
        intro = f'Welcome to {self.name}, We serves {self.crusine_type}.'
        print(intro)

    def open_restaurant(self):
        '''Display a welcome message indicate that it is open.'''
        print('We are open now!')

    def set_number_served(self, number_served):
        '''allow user to set the number of customers that have been served'''
        if self.number_served > 0:
            self.number_served = number_served
            print('We served ' + str(self.number_served) + ' people today.')

    def increment_number_served(self, add_customers):
        '''allow user to increment the number of customers served.'''
        if add_customers >= 0:
            self.number_served += add_customers
            print('We now serve ' + str(self.number_served) + ' person')
        else:
            print('Please add a positive number.')
noma = Restaurant('NOMA', 'new Nordic')
noma.number_served = 4
noma.set_number_served(3)
noma.increment_number_served(-23)

