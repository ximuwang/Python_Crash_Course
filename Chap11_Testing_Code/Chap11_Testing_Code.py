# Name: Ximu.W
# Date: 12/1/2020
# Subject: Chapter 11 - Testing Your Code

''':ivar
When you write a function or a class, you can also write tests for that code.
Testing proves that your code works as it is supposed to in response to all the input
types it is designed to receive. When you write tests, you can be confident that your
code will work correctly as more people begin to use your programs. You will also
be able to test new code as you add it to make sure your changes don't break your
program's existing behavior. Every programmer makes mistakes, so every programmer must test
their code often, catching problems before users encounter them.
In this chapter you will learn to test your code using tools in Python's unittest module.
You will learn to build a test case and check that a set of inputs results in the output
you want. You will see what a passing test looks like and what a failing test looks like,
and you will learn how a failing test can help you improve your code. You will learn to test
functions and classes, and you will start to understand how many tests to write for a project.
'''

# Testing a Function
'''
To learn about testing, we need code to test. Here's a simple fucntion that takes in a first 
and last name, and returns a neatly fornatted full name:
'''

def get_formatted_name(first, last, middle=''):
    '''Generate a neatly formatted full name.'''
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()

''':key
To check that get_formatted_name() works, let's make a program that uses this function. The program
let's users enter a first and last name, and see a neatly formatted full name:
'''
print("Enter 'q' to quit at any time.")
while True:
    first = input('\nPlease give me a first name: ')
    if first == 'q':
        break
    last = input('Please give me a last name: ')
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print('\tNeatly formatted name: ' + formatted_name + '.')

