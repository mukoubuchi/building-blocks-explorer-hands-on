# Explorer の起動

所要時間: 10 分（経過時間: 10–20 分）

## ステップ 1: ダウンロードして展開する

[公式の Explorer ZIP](https://raw.githubusercontent.com/ibm-self-serve-assets/building-blocks/f721f5ec1915225ade62d8d0e780fe6b19aa58b8/explore-BBs/building-blocks-explorer.zip) をダウンロードします。

=== "macOS"

    Finder で ZIP をダブルクリックして展開します。

=== "Windows"

    ZIP を右クリック →「すべて展開」を選びます。ZIP の表示画面ではなく、展開後のフォルダを使います。

## ステップ 2: Bob でモードを選ぶ

「Open Folder」で、`README.md` と `.bob` が入った `building-blocks-explorer` を開きます。Bob はフォルダを制限モードで開きます。帯の「管理」、続いて「信頼する」を選び、信頼の画面を閉じます。モードの選択欄で「🧱 IBM Building Blocks Explorer」を選びます。

## ステップ 3: 接続を確認する

Bob の設定（歯車のアイコン）で「MCP」を開き、次のサーバーを確認します。

| サーバー | 役割 |
| --- | --- |
| `building-blocks` | リモートのカタログを検索する |
| `building-blocks-installer` | uvx でローカルのインストーラーを動かす |

Bob のチャットへ貼り付けます。

```text
Building Blocks のカタログツールを使い、AI、Data、Automation から候補を 1 つずつ紹介する。
各候補には名前、用途、出典 URL を添える。
調査のみ。インストールとデプロイは対象外。
```

Bob はカタログのツールを呼ぶたびに承認を求めます（`List Building Blocks (building-blocks)` など）。「一度だけ承認」を選びます。

Explorer は導入操作もできるため、接続確認では調査だけを指示します。

`list_building_blocks` などのツールの実行結果を確認し、出典リンクを開きます。

??? tip "うまく動かない場合"
    | 症状 | 対処 |
    | --- | --- |
    | モードが表示されない | 展開先に `.bob` があることを確認し、Bob を再読み込みする |
    | インストーラーが使えない | uv/uvx を確認し、Bob を完全に再起動する。カタログが動けば課題は続けられる |
    | 初回起動が遅い | 依存パッケージのダウンロードを待つ |
    | カタログが使えない | Bob を 1 回再起動する。解決しなければ講師へ相談し、ペアで続ける |
    | 出典リンクが古い | [Building Blocks の概要](https://github.com/ibm-self-serve-assets/building-blocks/tree/5c610971dc72f9e9035821b3cb2c3edea868f8b4) から README を探し、参照し直した URL または未確認と記録する |

    Explorer を使わず README だけで進めた場合は、資料を読んだ代替演習と記録します。

参考: [公式の Explorer ガイド](https://github.com/ibm-self-serve-assets/building-blocks/tree/f721f5ec1915225ade62d8d0e780fe6b19aa58b8/explore-BBs)

[次へ →](part2.md){ .workshop-next }
