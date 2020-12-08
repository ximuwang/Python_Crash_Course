# 9-13 OrderedDict Rewrite

from collections import OrderedDict

python_tutorials = OrderedDict()
python_tutorials['1'] = 'Whetting Your Appetite'
python_tutorials['2'] = 'Using the Python Interpreter'
python_tutorials['3'] = 'An Informal Introduction to Python'
python_tutorials['4'] = 'More Control Flow Tools'
python_tutorials['5'] = 'Data Structure'
python_tutorials['6'] = 'Modules'
python_tutorials['7'] = 'Input and Output'
python_tutorials['8'] = 'Errors and Exceptions'
python_tutorials['9'] = 'Classes'
python_tutorials['10'] = 'Brief Tour of the Standard Library'
python_tutorials['11'] = 'Brief Tour of the Standard Library 2'
python_tutorials['12'] = 'Virtual Environments and Packages'
python_tutorials['13'] = 'What Now?'
python_tutorials['14'] = 'Interactive Input Editing and History Substitution'
python_tutorials['15'] = 'Floating Point Arithmetic: Issues and Limitations'
python_tutorials['16'] = 'Appendix'

print("Here's the glossary of the Python Tutorial")
for key, value in python_tutorials.items():
    print(key + ":" + value)
