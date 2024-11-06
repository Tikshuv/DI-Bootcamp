# Exercise 1 : What are you learning ?
# Instructions
# Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
# Call the function, and make sure the message displays correctly.
#
# def display_message():
#     print("In this course I'm learning Data Analysys")
#
#
# display_message()

#
# 🌟 Exercise 2: What’s your favorite book ?
# Instructions
# Write a function called favorite_book() that accepts one parameter called title.
# The function should print a message, such as "One of my favorite books is <title>".
# For example: “One of my favorite books is Alice in Wonderland”
# Call the function, make sure to include a book title as an argument when calling the function.
#
# def favorite_book(title):
#     print(f'One of my favorite books is: "{title}"')
#
#
# my_book = 'Strange Case of Dr Jekyll and Mr Hyde'
# favorite_book(my_book)

#
# 🌟 Exercise 3 : Some Geography
# Instructions
# Write a function called describe_city() that accepts the name of a city and its country as parameters.
# The function should print a simple sentence, such as "<city> is in <country>".
# For example “Reykjavik is in Iceland”
# Give the country parameter a default value.
# Call your function.
#
# def describe_city(city, country='Belarus'):
#     print(f"{city} is in {country}")
#
#
# my_city = 'Minsk'
# describe_city(my_city)
#
# Exercise 4 : Random
# Instructions
# Create a function that accepts a number between 1 and 100 and generates another number
# randomly between 1 and 100. Use the random module.
# Compare the two numbers, if it’s the same number, display a success message,
# otherwise show a fail message and display both numbers.
#
# from random import choice
#
#
# def rand_compare(number):
#     def_number = choice(range(1, 101))
#     if number == def_number:
#         print('Success')
#     else:
#         print(f"Mission failed, your number is: {number} and function's number is: {def_number}")
#
#
# rand_compare(49)

#
# 🌟 Exercise 5 : Let’s create some personalized shirts !
# Instructions
# Write a function called make_shirt() that accepts a size and the text of a message
# that should be printed on the shirt.
# The function should print a sentence summarizing the size
# of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
# Call the function make_shirt().
#
# Modify the make_shirt() function so that shirts are
# large by default with a message that reads “I love Python” by default.
# Call the function, in order to make a large shirt with the default message
# Make medium shirt with the default message
# Make a shirt of any size with a different message.
#
# Bonus: Call the function make_shirt() using keyword arguments.
#
# def make_shirt(size='L', text="I love Python"):
#     print(f'The size of the shirt is {size} and the text is "{text}"')
#
#
# my_size = 'XL'
# my_text = 'Monkeys'
# make_shirt(my_size, my_text)
# make_shirt()
# make_shirt('M')
# make_shirt(text="Apes")
#
# 🌟 Exercise 6 : Magicians …
# Instructions
# Using this list of magician’s names
#
# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
#
# Create a function called show_magicians(), which prints the name of each magician in the list.
# Write a function called make_great() that modifies the original list
# of magicians by adding the phrase "the Great" to each magician’s name.
# Call the function make_great().
# Call the function show_magicians() to see that the list has actually been modified.
#


# def show_magicians(names):
#     for name in names:
#         print(name)
#     print('')
#
#
# def make_great(names):
#     for i in range(len(names)):
#         names[i] += ' the Great'
#
#
# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
# show_magicians(magician_names)
# make_great(magician_names)
# show_magicians(magician_names)


#
# 🌟 Exercise 7 : Temperature Advice
# Instructions
# Create a function called get_random_temp().
# This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
# Test your function to make sure it generates expected results.
#
# Create a function called main().
# Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
# Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”
#

# Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
# below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
# between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
# between 16 and 23
# between 24 and 32
# between 32 and 40
#
# Change the get_random_temp() function:
# Add a parameter to the function, named ‘season’.
# Inside the function, instead of simply generating
# a random number between -10 and 40, set lower and upper
# limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
# Now that we’ve changed get_random_temp(), let’s change the main() function:
# Before calling get_random_temp(), we will need to decide
# on a season, so that we can call the function correctly. Ask the user to type
# in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
# Use the season as an argument when calling get_random_temp().
#
# from random import uniform
#
#
# def season_calc():
#     month = int(input("Type a number of current month: "))
#     if 2 < month <= 5:
#         return 'spring'
#     if 5 < month <= 8:
#         return 'summer'
#     if 8 < month <= 11:
#         return 'autumn'
#     if month > 0 or month == 12:
#         return 'winter'
#     else:
#         return 'winter'
#
#
# def get_random_temp(season):
#     if season.lower() == 'winter':
#         return round(uniform(-10, 16), 1)
#     elif season.lower() == 'summer':
#         return round(uniform(24, 41), 1)
#     else:
#         return round(uniform(16, 25), 1)
#
#
# def main():
#     # c_season = input("Type a current season(summer/winter/autumn or fall/spring):\n ")
#     c_season = season_calc()
#     print(f"It's a {c_season} right now")
#     temp = get_random_temp(c_season)
#     print(f"The temperature right now is {temp} degrees Celsius")
#     if temp < 0:
#         print("Brrr, that's freezing! Wear some extra layers today")
#     elif temp <= 16:
#         print("Quite chilly! Don't forget your coat")
#     elif temp <= 23:
#         print("Drop your coat")
#     elif temp <= 32:
#         print('Drop your tshirt')
#     elif temp <= 40:
#         print("Don't leave your home")
#
#
# main()
# Bonus: Give the temperature as a floating-point number instead of an integer.
# Bonus: Instead of asking for the season, ask the user for the
# number of the month (1 = January, 12 = December). Determine the season according to the month.
#
#
# 🌟 Exercise 8 : Star Wars Quiz
# Instructions
# This project allows users to take a quiz to test their Star Wars knowledge.
# The number of correct/incorrect answers are tracked and the user
# receives different messages depending on how well they did on the quiz.
#
# Here is an array of dictionaries, containing those questions and answers
#
# data = [
#     {
#         "question": "What is Baby Yoda's real name?",
#         "answer": "Grogu"
#     },
#     {
#         "question": "Where did Obi-Wan take Luke after his birth?",
#         "answer": "Tatooine"
#     },
#     {
#         "question": "What year did the first Star Wars movie come out?",
#         "answer": "1977"
#     },
#     {
#         "question": "Who built C-3PO?",
#         "answer": "Anakin Skywalker"
#     },
#     {
#         "question": "Anakin Skywalker grew up to be who?",
#         "answer": "Darth Vader"
#     },
#     {
#         "question": "What species is Chewbacca?",
#         "answer": "Wookiee"
#     }
# ]
#
#
# Create a function that asks the questions to the user, and check his answers.
# Track the number of correct, incorrect answers. Create a list of wrong_answers
# Create a function that informs the user of his number of correct/incorrect answers.
# Bonus : display to the user the questions he answered wrong, his answer, and the correct answer.
# If he had more then 3 wrong answers, ask him to play again.

# data = [
#     {
#         "question": "What is Baby Yoda's real name?",
#         "answer": "Grogu"
#     },
#     {
#         "question": "Where did Obi-Wan take Luke after his birth?",
#         "answer": "Tatooine"
#     },
#     {
#         "question": "What year did the first Star Wars movie come out?",
#         "answer": "1977"
#     },
#     {
#         "question": "Who built C-3PO?",
#         "answer": "Anakin Skywalker"
#     },
#     {
#         "question": "Anakin Skywalker grew up to be who?",
#         "answer": "Darth Vader"
#     },
#     {
#         "question": "What species is Chewbacca?",
#         "answer": "Wookiee"
#     }
# ]
#
#
# def quiz(q_a):
#     correct = 0
#     incorrect = 0
#     for question in q_a:
#         answer = input(f'{question['question']}\n')
#         if answer.lower() == question['answer'].lower():
#             correct += 1
#         else:
#             incorrect += 1
#             wrongs[question['question']] = answer.title()
#             answers[question['question']] = question['answer']
#         total['Correct answers'] = correct
#         total['Wrong answers'] = incorrect
#
#
# def results(answered, original, result):
#     print(f"You've answered {result['Correct answers']} "
#           f"questions correctly and {result['Wrong answers']} incorrectly")
#     for wrong in answered:
#         print(f"To the question {wrong}\nYou've answered: {answered[wrong]}\n"
#               f"Correct answer was: {original[wrong]}")
#
#
# total = {}
# wrongs = {}
# answers = {}
#
# quiz(data)
# results(wrongs, answers, total)
