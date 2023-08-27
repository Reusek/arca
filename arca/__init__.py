"""Useful tools for Python development."""

from typing import Any, Literal, Union, get_args, get_origin, List, Tuple
from dataclasses import is_dataclass

__version__ = "0.0.1"


def serialize(t: Union[Literal["csv"], Literal["json"]]):
    """Type guard for serialization formats."""
    return t


def get_links(obj: object) -> List[Tuple[str, Any]]:
    """Get all links from a dataclass."""

    links = []

    for key, cls in obj.__annotations__.items():
        print(key, cls)
        if get_origin(cls) is get_origin(List):
            args = get_args(cls)

            if (arg := next(iter(args), None)) is None:
                raise TypeError("Expected typing.List[<type>], got typing.List")
            if not is_dataclass(arg):
                raise TypeError(
                    f"Expected typing.List[dataclass], got typing.List[{arg}]"
                )

            if hasattr(arg, "__link__"):
                links.append((key, arg))

    return links
