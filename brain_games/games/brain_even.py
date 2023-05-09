from ..scripts.all_game import congrats
import random

NUMBER_1 = 1
NUMBER_2 = 100


def even(random_number):
    if random_number % 2 == 0:
        result = 'yes'
        return result
    else:
        result = 'no'
        return result


def even_game(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')

    counter = 3
    for i in range(counter):
        random_number = random.randint(NUMBER_1, NUMBER_2)
        print(f'Question: {random_number}')
        result = even(random_number)
        answer = input('Your answer: ')

        if answer.lower() == result.lower():
            print('Correct!')

        else:
            print(f"'{answer}' is wrong answer ;(.")
            print(f"Correct answer was '{result}'.")
            return print(f"Let's try again, {name}")
    congrats(name)
