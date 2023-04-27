import random
from brain_games.games.logic import congrats


def progression_game(name):
    print('What number is missing in the progression?')

    counter = 3
    for i in range(counter):
        NUM_1 = random.randint(1, 30)
        NUM_2 = random.randint(80, 100)
        N = random.randint(2, 10)
        numbers = []
        for inter in range(NUM_1, NUM_2, N):
            numbers.append(inter)
        index = numbers.index(numbers[random.randint(0, 5)])
        numbers[index] = '..'
        string = ' '.join(map(str, numbers))
        print(f'Question: {string}')

        answer = input('Your answer: ')
        if numbers.index(answer) == numbers.index(index):
            print('Correct!')
            counter += 1
        else:
            print(f"'{answer}' is wrong answer ;(.")
            print(f"'Correct answer was '{index}'.")
            break

    print(congrats(name, i))
