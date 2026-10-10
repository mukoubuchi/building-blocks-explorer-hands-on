# uv の導入

所要時間: 5 分（経過時間: 5–10 分）

Explorer のローカルインストーラーは、[uv](https://docs.astral.sh/uv/) に含まれる `uvx` を使います。Python の個別インストールは不要です。

## ステップ 1: ターミナルを開く

=== "macOS"

    アプリケーション → ユーティリティ → ターミナルを開きます。

=== "Windows"

    スタートメニューから PowerShell を開きます。

## ステップ 2: uv をインストールする

`uv --version` と `uvx --version` が動く場合は、ステップ 3 へ進みます。それ以外は、OS に合うコマンドをターミナルで実行します。

=== "macOS"

    ```bash
    curl -LsSf -A "BuildingBlocksWorkshop/0.1" https://astral.sh/uv/install.sh | sh
    ```

=== "Windows"

    ```powershell
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 -UserAgent 'BuildingBlocksWorkshop/0.1' | iex"
    ```

スクリプトの実行が制限されている場合は、組織で承認された方法を使います。代替手段は [公式のインストール手順](https://docs.astral.sh/uv/getting-started/installation/) を参照してください。

## ステップ 3: 動作を確認する

ターミナルを開き直し、実行します。

```text
uv --version
uvx --version
```

両方のバージョンが表示されれば完了です。作業を保存し、Bob を完全に終了して起動し直すと、更新した PATH が反映されます。

??? tip "コマンドが見つからない場合"
    単体インストーラーの標準の保存先を指定して確認します。

    === "macOS"

        ```bash
        "$HOME/.local/bin/uv" --version
        "$HOME/.local/bin/uvx" --version
        ```

    === "Windows"

        ```powershell
        & "$env:USERPROFILE\.local\bin\uv.exe" --version
        & "$env:USERPROFILE\.local\bin\uvx.exe" --version
        ```

    動く場合は、インストーラーの PATH 設定の案内に従います。解決しない場合は講師へ相談し、動作する環境の方とペアで続けます。

[次へ →](part1.md){ .workshop-next }
