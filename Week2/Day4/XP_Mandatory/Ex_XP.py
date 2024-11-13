# Exercise 1 – Random Sentence Generator Instructions Description: In this exercise we will create a random sentence
# generator. We will do this by asking the user how long the sentence should be and then printing the generated
# sentence.
#
# Hint : The generated sentences do not have to make sense.
#
# Download this word list
#
# Save it in your development directory.
#
# Create a function called get_words_from_file. This function should read the file’s content and return the words as
# a collection. What is the correct data type to store the words?
#
# Create another function called get_random_sentence which takes a single parameter called length. The length
# parameter will be used to determine how many words the sentence should have. The function should: use the words
# list to get your random words. the amount of words should be the value of the length parameter.
#
# Take the random words and create a sentence (using a python method), the sentence should be lower case.
#
# Create a function called main which will:
#
# Print a message explaining what the program does.
#
# Ask the user how long they want the sentence to be. Acceptable values are: an integer between 2 and 20. Validate
# your data and test your validation! If the user inputs incorrect data, print an error message and end the program.
# If the user inputs correct data, run your code.
# from random import choice
#
#
# def get_words_from_file(file):
#     with open(file, 'r') as f:
#         content = f.read()
#         # print(content)
#         # print(type(content))
#     return content.split()
#
#
# def get_random_sentence(length, words):
#     sentence = ''
#     sentence = ''.join([choice(words) + ' ' for i in range(length)])
#     sentence = sentence.rstrip().lower()
#     return sentence
#
#
# def main():
#     print("""
#     program accepts value from the user for future length of the sentence. then from 'sowpods.txt'
#     extracts list of words via get_words_from_file func, followed by get_random_sentence func which returns
#     a sentence with inputted length that consists of randomly selected words from the list
#     """)
#     try:
#         length = int(input('How long you want the sentence to be? Acceptable values are: an integer between 2 and 20: '))
#     except ValueError:
#         raise ValueError('It was supposed to be integer')
#     if not 2 <= length <= 20:
#         raise ValueError('Value has to be between 2 and 20')
#     words = get_words_from_file('sowpods.txt')
#     # print(words)
#     rand_s = get_random_sentence(length, words)
#     print(rand_s)
#
#
# main()
#
# 🌟 Exercise 2: Working with JSON
# Instructions
# import datetime
# import json
# sampleJson = """{
#    "company":{
#       "employee":{
#          "name":"emma",
#          "payable":{
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"""
# print(type(sampleJson))
# j_dict = json.loads(sampleJson)
# print(type(j_dict))
# print(j_dict)
# j_dict['company']['employee']['payable']['salary'] = 9000
# print(j_dict)
# # j_dict['company']['employee']['birth_date'] = datetime.date(1995, 10, 23)
# j_dict['company']['employee']['birth_date'] = '1985. 10. 23'
#
# print(j_dict)
#
# with open('sampleJson', 'w') as f:
#     json.dump(j_dict, f)
#
#
# Access the nested “salary” key from the JSON-string above.
# Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
# Save the dictionary as JSON to a file.
