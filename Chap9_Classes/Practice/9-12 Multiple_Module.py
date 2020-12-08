# 9-12 Multiple Module
from admin_p_module import Admin

ximu = Admin('ximu', 'wang')
ximu.describe_user()
ximu_privileges = ['shoot',
                   'ski',
                   'love',]
ximu.privileges.privileges = ximu_privileges
ximu.privileges.show_privileges()