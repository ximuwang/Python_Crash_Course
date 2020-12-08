# 10-10 Favorite Number
import json

# try:
#     with open(filename) as f_obj:
#         contents = json.load(f_obj)
#         print('Your favorite number is ' + contents + '!')
# except FileNotFoundError:
#     print('File is not found')
# else:
#     with open(filename, 'w') as f_obj:
#         json.dump(fav_num, f_obj)

def new_favorite_number():
    '''Prompts for the users favorite number.'''
    fav_num = input("What is your favorite number? ")
    filename = r'..\texts_file\favorite_number.json'
    with open(filename, 'w') as f_obj:
        json.dump(fav_num, f_obj)
        return fav_num

def get_favorite_number():
    '''Read the user's favorite number.'''
    filename = r'..\texts_file\favorite_number.json'
    try:
        with open(filename) as f_obj:
            fav_num = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return fav_num
def show_favorite_num():
    '''Display favorite num'''
    fav_num = get_favorite_number()
    if fav_num:
        print("Your favorite number is: " + fav_num + '!')
    else:
        fav_num = new_favorite_number()

show_favorite_num()

