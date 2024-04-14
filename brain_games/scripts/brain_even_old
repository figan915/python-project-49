#!/usr/bin/env python3
import random
import prompt


def main():

    print('Welcome to Brain Games')

    user_name = prompt.string('May I have your name? ')

    answere1 = (f"'no' is wrong answer ;(. Correct answer was 'yes'.\n"
                f"Let's try again, {user_name}")
    answere2 = (f"'yes' is wrong answer ;(. Correct answer was 'no'.\n"
                f"Let's try again, {user_name}")
    answere3 = (f"is wrong answer ;(. Correct answer was 'yes' or 'no'.\n"
                f"Let's try again, {user_name}")

    print(f'Hello, {user_name}!')

    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(3):

        number = random.randint(1, 100)

        print(f'Question:  {number}')

        answer = input()

        print(f'Answer: {answer}')

        if (number % 2 == 0 and answer.lower() == 'yes') or \
           (number % 2 != 0 and answer.lower() == 'no'):

            print('Correct!')

        elif (number % 2 == 0 and answer.lower() == 'no'):

            return answere1

        elif (number % 2 != 0 and answer.lower() == 'yes'):

            return answere2

        else:

            return answere3

    return f'Congratulations, {user_name}!'


if __name__ == '__main__':
    main()
