# 8-12 Sandwiches
def sandwich_items(*items):
    print('We will make a great sandwich.')
    for item in items:
        print('We are adding', item, "to your sandwich.")
    print('Your sandwich is done')
sandwich_items(' meatball', 'lettuce', 'tomatoes')