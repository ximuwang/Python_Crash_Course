# Name: Ximu.W
# Date: 11/24/2020
# Subject: Chapter 9 -- Classes first part

'''
Object-oriented programming is one of the most effective approaches to writing
software. In object-oriented programming you write classes that represent real-world
things and situations, and you create objects based on these classes. When you write
a class, you define the general behavior that a whole category of objects can have.

When you create individual objects from the class, each object is automatically equipped
with the general behavior; you can then give each object whatever unique traits you desire.
You will be amazed how well real-world situations can be modeled with object-oriented
programming.

Making an object from a class is called instantiation, and you work with instances of a class.
In this chapter, you will write classes and create instances of those classes. You will specify
the kind of information that can be stored in instances, and you will define actions that
can be taken with these instances. You will also write classes that extend the functionality of
existing classes, so similar classes can share code efficiently. You will store your classes in modules
and import classes written by other programmers into your own program files.

Understanding object-oriented programming will help you see the world as a programmer does. It will
help you really know your code, not just what is happening line by line, but also the bigger concepts
behind it. Knowing the logic behind classes will train you to think logically so you can write programs
that effectively address almost any problem you encounter.

Classes also make life easier for you and the other programmers you will need to work with as you
take on increasingly complex challenges. When you and other programmers write code based on the same kind
of logic, you will be able to understand each other's work. Your programs will make sense to many collaborators,
allowing everyone to accomplish more.
'''
def cut_off():
    print('-' * 40)
cut_off()
# Creating and using a class
'''
You can model almost anything using classes. Let's start by writing a simple class, Dog, that represents a dog-
not one dog in particular, but any dog. What do we know about most pet dogs? Well, they all have a name and age.
We also know that most dogs sit and roll over. Those two pieces of information and those two behaviors will go in
our dog class because they are common to most dogs. This class will tell Python how to make an object representing 
a dog. After our class is written, we will use it to make individual instances, each of which represents one specific
dog.
'''
# Creating the dog class
'''
Each instance created from the dog class will store a name and an age, and we will give each dog the ability to 
sit() and roll_over()
'''
class Dog():
    '''A simple attempt to model a dog.'''

    def __init__(self, name, age):
        '''Initialize name and age attributes.'''
        self.name = name
        self.age = age

    def sit(self):
        '''Simulate a dog sitting in response to a command.'''
        print(self.name.title() + ' is now sitting.')

    def roll_over(self):
        '''Simulate rolling over in response to a command.'''
        print(self.name.title() + ' rolled over!')
# The __init__() Method
'''
A function that's part of a class is a method. Everything you learned about functions applies to methods
as well; the only practical difference for now is the way we'll call methods. The __init__() method is a 
special method Python runs automatically whenever we create a new instance based on the Dog class. This 
method has two leading underscores and two trailing underscores, a convention that helps prevent Python's 
default method names from conflicting with your method names.

We define the __init__() method to have three parameters: self, name, and age. The self parameter is required
in the method definition, and it must come first before the other parameters. It must be included in the definition 
because when Python calls this __init__() method later (to create an instance of Dog), the method call will automatically 
passes self, which is a reference to the instance itself; It gives the individual instance access to the attributes 
and methods in the class. When we make an instance of Dog, Python will call the __init__() method from the dog class. 
We will pass Dog() a name and an age as arguments; self is passed automatically, so we don't need to pass it. Whenever
we want to make an instance from the Dog class, we will provide values for only the last two parameters, name and age.

The two variables defined each have the prefix self. Any variable prefixed with self is available to every method in the 
class, and we will also be able to access these variables through any instance created from the class. self.name = name
takes the value stored in the parameter name and stores it in the variable name, which is then attached to the instance 
being created. The same process happens with self.age = age. Variables that are accessible through instances like this 
are called attributes.

The Dog class has two other methods defined: sit() and roll_over(). Because these methods don't need additional 
information like a name or age, we just define them to have one parameter, self. The instances we create later will 
have access to these methods. In other words, they will be able to sit and roll over. For now, sit() and roll_over() 
don't do much. They simply print a message saying the dog is sitting or rolling over. But the concept can be extended to 
realistic situations: if this class were part of an actual computer game, these methods would contain code to make an 
animated dog sit and roll over. If this class was written to control a robot, these methods would direct movements that 
cause a dog robot to sit and roll over.
'''
# Making an instance from a class
my_dog = Dog('Willie', 6)
print('My dog\'s name is ' + my_dog.name.title() + '.')
print('My dog is ' + str(my_dog.age) + ' years old.')
my_dog.roll_over()
my_dog.sit()

