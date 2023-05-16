import random
NUMBER_1 = 2
NUMBER_2 = 100


def prime_calc(random_number):
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
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    counter = 3
    for i in range(counter):
        random_number = random.randint(NUMBER_1, NUMBER_2)
        print(f'Question: {random_number}')
        result = prime_calc(random_number)
        return result
