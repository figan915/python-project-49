#!/usr/bin/env python3
from brain_games.games import progression_game
from brain_games.engine.engine import run


def main():
    print("brain-progression\n")
    run(progression_game)


if __name__ == '__main__':
    main()
