# はじめに

## 概要

- **目的**: IBM Bob と Building Blocks Explorer モードを用い、業務上の関心に合う Building Blocks を、自然言語の問いによって出典とともに探す方法を理解する。
- **対象**: 初学者。インストールとサインインを済ませた IBM Bob を利用できることを前提とする。
- **学習事項**:
    - Building Blocks の構成（領域、グループ、個別の README）
    - カタログ、モード、スキルと Explorer の関係
    - Explorer が MCP を介してカタログを検索し、候補を出典とともに返す仕組み
- **演習内容**:
    - [Explorer の起動](part1.md): 公式の Explorer の ZIP を展開し、Bob でモードを選択し、カタログへの接続を確認する。
    - [演習](part2.md): 3 つの問い（データストリーミング、アクセス管理とシークレット管理、文書検索）を入力し、回答を確認する。
- **所要時間**: 35 分
- **環境**: Bob は各自の PC で動作し、カタログはインターネット経由で接続する外部のサービスである。クラウドの API キーは使用しない。

## シナリオ

ソリューションを検討している人が、リアルタイムのデータストリーミングやシークレット管理のような要件について、IBM の参照実装が既にあるかを知りたい場面を考えます。Building Blocks は 3 つの領域と 9 つのグループにまたがり、領域ごとに README があります。このハンズオンでは、Building Blocks Explorer モードの IBM Bob に自然言語で問い合わせ、Explorer がカタログを検索して、候補を出典とともに返します。この候補を出発点に、設計や実装を個別に用意する代わりに、既存の構成例やコードで製品の組み合わせを試せます。

## 必要なもの

- インストールとサインインを済ませ、利用できる IBM Bob
- インターネットに接続した macOS または Windows の PC

## 進め方

| 経過時間（分） | 内容 |
| ---: | --- |
| 0–5 | [はじめに](index.md) |
| 5–15 | [Explorer の起動](part1.md) |
| 15–30 | [演習 3 題](part2.md) |
| 30–35 | [まとめ](summary.md) |

## Building Blocks

Building Blocks は、IBM の参照実装や設計パターンを再利用するための資産です。

Building Blocks を使わない場合、設計や実装を個別に用意する必要があります。Building Blocks を使うと、既存の構成例やコードを出発点に、製品の組み合わせを試したり、用途に合わせて拡張したりできます。調査や試作の手間を減らし、業務要件の検証に時間を使えます。

| 領域 | グループ | 個別の README |
| --- | --- | --- |
| AI Control Plane | Agents, Control, Engineering | [AI Control Plane README](https://github.com/ibm-self-serve-assets/building-blocks/blob/5c610971dc72f9e9035821b3cb2c3edea868f8b4/ai/README.md) |
| Streamhouse | Real-Time, Pipelines, Lakehouse | [Streamhouse README](https://github.com/ibm-self-serve-assets/building-blocks/blob/5c610971dc72f9e9035821b3cb2c3edea868f8b4/streamhouse/README.md) |
| Automation | Operate, Secure, Optimize | [Automation README](https://github.com/ibm-self-serve-assets/building-blocks/blob/5c610971dc72f9e9035821b3cb2c3edea868f8b4/automation/README.md) |

参考: [Building Blocks 全体の README](https://github.com/ibm-self-serve-assets/building-blocks/blob/5c610971dc72f9e9035821b3cb2c3edea868f8b4/README.md)

## Building Blocks Explorer

Explorer は、Building Blocks を自然言語で探せる Bob のモードです。質問に応じてカタログや関連資料を調べ、用途や構成の検討を支援します。

| 用語 | Explorer との関係 | `.bob` 内のファイル |
| --- | --- | --- |
| カタログ | Building Blocks と関連資料、スキル、モードの情報をまとめた検索先 | 本体は外部サービス。接続先を `.bob/mcp.json` に定義 |
| モード | Bob の動作を作業に合わせて切り替える設定。Explorer もその 1 つ | `.bob/custom_modes.yaml` に名前や動作の指示などを定義 |
| スキル | 特定の作業に使う手順や知識。Explorer で関連するものを探せる | 追加すると `.bob/skills/<スキル名>/SKILL.md` に手順を配置。補助ファイルを含む場合もある |

公式の Explorer ZIP には `.bob/custom_modes.yaml` と `.bob/mcp.json` が含まれます。スキルのファイルはスキルを追加した場合に配置されます。

??? info "公式の Building Block との違い"
    Explorer のモードと接続の設定は、公式の Explorer ZIP（2026 年 9 月 9 日時点の版）をそのまま使います。このハンズオンでは ZIP を配らず、参加者が公式の ZIP をダウンロードします。Bob に貼り付ける文は、このハンズオン用に書いたものです。

    - **[接続確認の文](part1.md#3)**: 「調査のみ。インストールとデプロイは対象外。」と書く。Explorer は導入操作もできるため。
    - **[演習の 3 つの問い](part2.md)**: 公式の Explorer ガイドの 3 つの例（リアルタイムのデータストリーミング、アクセス管理とシークレット管理、文書から答える店舗のアシスタント）を基に、短い問いに書き直した。

## 参考文献

- Building Blocks: <https://github.com/ibm-self-serve-assets/building-blocks/tree/5c610971dc72f9e9035821b3cb2c3edea868f8b4>
- Building Blocks ドキュメント: <https://ibm-self-serve-assets.github.io/building-blocks-docs/>
- Explorer: <https://github.com/ibm-self-serve-assets/building-blocks/tree/f721f5ec1915225ade62d8d0e780fe6b19aa58b8/explore-BBs>

[次へ →](preparation.md){ .workshop-next }
