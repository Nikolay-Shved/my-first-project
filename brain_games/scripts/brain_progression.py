from ..games.brain_progression import game_body
from ..scripts.all_game import game_loop


def main():
    condition = game_condition()
    game_loop(condition, game_body)


def game_condition():
    return "What number is missing in the progression?"


if __name__ == '__main__':
    main()
