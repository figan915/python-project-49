import prompt
from brain_games.engine.engine import generate_question_gcd, check_response, welcome


def run_divider_game():

    user_name = welcome()
    print('Find the greatest common divisor of given numbers.')
    correct_count = 0
    for _ in range(3):
        expression, correct_answer =  generate_question_gcd()
        print(f"Question: {expression}")
        user_answer = prompt.string("Your answer: ")
        result = check_response(expression, correct_answer,
                                user_answer, user_name)
        if result == 'Correct!':
            print(result)
            correct_count += 1
        else:
            print(result)
            break

    if correct_count == 3:
        print(f"Congratulations, {user_name}!")
