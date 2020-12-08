# 10-3 Guest
filename = r'..\texts_file\guest.txt'
with open(filename, 'w') as file:
    name = input('Please enter your name please: \n')
    file.write(name.title() + '\n')
