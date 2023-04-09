import random
from brain_games.games.logic import congrats


def prime_game(name):

    i = 0
    while i < 3:
        num = random.randint(1, 100)

        for x in range(2, (num//2)+1):
            if num % x == 0:
                result = 'yes'
        result = 'no'

        print(f'Question: {num}')

        answer = input('Your answer: ')

        if answer == result:
            print('Correct!')
            i += 1
        else:
            print(f"'{answer}' is wrong answer. Correct answer was '{result}'.")
            break

    print(congrats(name, i))
