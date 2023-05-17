from .all_game import game_loop
from ..games.brain_calc import game_body
import prompt


def main():
    game_loop(greet, game_body)


def greet():
    return 'What is the result of the expression?'


if __name__ == '__main__':
    main()
