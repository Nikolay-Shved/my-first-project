from ..games.brain_progression import get_question_and_answer, GAME_QUESTION
from ..all_game import game_loop


def main():
    game_loop(GAME_QUESTION, get_question_and_answer)


if __name__ == '__main__':
    main()
