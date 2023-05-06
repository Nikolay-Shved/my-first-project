from ..scripts import brain_even
from ..logic import congrats


def even_game(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')

    counter = 3
    for i in range(counter):
        result = brain_even.even()
        answer = input('Your answer: ')

        if answer.lower() == result.lower():
            print('Correct!')
            i += 1

        else:
            print(f"'{answer}' is wrong answer ;(.")
            print(f"Correct answer was '{result}'.")
            break

    print(congrats(name, i))
