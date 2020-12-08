# 9-9 Battery Upgrade
class Car():
    '''A simple attempt to represent a car'''
    def __init__(self, make, model, year):
        '''Initialize attributes to describe a car.'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        '''Return a neatly formatted descriptive name.'''
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model.title()
        return long_name

    def read_odometer(self):
        '''Print a statement showing the car's mileage'''
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')

    def update_odometer(self, mileage):
        '''
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        '''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You can\'t roll back an odometer!')

    def increment_odometer(self, miles):
        '''Add the given amount to the odometer reading.'''
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print('You can\'t put negative values in it.')

class ElectricCar(Car):   # --eCar.1
    '''Represent aspects of a car, specific to electric vehicles.'''
    def __init__(self, make, model, year):
        '''
        Initialize attributes of the parent class
        Then initialize attributes specific to an electric car.
        '''
        super().__init__(make, model, year)     # --eCar.1
        self.battery_size = 70      # --eCar.2
        self.battery = Battery()    # --eCar.4

    def describe_battery(self):     # --eCar.2
        '''Print a statement describing the battery size.'''
        print("This car has a " + str(self.battery_size) + '-kwh battery.')

    def ElectricCar(Car):   # --eCar.3
        def fill_gas_tank():
            '''Electric cars don't have a gas tank.'''
            print("This car doesn't need a gas tank!")

class Battery():    #eCar.4
    '''A simple attempt to model a battery for an electric car.'''

    def __init__(self, battery_size=70):
        '''Initializing the battery's attributes.'''
        self.battery_size = battery_size

    def describe_battery(self):
        '''Print a statement describing the battery size.'''
        print("This car has a " + str(self.battery_size) + '-kWh battery.')

    def get_range(self):
        '''Print a statement about the range this battery provides.'''
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = 'This car can go approximately ' +str(range)
        message += ' miles on a full charge.'
        print(message)

    def upgrade_battery(self):
        if self.battery_size == 70:
            self.battery_size = 85
            print('Upgrade battery size to 85 kWh')
        else:
            print("The battery is already upgraded.")

my_tesla = ElectricCar('TESLA', 'Model S', 2020)
my_tesla.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
upgraded_battery = my_tesla.battery.battery_size
print(f"\nNow the battery has a size of: {upgraded_battery}")
my_tesla.battery.get_range()
