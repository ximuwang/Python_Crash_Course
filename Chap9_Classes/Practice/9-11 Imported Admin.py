# 9-11 Imported Admin

from admin import Privileges, Users, Admin

ximu = Admin('ximu', 'wang')
ximu_privileges = ['shoot',
                    'kill',
                    'love']
ximu.privileges.privileges = ximu_privileges
ximu.privileges.show_privileges()
ximu.describe_user()
ximu.greet_user()
login = ximu.login_attempts
print(login)
ximu.increment_login_attempts()
ximu.increment_login_attempts()
ximu.increment_login_attempts()
ximu.increment_login_attempts()
print(ximu.login_attempts)
ximu.reset_login_attempts()
print(ximu.login_attempts)