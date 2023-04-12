import random
from brain_games.games.logic import congrats


def even_game(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')

    counter = 0
    while counter < 3:
        num = random.randint(1, 100)
        print(f'Questions: {num}')
        if num % 2 == 0:
            result = 'yes'
        else:
            result = 'no'

        answer = input('Your answer: ')

        if answer == result:
            print('Correct!')
            counter += 1
        else:
            print(f"'{answer}' is wrong answer. Correct answer was '{result}'.")
            break

    print(congrats(name, counter))
