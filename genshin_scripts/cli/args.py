import argparse

from . import options


def parse():

    choices = {
        options.Friendship(),
    }

    parser = argparse.ArgumentParser(
        prog="genshin_scripts",
        description="Runs a script in the game for automation purposes",
        epilog="Select a script tu run",
    )

    subparsers = parser.add_subparsers(dest="script")

    for script in choices:
        script.add_arguments(subparsers)

    args = parser.parse_args()

    selection = next((s for s in choices if s.name == args.script), None)
    if selection is None:
        parser.error(f"Invalid script: {args.script}")

    selection.run(args)
