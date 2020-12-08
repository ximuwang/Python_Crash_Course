# 10-1 Learning Python
filename = r'C:\Users\Ximu\Documents\Self_Study_CS\Python Program\B-Python_Crash_Course' \
           r'\Chap10_Files_Exeptions\texts_file\learning_python.txt'

print("----------------Reading the entire file-----------------")
with open(filename) as f:
    contents = f.read()
print(contents)

print("----------------Looping over the file object-----------------")
with open(filename) as f:
    for line in f:
        print(line.rstrip())

print("----------------Storing lines in a list-----------------")
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    content = line.rstrip()
    print(content)
