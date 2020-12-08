# Name: Ximu.W
# Date: 11/19/2020
# Subject: Chap8 Functions

'''
In this chapter you will learn to write functions, which are named blocks of code
that are designed to do on specific job. When you want to perform a particular task
that you have defined in a function, you call the name of the function responsible for
it.
'''
'''
If you need to to perform that task multiple times throughout your program, you don't need
to type all the code for the same task again and again; you just call the function dedicated 
to handling that task, and the call tells Python to run the code inside the function. You will
find that using functions makes your programs easier to write, read, test, and fix.
'''
'''
In this chapter you will also learn ways to pass information to functions. You will learn how to 
write certain functions whose primary job is to display information and other functions designed to 
process data and return a value or set of values. Finally you will learn to store functions in 
separate files called modules to help organize your main program files.
'''
def greet_user():
    '''Display a simple greeting.'''
    print('Hello!')
greet_user()

# Passing information to a Function
def greet_user(username):
    '''Display a simple greeting.'''
    print("Hello, " + username.title() + '!')
greet_user('Ximu')

# Arguments and Parameters
'''
An argument is a piece of information that is passed from a function 
call to a function. When we call the function, we place the value we want the 
function to work with in parentheses.
People sometimes speak of arguments and parameters interchangeably. Don't be 
surprised if you see the variables in a function definition referred to as 
arguments or the variables in a function call referred to as parameters.
'''
# Passing arguments
'''
Because a function definition can have multiple parameters, a function call may 
need multiple arguments. You can pass arguments to your functions in a number of 
ways. You can use positional arguments, wihch need to be in the same order the 
parameters were written; keyword arguments, where each argument consists of a variable 
name and a value; and lists and dictionaries of values. 
'''
# Positional Arguments
'''
When you call a function, Python must match each argument in the function call with a 
parameter in the function definition. The simplest way to do this is based on the order
of the arguments provided. Values matched up this way are called positional arguments.
'''
# Pets.py
def describe_pet(animal_type, pet_name):
    '''Display information about a pet.'''
    print("\nI have a " + animal_type + '.')
    print("My " + animal_type + "\'s name is " + pet_name.title() + '.')

describe_pet('hamster', 'harry')
describe_pet(pet_name = 'harry', animal_type = 'dog')
describe_pet('dog', 'willie')
describe_pet('harry', 'hamster')    # The order in positional arguments matter.

# Keyword Arguments
'''
A keyword argument is a name-value pair that you pass to a function. You directly
associate the name and the value within the argument, so when you pass the argument
to the function, there's no confusion. Keyword arguments free you from having to worry
about correctly ordering your arguments in the function call, and they clarify the 
role of each value in the function call.
'''
describe_pet(animal_type = 'hamster', pet_name = 'harry')
describe_pet(pet_name = 'harry', animal_type = 'hamster')   # When you use keyword arguments,
                                                            # be sure to use the exact names of
                                                            # the parameters in the function's definition
# Default Values
'''
When writing a function, you can define a default value for each parameter. If an argument for a 
parameter is provided in the function call, Python uses the argument value, If not, it uses
the parameter's default value. So when you define a default value for a parameter, you can exclude the 
corresponding argument you'd usually write in the function call. Using default values can simplify
your function calls and clarify the ways in which your functions are typically used.
'''
def describe_pet(pet_name, animal_type = 'dog'):
    '''Display information about a pet.'''
    print("\nI have a " + animal_type + '.')
    print("My " + animal_type + "'s name is " + pet_name.title() + '.')
describe_pet(pet_name = 'willie')
# Equivalent Function calls
'''
Because positional arguments, keyword arguments, and default values can all be used together, often
you will have several equivalent ways to call a function.
'''
# A dog named Willie
describe_pet('willie')
describe_pet(pet_name = 'willie')
# A hamster named Harry
describe_pet('harry', 'hamster')
describe_pet(pet_name = 'hary', animal_type = 'hamster')
describe_pet(animal_type = 'hamster', pet_name = 'harry')

# Return Values
'''
A function does not always have to display its output directly. Instead, it can process 
some data and then return a value or set of values. The value the function returns is called 
a return value. The value the function returns is called a return value. The return statement 
takes a value from inside a function and sends it back to the line tht called the function.
Return values allow you to move much of your program's grunt work into functions, which can simplify the 
body of your program.
'''

# Returninn a Simple Value
def get_formatted_name(first_name, last_name):
    '''Return a full name, neatly formatted.'''
    full_name = first_name + ' ' + last_name
    full_name = full_name.title()
    return full_name
girlfriend = get_formatted_name('aki', 'ma')
print(girlfriend)

# Making an Argument Optional
def get_formatted_name(first_name, middle_name, last_name):
    '''Return a full name, neatly formatted.'''
    full_name = first_name.title() + " " + middle_name.title() + " " + last_name.title()
    return full_name.title()
name = get_formatted_name('ximu', 'Jeremy', 'wang')
print(name)

