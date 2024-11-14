from random import choice


class Game:
    choices = ['r','p', 's']

    @staticmethod
    def get_user_c():
        while True:
            user_c = input("Choose (r)ock, (p)aper or (s)cissors: ")
            if user_c in Game.choices:
                return user_c

    @staticmethod
    def pc_c():
        return choice(Game.choices)

    @staticmethod
    def get_game_results(user, pc):
        if user == pc:
            return 'draw'
        conditions = [['r', 's'], ['p', 'r'], ['s', 'p']]
        cond = [user, pc]
        for sit in conditions:
            if cond == sit:
                return 'win'
        return 'loss'


    def play(self):
        user_c = self.get_user_c()
        pc_c = self.pc_c()
        result = self.get_game_results(user_c, pc_c)
        print(f"You chose: {user_c}. The computer chose: {pc_c}. Result: {result}")
        return result


