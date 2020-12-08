# Name: Ximu.W
# Date: 11/27/2020
# Subject: Chapter 9 -- Classes second part

def cut_off():
    print('-' * 40)
cut_off()

# Importing Class
'''
As you add more functionality to your classes, your files can get long, even 
when you use inheritance properly. In keeping with the overall philosophy 
of Python, you’ll want to keep your files as uncluttered as possible. To help, 
Python lets you store classes in modules and then import the classes you 
need into your main program.
'''
# Importing a single class
'''
Let’s create a module containing just the Car class. This brings up a subtle 
naming issue: we already have a file named car.py in this chapter, but this 
module should be named car.py because it contains code representing a car. 
We’ll resolve this naming issue by storing the Car class in a module named 
car.py, replacing the car.py file we were previously using. From now on, any 
program that uses this module will need a more specific filename, such as 
my_car.py. Here’s car.py with just the code from the class Car:
'''

'''A class that can be used to represent a car.'''
# class Car:
#     """A simple attempt to represent a car."""
#
#     def __init__(self, make, model, year):
#         """Initialize attributes to describe a car."""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name."""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
#
#     def read_odometer(self):
#         """Print a statement showing the car's mileage."""
#         print(f"This car has {self.odometer_reading} miles on it.")
#
#     def update_odometer(self, mileage):
#         """
#         Set the odometer reading to the given value.
#         Reject the change if it attempts to roll the odometer back.
#         """
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
#
#     def increment_odometer(self, miles):
#         """Add the given amount to the odometer reading."""
#         self.odometer_reading += miles
#
#
# class Battery:
#     """A simple attempt to model a battery for an electric car."""
#
#     def __init__(self, battery_size=75):
#         """Initialize the battery's attributes."""
#         self.battery_size = battery_size
#
#     def describe_battery(self):
#         """Print a statement describing the battery size."""
#         print(f"This car has a {self.battery_size}-kWh battery.")
#
#     def get_range(self):
#         """Print a statement about the range this battery provides."""
#         if self.battery_size == 75:
#             range = 260
#         elif self.battery_size == 100:
#             range = 315
#
#         print(f"This car can go about {range} miles on a full charge.")
#
#
# class ElectricCar(Car):
#     """Models aspects of a car, specific to electric vehicles."""
#
#     def __init__(self, make, model, year):
#         """
#         Initialize attributes of the parent class.
#         Then initialize attributes specific to an electric car.
#         """
#         super().__init__(make, model, year)
#         self.battery = Battery()

from Module.my_car import Car
my_new_car = Car('Volkswagon', 'Golf-R', 2021)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 29
my_new_car.read_odometer()

'''
Importing classes is an effective way to program. Picture how long this file 
would be if the entire Car class were included. When you instead move the class 
to a module and import the module, you still get all the same functionality, but 
you keep your main program file clean and easy to read. You also store most of the logic
in separate files; once your classes work as you want them to, you can leave those files 
alone and focus on the higher_level logic of your main program.
'''

# Storing Multiple Classes in a Module
'''
You can store as many classes as you need in a single module, although each class in a module 
should be related somehow. The classes Battery and ElectricCar both help represent cars,
so let's add them to the module my_car.py:
'''
from Module.my_car import ElectricCar

my_tesla = ElectricCar('Tesla', 'Model S', 2020)
info = my_tesla.get_descriptive_name()
print(info)
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# Importing Multiple Classes from a Module
'''
You can import as many classes as you need into a program file. If we want to make a regular car and
an electric car in the same file, we need to import both classes, Car and ElectricCar
'''
from Module.my_car import Car, ElectricCar

my_beetle = Car('volkswagon', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'model X', 2020)
print(my_tesla.get_descriptive_name())

# Importing an Entire Module
'''
You can also import an entire module and then access the classes you need using dot notation. This approach is 
simple and results in code that is easy to read. Because every call that creates an instance 
of a class includes the module name, you won't have naming conflicts with any names used in the 
current file.
'''
import Module.my_car
my_beetle = Module.my_car.Car('Volkswagon', 'beetle', 2014)
print(my_beetle.get_descriptive_name())
my_tesla = Module.my_car.ElectricCar('Tesla', 'model z', 2034)
print(my_tesla.get_descriptive_name())

