# 🌟 Exercise 1 : Pets
# Instructions
# Using this code:
#
# class Pets:
#     def __init__(self, animals):
#         self.animals = animals
#
#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())
#
#
# class Cat:
#     all_cats = []
#     is_lazy = True
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Cat.all_cats.append(self)
#
#     def walk(self):
#         return f'{self.name} is just walking around'
#
#
# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
#
# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
#
# class Siamese(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
#
# cat1 = Bengal('Jo', 3)
# cat2 = Chartreux('Ro', 5)
# cat3 = Siamese('So', 10)
# for cat in Cat.all_cats:
#     print(cat.name)
# sara_pets = Pets(Cat.all_cats)
# sara_pets.walk()

#
# Create another cat breed named Siamese which inherits from the Cat class.
# Create a list called all_cats, which holds three cat instances : one Bengal, one Chartreux and one Siamese.
# Those three cats are Sara’s pets. Create a variable called sara_pets which value is an instance of the Pet class, and pass the variable all_cats to the new instance.
# Take all the cats for a walk, use the walk method.
#
#
# 🌟 Exercise 2 : Dogs
# Instructions
# Create a class called Dog with the following attributes name, age, weight.
# Implement the following methods in the Dog class:
# bark: returns a string which states: “<dog_name> is barking”.
# run_speed: returns the dogs running speed (weight/age*10).
# fight : takes a parameter which value is another Dog instance, called other_dog.
# This method returns a string stating which dog won the fight.
# The winner should be the dog with the higher run_speed x weight.
#
# Create 3 dogs and run them through your class.

# class Dog:
#     def __init__(self, name, age, weight):
#         self.name = name
#         self.age = age
#         self.weight = weight
#
#     def bark(self):
#         print(f"{self.name} is barking")
#
#     def run_speed(self):
#         return self.weight / self.age * 10
#
#     def fight(self, opponent):
#         our_dog_f = self.weight * self.run_speed()
#         opponent_f = opponent.weight * opponent.run_speed()
#         if our_dog_f > opponent_f:
#             print(f"{self.name}({our_dog_f}) won the fight with {opponent.name}({opponent_f})")
#         elif our_dog_f < opponent_f:
#             print(f"{opponent.name}({opponent_f}) won the fight with {self.name}({our_dog_f})")
#         else:
#             print("That's a tie")
#
#
# dog1 = Dog('Ba', 5, 50)
# dog2 = Dog('Ka', 10, 20)
# dog3 = Dog('Sa', 1, 10)
# dog2.bark()
# print(f"{dog1.name}'s speed is: {dog1.run_speed()}")
# dog3.fight(dog1)
#


# 🌟 Exercise 3 : Dogs Domesticated
# Instructions
# Create a new python file and import your Dog class from the previous exercise.
# In the new python file, create a class named PetDog that inherits from Dog.
# Add an attribute called trained to the __init__ method,
# this attribute is a boolean and the value should be False by default.
# Add the following methods:
# train: prints the output of bark and switches the trained boolean to True
#
# play: takes a parameter which value is a few names of other Dog instances (use *args).
# The method should print the following string: “dog_names all play together”.
#
# do_a_trick: If the dog is trained the method should print one of the following sentences at random:
# “dog_name does a barrel roll”.
# “dog_name stands on his back legs”.
# “dog_name shakes your hand”.
# “dog_name plays dead”.
#

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        print(f"{self.name} is barking")

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, opponent):
        our_dog_f = self.weight * self.run_speed()
        opponent_f = opponent.weight * opponent.run_speed()
        if our_dog_f > opponent_f:
            print(f"{self.name}({our_dog_f}) won the fight with {opponent.name}({opponent_f})")
        elif our_dog_f < opponent_f:
            print(f"{opponent.name}({opponent_f}) won the fight with {self.name}({our_dog_f})")
        else:
            print("That's a tie")


