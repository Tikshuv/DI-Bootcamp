# 🌟 Exercise 1: Currencies
# Instructions
# class Currency:
#     def __init__(self, currency, amount):
#         self.currency = currency
#         self.amount = amount
#
#     # Your code starts HERE
#
#     def __add__(self, other):
#         if isinstance(other, Currency) and other.currency != self.currency:
#             raise TypeError(f'Cannot add between Currency type {self.currency} and {other.currency}')
#         return int(self) + int(other)
#
#     def __iadd__(self, other):
#         if isinstance(other, Currency) and other.currency != self.currency:
#             raise TypeError(f'Cannot add between Currency type {self.currency} and {other.currency}')
#         self.amount += int(other)
#         return self
#
#     def __int__(self):
#         return self.amount
#
#     def __str__(self):
#         return f"{self.amount} {self.currency}"
#
#     def __repr__(self):
#         return f"{self.amount} {self.currency}"
#
#
# c1 = Currency('dollar', 5)
# c2 = Currency('dollar', 10)
# c3 = Currency('shekel', 1)
# c4 = Currency('shekel', 10)

# print('', c1, '\n', int(c2), '\n', str(c3), '\n', repr(c4))
# print(c1+c2)
# c1 += c2
# print(c1)
# c3 += c4
# print(c3)
# print(c4)
# # c1 += c4 # error
# # k = c1 + c4 # error

# # EX 2
# from some_functions import summ
# print(summ(c1, c2))

# Using the code above, implement the relevant methods and dunder methods which will output the results below.
# Hint : When adding 2 currencies which don’t share the same label you should raise an error.
# >>> c1 = Currency('dollar', 5)
# >>> c2 = Currency('dollar', 10)
# >>> c3 = Currency('shekel', 1)
# >>> c4 = Currency('shekel', 10)
#
# >>> str(c1)
# '5 dollars'
#
# >>> int(c1)
# 5
#
# >>> repr(c1)
# '5 dollars'
#
# >>> c1 + 5
# 10
#
# >>> c1 + c2
# 15
#
# >>> c1
# 5 dollars
#
# >>> c1 += 5
# >>> c1
# 10 dollars
#
# >>> c1 += c2
# >>> c1
# 20 dollars
#
# >>> c1 + c3
# TypeError: Cannot add between Currency type <dollar> and <shekel>
#
#
#
# 🌟 Exercise 2: Import
# Instructions
# In a file named func.py create a function that sum 2 numbers, and prints the result
# In a file named exercise_one.py import the function and call it to print the result
# Hint: You can use the the following syntaxes:
#
# import module_name
#
# OR
#
# from module_name import function_name
#
# OR
#
# from module_name import function_name as fn
#
# OR
#
# import module_name as mn
#

#
# 🌟 Exercise 3: String module
# Instructions
# Generate random String of length 5
# Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
# Hint: use the string module
#
# import string
# from random import choice
# rand_str = ''
# while len(rand_str) < 5:
#     rand_str += choice(string.ascii_letters)
# print(rand_str)


#
# 🌟 Exercise 4 : Current Date
# Instructions
# Create a function that displays the current date.
# Hint : Use the datetime module.
#
# from datetime import date
# print(date.today())
#
# Exercise 5 : Amount of time left until January 1st
# Instructions
# Create a function that displays the amount of time left from now until January 1st.
# (Example: the 1st of January is in 10 days and 10:34:01hours).
#

# from datetime import datetime as date
# now = date.now().replace(microsecond=0)
# january = date(2025, 1, 1)
# difference = january - now
# difference = str(difference).replace(',', " and")
# print(f"The 1st of January is in: {difference} hours")

#
# Exercise 6 : Birthday and minutes
# Instructions
# Create a function that accepts a birthdate as an argument (in the format of your choice),
# then displays a message stating how many minutes the user lived in his life.
#
# from datetime import datetime as date
#
#
# def how_long(b_date):
#     time = date.now() - b_date
#     return time
#
#
# birthday = date(1999, 10, 26)
# delta = how_long(birthday)
# minutes = round(delta.total_seconds()/60, 1)
# print(f"You've lived for a total of {minutes} minutes")
#
# Exercise 7 : Faker Module
# Instructions
# Install the faker module, and take a look at the documentation and learn how to properly implement faker in your code.
# Create an empty list called users. Tip: It should be a list of dictionaries.
# Create a function that adds new dictionaries to the users list.
# Each user has the following keys: name, adress, langage_code. Use faker to populate them with fake data.

# from faker import Faker
# fake = Faker()
#
#
# def adding():
#     for i in range(5):
#         users.append({})
#         users[i]['name'] = fake.name()
#         users[i]['address'] = fake.address()
#         users[i]['language_code'] = fake.language_code()
#
#
# users = []
# adding()
# for obj in users:
#     print(obj)
#