# Accessing Attributes
'''
To access the attributes of an instance, you use dot notation. Dot
notation is used often in Python. This syntax demonstrates how Python 
finds an attribute's value. 
'''

# Calling Methods
'''
After we create an instance from the class Dog. We can use dot notation
to call any method defined in Dog.
'''
my_dog = Dog('willie', 6)
my_dog.sit()
my_dog.roll_over()
# Creating Multiple Instance
'''
You can create as many instances from a class as you need. Let's create a 
second dog called your_dog
'''
my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)
print('\nYour dog\'s name is ' + your_dog.name.title() + '.')
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()


cut_off()
# Working with Classes and Instances
''' 
You can use classes to represent many real-world situations.
Once you write a class, You will spend most of your time working with instances
created from that class. One of the first tasks you will want to do is 
modify the attributes associated with a particular instance. You can modify the 
attributes of an instance directly or write methods that update attributes in specific
ways.
'''

# The car class
class Car():
    '''A simple attempt to represent a car'''
    def __init__(self, make, model, year):      # (car.1)
        '''Initialize attributes to describe a car.'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # Car.2

    def get_descriptive_name(self):
        '''Return a neatly formatted descriptive name.'''
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model.title()
        return long_name

    def read_odometer(self):
        '''Print a statement showing the car's mileage'''
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')

    def update_odometer(self, mileage):     # Car.3
        '''
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        '''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You can\'t roll back an odometer!')

    def increment_odometer(self, miles):    # refers to car.4
        '''Add the given amount to the odometer reading.'''
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print('You can\'t put negative values in it.')


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

# Setting a Default Value for an Attribute --Car.1
'''
Every attribute in a class needs an initial value, even if that value is 0 or an 
empty string. In some cases, such as when setting a default value, it makes sense 
to specify this initial value in the body of the __init__ method;
if you do this for an attribute, you don't have to include a parameter for that attribute.
'''
my_new_car.read_odometer()

# Modifying an attribute's value directly --Car.2
''' 
The simplest way to modify the value of an attribute is to access the attribute directly 
through an instance. Here we set the odometer reading to 23 directly.
'''
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# Modifying an attribute's value through a method --Car.3
''' 
It can be helpful to have methods that update certain attributes for you. 
Instead of accessing the attribute directly, you pass the new value to a method that 
handles the updating internally. 
'''
my_new_car.update_odometer(24)
my_new_car.read_odometer()
''' 
We can extend the method update_odometer() to do additional work every time the odometer reading is 
modified. Let's add a little logic to make sure no one tries to roll back the 
odometer reading:
'''
my_new_car.update_odometer(11)
my_new_car.read_odometer()

# Incrementing an Attribute's value through a method. --Car.4
'''
Sometimes you will want to increment an attribute's value by a certain amount rather than set and 
entirely new value. Say we buy a used car and put 100 miles on it between the time we buy it 
and the time we register it. Here's a method that allows us to pass this incremental amount and add
that value to the odometer reading:
'''
my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(-4)
my_used_car.read_odometer()

cut_off()
# Inheritance
'''
You don't always have to start from scratch when writing a class. If the class you are writing is 
a specialized version of another class you wrote, you can use inheritance. When one class inherits from 
another, it automatically takes on all the attributes and methods of the first class. The original class 
is called the parent class, and the new class is the child class. The child class inherits every attribute
and method from its parent class but it also is free to define new attributes and methods of its own.
'''

