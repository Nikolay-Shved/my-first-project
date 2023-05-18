import random
import math
SEQUENCE_ELEMENT_1 = 1
SEQUENCE_ELEMENT_2 = 100


def game_body():
    random_number_1 = random.randint(SEQUENCE_ELEMENT_1, SEQUENCE_ELEMENT_2)
    random_number_2 = random.randint(SEQUENCE_ELEMENT_1, SEQUENCE_ELEMENT_2)
    result = math.gcd(random_number_1, random_number_2)
    return f'Question: {random_number_1} {random_number_2}', result
