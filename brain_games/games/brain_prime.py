import random
from brain_games.games.logic import congrats


def prime_game(name):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    counter = 3
    for i in range(counter):
        NUM = random.randint(2, 100)
        print(f'Question: {NUM}')

        k = 0
        for inter in range(2, NUM // 2 + 1):
            if (NUM % inter == 0):
                k += 1
        if (k <= 0):
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
