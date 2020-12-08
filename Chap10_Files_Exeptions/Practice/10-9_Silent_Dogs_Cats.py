# 10-9 Silent Dogs and Cats
cats = r'..\texts_file\cats.txt'
dogs = r'..\texts_file\dogs.txt'
filenames = [dogs, cats]

for filename in filenames:
    print(f'We are reading the "{filename}" file:')
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        print(contents)