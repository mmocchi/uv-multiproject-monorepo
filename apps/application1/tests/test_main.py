"""application1のメインモジュールのテスト"""

import pytest

from application1.main import calculate_sum, parse_arguments


def test_parse_arguments_valid() -> None:
    """正常な引数のパースをテスト"""
    args = ["1", "2"]
    num1, num2 = parse_arguments(args)
    assert num1 == 1
    assert num2 == 2


def test_parse_arguments_invalid_count() -> None:
    """不正な引数の数の場合のテスト"""
    with pytest.raises(ValueError, match="引数は2つ必要です"):
        parse_arguments(["1"])

    with pytest.raises(ValueError, match="引数は2つ必要です"):
        parse_arguments(["1", "2", "3"])


def test_parse_arguments_invalid_type() -> None:
    """不正な型の引数の場合のテスト"""
    with pytest.raises(ValueError, match="引数は整数である必要があります"):
        parse_arguments(["a", "2"])

    with pytest.raises(ValueError, match="引数は整数である必要があります"):
        parse_arguments(["1", "b"])


def test_calculate_sum() -> None:
    """計算結果の文字列生成をテスト"""
    assert calculate_sum(1, 2) == "1 + 2 = 3"
    assert calculate_sum(-1, 5) == "-1 + 5 = 4"
    assert calculate_sum(0, 0) == "0 + 0 = 0"
