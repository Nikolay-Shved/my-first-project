
import random
from ..logic import congrats


def prime_calc():
        NUM = random.randint(2, 100)
        print(f'Question: {NUM}')
        k = 0
        for i in range(2, NUM // 2 + 1):
            if (NUM % i == 0):
                k += 1
            if (k <= 0):
                result = 'yes'
                return result
            else:
                result = 'no'
                return result


def prime_game(name):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    counter = 3
    for i in range(counter):
        result = prime_calc()
        answer = input('Your answer: ')

        if answer.lower() == result.lower():
            print('Correct!')
            i += 1
        else:
            print(f"'{answer}' is wrong answer ;(.")
            print(f"Correct answer was '{result}'.")
            break

    print(congrats(name, i))
