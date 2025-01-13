"""
module1のテストスイート.

このモジュールはmodule1の機能をテストするためのテストケースを含みます。
"""

import pytest
from pytest import param as p

from module1.module import add, subtract


@pytest.mark.parametrize(
    "a, b, expected",
    [
        p(1, 2, 3, id="add_small_positive_numbers"),
        p(10, 20, 30, id="add_large_positive_numbers"),
        p(-1, 1, 0, id="add_positive_and_negative"),
        p(-5, -3, -8, id="add_negative_numbers"),
        p(0, 5, 5, id="add_zero_and_positive"),
        p(0, 0, 0, id="add_zero_and_zero"),
    ],
)
def test_add(a: int, b: int, expected: int) -> None:
    """
    add関数のテストケース

    Args:
        a (int): 第1引数
        b (int): 第2引数
        expected (int): 期待される結果
    """
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        p(3, 2, 1, id="subtract_small_positive_numbers"),
        p(10, 5, 5, id="subtract_large_positive_numbers"),
        p(-1, -1, 0, id="subtract_negative_numbers"),
        p(1, -1, 2, id="subtract_positive_minus_negative"),
        p(5, 0, 5, id="subtract_positive_minus_zero"),
        p(0, 5, -5, id="subtract_zero_minus_positive"),
    ],
)
def test_subtract(a: int, b: int, expected: int) -> None:
    """
    subtract関数のテストケース

    Args:
        a (int): 第1引数
        b (int): 第2引数
        expected (int): 期待される結果
    """
    assert subtract(a, b) == expected