# The __init__() Method for a Child Class --eCar.1
'''
The first task Python has when creating an instance from a child class is to assign values to all attributes in the 
parent class. To do this, the __init__() method for a child class needs help from its parent class.
As an example, let's model an electric car. An electric car is just a specific kind of car,
so we can base our new electricCar class on the Car class we wrote earlier. Then we will only have to write 
code for the attributes and behavior specific to electric cars.
'''
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

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
'''
The super() function is a special function that helps Python make connections between the 
parent and child class. This line tells Python to call the __init__() method from ElectricCar's
parent class. The name super comes from a convention of calling the parent class a superclass
and the child class a subclass.
The super() function needs two arguments: a reference to the child class and the self object. 
These arguments are necessary to help Python make proper connections between the parent and child
classes.
'''

# Defining Attributes and Methods for the child class--eCar.2
'''
Once you have a child class that inherits from a parent class, you can add any new 
attributes and methods necessary to differentiate the child class from the parent class.
Let's add an attribute that's specific to electric cars and a method to report on this attribute.
We will store the battery size and write a method that prints a description of the battery.

There is no limit to how much you can specialize the ElectricCar class. You can add as many attributes
and methods you need to model an electric car to whatever degree of accuracy you need. An attribute or method
that could belong to any car, rather than one that's specific to an electric car, should be added to the Car class 
instead of the ElectricCar class. 
Then anyone who uses the Car class will have that functionality available as well, an the ElectricCar class will
only contain code for the information and behavior specific to electric vehicles.
'''

# Overriding Methods from the Parent Class--eCar.3
'''
You can override any method from the parent class that doesn't fit what you are trying to model with the child class.
To do this, you define a method in the child class with the same name as the method you want to override in the parent 
class. Python will disregard the parent class method and only pay attention to th method you define in the child class.
Say the class Car had a method called fill_gas_tank(). This method is meaningless for an all-electric vehicle, so you 
might want to override this method.
'''

# Instances as Attributes--eCar.4
'''
When modeling something from the real world in code, you may find that you are adding more and more detail to a class. 
You will find that you have a growing list of attributes and methods and that your files are becoming lengthy. In these 
situations, you might recognize that part of one class can be written as a separate class. You can break your large 
class into smaller classes that work together.
For example, if we continue adding detail to the ElectricCar class, we might notice 
that we are adding many attributes and methods specific to the car's battery. When we see this happening, we can stop
and move those attributes and methods to a separate class called Battery. Then we can use a Battery instance as an 
attribute in the ElectricCar class:
'''

# Modeling Real-World Objects
'''
As you begin to model more complicated items like electric cars, you will wrestle with 
interesting questions. Is the range of an electric car a property of the battery or of the car?
If we're only describing one car, it is probably fine to maintain the association of the method
get_range() with the Battery class. But if we are describing one car, it is probably fine 
to maintain the association of the method get_range() with the Battery class. But if we are describing
a manufacturer's entire line of cars, we probably want to move get_range() to the ElectricCar class. 
The get_range() method would still check the battery size before determining the range, but it would 
report a range specific to the kind of car it's associated with. Alternatively, we could maintain the 
association of the get_range() method with the battery but pass it a parameter such as car_model. The 
get_rang() method would then report a range based on the battery size and car model.

This brings you to an interesting point in your growth as a programmer. When you wrestle with questions like
these, you are thinking at a higher logical level rather than a syntax-focused level. You are thinking 
not about Python, but about how to represent the real worl in code. When you reach this point, you will 
realize there are often no right or wrong approaches to modeling real-world situations. Some approaches are 
more efficient than others, but it takes practice to find the most efficient representations. If your code is 
working as you want it to, you are doing well! Don't be discouraged if you find you are ripping apart your
classes and rewriting them several times using different approaches. In the quest to write accurate, efficient
code, everyone goes through this process. 
'''

cut_off()
