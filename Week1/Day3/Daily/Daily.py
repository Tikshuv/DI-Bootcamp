# Challenge 1
# Ask a user for a word
# Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.
#
# Make sure the letters are the keys.
# Make sure the letters are strings.
# Make sure the indexes are stored in a list and those lists are values.
# Examples
#
# "dodo" ➞ { "d": [0, 2], "o": [1, 3] }
#
# "froggy" ➞ { "f":  [0], "r": [1], "o": [2], "g": [3, 4], "y": [5] }
#
# "grapes" ➞ { "g": [0], "r": [1], "a": [2], "p": [3]}
#
# word = input("Please, type a word:\n")
# letter_dict = {letter: [] for letter in word}
# for i, letter in enumerate(word):
#     letter_dict[letter].append(i)
# print(letter_dict)
#
# Challenge 2
# Create a program that prints a list of the items you can afford in the store with the money you have in your wallet.
# Sort the list in alphabetical order.
# Return “Nothing” if you can’t afford anything from the store.
# Hint : make sure to convert the amount from dollars to numbers. Create a program that deletes the $ sign, and the comma (for thousands)
#The key is the product, the value is the price
#
# items_purchase = {
#   "Water": "$1",
#   "Bread": "$3",
#   "TV": "$1,000",
#   "Fertilizer": "$20"
# }
#
# wallet = "$300"
#
# ➞ ["Bread", "Fertilizer", "Water"]
#
# items_purchase = {
#   "Apple": "$4",
#   "Honey": "$3",
#   "Fan": "$14",
#   "Bananas": "$4",
#   "Pan": "$100",
#   "Spoon": "$2"
# }
#
# wallet = "$100"
#
# ➞ ["Apple", "Bananas", "Fan", "Honey", "Spoon"]
#
# # In fact the prices of Apple + Honey + Fan + Bananas + Pan is more that $100, so you cannot by the Pan,
# # instead you can by the Spoon that is $2
#
# items_purchase = {
#   "Phone": "$999",
#   "Speakers": "$300",
#   "Laptop": "$5,000",
#   "PC": "$1200"
# }
#
# wallet = "$1"
#
# ➞ "Nothing"

# wallet = input("How much money you have?(default is 100$\n") or '100$'
# wallet = int(''.join(num for num in wallet if num.isdigit()))
# items_purchase = {
#   "Apple": "$4",
#   "Honey": "$3",
#   "Fan": "$14",
#   "Bananas": "$4",
#   "Pan": "$100",
#   "Spoon": "$2"
# }
# shopp_list = []
# spending = wallet
# for product, price in items_purchase.items():
#     items_purchase[product] = int(''.join(num for num in price if num.isdigit()))
# for product, price in items_purchase.items():
#     if wallet - price >= 0:
#         if spending - price > 0:
#             shopp_list.append(product)
#             spending -= price
#         else:
#             print(f"You could've afforded {product}, but not with", ', '.join(shopp_list))
# if not shopp_list:
#     print('Nothing')
# else:
#     shopp_list = sorted(shopp_list)
#     print(shopp_list)




