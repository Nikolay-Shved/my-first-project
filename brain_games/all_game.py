import prompt
COUNTER = 3


def greet():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def game_loop(GAME_QUESTION, get_question_and_answer):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(GAME_QUESTION)

    for i in range(COUNTER):
        question, correct_answer = get_question_and_answer()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')

        if str(answer.lower()) == str(correct_answer):
            print('Correct!')

        else:
            print(f"'{answer}' is wrong answer ;(.")
            print(f"Correct answer was '{correct_answer}'.")
            return print(f"Let's try again, {name}!")
    print(f'Congratulations, {name}!')
