from ..games.brain_gcd import gcd_game
import random
import math
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
    counter = 0
    gcd_game(name)
    congrats(name, counter)


def gcd():
    NUM_1 = random.randint(1, 100)
    NUM_2 = random.randint(1, 100)
    print(f'Question: {NUM_1} {NUM_2}')
    result = math.gcd(NUM_1, NUM_2)
    return result


if __name__ == '__main__':
    main()
