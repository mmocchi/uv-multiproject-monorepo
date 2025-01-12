"""
application1のメインモジュール

module1のadd関数を使用して、コマンドライン引数で受け取った2つの整数を足し合わせる
"""
import sys
from typing import Sequence

from module1.module import add


def parse_arguments(args: Sequence[str]) -> tuple[int, int]:
    """
    コマンドライン引数をパースする

    Args:
        args: コマンドライン引数のリスト（sys.argvの[1:]に相当）

    Returns:
        tuple[int, int]: パースされた2つの整数

    Raises:
        ValueError: 引数の数が不正、または整数に変換できない場合
    """
    if len(args) != 2:
        raise ValueError("引数は2つ必要です")

    try:
        num1 = int(args[0])
        num2 = int(args[1])
        return num1, num2
    except ValueError:
        raise ValueError("引数は整数である必要があります")


def calculate_sum(num1: int, num2: int) -> str:
    """
    2つの整数の和を計算し、結果を文字列で返す

    Args:
        num1: 1つ目の整数
        num2: 2つ目の整数

    Returns:
        str: 計算結果の文字列（例: "1 + 2 = 3"）
    """
    result = add(num1, num2)
    return f"{num1} + {num2} = {result}"


def main() -> None:
    """
    メイン関数

    コマンドライン引数から2つの整数を受け取り、その和を表示する

    使用例:
        python -m application1.main 1 2
    """
    try:
        num1, num2 = parse_arguments(sys.argv[1:])
        result = calculate_sum(num1, num2)
        print(result)
    except ValueError as e:
        print(f"エラー: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
