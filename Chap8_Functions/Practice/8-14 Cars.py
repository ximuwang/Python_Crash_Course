# 8-14 cars
def car_info(manufacturer, model, **info):
    profile = {}
    profile['Manufacturer'] = manufacturer.title()
    profile['Model'] = model.title()
    for key, value in info.items():
        profile[key] = value
    return profile

subaru = car_info('Subaru', 'Forester',
                  year = 1999,
                  seats = 5)
print(subaru)
car = car_info('subaru', 'outback',
               color = 'blue',
               tow_package = True)
print(car)