# Importing all Classes from a Module
'''
You can import every class from a module using the following syntax:
from module_name import *

This method is not recommended fro two reasons. First it's helpful to be able to read the import 
statements at the top of a file and get a clear sense of which classes a program uses. With this 
approach it's unclear which classes a program uses. With this approach it's unclear which classes
you are using from the module. This approach can also lead to confusion with names in the file. If 
you accidentally import a class with the same name as something else in your program file, you can 
create errors that are hard to diagnose. I show this here because even though it's not a 
recommended approach, you are likely to see it in other people's code.

If you need to import many classes from a module, you are better off importing the entire module and 
using the module_name.class_name syntax. You won't see all the classes used at the top of the file, but 
you will see clearly where the module is used in the program. You will also avoid the potential naming
conflicts that can arise when you import every class in a module. 
'''

# Importing a Module into a Module.
'''
Sometimes you will want to spread out your classes over several modules to keep any one file from growing 
too large and avoid storing unrelated classes in the same module. When you store your classes in several 
modules, you may find that a class in one module depends on a class inn another module. When this happens
you can import the required class into the first module.
For example, let's store the Car class in one module and the ElectricCar and Battery classes in a separate 
module. We will make a new module called my_electric_car.py--replacing the electric_car.py we created earlier-
and copy just the Battery and ElectricCar classes into this file:
'''
# Find your own workflow
'''
As you can see, Python gives you many options for how to structure code in a large project. It is important to 
know all these possibilities so you can determine the best ways to organize your projects as well as understand 
other people's projects.
When you are starting out, keep your code structure simple. Try doing everything in one file and moving your classes
to separate modules once everything is working. If you like how modules and files interact, try storing your classes
in modules when you start a project. Find an approach that lets you write code that works, and go from there.
'''

cut_off()
# The Python Standard Library
'''
The Python standard library is a set of modules included with every Python installation. Now that you have a basic
understanding of how classes work, you can start to use modules like these that other programmers have written.
You can use any function or class in the standard library by including a simple import statement at the top of your
file. Let's look at one class, OrderedDict, from the module collections.

Dictionaries allow you to connect pieces of information, but they don't keep track of the order in which you add 
key-value pairs. If you are creating a dictionary and want to keep track of the order in which key-value pairs are added,
you can use the OrderedDict class from the collections module. Instances of the OrderedDict class behave almost 
exactly like dictionaries except they keep track of the order in which key-value pairs are added.
Let's revisit the favorite_languages.py example from Chapter 6. This time we will keep track of the order in which 
people respond to the poll:
'''

from collections import OrderedDict
favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    msg = f'{name.title()}\'s favorite language is {language.title()}.'
    print(msg)

# Styling Classes
'''
A few styling issues related to classes are worth clarifying, especially as your programs become
more complicated.
Class names should be written in CamelCaps. To do this, capitalize the first letter of each word in 
the name, and don't use underscores. Instance and module names should be written in lowercase with 
underscores between words.
    Every class should have a Docstring immediately following the class definition.
The docstring should be a brief description of what the class does, and you should 
follow the same formatting conventions you used for writing docstrings in functions. Each module should
also have a docstring describing what the classes in a module can be used for. 
    You can use blank lines to organized code, but don't use them excessively. Within a class you can 
use two blank lines to separate classes. 
    If you need to import a module from the standard library and a module that you wrote, place the import 
statement for the standard library module first. Then add a blank line and the import statement for the 
module you wrote. In programs with multiple import statements, this convention makes it easier to see 
where the different modules used in the program come from. 
'''

# Summary
'''
    In this chapter you learned how to write your own classes. You learned how to store information in a class 
using attributes and how to write methods that give your classes the behavior they need. You learned to write 
__init__() methods that create instances from your classes with exactly the attributes you want. You saw how to
modify the attributes of an instance directly and through methods. You learned that inheritance can simplify the 
creation of classes that are related to each other, and you learned to use instances of one class as attributes in 
another class to keep each class simple.
    You saw how storing classes in modules and importing classes you need into the files where they will be 
used can keep your projects organized. You started learning about the Python standard library, and you saw an example 
based on the OrderedDict class from the collections module. Finally, you learned to style your class using Python 
conventions.
'''