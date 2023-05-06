from ..logic import congrats
from ..scripts import brain_progression


def progression_game(name):
    print('What number is missing in the progression?')

    counter = 3
    for i in range(counter):
        correct_answer = brain_progression.progression()
        answer = input('Your answer: ')
        if int(answer) == int(correct_answer):
            print('Correct!')
            i += 1
        else:
            print(f"'{answer}' is wrong answer ;(.")
            print(f"'Correct answer was '{correct_answer}'.")
            break

    print(congrats(name, i))