# Cases for not-given middle name
def get_formatted_name(first_name, last_name, middle_name = ''):
    '''Return a full name, neatly formatted.'''
    if middle_name:
        full_name = first_name.title() + " " + middle_name.title() + " " + last_name.title()
    else:
        full_name = first_name.title() + ' ' + last_name.title()
    return full_name
name = get_formatted_name('ximu', 'wang', 'jeremy')
print(name)

# Returning a Dictionary
'''
A function can return any kind of value you need it to, including more complicated date structures
like lists and dictionaries. For example, the following function takes in parts of a name and return
a dictionary representing a person:
'''
def build_person(first_name, last_name):
    '''Return a dictionary of information about a person.'''
    person = {'first': first_name.title(), 'last': last_name.title()}
    return person
musician = build_person('jimi', 'hendrix')
print(musician)

def build_person(first_name, last_name, age = ''):
    '''Return a dictionary of information about a person.'''
    person = {'first': first_name.title(), 'last': last_name.title()}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix', age = 23)
print(musician)
# Using a Function with a while loop
def get_formatted_name(first_name, last_name, middle_name = ''):
    '''Return a full name, neatly formatted.'''
    if middle_name:
        full_name = first_name.title() + " " + middle_name.title() + " " + last_name.title()
    else:
        full_name = first_name.title() + ' ' + last_name.title()
    return full_name
# This is an infinite loop!
while True:
    print('\nPlease tell me your name:')
    print('(enter "q" anytime to quit)')

    f_name = input('first name: ')
    if f_name == 'q':
        break

    l_name = input('last name: ')
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print('Hello', formatted_name + '!')

# Passing a List
'''
You will often find it useful to pass a list to a function, whether it's a list
of names, numbers, or more complex objects, such as dictionaries. When you pass 
a list to a function, the function gets direct access to the contents of the list.
Let's use functions to make working with lists more efficient.
'''
# Say we have a list of users and want to print a greeting to each.
def greet_users(names):
    '''print a simple greeting to each user in the list.'''
    for name in names:
        msg = 'Hello, ' + name.title() + '!'
        print(msg)

usernames = ['hannah', 'ty', 'margot', 'ximu']
greet_users(usernames)

# Modifying a list in a function
'''
When you pass a list to a function, the function can modify the list.
Any changes made to the list inside the function's body are permanent, allowing
you to work efficiently even when you are dealing with large amount of data.
'''
'''Consider a company that creates 3D printed models of designs that user 
submit. Designs that need to be printed are stored in a list, and after being printed they are
moved to a separate list. The following code does this without using functions:
'''
# Start with some designs that need to be printed.
unprinted_designs = ['Iphone case', 'robor pendant', 'dodecahedron']
completed_designs = []
# Simulate printing each design, until none are left.
# Move each design to completed_design after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    # Simulate creating a 3D print from the design
    print('Printing Model: ' + current_design)
    completed_designs.append(current_design)
# Display all completed models.
print("\nThe following models have been printed: ")
for completed_design in completed_designs:
    print(completed_design)
'''
We can reorganize this code by writing two functions, each of which does one specific job.
Most of the code won't change; We are just making it more efficient. The first function will 
handle printing the designs, and the second will summarize the prints that have been 
made
'''
print('')
def print_models(unprinted_designs, completed_desings):
    '''
    Simulate printing each design, until none are left.
    Move each design to completed_designs after printing
    '''
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # Simulate creating a 3D print from the design.
        print('Printing Model: ' + current_design)
        completed_designs.append(current_design)

def show_completed_designs(completed_designs):
    '''Show all the models that were printed'''
    print('\nThe following models have been printed: ')
    for completed_design in completed_designs:
        print(completed_design)
unprinted_designs = ['Iphone case', 'robor pendant', 'dodecahedron']
completed_designs = []

print_models(unprinted_designs[:], completed_designs)
show_completed_designs(completed_designs)
print(unprinted_designs)

# Preventing a Function from Modifying a List
'''
Sometimes you'll want to prevent a function from modifying a list, For 
example, say that you start with a list of unprinted designs and write a function
to move them to a list of completed models, as in the previous example, 
You may decide that even though you have printed all the designs, you want
to keep the original list of unprinted designs for you records. But because 
you moved all the design names out of unprinted_designs, the list is now empty, and 
the empty list is the only version you have; the original is gone.

In this case, you can address this issue by passing the function a copy of the list,
not the original. Any changes the function makes to the list will affect only the copy
leaving the original list intact. 
'''

