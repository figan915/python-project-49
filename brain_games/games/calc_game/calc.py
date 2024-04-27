import random

DESCRIPTION = 'What is the result of the expression?'


def generate_question_and_answer():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operator = random.choice(['+', '-', '*'])
    expression = f"{num1} {operator} {num2}"
    answer = str(eval(expression))
    return expression, answer
