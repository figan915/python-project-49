import random


def run_game_even(welcome, rules, check_response):
    print('Welcome to Brain Games')
    user_name = welcome()
    rules()
    count = 0
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
        count += 1

    if count == 3:
        print(f'Congratulations, {user_name}!')
