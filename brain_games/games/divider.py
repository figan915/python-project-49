from brain_games.engine.is_divider_engine import generate_question, check_response
import prompt

user_name = None

def run_divider_game():
    global user_name
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(f'Find the greatest common divisor of given numbers.')
    correct_count = 0

    for _ in range(3):
        expression, correct_answer =  generate_question()
        print(f"Question: {expression}")
        user_answer = input("Your answer: ")
        result = check_response(expression, correct_answer, user_answer)
        if result == 'Correct!':
            print(result)
            correct_count += 1
        else:
            print(result)
            print(f"Let's try again, {user_name}!")
            break

    if correct_count == 3:
        print(f"Congratulations, {user_name}!")