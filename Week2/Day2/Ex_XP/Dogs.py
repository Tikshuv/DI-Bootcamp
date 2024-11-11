from XP_Mandatory import Dog
from random import choice


class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        self.bark()
        if not self.trained:
            self.trained = True
            print(f"{self.name} is trained now")

    def play(self, *names):
        print(", ".join(name for name in names), f'and {self.name} are all playing together')

    def do_a_trick(self):
        tricks = ['does a barrel roll', 'stands on his back legs', 'shakes your hand', 'plays dead']
        if self.trained:
            print(f"{self.name} {choice(tricks)}")
        else:
            print(f"{self.name} is a bad dog")


dog1 = PetDog('Ba', 5, 50)
dog2 = PetDog('Ka', 10, 20)
dog3 = PetDog('Sa', 1, 10)
# dog2.bark()
# print(f"{dog1.name}'s speed is: {dog1.run_speed()}")
# dog3.fight(dog1)
dog1.train()
dog1.train()
dog1.play('Sa', 'Ra', 'Co', 'No')
dog1.do_a_trick()
dog2.do_a_trick()
