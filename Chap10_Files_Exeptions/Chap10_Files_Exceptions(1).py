# Name: Ximu.W
# Date: 11/28/2020
# Subject: Chapter 10 -- Files and Exceptions
'''
  Now that you have mastered the basic skills you need to write organized programs that are easy to use
It is time to think about making your programs even more relevant and usable. In this chapter you will
learn to work with files so your programs can quickly analyze lots of data.
  You will learn to handle errors so your programs don't crash when they encounter unexpected situations.
You will learn about exceptions, which are special objects Python creates to manage errors that arise while
a program is running. You will also learn about the json module, which allows you to save user date so
it isn't lost when your program stops running.
  Learning to work with files and save data will make your programs easier for people to use. Users will be
able to choose what data to enter and when to enter it. People can run your program, do some work, and then close
the programs more robust when they encounter bad data. Whether it comes from innocent mistakes or from malicious
attempts to break your programs. With the skills you will learn in this chapter, you will make your programs
more applicable, usable, and stable.
'''

# Reading from a file --file_reader.1
""":ivar
  An incredible amount of data is available in text files. Text files can contain weather data, traffic data, 
socioeconomic data, literary works, and more. Reading from a file is particularly useful in data analysis 
applications, but it is also applicable to any situation in which you want to analyze or modify 
information stored in a file. For example, you can write a program that reads in the contents of a text file and 
rewrites the file with formatting that allows a browser to display it. 
  When you want to work with the information in a text file, the first step is to read the file into memory. You 
can read the entire contents of a file, or you can work through the file one line at a time.
"""
# Reading an Entire File
''':ivar
To begin, we need a file with a few lines of text in it. Let's start with a file that contains pi to 30 decimal 
places per line:
'''

with open('texts_file\pi_digits.txt') as file_object:  # file_reader.1
    contents = file_object.read()
    print(contents.rstrip())    # file_reader.2

''':key 
 The first line of this program has a lot going on. Let's start by looking at the open() function. To do any work with 
a file, even just printing its contents, you first need to open the file to access it. The open() function needs 
one argument: the name of the file you want to open. Python looks for this file in the directory where the program 
that's currently running, so Python looks for pi_digits.txt in the directory where file_reader.py is stored. The open()
function returns an object representing the file. Here, open('pi_digits.txt') returns an object, which we will work 
with later in the program.
  The keyword with closes the file once access to it is no longer needed. Notice how we call open() in this program 
but not close(). You could open and close the file by calling open() and close(), but if a bug in your program prevents
the close() statement from being executed, the file may never close. This may seem trivial, but improperly closed files
can cause data to be lost or corrupted. And if you call close() too early in your program, you will find yourself 
trying to work with a closed file (a file you can't accesss), which leads to more errors. It is not always easy to know 
exactly when you should closea file, but with the structure shown here. Python will figure that out for you. 
All you have to do is open the file and work with it as desired, trusting that Python will close it automatically when 
time is right. 
  Once we have a file object representing pi_digits.txt, we use the read() method in the second line of our program to
read the entire contents of the file and store it as one long string in contents. When we print the value of contents,
we get the entire text file back:
'''
''':key
The only difference between this output and the original file is the extra blank line at the end of the output. The 
blank line appears because read() returns an empty string when it reaches the end of the file. 
this empty string shows up as a blank line. If you want to remove the extra blank line, you can use 
rstrip() in the print statement. #--file.reader.2
'''

# Find Paths
''':key
  When you pass a simple filename like py_digits.txt to the open() function, Python looks in the directory
where the file that's currently being executed is stored. To get Python to open files from a directory other than the 
one where your program file is stored, you need to provide a file path, which tells Python to look in a specific 
location on your system.
  You could use a relative file path to open a file from {text_files}. A relative file path tells Python to 
look for a given location relative to the directory where the currently running program file is stored.
you use a backslash(\)
  You can also tell Python exactly where the file is on your computer regardless of where the program that's 
being executed is stored. This is called an absolute file path. Absolute path are usually longer than relative paths
so it is helpful to store them in a variable and then pass that variable to open().
'''

