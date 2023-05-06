from argparse import ArgumentParser
from typing import List, TypeVar

from scripts.options import Script

T = TypeVar('T', bound=Script)


def parse(choices: List[T]) -> None:
    parser = ArgumentParser(
        prog="genshin_scripts",
        description="Runs a script in the game for automation purposes",
        epilog="Select a script to run",
    )

    subparsers = parser.add_subparsers(dest='script')
    for script in choices:
        subparser = subparsers.add_parser(str(script), help=script.__doc__)
        script.add_arguments(subparser)

    args = parser.parse_args()

    args_dict = vars(args)
    selection = next(
        (s for s in choices if str(s) == args_dict.get('script', None)),
        None
    )

    if selection is None:
        parser.error(f"Invalid script: {args_dict.get('script', None)}")

    selection.run(args)
