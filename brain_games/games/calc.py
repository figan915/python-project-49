import random

DESCRIPTION = 'What is the result of the expression?.'

OPERATIONS = ("+", "-", "*")

MIN_NUMBER = 1
MAX_NUMBER = 100


def generate_question_and_answer():
    num1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    operator = random.choice(OPERATIONS)
    expression = f'{num1} {operator} {num2}'
    if operator == '+':
        answer = str(num1 + num2)
    elif operator == '-':
        answer = str(num1 - num2)
    elif operator == '*':
        answer = str(num1 * num2)
    return expression, answer
