# Exercise 1 : Convert lists into dictionaries
# Instructions
# Convert the two following lists, into dictionaries.
# Hint: Use the zip method


# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# kv_dict = dict(zip(keys, values))
# print(kv_dict)

# Expected output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
#

#
# 🌟 Exercise 2 : Cinemax #2
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.
#
# Given the following object:
# How much does each family member have to pay ?
# Print out the family’s total cost for the movies.

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# check = {}
# cost = 0
# total = 0
# for member, age in family.items():
#     if age > 12:
#         cost = 15
#     elif age >= 3:
#         cost = 10
#     else:
#         cost = 0
#     total +=cost
#     check[member] = cost
# print(check)
# print(total)

#
# Bonus: Ask the user to input the names and ages instead of using the provided family variable (Hint: ask the user
# for names and ages and add them into a family dictionary that is initially empty).

# custom_family = input('Enter your names and ages separating them with spaces:\n')
# fam_list = custom_family.split()
# for i, item in enumerate(fam_list):
#     if item.isdigit():
#         fam_list[i] = int(item)
# family = {fam_list[i]: fam_list[i+1] for i in range(0, len(fam_list), 2)}
# print(family)
# total = 0
# check = {}
# for member, age in family.items():
#     if age > 12:
#         cost = 15
#     elif age >= 3:
#         cost = 10
#     else:
#         cost = 0
#     total += cost
#     check[member] = cost
# print(check)
# print(total)

#
# 🌟 Exercise 3: Zara
# Instructions
# Here is some information about a brand.

#
# name: Zara
# creation_date: 1975
# creator_name: Amancio Ortega Gaona
# type_of_clothes: men, women, children, home
# international_competitors: Gap, H&M, Benetton
# number_stores: 7000
# major_color:
#     France: blue,
#     Spain: red,
#     US: pink, green
#
# 2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).
# The values type_of_clothes and international_competitors should be a list.
# The value of major_color should be a dictionary.
# 3. Change the number of stores to 2.
# 4. Print a sentence that explains who Zaras clients are.
# 5. Add a key called country_creation with a value of Spain.
# 6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
# 7. Delete the information about the date of creation.
# 8. Print the last international competitor.
# 9. Print the major clothes colors in the US.
# 10. Print the amount of key value pairs (ie. length of the dictionary).
# 11. Print the keys of the dictionary.
# 12. Create another dictionary called more_on_zara with the following details:
#
# creation_date: 1975
# number_stores: 10 000
#
#
# 13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
# 14. Print the value of the key number_stores. What just happened ?
#
# brand = {'name': 'Zara', 'creation_date': 1975,
#          'creator_name': 'Amancio Ortega Gaona',
#          'type_of_clothes': ['men', 'women', 'children', 'home'],
#          'international_competitors': ['Gap', 'H & M', 'Benetton'],
#          'number_of_stores': 7000, 'major_color': {'France': 'blue', 'Spain': 'red', 'US': ['pink', 'green']}}
#
# brand['number_of_stores'] = 2
# for client in brand['type_of_clothes']:
#     print(f"Our clients are interested in products for {client}")
# brand['country_creation'] = 'Spain'
# if 'international_competitors' in brand:
#     brand['international_competitors'].append('Desigual')
# del(brand['creation_date'])
# print(brand['international_competitors'][-1])
# print(' and '.join(brand['major_color']['US']))
# print(len(brand))
# for key in brand:
#     print(key)
# more_on_zara = {'creation_date': 1975, 'number_of_stores': 10000}
# print(brand['number_of_stores'])
# brand.update(more_on_zara)
# print(brand)
# print(brand['number_of_stores'])
# updated key number of stores overwrites the one that was in original dictionary
#
#
# Exercise 4 : Disney characters
# Instructions
# Use this list :
#
# users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
# Analyse these results :
#
# #1/

# >>> print(disney_users_A)
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}
#
# #2/
#
# >>> print(disney_users_B)
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
#
# #3/
#
# >>> print(disney_users_C)
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}
#
#
# Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
# Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
# Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
# Only recreate the 1st result for:
# The characters, which names contain the letter “i”.
# The characters, which names start with the letter “m” or “p”.

# users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
# dict_users = {}
# dict_users2 = {}
# dict_users3 = {}
# dict_users4 = {}
# dict_users5 = {}
# sorted_users = sorted(users)
# for i in range(len(users)):
#     dict_users[users[i]] = i
#     dict_users2[i] = users[i]
#     dict_users3[sorted_users[i]] = i
#     if 'i' in users[i]:
#         dict_users4[users[i]] = 0 + len(dict_users4)
#     if users[i][0] == 'M' or users[i][0] == 'P':
#         dict_users5[users[i]] = 0 + len(dict_users5)
#
# print(dict_users)
# print(dict_users2)
# print(dict_users3)
# print(dict_users4)
# print(dict_users5)
