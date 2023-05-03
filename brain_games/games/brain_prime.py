from ..logic import congrats
from ..scripts import brain_prime


def prime_game(name):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    counter = 3
    for i in range(counter):
        result = brain_prime.prime_calc()
        answer = input('Your answer: ')

        if answer.lower() == result.lower():
            print('Correct!')
            i += 1
        else:
            print(f"'{answer}' is wrong answer ;(.")
            print(f"Correct answer was '{result}'.")
            break

    print(congrats(name, i))
