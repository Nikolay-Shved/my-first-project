import random
import prompt
from random import choice

OPERATIONS = '+-*'
NUMBER_1 = 1
NUMBER_2 = 100


def calculation(random_number_1, random_number_2, random_operation):
    if random_operation == '+':
        result = random_number_1 + random_number_2
        return result
    elif random_operation == '-':
        result = random_number_1 - random_number_2
        return result
    else:
        result = random_number_1 * random_number_2
        return result


def calc_game():
    random_number = random.randint(NUMBER_1, NUMBER_2)
    random_number_1 = random.randint(NUMBER_1, NUMBER_2)
    random_operation = choice(OPERATIONS)
    print(f'Question: {random_number} {random_operation} {random_number_1}')
    result = calculation(random_number, random_number_1, random_operation)
    return result


def script_answer(name):
    counter = 3
    for i in range(counter):
        result = calc_game()
        answer = prompt.string('Your answer: ')

        if int(answer) == int(result):
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(.")
            print(f"Correct answer was '{result}'.")
            return print(f"Let's try again, {name}")
    print(f'Congratulations, {name}!')
