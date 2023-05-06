from ..logic import congrats
from ..scripts import brain_calc


counter = 3


def calc_game(name):
    for i in range(counter):
        result = brain_calc.calculation()
        answer = input('Your answer: ')

        if str(answer) == str(result):
            print('Correct!')
            i += 1
        else:
            print(f"'{answer}' is wrong answer ;(.")
            print(f"Correct answer was '{result}'.")
            break
    print(congrats(name, i))
