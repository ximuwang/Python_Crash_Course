# 10-6 Additions
def add_num():
    try:
        num_1 = int(input('The first Number: \n'))
        num_2 = int(input('The second Number: \n'))
    except ValueError:
        print('Sorry, but I need numbers.')
    else:
        result = num_1 + num_2
        print('The result of adding {} and {} is {}.'.format(num_1, num_2, result))

add_num()