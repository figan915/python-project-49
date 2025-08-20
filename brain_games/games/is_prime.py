import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def generate_question_and_answer():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    answer = 'yes' if is_prime(number) else 'no'
    return str(number), answer