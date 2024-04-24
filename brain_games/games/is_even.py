import prompt
from brain_games.engine.engine import generate_question_is_even, check_response
from brain_games.engine.engine import welcome


def run_is_even_game():
    user_name = welcome()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    for _ in range(3):
        expression, correct_answer = generate_question_is_even()
        print(f"Question: {expression}")
        user_answer = prompt.string("Your answer: ")
        result = check_response(expression, correct_answer,
                                user_answer, user_name)
        if result == 'Correct!':
            print(result)
            count += 1
        else:
            print(result)
            break

    if count == 3:
        print(f'Congratulations, {user_name}!')
