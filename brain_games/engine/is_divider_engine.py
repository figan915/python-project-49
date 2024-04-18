import random


def generate_question():
    

    def is_divider():
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        expression = f'{num1}, {num2}'

        while num2:
            num1, num2 = num2, num1 % num2

        correct_answer = str(num1)

        return expression, correct_answer
    
    return is_divider()


def check_response(expression, correct_answer, user_answer):
    if user_answer == correct_answer:
        return 'Correct!'
    else:
        return (f"'{user_answer}' is the wrong answer ;(."
               f"Correct answer was '{correct_answer}'")
