import random


def generate_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operator = random.choice(['+', '-', '*'])
    expression = f"{num1} {operator} {num2}"
    correct_answer = str(eval(expression))
    return expression, correct_answer


def check_response(expression, correct_answer, user_answer):

    if user_answer == correct_answer:
        return 'Correct!'
    else:
        return (f"'{user_answer}' is the wrong answer ;(."
                f"Correct answer was '{correct_answer}'.")
