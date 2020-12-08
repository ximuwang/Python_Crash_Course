# 9-3 Users
class Users():
    '''A class representing users'''
    def __init__(self, first, last, user_profile):
        '''Initialize the users'''
        self.first_name = first
        self.last_name = last
        self.user_profile = user_profile


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

ximu = Users('ximu', 'wang', '')
ximu.greet_user()
ximu.describe_user()

aki = Users('aki', 'ma', '')
aki.greet_user()
aki.describe_user()