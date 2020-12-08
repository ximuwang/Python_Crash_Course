# A admin Module

class Users():
    '''A class representing users'''
    def __init__(self, first, last, user_profile):
        '''Initialize the users'''
        self.first_name = first
        self.last_name = last
        self.user_profile = user_profile
        self.login_attempts = 0


    def describe_user(self):
        '''Display the information of users'''
        print('')
        print("First name: " + self.first_name.title())
        print("Last name: " + self.last_name.title())
        print("Profile: " + self.user_profile)

    def greet_user(self):
        '''Display a message that greet the user'''
        full_name = self.first_name + ' ' + self.last_name
        full_name = full_name.title()
        print('\n\nWelcome! ' + '\n' + full_name)

    def increment_login_attempts(self):
        self.login_attempts += 1
        return self.login_attempts

    def reset_login_attempts(self):
        self.login_attempts = 0
        return self.login_attempts

class Admin(Users):
    '''A class representing Administrators in Users.'''
    def __init__(self, first, last, user_profile=''):
        '''Initialize admin's attribute from Users.'''
        super().__init__(first, last, user_profile)
        self.privileges = Privileges()

class Privileges():
    '''Create a privilege class'''
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        '''Display the privileges of a Administrator'''
        print('The administrator has the following privileges: ')
        if self.privileges:
            for privilege in self.privileges:
                print(privilege)