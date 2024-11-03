# Exercise 1 : Hello World
# Instructions
# Print the following output in one line of code:
#
# Hello world
# Hello world
# Hello world
# Hello world

# print('Hello world\n'*4)

#
# Exercise 2 : Some Math
# Instructions
# Write code that calculates the result of: (99^3)*8 (meaning 99 to the power of 3, times 8).

# b, a, c = 99, 3, 8
# print(b**a*c)

# Exercise 3 : What is the output ?
# Instructions
# Predict the output of the following code snippets:
# >>> 5 < 3 False
# >>> 3 == 3 True
# >>> 3 == "3" Error
# >>> "3" > 3 Error
# >>> "Hello" == "hello" False
#

#
# 🌟 Exercise 4 : Your computer brand
# Instructions
# Create a variable called computer_brand which value is the brand name of your computer.
# Using the computer_brand variable print a sentence that states the following: "I have a <computer_brand> computer".
#
# computer_brand = 'MBook_m3'
# print(f"I have a {computer_brand} computer")
#
# 🌟 Exercise 5 : Your information Instructions Create a variable called name, and set it’s value to your name.
# Create a variable called age, and set it’s value to your age. Create a variable called shoe_size, and set it’s
# value to your shoe size. Create a variable called info and set it’s value to an interesting sentence about
# yourself. The sentence must contain all the variables created in parts 1, 2 and 3. Have your code print the info
# message. Run your code
#
# name = 'Dzmitry'
# age = 25
# shoe_size = 43
# info = f"\tName: {name}\n\tAge: {age}\n\tShoe size: {shoe_size}"
# print(info)
#
# 🌟 Exercise 6 : A & B
# Instructions
# Create two variables, a and b.
# Each variable value should be a number.
# If a is bigger then b, have your code print Hello World.
#
# a = 3
# b = 3.0000000001
# if a > b:
#     print('Hello world')
#
# Exercise 7 : Odd or Even
# Instructions
# Write code that asks the user for a number and determines whether this number is odd or even.
#
# number = input('Type a number: ')
# while not number.isdecimal:
#     number = input('Please, type a number')
# if abs(int(number)) % 2 == 1:
#     print(f"Your number({number}) is an odd number")
# else:
#     print(f"Your number({number}) is an even number")
#
# 🌟 Exercise 8 : What’s your name ? Instructions Write code that asks the user for their name and determines whether
# or not you have the same name, print out a funny message based on the outcome.
#
# my_name = 'Dzmitry'
# user_name = input('Enter your name: ')
# if my_name == user_name.title():
#     print("We share same name")
# else:
#     print("We're different")
#
# 🌟 Exercise 9 : Tall enough to ride a roller coaster
# Instructions
# Write code that will ask the user for their height in centimeters.
# If they are over 145cm print a message that states they are tall enough to ride.
# If they are not tall enough print a message that says they need to grow some more to ride.

# number = input("Enter your height(use whole numbers or I'll break: ")
# while not number.isdecimal:
#     number = input('Please, enter your height using only numbers')
# number = abs(int(number))
# if number > 145:
#     print("Tall enough for a ride")
# else:
#     print("Too short, need to grow some more for a ride")

