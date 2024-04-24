import prompt
from brain_games.engine.engine import generate_question_progression
from brain_games.engine.engine import welcome, check_response


def run_progression_game():
    user_name = welcome()
    print('What number is missing in the progression?')
    correct_count = 0
    for _ in range(3):
        expression, correct_answer = generate_question_progression()
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
