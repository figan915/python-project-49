# #!/usr/bin/env python3

from brain_games.games.gcd_game import divider
from brain_games.engine.engine import run


def main():
    print('brain-gcd\n')

    run(divider)


if __name__ == '__main__':
    main()
