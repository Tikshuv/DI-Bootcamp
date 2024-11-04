# Challenge 1
# Ask the user for a number and a length.
# Create a program that prints a list of multiples of the number until the list length reaches length.
# Examples
#
# number: 7 - length 5 ➞ [7, 14, 21, 28, 35]
#
# number: 12 - length 10 ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]
#
# number: 17 - length 6 ➞ [17, 34, 51, 68, 85, 102]
#
# number = int(input('Enter a number: '))
# length = int(input('Enter a length '))
# multiples = []
# for i in range(length):
#     multiples.append(number*(i+1))
# print(multiples)
#
# Challenge 2 Write a program that asks a string to the user, and display a new string with any duplicate consecutive
# letters removed.
# Examples
#
# user's word : "ppoeemm" ➞ "poem"
#
# user's word : "wiiiinnnnd" ➞ "wind"
#
# user's word : "ttiiitllleeee" ➞ "title"
#
# user's word : "cccccaaarrrbbonnnnn" ➞ "carbon"
# Notes
# Final strings won’t include words with double letters (e.g. “passing”, “lottery”).
#
# text = input('Enter a string with duplicate consecutive letters:\n')
# edit_text = list(text)
# text_copy = edit_text.copy()
# i = 0
# while i < len(edit_text)-1:
#     if edit_text[i] == edit_text[i+1]:
#         edit_text.pop(i+1)
#         i-=1
#     else:
#         i+=1
# edit_text = ''.join(edit_text)
# print(edit_text)
