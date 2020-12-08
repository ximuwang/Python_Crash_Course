# 10-4 Guest Book
filename = r'..\texts_file\guest.txt'
print("Enter 'quit' if you aire finished!")
while True:
    names = input("Please enter your name: \n")
    name = names.title()
    if name == "Quit":
        break
    else:
        with open(filename, 'a') as file:
            print("Welcome, {}".format(name))
            file.write(name + '\n')
