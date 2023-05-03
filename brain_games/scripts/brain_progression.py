from ..logic import greet, congrats
from ..games.brain_progression import progression_game


def main():
    name = greet()
    counter = 0
    progression_game(name)
    congrats(name, counter)


if __name__ == '__main__':
    main()
