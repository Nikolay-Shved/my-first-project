import random
from random import choice
from brain_games.games.logic import congrats


def calc_game(name):
    print('What is the result of the expression?')

    counter = 0
    while counter < 3:
        operation = ('+-*')
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        num3 = choice(operation)
        print(f'Question: {num1} {num3} {num2}')

        if num3 == '+':
            result = num1 + num2
        elif num3 == '-':
            result = num1 - num2
        else:
            result = num1 * num2

        answer = input('Your answer: ')

        if int(answer) == int(result):
            print('Correct!')
            counter += 1
        else:
            print(f"'{answer}' is wrong answer. Correct answer was '{result}'.")
            print(f"Let's try again, {name}!")
            break

    print(congrats(name, counter))
