import random
import math
from brain_games.games.logic import congrats


def gcd_game(name):
    print('Find the greatest common divisor of given numbers.')

    i = 0
    while i < 3:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        print(f'Question: {num1} {num2}')

        answer = input('Your answer: ')

        result = math.gcd(num1, num2)
        if int(result) == int(answer):
            print('Correct!')
            i += 1
        else:
            print(f"'{answer}' is wrong answer. Correct answer was '{result}'.")
            print(f"Let's try again, {name}!")
            break

    print(congrats(name, i))