# dog1 = Dog('Ba', 5, 50)
# dog2 = Dog('Ka', 10, 20)
# dog3 = Dog('Sa', 1, 10)
# dog2.bark()
# print(f"{dog1.name}'s speed is: {dog1.run_speed()}")
# dog3.fight(dog1)
#
#
# Exercise 4 : Family
# Instructions
# Create a class called Family and implement the following attributes:
#
# members: list of dictionaries
# last_name : (string)
#
# Implement the following methods:
#
# born: adds a child to the members list (use **kwargs), don’t forget to print a message congratulating the family.
# is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not.
# family_presentation: a method that prints the family’s last name and all the members’ details.
#
# Create an instance of the Family class, with the last name of your choice,
# and the below members. Then call all the methods you created in Point 2.
#
# [
#     {'name':'Michael','age':35,'gender':'Male','is_child':False},
#     {'name':'Sarah','age':32,'gender':'Female','is_child':False}
# ]
#
# class Family:
#     def __init__(self, members, last_name):
#         self.members = members
#         self.last_name = last_name
#
#     def born(self, **kwargs):
#         self.members.append(kwargs)
#         print("Congratulations with a newborn")
#
#     def is_18(self, name):
#         for member in self.members:
#             if member['name'] == name:
#                 if member['age'] > 18:
#                     return True
#                 else:
#                     return False
#
#     def family_presentation(self):
#         print(self.last_name)
#         for member in self.members:
#             print(''.join(f"{key} is {value}, " for key, value in member.items() if key != 'is_child'))
#
#
# family = Family([
#     {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
#     {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
# ], 'Simpsons')
# family.born(name='Jack', age=0, gender='Unknown', is_child=True)
# print(family.is_18('Sarah'))
# family.family_presentation()
#
# Exercise 5 : TheIncredibles Family
# Instructions
# Create a class called TheIncredibles. This class should inherit from the Family class:
# This is no random family they are an incredible family, therefore the members attributes,
# will be a list of dictionaries containing the additional keys : power and incredible_name. (See Point 4)
#
#
# Add a method called use_power, this method should print the power of a member only if they are over 18 years old.
# If not raise an exception (look up exceptions) which stated they are not over 18 years old.
#
#
# Add a method called incredible_presentation which :
#
# Print a sentence like “*Here is our powerful family **”
# Prints the family’s last name and all the members’ details (ie. use the super() function,
# to call the family_presentation method)
#
#
# Create an instance of the Incredibles class, with the “Incredibles” last name, and the below members.
#
#     [
#         {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
#         {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
#     ]
#
#
# Call the incredible_presentation method.
#
#
# Use the born method inherited from the Family class to add Baby Jack with the following power: “Unknown Power”.
#
#
# Call the incredible_presentation method again.

# class Family:
#     def __init__(self, members, last_name):
#         self.members = members
#         self.last_name = last_name
#
#     def born(self, **kwargs):
#         self.members.append(kwargs)
#         print("Congratulations with a newborn")
#
#     def is_18(self, name):
#         for member in self.members:
#             if member['name'] == name:
#                 if member['age'] > 18:
#                     return True
#                 else:
#                     return False
#
#     def family_presentation(self):
#         print(self.last_name)
#         for member in self.members:
#             print(''.join(f"{key} is {value}, " for key, value in member.items() if key != 'is_child'))
#
#
# class TheIncredibles(Family):
#     def use_power(self, name):
#         for member in self.members:
#             if member['name'] == name or member['incredible_name'] == name:
#                 if member['age'] > 18:
#                     print(f"{name}'s power is: {member['power']}")
#                 else:
#                     raise Exception("Member isn't 18 years old")
#                 break
#
#     def incredible_presentation(self):
#         print(f"Here is our power family {self.last_name}")
#         super().family_presentation()
#
#
# incredibles = TheIncredibles([
#     {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
#     {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds',
#      'incredible_name': 'SuperWoman'}
# ], 'Borisovs')
#
# incredibles.born(name='Jack', age=0, gender='Unknown', is_child=True, power='Unknown', incredible_name='UknownBaby')
# incredibles.incredible_presentation()
# incredibles.use_power('Michael')
# incredibles.use_power('UknownBaby')  # Raise Exception
