import prompt
REPEATCOUNT = 3


def run_game(GAME_QUESTION, get_question_and_answer):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(GAME_QUESTION)

    for i in range(REPEATCOUNT):
        question, correct_answer = get_question_and_answer()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')

        if str(answer.lower()) != str(correct_answer):
            print(f"'{answer}' is wrong answer ;(.")
            print(f"Correct answer was '{correct_answer}'.")
            return print(f"Let's try again, {name}!")
        print('Correct!')
    print(f'Congratulations, {name}!')
