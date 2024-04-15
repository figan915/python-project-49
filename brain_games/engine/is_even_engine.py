import random
import prompt


def run_game(welcome, rules, check_response):
    print('Welcome to Brain Games')
    user_name = welcome()


    rules()


    for _ in range(3):
        number = random.randint(1, 100)
        print(f'Question:  {number}')
        answer = input()

        result = check_response(number, answer)
        if result is not None:
            print(result)
            break
        else:
            print('Correct!')

    return f'Congratulations, {user_name}!'