from .all_game import game_loop
from ..games.brain_calc import game_body


def main():
    condition = game_condition()
    game_loop(condition, game_body)


def game_condition():
    return 'What is the result of the expression?'


if __name__ == '__main__':
    main()
