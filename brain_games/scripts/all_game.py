import prompt



def greet():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('What is the result of the expression?')
    print(f'Hello, {name}!')
    return name


def script_answer(name, game_body):
    counter = 3
    for i in range(counter):
        result = game_body()
        answer = prompt.string('Your answer: ')

        if int(answer) == int(result):
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(.")
            print(f"Correct answer was '{result}'.")
            return print(f"Let's try again, {name}!")
    print(f'Congratulations, {name}!')


def script_answer_2(name, game_body):
    counter = 3
    for i in range(counter):
        result = game_body()
        answer = prompt.string('Your answer: ')

        if answer.lower() == result.lower():
            print('Correct!')

        else:
            print(f"'{answer}' is wrong answer ;(.")
            print(f"Correct answer was '{result}'.")
            return print(f"Let's try again, {name}!")
        print(f'Congratulations, {name}!')