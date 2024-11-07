# Challenge 1 : Sorting
# Instructions
# Write a program that accepts a comma separated sequence of words as input
# and prints the words in a comma-separated sequence after sorting them alphabetically.
# Use List Comprehension
# Example:
#
# Suppose the following input is supplied to the program: without,hello,bag,world
# Then, the output should be: bag,hello,without,world


# words = input("Type a sequence of words separated by comma:\n")
# words_sort = sorted([word.capitalize() for word in words.split(',')])
# # or just words_sort = sorted(words.split(','))
#
#
# print(','.join(words_sort))


# Challenge 2 : Longest Word
# Instructions
# Write a function that finds the longest word in a sentence.
# If two or more words are found, return the first longest word.
# Characters such as apostrophe, comma, period count as part of the word (e.g. O’Connor is 8 characters long).
# Examples
#
# longest_word("Margaret's toy is a pretty doll.") ➞ "Margaret's"
#
# longest_word("A thing of beauty is a joy forever.") ➞ "forever."
#
# longest_word("Forgetfulness is by all means powerless!") ➞ "Forgetfulness"


# def longest_word(sent):
#     word_list = sent.split()
#     max_len = 0
#     longest = 0
#     for i, word in enumerate(word_list):
#         if len(word) > max_len:
#             max_len = len(word)
#             longest = word
#     print(f'Longest word is : {longest}", with a total of {max_len} characters')
#
#
# longest_word(input("Type a sequence of words separated by spaces:\n"))

