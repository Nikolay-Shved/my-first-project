import prompt


def game_loop(greet, game_body):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    greet = greet()
    print(greet)
    
    counter = 3
    for i in range(counter):
        question, result = game_body()
        print(question)
        answer = prompt.string('Your answer: ')

        if int(answer) == int(result):
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(.")
            print(f"Correct answer was '{result}'.")
            return print(f"Let's try again, {name}!")
    print(f'Congratulations, {name}!')


def game_loop_2(name, game_body):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    
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
