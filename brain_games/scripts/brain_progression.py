import random
from ..games.brain_progression import progression_game
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
    progression_game(name)
    congrats(name, counter)


def progression():
    NUM_1 = random.randint(1, 30)
    NUM_2 = random.randint(80, 100)
    N = random.randint(2, 10)
    numbers = []
    for inter in range(NUM_1, NUM_2, N):
        numbers.append(inter)
    index = numbers.index(numbers[random.randint(0, 5)])
    correct_answer = numbers[index]
    numbers[index] = '..'
    string = ' '.join(map(str, numbers))
    print(f'Question: {string}')
    return correct_answer


if __name__ == '__main__':
    main()
