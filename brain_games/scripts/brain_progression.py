from ..games.brain_progression import game_body
from ..scripts.all_game import script_answer, greet



def main():
    name = greet()
    script_answer(name, game_body)


if __name__ == '__main__':
    main()