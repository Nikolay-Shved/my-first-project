import random
from ..scripts.all_game import congrats
rundom_number = random.randint(2, 100)

def prime_calc():
    k = 0
    for i in range(2, rundom_number // 2 + 1):
        if (rundom_number % i == 0):
            k += 1
        if (k <= 0):
            result = 'yes'
            return result
        else:
            result = 'no'
            return result


def prime_game(name):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    print(f'Question: {rundom_number}')

    counter = 3
    for i in range(counter):
        result = prime_calc()
        answer = input('Your answer: ')

        if answer.lower() == result.lower():
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(.")
            print(f"Correct answer was '{result}'.")
            return print(f"Let's try again, {name}!")

    congrats(name)
