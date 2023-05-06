from ..games.brain_even import even_game
import random
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
    even_game(name)
    congrats(name, counter)


def even():
    NUM = random.randint(1, 100)
    print(f'Question: {NUM}')
    if NUM % 2 == 0:
        result = 'yes'
        return result
    else:
        result = 'no'
        return result


if __name__ == '__main__':
    main()
