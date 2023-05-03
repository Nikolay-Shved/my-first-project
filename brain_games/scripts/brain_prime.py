from ..logic import greet, congrats
from ..games.brain_prime import prime_game
import random


def main():
    name = greet()
    counter = 0
    prime_game(name)
    congrats(name, counter)


def prime_calc():
        NUM = random.randint(2, 100)
        print(f'Question: {NUM}')
        k = 0
        for i in range(2, NUM // 2 + 1):
            if (NUM % i == 0):
                k += 1
            if (k <= 0):
                result = 'yes'
                return result
            else:
                result = 'no'
                return result


if __name__ == '__main__':
    main()
