import random
NUMBER_1 = 1
NUMBER_2 = 30
NUMBER_3 = 80
NUMBER_4 = 100
NUMBER_5 = 2
NUMBER_6 = 10


def progression(random_number, random_number_1, step):
    numbers = []
    for inter in range(random_number, random_number_1, step):
        numbers.append(inter)
    index = numbers.index(numbers[random.randint(0, 5)])
    correct_answer = numbers[index]
    numbers[index] = '..'
    string = ' '.join(map(str, numbers))
    print(f'Question: {string}')
    return correct_answer


def game_body():

    counter = 3
    for i in range(counter):
        random_number = random.randint(NUMBER_1, NUMBER_2)
        random_number_1 = random.randint(NUMBER_3, NUMBER_4)
        step = random.randint(NUMBER_5, NUMBER_6)
        result = progression(random_number, random_number_1, step)
        return result
