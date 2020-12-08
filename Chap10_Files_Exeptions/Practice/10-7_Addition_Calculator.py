# 10-7 Addition Calculator

def add_num():
    print('Enter "q" to quit: ')
    while True:
        try:
            num_1 = (input('The first Number: \n'))
            if num_1 == 'q':
                break
            num_1 = int(num_1)
            num_2 = (input('The second Number: \n'))
            if num_2 == 'q':
                break
            num_2 = int(num_2)
        except ValueError:
            print('Sorry, but I need numbers.')
        else:
            result = num_1 + num_2
            print('The result of adding {} and {} is {}.'.format(num_1, num_2, result))


add_num()
