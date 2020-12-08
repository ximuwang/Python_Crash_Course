# 10-5 Programming Polls
filename = r'..\texts_file\response.txt'
info = {}
print("Enter 'quit' to quit.")
while True:
    names = input('please enter a name: \n')
    if names == 'quit':
        break
    else:
        with open(filename, 'w') as file:
            reasons = input("Why do you like programming: \n")
            info[names] = reasons
            for name, value in info.items():
                file.write(name + " : " + value + '\n')



