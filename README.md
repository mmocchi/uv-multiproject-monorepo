# UV Multiproject Monorepo

## プロジェクトの概要

このリポジトリは、[uv](https://github.com/astral-sh/uv)を使用したPythonのマルチプロジェクトのモノレポの実装例です。以下のプロジェクトで構成されています：

- `shared/module1`: 共有可能な再利用可能なPythonモジュール
- `apps/application1`: `module1`を使用したサンプルアプリケーション

## 前提ソフトウェア

- Visual Studio Code
- Python 3.10以上
- [mise](https://github.com/mise-rs/mise) - パッケージマネージャー
- [uv](https://github.com/astral-sh/uv) - 依存関係管理ツール
- [Task](https://taskfile.dev/) - タスクランナー
- [Visual Studio Code](https://code.visualstudio.com/) - 推奨エディタ

### VSCode拡張機能

- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) - Python言語サポート
- [Ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff) - Pythonリンター
- [Mypy Type Checker](https://marketplace.visualstudio.com/items?itemName=ms-python.mypy-type-checker) - Mypyのサポート

## セットアップ手順

1. リポジトリのクローン
```bash
git clone https://github.com/mmocchi/uv-multiproject-monorepo.git
cd uv-multiproject-monorepo
```

2. 各プロジェクトのセットアップ
各プロジェクトのREADMEを参照して、それぞれのプロジェクトをセットアップしてください。

3. VSCode Multi Root Workspaceの設定
このリポジトリは、VSCodeのMulti Root Workspace機能を使用して、各プロジェクトの独立した開発環境設定を管理しています。

```bash
code uv-multiproject-monorepo.code-workspace
```

各プロジェクトの`.vscode/settings.json`には、そのプロジェクト固有の設定が含まれており、以下のような設定が可能です：
- Pythonインタープリターのパス
- リンターとフォーマッターの設定
- テスト設定
- その他のプロジェクト固有の設定

## プロジェクト構成

```
.
├── apps/
│   └── application1/      # サンプルアプリケーション
│       └── .vscode/      # application1固有のVSCode設定
├── shared/
│   └── module1/          # 共有モジュール
│       └── .vscode/      # module1固有のVSCode設定
└── shared_config/        # 共有設定ファイル
```

## 開発ワークフロー

各プロジェクトディレクトリには、独自の開発用コマンドが用意されています。詳細は各プロジェクトのREADMEを参照してください：

- [module1のREADME](shared/module1/README.md)
- [application1のREADME](apps/application1/README.md)
