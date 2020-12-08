# admin and privileges module
from user_module import Users

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