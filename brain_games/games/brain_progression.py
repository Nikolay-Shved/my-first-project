import random
START_SEQUENCE_1 = 1
END_SEQUENCE_1 = 30
START_SEQUENCE_2 = 80
END_SEQUENCE_2 = 100
START_SEQUENCE_3 = 2
END_SEQUENCE_3 = 10
GAME_QUESTION = "What number is missing in the progression?"


def get_progression(first_number, second_number, step):
    numbers = []
    for inter in range(first_number, second_number, step):
        numbers.append(inter)
    return numbers


def get_question_and_answer():
    first_number = random.randint(START_SEQUENCE_1, END_SEQUENCE_1)
    second_number = random.randint(START_SEQUENCE_2, END_SEQUENCE_2)
    step = random.randint(START_SEQUENCE_3, END_SEQUENCE_3)
    numbers = get_progression(first_number, second_number, step)
    index = numbers.index(numbers[random.randint(0, 5)])
    correct_answer = numbers[index]
    numbers[index] = '..'
    string = ' '.join(map(str, numbers))
    return f'{string}', correct_answer
