import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    if number < 1:
        return False
    if number % 2 != 0:
        return False
    return True


def generate_question_and_answer():
    number = random.randint(1, 100)
    answer = 'yes' if is_even(number) else 'no'
    return str(number), answer
