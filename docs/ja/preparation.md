# uv の導入

所要時間：10 分・経過時間：10〜20 分

uv は Python のツールを管理し、`uvx` はツールを独立した環境で実行します。Explorer のローカルインストーラーは uvx を使います。自分の OS のタブだけを進めてください。コマンドは Bob のチャット欄ではなく、ターミナルへ入力します。

## ステップ 1：ターミナルを開く

=== "macOS"

    「アプリケーション」→「ユーティリティ」から「ターミナル」を開きます。Spotlight で「ターミナル」と検索しても構いません。標準のシェルは通常 zsh です。

=== "Windows"

    スタートメニューから「PowerShell」を開くか、Windows Terminal で PowerShell のプロファイルを選びます。以下の PowerShell 用コマンドは、コマンドプロンプトでは実行しません。

## ステップ 2：uv をインストールする

`uv --version` と `uvx --version` が既に動く場合は、ステップ 3 へ進みます。それ以外は OS に合うコマンドを実行します。組織の制限がある場合は、組織で認められた導入方法を使ってください。

=== "macOS"

    ```bash
    curl -LsSf -A "BuildingBlocksWorkshop/0.1" https://astral.sh/uv/install.sh | sh
    ```

    公式の単体インストーラーを使うコマンドに、取得時の User-Agent を付けています。Homebrew を既に使っている場合は、`brew install uv` でも導入できます。両方を実行する必要はありません。

=== "Windows"

    ```powershell
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 -UserAgent 'BuildingBlocksWorkshop/0.1' | iex"
    ```

    公式の単体インストーラーを使うコマンドに、User-Agent を付けています。このコマンドの実行ポリシーは当該プロセスへ適用されます。組織がスクリプト実行を制限している場合は、利用可能であれば `winget install --id=astral-sh.uv -e` など、承認された方法を使います。PC 全体のポリシーは変更しません。

出典：[uv の公式インストール手順](https://docs.astral.sh/uv/getting-started/installation/)。実行前に内容を確認したい場合は、ブラウザで [install.sh](https://astral.sh/uv/install.sh) または [install.ps1](https://astral.sh/uv/install.ps1) を開けます。

## ステップ 3：ターミナルを開き直して確認する

ターミナルを閉じ、新しく開きます。どちらの OS でも次の 2 つを実行してください。

```text
uv --version
uvx --version
```

それぞれ `uv 0.x.y` や `uvx 0.x.y` のようにバージョンが表示されれば成功です。番号は環境により異なります。編集中の内容を保存してから Bob を完全に終了し、起動し直します。これで Bob のプロセスにも更新後の PATH が反映されます。

## コマンドが見つからない場合

=== "macOS"

    単体インストーラーの標準の保存先を直接指定して確認します。

    ```bash
    "$HOME/.local/bin/uv" --version
    "$HOME/.local/bin/uvx" --version
    ```

=== "Windows"

    単体インストーラーの標準の保存先を直接指定して確認します。

    ```powershell
    & "$env:USERPROFILE\.local\bin\uv.exe" --version
    & "$env:USERPROFILE\.local\bin\uvx.exe" --version
    ```

直接指定なら動く場合は、インストーラーの PATH に関する案内に従い、ターミナルと Bob を再起動します。独自の設定やパッケージ管理ツールでは保存先が異なる場合があります。どちらも動かない場合は、エラーを講師へ共有してください。

!!! tip "開始 20 分で次へ進む"
    ネットワークや端末の制限で導入できない場合は、動作している方とペアになって演習を続けます。問題は後で確認する事項として記録し、残り時間をセキュリティ設定の変更に使わないようにします。

- [ ] 両方のバージョンを表示できた。または、動作する環境の方とペアになった。
- [ ] インストール後に Bob を再起動した。

[次へ：Explorer の起動 →](part1.md)