# Reading line by line
'''
  When you are reading a file, you will often want to examine each line of the file. You might be looking for certain 
information in the file, or you might want to modify the text in the file in some way. For example, you might want to 
read through a file of weather data and work with any line that includes the word sunny in the description of that day
weather. In a news report, you might look for any line with the tag <headline> and rewrite that line with a specific 
kind of formatting.
  You can use a for loop on the file object to examine each line from a file one at a time.  
'''
filename = r'C:\Users\Ximu\Documents\Self_Study_CS\Python Program\B-Python_Crash_Course\Chap10_Files_Exeptions\texts_file\pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# Making a List of Lines from a File --file.reader.3
''':key
  When you use with, the file object returned by open() is only available inside the with block that contains it. 
If you want to retain access to a file's contents outside the with block, you can store the file's line in a list 
You can process parts of the file immediately and postpone some precessing for later in the program.
  The following example stores the lines of pi_digits.txt in a list inside the with block and then prints the lines 
outside the with block:
'''
with open(filename) as file_object:     # --file.reader.3
    lines = file_object.readlines()     # store the content in a list called lines

# for line in lines:
#     print(line.rstrip())

pi_string = ''      # --file.reader.4
for line in lines:
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))
''':key
  At the readlines() method takes each line from the file and stores it in a list. This
list is then stored in lines. Which we can continue to work with after the with block ends
Then we use a simple for loop to print each line from lines. Because each item in lines 
corresponds to each line in the file, the output matches the contents of the file exactly.
'''

# Working with a File's Contents #--file.reader.4
''':key
  After you have read a file into memory, you can do whatever you want with that data, so let's 
briefly explore the digits of pi. First, we will attempt to build a single string containing all 
the digits in the file with no whitespace in it.
  The variable pi_string contains the whitespace that was on the left sisde of the digits in each
line, but we can get rid of that by using strip() instead of rstrip().
  Now we have a string containing pi to 30 decimal places. The string is 32 characters long because
it also includes the leading 3 and a decimal point.  
'''

# Large Files, One Millions Digits--pi_mdigits.1
'''
So far we have focused on analyzing a text file that contains only three lines, but the code in these
examples would work just as well on much larger files. If we start with a text file that contains pi to
1000000 decimal places instead of just 30, we can create a single string containing all these digits. We
don't need to change our program at all except to pass it a different file. We will alos print just the first 50 
decimal places, so we don't have to watch a million digits scroll by in the terminal.
'''
import re
filename = 'texts_file\pi_million_digits.txt'   # --pi_mdigits.1
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string[:52] + '...')
print(len(pi_string))
#
# birthday = input('Enter your birthday, in the form mmddyy: ')       # --pi.mdigits.2
# if birthday in pi_string:
#     print(f'Your birthday appears in the first million digits of pi.')
#     match = re.search(birthday, pi_string)
#     s = match.start()
#     e = match.end()
#     print(f"Your birthday '{birthday}' appears in pi from index {s} to {e} ('{pi_string[s:e]}') ")
# else:
#     print("Your birthday does not appear in the first million digits of pi.")
# Is your Birthday Contained in Pi      # pi_mdigits.2
'''
I have always been curious to know if my birthday appears anywhere in the digits of pi.
let's use the program we just wrote to find out if someone's birthday appears anywhere in
the first million digits of pi. We can do this by expressing each birthday as a string of 
digits and seeing if that string appears anywhere in pi_string:
'''

# Write to a File
''':key
One of the simplest ways to save data is to write it to a file. When you write text to a file, the 
output will still be available after you close the terminal containing your program's output. You can 
examine output files with others as well. You can also write programs that read the text back into 
memory and work with it again later.
'''
# Writing to an Empty file # -- write.message.1
''':key
To write text to a file, you need to call open() with a second argument telling Python that you want to 
write to the file. To see how this works, let's write a simple message and store it in a file instead of 
printing it to the screen:

'''
# -- write.message.1
filename = 'texts_file\programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love Programming.\n")
    file_object.write('I love creating new games.\n')
''':key
The call to open() in this example has two arguments. The first argument is still the name of the file we want 
to open. The second argument, 'w' tells Python that we want to open the file in write mode. You can open a file in 
read mode('r'), write mode('w'), append mode('a'), or a mode that allows you to read and write to the file ('r+').
If you omit the mode argument, Python opens the file in read-only mode by default. 
The open() function automatically creates the file you are writing to if it doesn't already exist. However, be careful
opening a file in write mode('w') because if the file does exist, Python will erase the file before returning the file
object.
We use the write() method on the file object to write a string to the file. This program has no terminal output, but if
you open the file programming you will see one line.
'''
# filename = 'texts_file\programming.txt'
# with open(filename, 'w') as file_object:
#     file_object.write("I love Programming my ass.")
''':key
Python can only write strings to a text file. If you want to store numerical data in a text file, you will have to 
convert the data to string format first using the str() function. 
'''

