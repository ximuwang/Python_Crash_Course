# 10-13 Verify User

import json

def get_stored_username():
    '''Get stored username if available.'''
    filename = r'..\texts_file\username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    '''Prompt for a new username.'''
    username = input("What is your name? ")
    filename = r'..\texts_file\username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        return username
def greet_user():
    '''Great the user by name.'''
    username = get_stored_username()
    if username:
        correct = input(f"Are you {username}? (y/n)")
        if correct == 'y':
            print("Welcome back, " + username + '!')
        else:
            username = get_new_username()
            print("We will remember you when you come back, " + username + '!')
    else:
        username = get_new_username()
        print("We will remember you when you come back, " + username + '!')


greet_user()
