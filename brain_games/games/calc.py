from brain_games.engine.calc_engine import generate_question, check_response

user_name = None


def run_calculator_game():
    global user_name
    user_name = input('May I have your name? ')
    print(f'Hello, {user_name}!')

    correct_count = 0
    for _ in range(3):
        question, correct_answer = generate_question()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")
        result = check_response(question, correct_answer, user_answer)
        if result == 'Correct!':
            print(result)
            correct_count += 1
        else:
            print(result)
            print(f"Let's try again, {user_name}!")
            break

    if correct_count == 3:
        print(f"Congratulations, {user_name}!")
