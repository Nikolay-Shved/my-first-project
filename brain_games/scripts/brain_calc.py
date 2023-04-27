from ..logic import greet, congrats
from ..games.brain_calc import calc_game, calculations
import random
from random import choice

def main():
    name = greet()
    result = calculation()
    i = 0
    calc_game(name)
    congrats(name, i)
    calculations(result)



if __name__ == '__main__':
    main()



def calculation():
    OPERATION = ('+-*')
    NUM_1 = random.randint(1, 100)
    NUM_2 = random.randint(1, 100)
    NUM_3 = choice(OPERATION)
    print(f'Question: {NUM_1} {NUM_3} {NUM_2}')

    if NUM_3 == '+':
        result = NUM_1 + NUM_2
        return result
    elif NUM_3 == '-':
         result = NUM_1 - NUM_2
         return result
    else:
        result = NUM_1 * NUM_2
        return result

    nswer = input('Your answer: ')
