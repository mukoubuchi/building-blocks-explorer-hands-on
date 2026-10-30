# Explorer の起動

所要時間: 10 分（経過時間: 15–25 分）

## ステップ 1: ダウンロードして展開する

[公式の Explorer ZIP](https://raw.githubusercontent.com/ibm-self-serve-assets/building-blocks/f721f5ec1915225ade62d8d0e780fe6b19aa58b8/explore-BBs/building-blocks-explorer.zip) をダウンロードします。

=== "macOS"

    Finder で ZIP をダブルクリックして展開します。

=== "Windows"

    ZIP を右クリック →「すべて展開」を選びます。ZIP の表示画面ではなく、展開後のフォルダを使います。

## ステップ 2: Bob でモードを選ぶ

1. IBM Bob を起動します。
1. `README.md` と `.bob` が入った `building-blocks-explorer` フォルダを開きます。

    === "macOS"

        メニューの <kbd>ファイル</kbd> → <kbd>開く...</kbd> を選び、`building-blocks-explorer` フォルダを選びます。<kbd>⌘</kbd> + <kbd>O</kbd> でも開けます。

    === "Windows"

        メニューの <kbd>ファイル</kbd> → <kbd>フォルダーを開く...</kbd> を選び、`building-blocks-explorer` フォルダを選びます。

1. 制限モードの帯が出た場合は、帯の「管理」、続いて「信頼する」を選び、信頼の画面を閉じます。
1. IBM Bob のパネルで、チャット入力欄の下にあるモードの選択欄を開き、「🧱 IBM Building Blocks Explorer」を選びます。

## ステップ 3: 接続を確認する

IBM Bob のパネルの右上にある小さな歯車のアイコン（Settings）を選びます。画面の左下にある歯車（管理）とは別のものです。画面の右下の `Bob設定` からも、同じ設定の画面が開きます。開いた設定の画面で、左の一覧の「MCP」を選び、次のサーバーを確認します。

| サーバー | 役割 |
| --- | --- |
| `building-blocks` | リモートのカタログを検索する。 |
| `building-blocks-installer` | uvx でローカルのインストーラーを動かす。 |

!!! warning "インストーラーの不具合"
    `building-blocks-installer` は上流の不具合（[#262](https://github.com/ibm-self-serve-assets/building-blocks/issues/262)）で起動せず、MCP の画面では「切断済み」と表示されます。[課題 1〜3](part2.md) はカタログだけを使うので、そのまま進めます。[追加の演習](part2.md#extra) にはインストーラーが必要です。

Bob のチャットへ貼り付けます。

```text
Building Blocks のカタログツールを使い、AI Control Plane（旧: AI）、Data、Automation から候補を 1 つずつ紹介する。
各候補には名前、用途、出典 URL を添える。
調査のみ。インストールは対象外。
```

Bob はカタログのツールを呼ぶたびに承認を求めます（`List Building Blocks (building-blocks)` など）。「一度だけ承認」を選びます。

Explorer は導入操作もできるため、接続確認では調査だけを指示します。

`list_building_blocks` などのツールの実行結果を確認し、出典リンクを開きます。

??? tip "うまく動かない場合"
    | 症状 | 対処 |
    | --- | --- |
    | モードが表示されない | 展開先に `.bob` があることを確認し、Bob を再読み込みする。 |
    | インストーラーが使えない | uv/uvx を確認し、Bob を完全に再起動する。カタログが動けば [課題 1〜3](part2.md) は続けられる。 |
    | 初回起動が遅い | 依存パッケージのダウンロードを待つ。 |
    | カタログが使えない | Bob を 1 回再起動する。解決しなければ講師へ相談し、講師の画面共有で続ける。 |
    | 出典リンクが古い | [Building Blocks の概要](https://github.com/ibm-self-serve-assets/building-blocks/tree/031ceebaed354fddab43b5ff4ef53bff0ed9ffc5) から README を探し、参照し直した URL または未確認と記録する。 |

    Explorer を使わず README だけで進めた場合は、資料を読んだ代替演習と記録します。

参考: [公式の Explorer ガイド](https://github.com/ibm-self-serve-assets/building-blocks/tree/f721f5ec1915225ade62d8d0e780fe6b19aa58b8/explore-BBs)

[次へ →](part2.md){ .workshop-next }