''':key
We can see that the names generated here are correct. But let's say we want to modify 
get_formatted_name() so it can also handle middle names.
As we do so, we want to make sure we don't break the way the function handles names that have
only a first and last name. We could test our code by running names.py and entering a name
like Janis Joplin every time we modify get_formatted_name(), but that would become tedious. 
Fortunately, Python provides an efficient way to automate the testing of a function's output. 
If we automate the testing of get_formatted_name(), we can always be confident that the function
will work when given the kinds of names we have written tests for.
'''
# Unit Tests and Test Cases
''':key
The module unittest from the Python standard library provides tools for testing your code. A unit 
test verifies that one specific aspect of a function's behavior is correct. A test case is a 
collection of uni tests that together prove that a function behaves as it is supposed to, within 
the full range of situations you expect it to handle. A good test case considers all the possible 
kinds of input a function could receive and includes tests to represent each of these situations. A
test case with full coverage includes a full range of unit tests covering all the possible ways you can use 
a function. Achieving full coverage on a large project can be daunting. It's often good enough to write
tests for your code's critical behaviors and then aim for full coverage only if the project starts to see
widespread use.
'''
# A passing Test
''':key
The syntax for setting up a test case takes some getting used to, but once you have set up the test case
it is straightforward to add more unit tests for your functions. To write a test case for a function, import
the unittest module and the function you want to test. Then create a class that inherits from unittest. 
TestCase, and write a series of methods to test different aspects of your function's behavior.
Here's a test case with one method that verifies that the function get_formatted_name works correctly when 
given a first and last name:
'''
import unittest
class NamesTestCase(unittest.TestCase):
    '''Tests for "name_function.py"'''
    def test_first_last_name(self):
        '''Do names like "Janis Joplin" works'''
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
        
    def test_first_middle_last_name(self):
        '''Do names like "Wolfgang Amadeus Mozart" work?'''
        formatted_name = get_formatted_name(
        'wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

# unittest.main()
# A failing Test
''':key
  What does a failing test look like? Let's modify get_formatted_name() so it can handle middle names, but we will do so 
in a way that breaks the function for names with just a first and last name, like Janis Joplin.
  There is a lot of information here becasue there's a lot you might need to know 
when a test fails. The first item in the output is a single E, which tells us one unit test in the 
test case resulted in an error. Next, we se that test_first_last_name() in NamesTestCase caused an error.
Knowing which test failed is critical when your test case contains many unit tests.
At 3 we see a standard traceback, which reports that the function call get_formatted_name('janis,
'joplin') no longer works because it is missing a required positional argument.
  We also see that one unit test was run. Finally, we see an additional message that the overall test
case failed and that one error occurred when running the test case. This information appears at the 
end of the output so you see it right away; you don't want to scroll up through a long output listing
to find out how many tests failed.
'''

# Responding to a Failed Test
''':key
  What do you do when a test fails? Assuming you are checking the right conditions, a passing test means the 
function is behaving correctly and a failing test means there's an error in the new code you wrote. So when a test
fails, don't change the test. Instead, fix the code that caused the test to fail. Examine the changes you just 
made to the function, and figure out how those changes broke the desired behavior. 
  In this case get_formatted_name() used to require only two parameters: a first name and a last name. Now it requires a 
first name, middle name, and a last name. The addition of that mandatory middle name parameter broke the desired behavior
of get_formatted_name(). The best option here is to make the middle name optional. Once we do, our test for names like
janis joplin should pass again, and we should be able to accept middle names as well. Let's modify get_formatted_name() so
middle names are optional and then run the test case again. If it passes, we will move on 
to making sure the function handles middle names properly.
  To make middle names optional, we move the parameter middle to the end of the parameter list in the function
definition and give it an empty default value. We also add an if test that builds the full name properly, 
depending on whether or not a middle name is provided:
'''

# Adding New Tests
''':key
Now that we know get_formatted_name() works for simple names again, let's write a second test for people who include
a middle name. We do this by adding another method to the class NameTestCase:
We name this new method test_first_middle_last_name(). The method name must start with test_ so the method runs automatically
when we run the test_name_function.py. We name the method to make it clear which behavior of get_formatted_name() we are
testing. As a result, if the test fails, we know right away what kinds of names are affected. It's fine to have long method
names in your TestCase classes. They need to be descriptive so you can make sense of the output when you tests fails, and 
because Python calls them automatically, you will never have to write code that calls these methods.
'''

# Testing a Class
''':key
  In the first part of this chapter, you wrote tests for a single function. Now you wll write tests for a class. You will
use classes in many of your own programs. So it is helpful to be able to prove that your classes work correctly. If you have
passing tests for a class you are working on. You can be confident that improvements you make to the class won't 
accidently break its current behavior.
'''
# A variety of Assert Methods
''':key
  Python provides a number of assert methods in the unittest.TestCase class. As
mentioned earlier, assert methods test whether a condition you believe is true at a specific point
in your code is indeed true. If the condition is true as expected, your assumption about how that part of your 
program behaves is confirmed; you can be confident that no errors exist. If the condition you assume is 
true is actually not true, Python raises an exception.
  Table 11-1 describes six commonly used assert methods. With these methods you can verify that returned 
values equal or don't equal expected values, that values are True or False, and that values are in or not in a 
given list. You can use these methods only in a class that inherits from unittest.TestCase, so let's look at how
we can use one of these methods in the context of testing an actual class.
'''
''':key
Table 11-1: Assert Methods Availble from the unittest Module
Method                      use
assertEqual(a, b)           Verify that a == b
assertNotEqual(a, b)        Verify that a != b
assertTrue(x)               Verify that x is True
assertFlase(x)              Verify that x is False
assertIn(item, list)        Verify that item is in list
assertNotIn(item, list)     Verify that item is not in list
'''

# A Class to Test
''':key
  Testing a class is similar to testing a function--much of your work involves testing the behavior of the 
methods in the class. But there are a few differences, so let's write a class to test. Consider a class that helps
administer anonymous surveys:
'''
class AnonymousSurvey():
    '''Collect anonymous answers to a survey question.'''

    def __init__(self, question):
        '''Store a question, and prepare to store responses.'''
        self.question = question
        self.responses = []

    def show_question(self):
        '''Show the survey question.'''
        print(question)

    def store_response(self, new_response):
        '''Store a single response to the survey.'''
        self.responses.append(new_response)

    def show_results(self):
        '''Show all the responses that have been given.'''
        print("Survey Results:")
        for response in self.responses:
            print('- ' + response)

# Define a question, and make a survey.
question = 'What language did you first learn to speak?'
my_survey = AnonymousSurvey(question)

# Show the question, and store responses to the question.
# my_survey.show_question()
# print('Enter "q" at any time to quit.\n')
# while True:
#     response = input("Language: ")
#     if response == 'q':
#         break
#     my_survey.store_response(response)
# # Show the survey results.
# print('\nThank you to everyone who participated in the survey!')
# my_survey.show_results()

''':key
  This class works for a simple anonymous survey. But let's say we want to improve AnonymousSurvey and the 
module it is in, survey. We could allow each user to enter more than one response. We could write a method to 
list only unique responses and to report how many times each response was given.
We could write another class to manage nonanonymous surveys. 
  Implementing such changes would risk affecting the current behavior of the class AnonymousSurvey. For example, it is possible that
while trying to allow each user to enter multiple responses, we could accidentally change how single responses are handled.
To ensure we don't break existing behavior as we develop this module, we can write tests for the class.
'''
# Testing the AnonymousSurvey Class
''':key
  Let's write a test that verifies one aspect of the way AnonymousSURVEY Behaves. We will write a test to verify that a 
single response to the survey question is stored properly. We will use the assertIn() method to verify that the response
is in the list of responses after it is been stored:
'''
import unittest

class TestAnonymousSurvey(unittest.TestCase):
    '''Tests for the class AnonymousSurvey.'''

    def setUp(self):
        '''
        Create a survey and a set of responses for use in all test methods.
        '''
        question = 'What language did you first learn to speak?'
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_stored_single_response(self):
        '''test that a sigle response is stored properly.'''
        my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], my_survey.responses)

    def test_store_three_responses(self):
        '''Test that three individual responses are stored properly.'''
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()

