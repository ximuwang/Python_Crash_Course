# 11-1 City Country

def city_function(city, country):
    '''Return a single string of the form city, country.'''
    return f'{city.title()}, {country.title()}.'

city_function('sandiago', 'chile')