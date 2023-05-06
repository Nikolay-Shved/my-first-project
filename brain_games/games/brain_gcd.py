from ..scripts import brain_gcd
from ..logic import congrats


def gcd_game(name):
    print('Find the greatest common divisor of given numbers.')

    counter = 3
    for i in range(counter):
        result = brain_gcd.gcd()
        answer = input('Your answer: ')
        if int(result) == int(answer):
            print('Correct!')
            i += 1
        else:
            print(f"'{answer}' is wrong answer ;(.")
            print(f"Correct answer was '{result}'.")
            break

    print(congrats(name, i))