''':key
This works perfectly. However, these tests are a bit repetitive, so we will use another
feature of unittest to make them more efficient.
'''

# The setUp() Method
''':key
  In test_survey.py we created a new instance of AnonymousSurvey in each test method, and we created 
new responses in each method. The unittest.TestCase class has a setUp() method that allows you to create 
these objects once and then use them in each of your test methods. When you include a setUp()
method in a TestCase class, Python runs the setUp() method before running each method starting with test_. 
Any objects created in the setUp() method are then available in each test method you write.
  Let's use setUp() to create a survey instance and a set of responses that can be used in test_store_single_response()
and test_store_three_responses():
'''

''':key
  The method setUp() does two things: it creates a survey instance, and it creates a list of responses. Each of these is prefixed
by self. so they can be used anywhere in the class. This makes the two test methods simpler, because neither one has to make
a survey instance or a response. The method test_store_single_response() verifies that the first response in
self.responses--self.responses[0]--can be stored correctly, and test_store_single_response() verifies that all three responses
in self.responses can be stored correctly.
  When we run test_survey.py again, both tests still pass. These tests would be particularly useful when trying to expand
AnonymousSurvey to handle multiple responses for each person. After modifying the code to accept multiple
responses, you could run these tests and make sure you have not affected the ability to store a 
single response or a series of individual responses.
  When you are testing your own classes, the setUp() method can make your test methods easier to write. You make one set of 
instances and attributes in setUp() and then use these instances in all your test methods. This is much easier than making
a new set of instances and attributes in each test method.
'''
''':key
When a test case is running, Python prints one character for each unit test as it is completed. A passing test prints a dot,
a test that results in an error prints an E, and a tst that results in a failed assertion prints an F. This is why you will
see a different number of dots and characters on the first line of output when you run your test cases.
If a test case takes a long time to run because it contains many unit tests, you can watch these results to get
a sense of how many tests are passing.
'''

# Summary
''':cvar
  In this chapter you learned to write tests fro functions and classes using tools in the unittest module. You learned
to write a class that inherits from unittest.TestCase, and you learned to write test methods that verify specific 
behaviors your functions and classes should exhibit. You learned to use the setUp() method to efficiently create instances
and attributes from your classes that can be used in all the test methods for a class.
  Testing is an important topic that many beginners don't learn. You don't have to write tests for all the simple projects you try
as a beginner. But as soon as you start to work on projects that involves significant development
effort, you should test the critical behaviors of your functions and classes. You will be more confident that new work on 
your project won't break the parts that work, and this will give you the freedom to make improvements to your code. If you 
accidentally break existing functionality, you will know right away, so you can still fix the problem easily. Responding to a failed 
test that you ran is much easier than responding to a bug report from an unhappy
user.
  Other programmers respect your projects more if you include some initial tests. They will feel more comfortable experimenting 
with your code and be more willing to work with you on projects. If you want to contribute to a project that other
programmers are working on, you will be expected to show that your code passes existing tests and you will usually be expected 
to write tests for new behavior you introduce to the project.
  Play around with tests to become familiar with the process of testing your code. Write tests for the most critical behaviors 
of your functions and classes, but don't aim for full coverage in early projects unless you have a specific reason to do so. 
'''