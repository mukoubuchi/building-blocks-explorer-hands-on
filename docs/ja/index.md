# はじめに

IBM Bob で関心事に最適な Building Blocks を探すハンズオンです。

## 必要なもの

- インストール・サインイン済みで利用できる IBM Bob
- インターネットに接続した macOS または Windows の PC
- ハンズオン中に uv をインストールできる権限

## 進め方

| 経過時間（分） | 内容 |
| ---: | --- |
| 0–10 | はじめに |
| 10–20 | [uv の導入](preparation.md) |
| 20–30 | [Explorer の起動](part1.md) |
| 30–45 | [演習 3 題](part2.md) |
| 45–50 | [まとめ](summary.md) |

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

## 参考文献

- Building Blocks: <https://github.com/ibm-self-serve-assets/building-blocks>
- Building Blocks ドキュメント: <https://ibm-self-serve-assets.github.io/building-blocks-docs/>
- Explorer: <https://github.com/ibm-self-serve-assets/building-blocks/tree/main/explore-BBs>

[次へ →](preparation.md){ .workshop-next }
