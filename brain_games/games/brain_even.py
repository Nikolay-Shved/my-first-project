from ..scripts.all_game import congrats
import random
rundom_number = random.randint(1, 100)

def even():
    if rundom_number % 2 == 0:
        result = 'yes'
        return result
    else:
        result = 'no'
        return result


def even_game(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    print(f'Question: {rundom_number}')

    counter = 3
    for i in range(counter):
        result = even()
        answer = input('Your answer: ')

        if answer.lower() == result.lower():
            print('Correct!')

        else:
            print(f"'{answer}' is wrong answer ;(.")
            print(f"Correct answer was '{result}'.")
            return print(f"Let's try again, {name}")
    congrats(name)
