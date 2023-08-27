from typing import List
from dataclasses import dataclass

import arca
import pytest


class TestWithouthDataclass:
    __test__ = False
    a: List[str]


@dataclass
class TestWithouthListGeneric:
    __test__ = False
    a: List


def test_type_list_without_generic() -> None:
    with pytest.raises(TypeError):
        arca.get_links(TestWithouthListGeneric)


def test_type_list_without_dataclass() -> None:
    with pytest.raises(TypeError):
        arca.get_links(TestWithouthDataclass)


@dataclass
class TestLink:
    __test__ = False
    __link__ = True
    a: str


@dataclass
class TestClass:
    __test__ = False
    a: List[TestLink]


def test_link() -> None:
    a = arca.get_links(TestClass)
    assert a == [("a", TestLink)]