# Writing Multiple Lines
''':key
The write() function does not add any newlines to the text you write. So if you write more than one line without 
including newline characters, your file may not look the way you want it to:
'''

# Appending to a File
''':key
If you want to add content to a file instead of writing over existing content, you can open 
the file in append mode. When you open a file in append mode, Python does not erase the file before
retuning the file_object. Any lines you write to the file will be added at the end of the file. If 
the file does not exist yet, Python will create an empty file for you.
'''

with open(filename, 'a') as file_object:
    file_object.write('I also love finding meaning in large datasets.\n')
    file_object.write('I love creating apps that can run in a browser.\n')

# Exceptions
''':key
  Python uses special objects called exceptions to manage errors that arise during a program's 
execution. Whenever an error occurs that makes Python unsure what to do next, it creates an exception 
object. If you write code that handles the exception, the program will continue running. If you don't 
handle the exception, the program will halt and show a traceback, which includes a report of the 
exception that was raised.
  Exceptions are handled with try-except blocks. A try-except block asks Python to do something, but it 
also tells Python what to do if an exception is raised. When you use try-except blocks, your programs will
continue running even if things start to go wrong. Instead of tracebacks, which can be confusing for users
to read, users will see friendly error messages that you write. 
'''

# Handling the ZeroDivisionError Exception
# Using try_except Blocks
''':key
  When you think an error may occur, you can write a try-except block to handle the exception that might be 
raised. You tell Python to try running some code, and you tell it what to do if the code results in a particular 
kind of exception.
'''
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
''':key
If the code in a try block works, Python skips over the except block. If the code in the try block causes an 
error, Python looks for an except block whose error matches the one that was raised and runs the code in that 
block. 
In this example, the code in the try block produces a ZeroDivisionError, so Python looks for an except block 
telling it how to respond. Python then runs the code in that block, and the user sees a friendly error message
instead of a traceback:
'''
# Using Exceptions to Prevent Crashes
''':key
  Handling errors correctly is especially important when the program has more work to do after the error occurs
This happens often in programs that prompt users for input. If the program responds to invalid input appropriately, 
it can prompt for more valid input instead of crashing
'''
print("Give me two numbers, and I will divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst Number: ")
    if first_number == 'q':
        break
    second_number = input('Second Number: ')
    if second_number == 'q':
        break
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print('You can divide by 0! ')
    else:
        print(answer)
''':key
It's bad that the program crashed, but it is also not a good idea to let users see
tracebacks. Nontechnical users will be confused by them, and in a malicious setting, attackers will
learn more than you want them to know from a traceback. For example, they will know the 
name of your program file, and they will see a part of your code that isn't working 
properly. A skilled attacker can sometimes use this information to determine which kind
of attacks to use against your code.
'''
# The Else Block
''':key
We can make this program more error resistant by wrapping the line that might produce errors
in a try-except block. The error occurs on the line that performs the division, so that's where
we will put the try-except block. This example also includes an else block. Any code that depends 
on the try block executing successfully goes in the else block.
'''
''':key
  The try-except-else block works like this: Python attempts to run the code in the try statement.
The only code that should go in a try statement is code that might cause an exception to be raised. 
Sometimes you will have additional code that should run only if the try block was successful; this code 
goes in the else block. The except block tells Python what to do in case a certain exception arises 
when it tries to run the code in the try statement.
  By anticipating likely sources of errors, you can write robust programs that continue to run even 
when they encounter invalid data and missing resources. Your code will be resistant to innocent user mistakes
and malicious attacks.
'''

# Handling the FileNotFoundError Exception
''':key
One common issue when working with files is handling missing files. The files is handling missing files. 
The file you are looking for might be in a different location, the filename may be misspelled, or the file may
not exist at all. You can handle all of these situations in a straightforward way with a try-except block.
  Let's try to read a file that doesn't exist. The following program tries to read in the contents of alice in
wonderland, but I haven't saved the file alice.txt in the same directory as alice.py:
'''
filename = r'texts_file\alice.txt'
try:
    with open(filename, encoding='utf-8') as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = 'Sorry, the file ' + filename + ' does not exist.'
    print(msg)
else:
    # Count the approximate number of words in the file.
    words = contents.split()
    num_words = len(words)
    print('The file ' + filename + ' has about ' + str(num_words) + ' words')
