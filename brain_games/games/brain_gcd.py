from ..scripts.all_game import congrats
import random
import math

rundom_number_1 = random.randint(1, 100)
rundom_number_2 = random.randint(1, 100)
result = math.gcd(rundom_number_1, rundom_number_2)


def gcd_game(name):
    print('Find the greatest common divisor of given numbers.')
    print(f'Question: {rundom_number_1} {rundom_number_2}')

    counter = 3
    for i in range(counter):
        answer = input('Your answer: ')
        if int(result) == int(answer):
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(.")
            print(f"Correct answer was '{result}'.")
            return print(f"Let's try again, {name}")
    congrats(name)
