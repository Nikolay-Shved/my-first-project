from ..scripts.all_game import script_answer, greet
from ..games.brain_calc import game_body

def main():
    name = greet()
    script_answer(name, game_body)


if __name__ == '__main__':
    main()
