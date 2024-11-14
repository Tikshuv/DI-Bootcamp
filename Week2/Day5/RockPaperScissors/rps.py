from game import Game


def get_user_menu_choice():
    # choices = ['Play a new game', 'Show scores and quit']
    choice = input("\tMenu:\n\t(p) Play a new game\n\t(q) Show scores and quit\n\t: ")
    choices = ['p', 'q']
    if choice.isalpha():
        choice = choice.lower()
    if choice in choices:
        return choice
    print("\tWrong choice, try again:")
    get_user_menu_choice()
    # raise ValueError("Wrong choice")


def print_results(results):
    print(f"\tGame Results:\n\t You won {results['w']} times\n\t You lost {results['l']} times"
          f"\n\t You drew {results['d']} times\n\tThank you for playing!")


def main():
    scores = {'w': 0, 'l': 0, 'd': 0}
    while True:
        choice = get_user_menu_choice()
        if choice == 'q':
            break
        game = Game()
        result = game.play()
        if result == 'loss':
            scores['l'] += 1
        elif result == 'win':
            scores['w'] += 1
        else:
            scores['d'] += 1
    print_results(scores)


main()
