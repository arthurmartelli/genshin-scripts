from argparse import Namespace, _SubParsersAction

import scripts


class Script():
    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return self.name

    def add_arguments(self, subparsers):
        raise NotImplementedError

    def run(self):
        raise NotImplementedError


class Friendship(Script):
    def __init__(self):
        super().__init__(name="friendship")

    def run(self, args: Namespace):
        scripts.friendship.run(args.iterations)
        # we added the iterations arg underneath

    def add_arguments(self, subparsers: _SubParsersAction):
        parser = subparsers.add_parser(
            self.name,
            help="Automate a friendship script",
        )

        parser.add_argument(
            "-i",
            "--iterations",
            default=10,
            required=False,
            type=int,
            help="Number of times to run the script, defaults to 10",
        )
