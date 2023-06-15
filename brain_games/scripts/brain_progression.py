from brain_games.all_game import run_game
from brain_games.games.brain_progression import get_question_and_answer
from brain_games.games.brain_progression import GAME_QUESTION


def main():
    run_game(GAME_QUESTION, get_question_and_answer)


if __name__ == '__main__':
    main()
