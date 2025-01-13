# Application1

## プロジェクトの概要

このプロジェクトは、`module1`を使用したサンプルアプリケーションです。Python 3.10以上で動作する、モジュール化されたアプリケーションの実装例を提供します。

## 推奨ソフトウェア

- Visual Studio Code
- Python 3.10以上
- [mise](https://github.com/mise-rs/mise) - パッケージマネージャー
- [uv](https://github.com/astral-sh/uv) - 依存関係管理ツール
- [Task](https://taskfile.dev/) - タスクランナー

### VSCode拡張機能

- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) - Python言語サポート
- [Ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff) - Pythonリンター
- [Mypy Type Checker](https://marketplace.visualstudio.com/items?itemName=ms-python.mypy-type-checker) - Mypyのサポート

## セットアップ手順

1. Python仮想環境の作成
```bash
cd apps/application1
uv sync
```

## 開発用コマンド

以下のコマンドは`task`を使用して実行できます：

### リンターとフォーマッター

- コード解析の実行:
```bash
task lint        # ruffとmypyによる静的解析
task lint:ruff   # ruffのみ実行
task lint:mypy   # myypのみ実行
```

- コードフォーマット:
```bash
task format      # コードフォーマットの実行
task fix:ruff    # ruffによる自動修正
```

### テスト

- テストの実行:
```bash
task test        # pytestによるテスト実行
```

### 統合コマンド

- すべてのチェックを実行:
```bash
task check       # lint, format, testをすべて実行
```

- 開発モード（ファイル変更の監視）:
```bash
task watch       # ファイル変更を監視して自動的にチェックを実行
```
