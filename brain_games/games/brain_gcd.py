import random
import math
from brain_games.games.logic import congrats


def gcd_game(name):
    print('Find the greatest common divisor of given numbers.')

    counter = 3
    for i in range(counter):
        NUM_1 = random.randint(1, 100)
        NUM_2 = random.randint(1, 100)
        print(f'Question: {NUM_1} {NUM_2}')

        answer = input('Your answer: ')

        result = math.gcd(NUM_1, NUM_2)
        if int(result) == int(answer):
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(.")
            print(f"Correct answer was '{result}'.")
            break

    print(congrats(name, i))
