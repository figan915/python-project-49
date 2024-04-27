import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_question_and_answer():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    expression = f"{num1} {num2}"
    while num2:
        num1, num2 = num2, num1 % num2
    answer = str(num1)
    return expression, answer
