import random

DESCRIPTION = 'What number is missing in the progression?'

MIN_NUMBER = 1
MAX_NUMBER = 100
MIN_DIFF = 1
MAX_DIFF = 10
MIN_LENGTH = 5
MAX_LENGTH = 10


def generate_question_and_answer():
    start = random.randint(MIN_NUMBER, MAX_NUMBER)
    diff = random.randint(MIN_DIFF, MAX_DIFF)
    length = random.randint(MIN_LENGTH, MAX_LENGTH)

    progression = list(range(start, start + (length * diff), diff))

    elem = random.choice(progression)
    answer = str(elem)
    for index, item in enumerate(progression):
        if item == elem:
            progression[index] = '..'
            break
    expression = ' '.join(map(str, progression))
    return expression, answer