# Traceback (most recent call last):
#   File "C:/Users/Ximu/Documents/Self_Study_CS/Python Program/B-Python_Crash_Course/Chap10_Files_Exeptions/Chap10_Files_Exceptions(1).py", line 309, in <module>
#     with open(filename) as f_obj:
# FileNotFoundError: [Errno 2] No such file or directory: 'texts_file\\alice.txt'
''':key
The last line of the traceback reports a FileNotFoundError: this is the exception Python creates when it can't find the 
file it's trying to open. In this example, the open() function produces the error, so to handle it,
the try block will begin just before the line that contains open():
'''
''':key
The program has nothing more to do if the file does not exist, so the error-handling code does not 
add much to this program. Let's build on this example and see how exception handling can help when you
are working with more than one file.
'''
# Analyzing Text
''':key
You can analyze text files containing entire books. Many classic works of literature are available as simple
text files because they are in the public domain. The texts used in this section come from Project Gutenberg
(http://gutenberg.org/). Project Gutenberg maintains a collection of literary works that are available in the 
public domain, and it is a great resource if you are interested in working with literary texts in your program
projects.
  Let's pull in the text of alice in wonderland and try to count the number of words in the text. We will use the 
string method split() does with a string containing just the title 'Alice in Wonderland'
'''
title = '\nAlice in Wonderland'
title = title.split()
print(title)
''':key
The split() method separates a string into parts wherever it finds a space and stores all 
the parts of the string in a list. The result is a list of words from the string, although some punctuation
may also appear with some of the words. To count the number of words in Alice in Wonderland,
we will use split() on the entire text. Then we will count the items in the list to get a rough idea of the 
number of words in the text:
'''
# Working with Multiple Files
''':key
Let's add more books to analyze. But before we do, let's move the bulk of this program to a function called 
count_words(). By doing so, it will be easier to run the analysis for multiple books:
'''
def count_words(filename):
    '''Count the approximate number of words in a file.'''
    try:
        with open(filename, encoding='utf-8') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        # Count approximate number of the words in the file.
        words = contents.split()
        num_words = len(words)
        print('The file ' + filename + ' has about ' + str(num_words) + ' words.')
filename = r'texts_file\alice.txt'
count_words(filename)
''':key
  Most of this code is unchanged. We simply indented it and moved it into the body of count_words(). It is 
a good habit to keep comments up to date when you are modifying a program. So we changed the comment to a 
docstring and reworded it slightly.
  Now we can write a simple loop to count the words in any text we want to analyze. We do this by storing the names 
of the files we want to analyze in a list, and then we call count_words() for each file in the list. We will 
try to count the words for alice in wonderland, siddhartha, moby dick, and little women, which are all available
in the public domain. I have intentionally left siddhartha.txt out of the directory containing word_count.py, so we can 
see how well our program handles a missing file:
'''
filenames = [r'texts_file\alice.txt', r'texts_file\siddhartha.txt', r'texts_file\moby_dick.txt', r'texts_file\little_women.txt']
for file in filenames:
    count_words(file)
''':key
  Using the try-except block in this example provides two significant advantages. We prevent our users from seeing 
a traceback, and we let the program continue analyzing the texts it is able to find. If we don't catch the FileNot
FoundError that siddhartha.txt raised, the user would see a full traceback, and the program would stop running after
trying to analyze siddhartha. It would never analyze Moby Dick or Little Women.
'''
# Failing Silently
''':key
In the previous example, we informed our users that one of the files was unavailable. But you don't need to report 
every exception you catch. Sometimes you will want the program to fail silently when an exception occurs and continue
on as if nothing happened. To make a program fail silently, you write a try block as usual, but you explicitly tell
Python to do nothing in the except block. Python has a pass statement that tells it to do nothing in a block:
'''
# Deciding Which Errors to Report
''':key
How do you know when to report an error to your users and when to fail silently? If users know which texts are supposed
to be analyzed, they might appreciate a message informing them why some texts were not analyzed. If users except to see
some results but don't know which books are supposed to be analyzed, they might not need to know that some texts were 
unavailable. Giving users information they are not looking for can decrease the usability of your program.
Python's error-handling structures give you fine-grained control over how much to share with users when things go 
wrong; it's up to you to decide how much information to share.
Well-written, properly tested code is not very prone to internal errors, such as syntax or logical errors. But 
every time your program depends on something external, such as user input, the existence of a file, or the availability  
of a network connection, there is a possibility of an exception being raised. A little experience will help you know 
where to include exception handling blocks in your program and how much to report to users about errors that arise.
'''
