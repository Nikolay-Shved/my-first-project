from brain_games.games.logic import greet, congrats
from brain_games.games.brain_calc import calc_game


def main():
    name = greet()
    counter = 0
    calc_game(name)
    congrats(name, counter)


if __name__ == '__main__':
    main()
