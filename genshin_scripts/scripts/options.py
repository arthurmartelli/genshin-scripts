from argparse import ArgumentParser
from typing import Any, Protocol, Tuple, Dict


class Script(Protocol):
    name: str
    args: Tuple[Any]
    kwargs: Dict

    def __init__(self, name: str, *args, **kwargs) -> None:
        self.name = name
        self.args = args
        self.kwargs = kwargs

    def __str__(self) -> str:
        return self.name

    def add_arguments(self, subparsers: ArgumentParser):
        ...

    def run(self, *args, **kwargs):
        ...
