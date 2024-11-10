# Instructions : Old MacDonald’s Farm
# Take a look at the following code and output:
# File: market.py
#
# macdonald = Farm("McDonald")
# macdonald.add_animal('cow',5)
# macdonald.add_animal('sheep')
# macdonald.add_animal('sheep')
# macdonald.add_animal('goat', 12)
# print(macdonald.get_info())
# Output
#
# McDonald's farm
#
# cow : 5
# sheep : 2
# goat : 12
#
#     E-I-E-I-0!
#
# Create the code that is needed to receive the result provided above.
# Below are a few questions to assist you with your code:
#
# Create a class called Farm. How should it be implemented?
# Does the Farm class need an __init__ method? If so, what parameters should it take?
# How many methods does the Farm class need?
# Do you notice anything interesting about the way we are calling the add_animal method?
# What parameters should this function have? How many…?
# Test your code and make sure you get the same results as the example above.
# Bonus: nicely line the text in columns as seen in the example above. Use string formatting.
#
#
# Expand The Farm
# Add a method called get_animal_types to the Farm class. This method should return a sorted list of all the animal
# types (names) in the farm. With the example above, the list should be: ['cow', 'goat', 'sheep'].
#
# Add another method to the Farm class called get_short_info. This method should return the following string:
# “McDonald’s farm has cows, goats and sheeps.”. The method should call the get_animal_types function to get a
# list of the animals.
# Note : In English the plural form of the word “sheep” is sheep. But for the purpose of the exercise,
# let’s say that if there is more than 1 animal, an “s” should be added at the end of the word.

# class Farm:
#
#     def __init__(self, name):
#         self.name = name
#         self.animals = {}
#
#     def add_animal(self, *animals, count=1):
#         for animal in animals:
#             animal = animal.lower()
#             self.animals[animal] = self.animals.get(animal, 0) + count
#             # try:
#             #     self.animals[animal] += count
#             # except KeyError:
#             #     self.animals[animal] = count
#
#     def get_info(self):
#         print(f"{self.name}'s farm\n")
#         for animal, count in self.animals.items():
#             print(f"{animal}: {count}")
#         print("\n\t E-I-E-I-O")
#
#     def get_animal_types(self):
#         types = sorted(list(self.animals.keys()))
#         return types
#
#     def short_info(self):
#         edit_animals = self.get_animal_types()
#         for i, animal in enumerate(edit_animals):
#             if self.animals[animal] > 1:
#                 edit_animals[i] += 's'
#         print(f"{self.name}'s farm has", ','.join(edit_animals[:-1]), f"and {edit_animals[-1]}")
#
#
# mcdonald = Farm('McDonald')
# mcdonald.add_animal('sheep')
# mcdonald.add_animal('sheep', count=5)
# mcdonald.add_animal('Cow', count=12)
# mcdonald.add_animal('goat', count=3)
# mcdonald.add_animal('goat')
# mcdonald.add_animal('goat')
# mcdonald.add_animal('dog', 'cat', 'tiger', 'tiger')
# mcdonald.get_info()
# print(mcdonald.get_animal_types())
# mcdonald.short_info()
#
