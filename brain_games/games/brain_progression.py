from ..scripts.all_game import congrats
import random
NUMBER_1 = 1
NUMBER_2 = 30
NUMBER_3 = 80
NUMBER_4 = 100
NUMBER_5 = 2
NUMBER_6 = 10


def progression(random_number_1, random_number_2, random_step):
    numbers = []
    for inter in range(random_number_1, random_number_2, random_step):
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
        random_number_1 = random.randint(NUMBER_1, NUMBER_2)
        random_number_2 = random.randint(NUMBER_3, NUMBER_4)
        random_step = random.randint(NUMBER_5, NUMBER_6)
        correct_answer = progression(random_number_1, random_number_2, random_step)
        answer = input('Your answer: ')
        if int(answer) == int(correct_answer):
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(.")
            print(f"'Correct answer was '{correct_answer}'.")
            return print(f"Let's try again, {name}!")

    congrats(name)
