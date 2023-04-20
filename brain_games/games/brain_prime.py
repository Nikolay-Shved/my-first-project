import random
from brain_games.games.logic import congrats


def prime_game(name):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    counter = 0
    while counter < 3:
        num = random.randint(2, 100)
        print(f'Question: {num}')

        k = 0
        for i in range(2, num // 2 + 1):
            if (num % i == 0):
                k += 1
        if (k <= 0):
            result = 'yes'
        else:
            result = 'no'

        answer = input('Your answer: ')

        if answer == result:
            print('Correct!')
            counter += 1
        else:
            print(f"'{answer}' is wrong answer ;(.")
            print(f"Correct answer was '{result}'.")
            break

    print(congrats(name, counter))
