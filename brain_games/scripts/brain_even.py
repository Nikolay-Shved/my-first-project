import random
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    i = 0
    while i < 3:
        num = random.randint(1, 100)
        print(f'Questions: {num}')
        if num % 2 == 0:
            result = 'yes'
        else:
            result = 'no'

        answer = prompt.string('Your answer: ')

        if answer == result:
            print('Correct!')
            i += 1

        else:
            print(f'{answer} is wrong answer ;(. Correct answer was {result}.')
            print(f"Let's try again, {name}!")
            break

    if i == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
