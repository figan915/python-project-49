#!/usr/bin/env python3
from brain_games.games.calc_game import calc
from brain_games.engine.engine import run


def main():
    print('brain-calc\n')
    run(calc)


if __name__ == '__main__':
    main()
