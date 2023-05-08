from ..games.brain_gcd import gcd_game
import prompt


def greet():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    return name


def main():
    name = greet()
    gcd_game(name)


if __name__ == '__main__':
    main()
