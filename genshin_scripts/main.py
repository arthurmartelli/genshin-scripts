"""
This file contains the main function that runs the
bot script to interact with the game "Genshin Impact".

The game needs to be open with a resolution of 1600x900
and in the center of the screen for the script to work.

The main function switches to the game window and runs
the bot script for a set number of iterations, printing
the iteration number at the end of each run.

To run the script, it needs to be executed with administrator
privileges in order to interact with the game.

Functions:
- main(): The main function that runs the bot script for a set number of iterations.

Modules:
- process: Contains the functions that make up the bot script to interact with the game.
- utils: Contains utility functions used by the bot script and the main function.
"""

import cli


def main() -> None:
    """
    Runs the main process to gain friendship with a bot in Genshin Impact.

    Preconditions:
    - The game needs to be open in order for the process to work.
    - The resolution needs to be set to 1600x900.
    - The game needs to be in the center of the screen (automatically done).
    - The script needs to be run as admin to interact with the game.
    """
    cli.args.parse()


if __name__ == "__main__":
    main()
