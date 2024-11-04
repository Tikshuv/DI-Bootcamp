# Exercise 1 : Favorite Numbers
# Instructions
# Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.
# Remove the last number.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.
#
# my_nums = {3, 7}
# my_nums.remove(7)
# print(my_nums)
# fr_nums = {9, 11}
# our_nums = my_nums.union(fr_nums)
# print(my_nums)
# print(our_nums)
#
# 🌟 Exercise 2: Tuple
# Instructions
# Given a tuple which value is integers, is it possible to add more integers to the tuple?
#
# int_tuple = (3, 2, 7, 4, 2)
# int_tuple = list(int_tuple)
# print(int_tuple)
# int_tuple.append(5)
# int_tuple = tuple(int_tuple)
# print(int_tuple, type(int_tuple))
#
# 🌟 Exercise 3: List
# Instructions
# Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];
#
# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Add “Kiwi” to the end of the list.
# Add “Apples” to the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)
#
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.remove('Banana')
# basket.remove('Blueberries')
# print(basket)
# basket.append('Kiwi')
# basket.insert(0, 'Apples')
# print(basket)
# print(basket.count('Apples'))
# while len(basket):
#     basket.pop()
#     print(basket)
# print(f"Basket now contains {len(basket)} items")
#
# 🌟 Exercise 4: Floats
# Instructions
# Recap – What is a float? What is the difference between an integer and a float?
# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
# Can you think of another way to generate a sequence of floats?
#
# floats = [1 + 0.5 * i for i in range(1, 9)]
# print(floats)
#
# 🌟 Exercise 5: For Loop
# Instructions
# Use a for loop to print all numbers from 1 to 20, inclusive.
# Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.
#
# for num in range(1, 21):
#     print(num)
# nums = list(range(1, 21))
# print(nums)
# for i, num in enumerate(nums):
#     if i % 2 == 0:
#         print(num)

#
# 🌟 Exercise 6 : While Loop
# Instructions
# Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.
#
# my_name = 'Dzmitry'
# your_name = ''
# while my_name != your_name:
#     your_name = input('Enter your name: ')

#
# 🌟 Exercise 7: Favorite fruits
# Instructions
# Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# Now that we have a list of fruits, ask the user to input a name of any fruit.
# If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.
#
# fruit = input("What's your favourite fruits? (Please use space if you have more than one)\n")
# fruits = set(fruit.split(' '))
# print(fruits)
# if input('Name a fruit\n') in fruits:
#     print("You chose one of your favourite fruits! Enjoy!")
# else:
#     print("You chose a new fruit. I hope you enjoy")
#
# Exercise 8: Who ordered a pizza ?
# Instructions
# Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).
#
# topping = ''
# toppings = []
# while True:
#     topping = input('Choose a next topping for your pizza (to stop type "quit")\n ')
#     if topping == 'quit':
#         break
#     else:
#         print(f"We'll add {topping} to your order")
#         toppings.append(topping)
# print("Toppings of your choice are: ", ', '.join(toppings), f'\nAnd your total is: {10+2.5 * len(toppings)}')
#
# Exercise 9: Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.
#
# Ask a family the age of each person who wants a ticket.
# Store the total cost of all the family’s tickets and print it out.
#
# family = int(input('How many tickets? '))
# fam_age = []
# your_cost = 0
# for i in range(family):
#     fam_age.append(int(input(f"What's the age of {i+1} person? ")))
#     if 3 < fam_age[i] < 12:
#         your_cost += 10
#     elif fam_age[i] > 12:
#         your_cost += 15
# print(f"Total cost is: {your_cost}")
#
# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
# At the end, print the final list.
#
# teen_list = ['Mark', 'Clark', 'Sean', 'Bean']
# for name in teen_list.copy():
#     if not 16 <= int(input(f"{name}, what's your age?\n")) <= 21:
#         teen_list.remove(name)
# if len(teen_list) > 0:
#     print(", ".join(teen_list), ' are allowed to watch the movie')
# else:
#     print('No one is going to watch a movie today')

#
# Exercise 10 : Sandwich Orders
# Instructions
# Using the list below :
#
# sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich",
# "Chicken sandwich", "Pastrami sandwich"]
#
# The deli has run out of pastrami, use a while loop to remove all occurrences of “Pastrami sandwich” from
# sandwich_orders.
# We need to prepare the orders of the clients: Create an empty list called finished_sandwiches. One
# by one, remove each sandwich from the sandwich_orders while adding them to the finished_sandwiches list. After all
# the sandwiches have been made, print a message listing each sandwich that was made, such as: I made your tuna
# sandwich I made your avocado sandwich I made your egg sandwich I made your chicken sandwich

# sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich",
#                    "Chicken sandwich", "Pastrami sandwich"]
# while 'Pastrami sandwich' in sandwich_orders:
#     sandwich_orders.remove('Pastrami sandwich')
# print(sandwich_orders)
#
# finished_sandwiches = []
# while sandwich_orders:
#     finished_sandwiches.append(sandwich_orders.pop())
# for sandwich in finished_sandwiches:
#     print(f"I made your {sandwich}")
