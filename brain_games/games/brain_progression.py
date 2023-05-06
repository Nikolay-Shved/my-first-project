import random
from ..logic import congrats


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
        correct_answer = numbers[index]
        numbers[index] = '..'
        string = ' '.join(map(str, numbers[0:10]))
        print(f'Question: {string}')
        answer = input('Your answer: ')
        if  int(answer) == int(correct_answer):
            print('Correct!')
            i += 1
        else:
            print(f"'{answer}' is wrong answer ;(.")
            print(f"'Correct answer was '{correct_answer}'.")
            break

    print(congrats(name, i))
