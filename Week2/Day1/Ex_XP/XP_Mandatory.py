# Exercise 1: Cats
# Instructions
# Using this class
#
# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age
# Instantiate three Cat objects using the code provided above.
# Outside of the class, create a function that finds the oldest cat and returns the cat.
# Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.
#
# class Cat:
#     cats = []
#
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age
#         Cat.cats.append(self)
#
#
# cat1 = Cat('Bianka', 2)
# cat2 = Cat('Raska', 5)
# cat3 = Cat('Mark', 1)
#
#
# def oldest_cat_calc():
#     age = 0
#     for i, cat in enumerate(Cat.cats):
#         if cat.age > age:
#             age = cat.age
#             oldest = cat
#     return oldest
#
#
# oldest_cat = oldest_cat_calc()
# print(f"Oldest cat is {oldest_cat.name} with an age of {oldest_cat.age}")

#
# 🌟 Exercise 2 : Dogs
# Instructions
# Create a class called Dog.
# In this class, create an __init__ method that takes two parameters : name and height.
# This function instantiates two attributes, which values are the parameters.
# Create a method called bark that prints the following string “<dog_name> goes woof!”.
# Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
# Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
# Print the details of his dog (ie. name and height) and call the methods bark and jump.
# Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# Print the details of her dog (ie. name and height) and call the methods bark and jump.
# Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.

# class Dog:
#
#     def __init__(self, name, height):
#         self.name = name
#         self.height = height
#
#     def bark(self):
#         print(f"{self.name} goes woof!")
#
#     def jump(self):
#         x = self.height * 2
#         print(f"{self.name} jumps {x}cm high!")
#
#
# davids_dog = Dog('Rex', 50)
# sarahs_dog = Dog('Teacup', 20)
# print(f"David's dog name is {davids_dog.name} and dog's height is {davids_dog.height}")
# davids_dog.bark()
# davids_dog.jump()
# print(f"Sarah's dog name is {sarahs_dog.name} and dog's height is {sarahs_dog.height}")
# sarahs_dog.bark()
# sarahs_dog.jump()
# if davids_dog.height > sarahs_dog.height:
#     print(f"{davids_dog.name} is bigger than {sarahs_dog.name}")
# else:
#     print(f"{sarahs_dog.name} is bigger than {davids_dog.name}")

#
#
# 🌟 Exercise 3 : Who’s the song producer?
# Instructions
# Define a class called Song, it will show the lyrics of a song.
# Its __init__() method should have two arguments: self and lyrics (a list).
# Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.
# Create an object, for example:
#
# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
#
#
# Then, call the sing_me_a_song method. The output should be:
#
# There’s a lady who's sure
# all that glitters is gold
# and she’s buying a stairway to heaven
#
# class Song:
#
#     def __init__(self, lyrics):
#         self.lyrics = lyrics
#
#     def sing_me_a_song(self):
#         for line in self.lyrics:
#             print(line)
#
#
# stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
# stairway.sing_me_a_song()
#
# Exercise 4 : Afternoon at the Zoo
# Instructions
# Create a class called Zoo.
# In this class create a method __init__ that takes one parameter: zoo_name.
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).
# Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
# Create a method called get_animals that prints all the animals of the zoo.
# Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.
# Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
# Example
#
# {
#     1: "Ape",
#     2: ["Baboon", "Bear"],
#     3: ['Cat', 'Cougar'],
#     4: ['Eel', 'Emu']
# }
#
#
# Create a method called get_groups that prints the animal/animals inside each group.
#
# Create an object called ramat_gan_safari and call all the methods.
# Tip: The zookeeper is the one who will use this class.
# Example
# Which animal should we add to the zoo --> Giraffe
# x.add_animal(Giraffe)

#
# class Person:
#     def __init__(self, p_name, p_age, p_height):
#         self.name = p_name
#         self.age = p_age
#         self.height = p_height
#
#     def presentation(self):
#         print(f"Halo, my name is {self.name}, I am {self.age} old")
#
#
# me = Person('Dzmitry', 25, 180)
# print(f"Name: {me.name}, Age: {me.age}, Height: {me.height}")
# me.presentation()
#

class Zoo:

    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
        else:
            print("There's no such animal in the", self.name)

    def sort_animal(self):
        sorted_animals = sorted(self.animals)
        alph_animals = {}
        animals = []
        i = 1
        letter = sorted_animals[0][0]
        for animal in sorted_animals:
            if letter.lower == animal[0].lower:
                animals.append(animal)
                alph_animals[i] = animals
            else:
                i += 1
                letter = animal[0]
                animals = [animal]
                alph_animals[i] = animals
        print(alph_animals)
        return alph_animals

    def get_groups(self):
        animals = self.sort_animal()
        for group, animals in animals.items():
            print(f"Group of animals number {group} consists of: {[animal for animal in animals]}")


ramat_gan_safari = Zoo("Ramat Gan Safari")
ramat_gan_safari.animals = ['Monkey', 'Zebra', 'Ape', 'Dog', 'Cat', 'Panda', 'Baboon', 'Bear']
ramat_gan_safari.add_animal('Giraffe')
ramat_gan_safari.get_groups()
ramat_gan_safari.sort_animal()

