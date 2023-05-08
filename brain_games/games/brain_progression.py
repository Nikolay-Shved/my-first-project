from ..scripts.all_game import congrats
import random


rundom_number_1 = random.randint(1, 30)
rundom_number_2 = random.randint(80, 100)
step = random.randint(2, 10)


def progression():
    numbers = []
    for inter in range(rundom_number_1, rundom_number_2, step):
        numbers.append(inter)
    index = numbers.index(numbers[random.randint(0, 5)])
    correct_answer = numbers[index]
    numbers[index] = '..'
    string = ' '.join(map(str, numbers))
    print(f'Question: {string}')
    return correct_answer


def progression_game(name):

    counter = 3
    for i in range(counter):
        correct_answer = progression()
        answer = input('Your answer: ')
        if int(answer) == int(correct_answer):
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(.")
            print(f"'Correct answer was '{correct_answer}'.")
            return print(f"Let's try again, {name}!")

    congrats(name)
