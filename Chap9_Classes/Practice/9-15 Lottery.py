# 9-15 Lottery

from random import choice
pulls = ['1', '43', '324', '42', '2', '71', '23', '81', '123', '74', 'a', 'f', 'e', 'x', 'm']
print(pulls)
count = 1
for i in range(4):
    result = choice(pulls)
    msg = f'the {count} selected result is: {result}'
    print(msg)
    count += 1


pulls = ['1', '43', '324', '42', '2', '71', '23', '81', '123', '74', 'a', 'f', 'e', 'x', 'm']
winning_ticket = []
# we dont want to repeat winning numbers or letters, so we will use a while loop

print('let\'s see the winning ticket: ...')
while len(winning_ticket) < 4:
    pulled_item = choice(pulls)
    # Only add the pulled item to the winning ticket if it hasn't already been pulled
    if pulled_item not in winning_ticket:
        print(f"We pulled a {pulled_item}")
        winning_ticket.append(pulled_item)
