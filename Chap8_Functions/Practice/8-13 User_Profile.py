# 8-13 User_Profile
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first.title()
    profile['last_name'] = last.title()
    for key, value in user_info.items():
        profile[key] = value
    return profile
ximu = build_profile('ximu', 'wang',
                     location = 'Qinhuangdao',
                     age = 26,
                     place_to_go = 'Longyearbyrn, Svalbard')
print(ximu)