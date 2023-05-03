from ..logic import greet, congrats
from ..games.brain_calc import calc_game

def main():
    name = greet()
    i = 0
    calc_game(name)
    congrats(name, i)


if __name__ == '__main__':
    main()

