#!/usr/bin/env python3

from brain_games.engine.is_even_engine import run_game
from brain_games.games.is_even import welcome_is_even, rules_is_even, check_is_even

def main():
    run_game(welcome_is_even, rules_is_even, check_is_even)

if __name__ == '__main__':
    main()
