# #!/usr/bin/env python3
from brain_games.games import is_prime_number_game
from brain_games.engine.engine import run


def main():
    print('brain-prime\n')

    run(is_prime_number_game)


if __name__ == '__main__':
    main()
