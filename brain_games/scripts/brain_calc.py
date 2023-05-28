from ..all_game import game_loop
from ..games.brain_calc import get_question_and_answer, GAME_QUESTION


def main():
    game_loop(GAME_QUESTION, get_question_and_answer)


if __name__ == '__main__':
    main()
