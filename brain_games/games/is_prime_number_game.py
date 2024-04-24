import random
import prompt
from brain_games.engine.engine import is_prime, welcome


def run_is_prime_number_game():
    user_name = welcome()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 0
    while count < 3:
        number = random.randint(1, 100)
        print(f"Question: {number}")

        user_answer = prompt.string("Your answer: ")

        if ((is_prime(number) and user_answer == 'yes')
           or (not is_prime(number) and user_answer == 'no')):
            print("Correct!")
            count += 1
        else:
            correct_answer = 'yes' if is_prime(number) else 'no'
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            break

    if count == 3:
        print(f'Congratulations, {user_name}!')
