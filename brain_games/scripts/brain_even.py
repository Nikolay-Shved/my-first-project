from ..games.brain_even import game_body
from .all_game import script_answer_2, greet


def main():
    name = greet()
    script_answer_2(name, game_body)


if __name__ == '__main__':
    main()
