# Name: X.W
# Date: 11/6/2020
# Topic: Try it your self practice

# Page 62
# 2-3
name = 'Ximu. W'
greetings = 'Hello {}, would you like to learn some Python today?'.format(name)
print(greetings)

# 2-4
print(name.upper())
print(name.lower())
print(name.title())

# 2-5
# class FamousWord:
#     def __init__(self):
#         pass
#     def famous_quote():
#         global author, quote
#         author = input(">")
#         author = author.title()
#         quote = input(">")
#         quote = quote.capitalize()
#         a = print(author, 'said,', "'{}'".format(quote))
# x = FamousWord
# x.famous_quote()
#
# # 2-6
# famous_person = author
# message = quote
# print(famous_person, "said,", '"{}"'.format(message))

# 2-7
first_name = '  Greg'
last_name = ' Olsen    '
middle_name = 'Russ '
full_name = (first_name.lstrip() + '\t' + middle_name.rstrip() + "\n" + last_name.strip())
print(full_name)

# 2-8
print(5 + 3)
print(2 * 4)
print(1000 - 992)
print(int(64 / 8))

# 2-9
favorite_number = 8
message = "Your favorite number is" + ": " + str (favorite_number)
print(message)