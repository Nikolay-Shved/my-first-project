import random

SEQUENCE_ELEMENT_1 = 1
SEQUENCE_ELEMENT_2 = 100


def even_game(random_number):
    if random_number % 2 == 0:
        result = 'yes'
        return result
    else:
        result = 'no'
        return result


def game_body():
    random_number = random.randint(SEQUENCE_ELEMENT_1, SEQUENCE_ELEMENT_2)
    result = even_game(random_number)
    return f'Question: {random_number}', result
