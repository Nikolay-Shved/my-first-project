from ..games.brain_calc import calc_game
import random
from random import choice
import prompt


def greet():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    return name


def congrats(name, i):
    if i == 3:
        return f'Congratulations, {name}!'
    else:
        return f"Let's try again, {name}!"


def main():
    name = greet()
    i = 0
    calc_game(name)
    congrats(name, i)


def calculation():
    OPERATION = '+-*'
    NUM_1 = random.randint(1, 100)
    NUM_2 = random.randint(1, 100)
    NUM_3 = choice(OPERATION)
    print(f'Question: {NUM_1} {NUM_3} {NUM_2}')
    if NUM_3 == '+':
        result = NUM_1 + NUM_2
        return result
    elif NUM_3 == '-':
        result = NUM_1 - NUM_2
        return result
    else:
        result = NUM_1 * NUM_2
        return result


if __name__ == '__main__':
    main()
