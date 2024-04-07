#!/usr/bin/env python3
import random
import prompt
#from cli import welcome_user

def main():
    print('Welcome to Brain Games')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        number = random.randint(1,100)
        print(f'Question:  {number}')
        answer = input()
        print(f'Answer: {answer}')
        if (number % 2 == 0 and answer.lower() == 'yes') or (number % 2 != 0 and answer.lower() == 'no'):
            print('Correct!')
        elif (number % 2 == 0 and answer.lower() == 'no'):
            return f'no is wrong answer ;(. Correct answer was yes.\nLet\'s try again, {user_name}'
        elif (number % 2 != 0 and answer.lower() == 'yes'):
            return f'yes is wrong answer ;(. Correct answer was no.\nLet\'s try again, {user_name}'
        else:
            return f'is wrong answer ;(. Correct answer was yes or no.\nLet\'s try again, {user_name}'
        
    return f'Congratulations,  {user_name}!'
if __name__ == '__main__':
    main()
