# #!/usr/bin/env python3

from brain_games.games.is_even_game import is_even
from brain_games.engine.engine import run


def main():
    print('brain-even\n')

    run(is_even)


if __name__ == '__main__':
    main()
