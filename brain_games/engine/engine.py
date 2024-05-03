import prompt

GAME_ROUNDS_COUNT = 3


def welcome_user():
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    return user_name


def run(game, rounds=GAME_ROUNDS_COUNT):
    player = welcome_user()
    print(game.DESCRIPTION)
    for _ in range(rounds):
        question, answer = game.generate_question_and_answer()
        print(f'Question: {question}')
        user_answer = input('Your answer: ')

        if (str(user_answer) == str(answer)
            or (isinstance(user_answer, int) and isinstance(answer, int)
                and int(user_answer) == int(answer))):
            print('Correct!')
        else:
            print(f"'{user_answer}' is the wrong answer ;(. "
                  f"Correct answer was '{answer}'.")
            print(f"Let's try again, {player}!")
            return
    print(f'Congratulations, {player}!')
