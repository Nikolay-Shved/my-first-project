import random
FIRST_SEQUENCE_1 = 1
FIRST_SEQUENCE_2 = 30
SECOND_SEQUENCE_1 = 80
SECOND_SEQUENCE_2 = 100
THIRD_SEQUENCE_1 = 2
THIRD_SEQUENCE_2 = 10


def progression_game(random_number, random_number_1, step):
    numbers = []
    for inter in range(random_number, random_number_1, step):
        numbers.append(inter)
    index = numbers.index(numbers[random.randint(0, 5)])
    correct_answer = numbers[index]
    numbers[index] = '..'
    string = ' '.join(map(str, numbers))
    return correct_answer, string


def game_body():
    random_number = random.randint(FIRST_SEQUENCE_1, FIRST_SEQUENCE_2)
    random_number_1 = random.randint(SECOND_SEQUENCE_1, SECOND_SEQUENCE_2)
    step = random.randint(THIRD_SEQUENCE_1, THIRD_SEQUENCE_2)
    result, string = progression_game(random_number, random_number_1, step)
    return f'Question: {string}', result
