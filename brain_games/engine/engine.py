import random
import prompt


def welcome():
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    return user_name


def generate_question_is_even():
    number = random.randint(1, 100)
    expression = f'{number}'
    if number % 2 == 0:
        correct_answer = 'yes'
    elif number % 2 != 0:
        correct_answer = 'no'

    return expression, correct_answer


def generate_question_calc():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operator = random.choice(['+', '-', '*'])
    expression = f"{num1} {operator} {num2}"
    correct_answer = str(eval(expression))
    return expression, correct_answer


def generate_question_gcd():

    def gcd() -> str:
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
        expression = f"{num1}, {num2}"
        while num2:
            num1, num2 = num2, num1 % num2
        correct_answer = str(num1)
        return expression, correct_answer
    return gcd()


def generate_question_progression():

    def progression():
        start = random.randint(1, 100)
        diff = random.randint(1, 10)
        length = random.randint(5, 10)

        prog = list(range(start, start + (length * diff), diff))

        elem = random.choice(prog)
        correct_answer = str(elem)
        for index, item in enumerate(prog):
            if item == elem:
                prog[index] = '..'
                break
        expression = (' '.join(map(str, prog)))
        return expression, correct_answer
    return progression()


def is_prime(number):
    if number < 2:
        return False
    if number in (2, 3):
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False

    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


def check_response(expression, correct_answer, user_answer, user_name):

    if user_answer == correct_answer:
        return 'Correct!'
    else:
        print(f"'{user_answer}' is the wrong answer ;(. "
              f"Correct answer was '{correct_answer}'.")
        return f"Let's try again, {user_name}!"
