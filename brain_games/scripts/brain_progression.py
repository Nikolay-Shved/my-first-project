import prompt
from ..games.brain_progression import progression_game

def greet():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    return name

def main():
    name = greet()
    progression_game(name)


if __name__ == '__main__':
    main()