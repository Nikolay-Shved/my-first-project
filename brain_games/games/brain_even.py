import random
from brain_games.games.logic import congrats


def even_game(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')

    counter = 3
    for i in range(counter):
        NUM = random.randint(1, 100)
        print(f'Question: {NUM}')
        if NUM % 2 == 0:
            result = 'yes'
        else:
            result = 'no'

        answer = input('Your answer: ')

        if answer == result:
            print('Correct!')
            
        else:
            print(f"'{answer}' is wrong answer ;(.")
            print(f"Correct answer was '{result}'.")
            break

    print(congrats(name, i))
