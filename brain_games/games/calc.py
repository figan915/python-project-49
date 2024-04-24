import prompt
from brain_games.engine.engine import generate_question_calc, check_response
from brain_games.engine.engine import welcome


def run_calculator_game():

    user_name = welcome()
    print('What is the result of the expression?')
    correct_count = 0
    for _ in range(3):
        question, correct_answer = generate_question_calc()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")
        result = check_response(question, correct_answer,
                                user_answer, user_name)
        if result == 'Correct!':
            print(result)
            correct_count += 1
        else:
            print(result)
            break

    if correct_count == 3:
        print(f"Congratulations, {user_name}!")
