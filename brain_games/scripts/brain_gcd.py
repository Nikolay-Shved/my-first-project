from ..games.brain_gcd import game_body
from .all_game import game_loop


def main():
    condition = game_condition()
    game_loop(condition, game_body)


def game_condition():
    return "Find the greatest common divisor of given numbers."


if __name__ == '__main__':
    main()
