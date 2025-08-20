import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'

MIN_NUMBER = 1
MAX_NUMBER = 50


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def generate_question_and_answer():
    num1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    expression = f'{num1} {num2}'
    answer = str(gcd(num1, num2))
    return expression, answer