from ..games.brain_prime import prime_game
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
    prime_game(name)
    congrats(name, counter)


def prime_calc():
    NUM = random.randint(2, 100)
    print(f'Question: {NUM}')
    k = 0
    for i in range(2, NUM // 2 + 1):
        if (NUM % i == 0):
            k += 1
        if (k <= 0):
            result = 'yes'
            return result
        else:
            result = 'no'
            return result


if __name__ == '__main__':
    main()
