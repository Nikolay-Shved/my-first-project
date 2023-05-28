import random
START_SEQUENCE_1 = 1
END_SEQUENCE_1 = 30
START_SEQUENCE_2 = 80
END_SEQUENCE_2 = 100
START_SEQUENCE_3 = 2
END_SEQUENCE_3 = 10
GAME_QUESTION = "What number is missing in the progression?"


def calculate(first_number, second_number, step):
    numbers = []
    for inter in range(first_number, second_number, step):
        numbers.append(inter)
    index = numbers.index(numbers[random.randint(0, 5)])
    correct_answer = numbers[index]
    numbers[index] = '..'
    progression_string = ' '.join(map(str, numbers))
    return correct_answer, progression_string


def get_question_and_answer():
    first_number = random.randint(START_SEQUENCE_1, END_SEQUENCE_1)
    second_number = random.randint(START_SEQUENCE_2, END_SEQUENCE_2)
    step = random.randint(START_SEQUENCE_3, END_SEQUENCE_3)
    correct_answer, progression_string = calculate(first_number, second_number, step)
    return f'{correct_answer}', progression_string
