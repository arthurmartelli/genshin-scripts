from argparse import ArgumentParser, Namespace
from typing import Any, Protocol, Dict


class Script(Protocol):
    name: str
    args: Any
    kwargs: Dict[str, Any]

    def __init__(self, name: str, *args: Any, **kwargs: Dict[str, Any]) -> None:
        self.name = name
        self.args = args
        self.kwargs = kwargs

    def __str__(self) -> str:
        return self.name

    def add_arguments(self, parser: ArgumentParser):
        ...

    def run(self, args: Namespace):
        ...
