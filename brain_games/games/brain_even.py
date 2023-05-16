import random

NUMBER_1 = 1
NUMBER_2 = 100


def even(random_number):
    if random_number % 2 == 0:
        result = 'yes'
        return result
    else:
        result = 'no'
        return result


def game_body():
    print('Answer "yes" if the number is even, otherwise answer "no".')

    random_number = random.randint(NUMBER_1, NUMBER_2)
    print(f'Question: {random_number}')
    result = even(random_number)
    return result
