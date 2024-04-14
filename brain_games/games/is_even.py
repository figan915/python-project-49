

import prompt

user_name = None

def welcome_is_even():
    global user_name
    user_name = input('May I have your name? ')
    print(f'Hello, {user_name}!')
    return user_name


def rules_is_even():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def check_is_even(number, answer):
    answere1 = (f"'no' is wrong answer ;(. Correct answer was 'yes'.\n"
                f"Let's try again, {user_name}")
    answere2 = (f"'yes' is wrong answer ;(. Correct answer was 'no'.\n"
                f"Let's try again, {user_name}")
    answere3 = (f"is wrong answer ;(. Correct answer was 'yes' or 'no'.\n"
                f"Let's try again, {user_name}")
    
    if (number % 2 == 0 and answer.lower() == 'yes') or \
       (number % 2 != 0 and answer.lower() == 'no'):
           return None
    elif (number % 2 == 0 and answer.lower() == 'no'):

            return answere1

    elif (number % 2 != 0 and answer.lower() == 'yes'):
            

            return answere2

    else:
          return answere3