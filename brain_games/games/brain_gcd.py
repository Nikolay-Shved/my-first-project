import random
import math
NUMBER_1 = 1
NUMBER_2 = 100


def game_body():
    print('Find the greatest common divisor of given numbers.')

    counter = 3
    for i in range(counter):
        random_number_1 = random.randint(NUMBER_1, NUMBER_2)
        random_number_2 = random.randint(NUMBER_1, NUMBER_2)
        print(f'Question: {random_number_1} {random_number_2}')
        result = math.gcd(random_number_1, random_number_2)
        return result
