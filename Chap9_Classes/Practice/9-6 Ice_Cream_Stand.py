#9-6 Ice Cream Stand

'''Import class Restaurant from the Restaurant module'''
from Restaurant import Restaurant

class IceCreamStand(Restaurant):
    '''Represent aspect of a restaurant, specifically an IceCreamStand'''
    def __init__(self, name, cuisine_type='ice_cream'):
        '''
        Initialize the attributes from a parent class Restaurant
        '''
        super().__init__(name, cuisine_type)
        self.flavors = []

    def display_flavors(self):
        print("We have the following flavors: ")
        for self.flavor in self.flavors:
            print(f"\t{self.flavor}")

big_one = IceCreamStand('The Big One')
big_one.flavors = ["Vanilla", "Chocolate", "Watermelon", "Lavendor"]
big_one.describe_restaurant()
big_one.display_flavors()
