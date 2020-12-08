# 10-10 Common Words
verrochio = r'..\texts_file\verrochio.txt'
bob_hazard = r'..\texts_file\bob_hazard.txt'
history_of_egypt = r'..\texts_file\history_of_egypt.txt'
filenames = [verrochio, bob_hazard, history_of_egypt]
def count_words(filename, word):
    '''Count how many words appear in a file'''
    for filename in filenames:
        print('We are counting the words for {}'.format(filename))
        try:
            with open(filename, encoding='utf-8') as f:
                contents = f.read()
        except FileNotFoundError:
            pass
        else:
            words = len(contents)
            times = contents.count(word)
            msg = f'the phrase "{word}" appears {times} times in {filename} '
            print(f'The total words in {filename} is {words}')
            print(msg + '\n')
count_words(filenames, 'please')