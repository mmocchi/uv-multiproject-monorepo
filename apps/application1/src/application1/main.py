"""
application1のメインモジュール

module1のadd関数を使用して、コマンドライン引数で受け取った2つの整数を足し合わせる
"""

import sys

from module1.module import add


def main() -> None:
    """
    メイン関数

    コマンドライン引数から2つの整数を受け取り、その和を表示する

    使用例:
        python -m application1.main 1 2
    """
    if len(sys.argv) != 3:
        print("使用方法: python -m application1.main <数値1> <数値2>")
        sys.exit(1)

    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
    except ValueError:
        print("エラー: 引数は整数である必要があります")
        sys.exit(1)

    result = add(num1, num2)
    print(f"{num1} + {num2} = {result}")


if __name__ == "__main__":
    main()
