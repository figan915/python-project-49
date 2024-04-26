import random

DESCRIPTION = 'What number is missing in the progression?'


def generate_question_and_answer():
    start = random.randint(1, 100)
    diff = random.randint(1, 10)
    length = random.randint(5, 10)

    prog = list(range(start, start + (length * diff), diff))

    elem = random.choice(prog)
    answer = str(elem)
    for index, item in enumerate(prog):
        if item == elem:
            prog[index] = '..'
            break
    expression = (' '.join(map(str, prog)))
    return expression, answer
