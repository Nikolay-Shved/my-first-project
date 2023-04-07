import prompt
import random
from random import choice


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')

    i = 0
    while i < 3:
        operation = ('+-*')
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        num3 = choice(operation)
        print(f'Question: {num1} {num3} {num2}')

        answer = prompt.string('Your answer: ')

        if int(answer) == int(result):
            print('Correct!')
            i += 1
        else:
            print(f"'{answer}' is wrong answer. Correct answer was '{result}'.")
            print(f"Let's try again, {name}!")
            break

    if i == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
