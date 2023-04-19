import random
from brain_games.games.logic import congrats


def progression_game(name):
    print('What number is missing in the progression?')

    counter = 0
    while counter < 3:
        num1 = random.randint(1, 30)
        num2 = random.randint(80, 100)
        n = random.randint(2, 10)
        numbers = []
        for i in range(num1, num2, n):
            numbers.append(i)
        numbers.sort()
        rundom_number = numbers[random.randint(0, 5)]
        index = numbers.index(rundom_number)
        numbers[index] = '..'
        string = ' '.join(map(str, numbers[0:10]))
        print(f'Question: {string}')

        answer = input('Your answer: ')
        if int(answer) == int(rundom_number):
            print('Correct!')
            counter += 1
        else:
            print(f"'{answer}' is wrong answer ;(.")
            print(f"'Correct answer was '{rundom_number}'.")
            break

    print(congrats(name, counter))
