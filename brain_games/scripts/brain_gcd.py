from ..games.brain_gcd import game_body
from .all_game import script_answer, greet





def main():
    name = greet()
    script_answer(name, game_body)


if __name__ == '__main__':
    main()
