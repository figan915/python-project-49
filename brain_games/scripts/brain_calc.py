#!/usr/bin/env python3


import random


def main():

    operand = ('+', '-', '*')
    for _ in range(3):
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        oper = random.choice(operand)
        quest = (f'{int(number1)} {oper} {int(number2)}')
        print(quest)
        if oper == '+':
            result = number1 + number2
            answer = int(input())
            if result == answer:
                print('ZBS')
            else:
                return f'xyu, otvet = {result}'
        elif oper == '-':
            result = number1 - number2
            answer = int(input())
            if result == answer:
                print('ZBS')
            else:
                return f'xyu, otvet = {result}'
        elif oper == '*':
            result = number1 * number2
            answer = int(input())
            if result == answer:
                print('ZBS')
            else:
                return f'xyu, otvet = {result}'


print(main())
