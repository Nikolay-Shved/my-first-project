import random
from brain_games.games.logic import congrats


def even_game(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')

    i = 0
    while i < 3:
        num = random.randint(1, 100)
        print(f'Questions: {num}')
        if num % 2 == 0:
            result = 'yes'
        else:
            result = 'no'

        answer = input('Your answer: ')

        if answer == result:
            print('Correct!')
            i += 1
        else:
            print(f"'{answer}' is wrong answer. Correct answer was '{result}'.")
            break

    print(congrats(name, i))
