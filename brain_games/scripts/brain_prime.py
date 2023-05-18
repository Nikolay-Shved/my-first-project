from ..games.brain_prime import game_body
from .all_game import game_loop_2


def main():
    condition = game_condition()
    game_loop_2(condition, game_body)


def game_condition():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


if __name__ == '__main__':
    main()
