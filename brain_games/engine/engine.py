from brain_games.cli import welcome_user

GAME_ROUNDS_COUNT = 3


def run(game, rounds=GAME_ROUNDS_COUNT):
    player = welcome_user()
    print(game.DESCRIPTION)
    for _ in range(rounds):
        question, answer = game.generate_question_and_answer()
        print(f'Question: {question}')
        user_answer = input('Your answer: ')
        if user_answer != answer:

            print(f"'{user_answer}' is the wrong answer ;(. "
                  f"Correct answer was '{answer}'.")
            print(f"Let's try again, {player}!")
            return
        print('Correct!')
    print(f'Congratulations, {player}!')
