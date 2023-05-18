import random
SEQUENCE_ELEMENT_1 = 2
SEQUENCE_ELEMENT_2 = 100


def prime_game(random_number):
    k = 0
    for i in range(2, random_number // 2 + 1):
        if (random_number % i == 0):
            k += 1
        if (k <= 0):
            result = 'yes'
            return result
        else:
            result = 'no'
            return result


def game_body():
    random_number = random.randint(SEQUENCE_ELEMENT_1, SEQUENCE_ELEMENT_2)
    result = prime_game(random_number)
    return f'Question: {random_number}', result