# Passing an Arbitrary Number of Arguments
'''
Sometimes you won't know ahead of time how many arguments a function needs to accept. 
Fortunately, Python allows a function to collect an arbitrary number of arguments from 
the calling statement.
For example, condiser a function that builds a pizza. It needs to accept a number of 
toppings, but you can't know ahead of time how many toppings a person will want. The 
function in the following example has one parameter *toppings, but this parameter collects
as many arguments as the calling line provides.
'''
def make_pizza(*toppings):
    '''Print the list of toppings that have been requested.'''
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
'''The asterisk in the parameter name *toppings tells Python to make an empty tuple called 
toppings and pack whatever values it receives into this tuple.
The print statement in the function body produces output showing that Python can handle a 
function call with one value and a call with three values. 
It treats the different calls similarly. Note that Python packs the arguments into a tuple,
even if the function receives only one value.'''
'''Now we can replace the print statement with a loop that runs through the list of 
toppings and describes the pizza being ordered.'''
def make_pizza(*toppings):
    '''Summarize the pizza we are about to make.'''
    print('\nMaking a pizza wit the following toppings:')
    for topping in toppings:
        print('-' + topping)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# Mixing positional and arbitrary arguments
'''If you want a function to accept several different kinds of arguments, the parameter that 
accepts an arbitrary number of arguments must be placed last in the function definition. Python
matches positional and keyword arguments first and then collects any remaining arguments in the 
final parameter.
'''
def make_pizza(size, *toppings):
    '''Summarize the pizza we are about to make'''
    print('\nMaking a ' +str(size) +
          '-inch pizza with the following toppings:')
    for topping in toppings:
        print('-' + topping)
make_pizza(12, 'pepperoni')
make_pizza(42, 'mushrooms', 'green onions', 'extra cheese')

# Using Arbitrary Keyword Argument
'''Sometimes you will want to accept an arbitrary number of arguments, but you won't know ahead of 
time what kind of information will be passed to the function. In this case, you can write functions 
that accept as many key-value pairs as the calling statement provides. One example involves building 
user profiles: you know you will get information about a user, but you are 
not sure what kind of information you will receive.
'''

def build_profile(first, last, **user_info):
    '''Build a dictionary containing everything we know about a user.'''
    profile = {}
    profile['first_name'] = first.title()
    profile['last_name'] = last.title()
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
                             location = 'princeton',
                             field = 'physics')
print(user_profile)
'''
The definition of build_profile() expects a first and last name, and then it 
allows the user to pass in as many name-value pairs as they want. The double 
asterisks before the parameter **user_info cause Python to create an empty dictionary
called user_info and pack whatever name-value pairs it receives into this dictionary.
Within the function, you can access the name-value pairs in user_info just as you would 
for any dictionary.
'''
# Storing Your Functions in Modules
''' 
One advantage of functions is the way they separate blocks of code from your 
main program. By using descriptive names for your functions, your main program
will be much easier to follow. You can go a step further by storing your functions 
in a separate file called a module and the importing that module into your main
program. An import statement tells Python to make the code in a module available
in the currently running program file.
'''
# Importing an entire module
''' 
To start importing functions, we first need to create a module. A module is a file 
ending in .py that contains the code you want to import into your program. Let's make
a module that contains the function make_pizza(). To make this module, we will remove 
everything from the file pizza.py except the function make_pizza():
'''

import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Importing Specific Functions
'''You can also import a specific function from a module.
here is a general syntax for this approach

from module_name import function_name, function_1, function_2
'''
from pizza import make_pizza

make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Using as to give a function an alias
''' 
If a name of a function you are importing might conflict with an existing name in 
your program or if the function name is long. You can use a short, unique alias-an
alternate name similar to a nickname for the function. You will give the function this 
special nickname when you import the function
'''
from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# Using as to give a Module an Alias
'''You can also provide an alias for a module name. Giving a module a short alias,
like p for pizza, allows you to call the module's functions more quickly.
Calling p.make_pizza() is more concise than calling pizza.make_pizza()
'''
import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')

# Importing all functions in a Module
'''
You can tell Python to import every function in a module by using the asterisk(*) 
operator:
'''
from pizza import *
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
'''
The asterisk in the import statement tells Python to copy every function from the 
module pizza into this program file. Because every function is imported, you can call
each function by name without using the dot notation. However, It's best not to use this
approach when you are working with larger modules that you didn't write: if the module 
has a function name that matches an existing name in your project, you can get some 
unexpected results. Python may see several functions or variables with the same name, and
instead of importing all the functions separately, it will overwrite the functions.
The best approach is to import the function or functions you want, or import the entire 
module and use the dot notation. This leads to clear code that's easy to read and understand.
I include this section so you will recognize import statements like the following when you 
see them in other people's code.
'''

# Styling Functions
'''
You need to keep a few details in mind when you're styling functions.
Functions should have descriptive names, and these names should use lowercase
letters and underscores. Descriptive names help you and others understand what your code is 
trying to do. Module names should use these conventions as well.
Every function should have a comment that explains concisely what the function
does. This comment should appear immediately after the function definition and use 
the docstring format. In a well-documented function, other programmers can use the 
function by reading only the description in the docstring. They should be able to 
trust that the code works as described, and as long as they know the name of the function,
the arguments it needs, and the kind of value it returns, they should be able to use it in 
their programs.
If you specify a default value for a parameter, no spaces should be used on either side of the
equal sign:
def function_name(parameter_0, parameter_1='default value')
the same convention should be used for keyword arguments in function calls:
function_name(value_0, parameter_1='value')
'''