# 10-2 Learning C

filename = r'C:\Users\Ximu\Documents\Self_Study_CS\Python Program\B-Python_Crash_Course' \
           r'\Chap10_Files_Exeptions\texts_file\learning_python.txt'

with open(filename) as f:
    lines = f.readlines()
for line in lines:
    line = line.replace('python', 'C').replace('Python', 'C')
    print(line.strip())

