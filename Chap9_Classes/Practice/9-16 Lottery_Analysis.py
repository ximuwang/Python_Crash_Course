# 9-16 Lottery Analysis
from random import choice

def get_winning_ticket(pulls):
    winning_ticket = []
    # we dont want to repeat winning numbers or letters, so we will use a while loop
    print('let\'s see the winning ticket: ...')
    while len(winning_ticket) < 4:
        pulled_item = choice(pulls)
        if pulled_item not in winning_ticket:
            print(f'we pulled a {pulled_item}')
            winning_ticket.append(pulled_item)
    return winning_ticket


def check_winning_ticket(played_ticket, winning_ticket):
    '''Check all elements in the played ticket. If any are not
        in the winning ticket, return False.'''
    for element in played_ticket:
        if element not in winning_ticket:
            return False
    '''We must have a winning ticket!'''
    return True

def make_random_ticket(pulls):
    '''Return a random ticket from a set of possibilities.'''
    ticket = []
    while len(ticket) < 4:
        pulled_ticket = choice(pulls)
        if pulled_ticket not in ticket:
            ticket.append(pulled_ticket)

    return ticket

pulls = ['1', '43', '324', '42', '2', '71', '23', '81', '123', '74', 'a', 'f', 'e', 'x', 'm']
winning_ticket = get_winning_ticket(pulls)

# Let's set a max number of tries, in case this takes forever!
plays = 0
won = False
max_tries = 1_000_000

while not won:
    new_ticket = make_random_ticket(pulls)
    won = check_winning_ticket(new_ticket, winning_ticket)
    plays += 1
    if plays >= max_tries:
        break

if won:
    print("We have a winning ticket!")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")
    print(f"It only took {plays} tries to win!")
else:
    print(f"Tried {plays} times, without pulling a winner. :(")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")


