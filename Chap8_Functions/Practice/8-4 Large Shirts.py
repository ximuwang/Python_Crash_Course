# Large Shirts
def make_shirt(size, message = 'I love Python'):
    print(f'\nThe t_shirt\'s size is {size.title()}')
    print(f'with the sentence: {message.title()}')
make_shirt('small')
make_shirt('large')
make_shirt('medium')
make_shirt('extra large', 'Python loves me!')