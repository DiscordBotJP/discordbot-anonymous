# discordbot-anonymous

Discord チャンネルに匿名投稿ボタンを設置する Bot です。

## 機能

- `/匿名投稿ボタン` で匿名投稿ボタンを設置します。
- ボタンを押すとモーダルが開き、任意のペンネームと本文を投稿できます。
- 投稿後は匿名投稿ボタンをチャンネル末尾に再設置します。

## 先行公開範囲

Discord Bot JP の先行公開では、この repo は `discordbot-anonymous` として匿名投稿ボタンだけを案内対象にします。

- 対象: 匿名投稿ボタンの設置、匿名投稿モーダル、投稿後のボタン再設置
- 対象外: テンプレメッセージ投稿ボタンの新規案内、テンプレ文面の追加、テンプレ機能の拡張

既存互換のため `template` extension は読み込まれていますが、公開導線では匿名投稿と分けて扱います。

## commands / extensions 棚卸し

| Extension | Slash command | Persistent components | User flow | 先行公開での扱い |
| --- | --- | --- | --- | --- |
| `extensions.anonymous` | `/匿名投稿ボタン` | `secret_post:post` button, anonymous post modal | 管理者が投稿ボタンを設置し、参加者がペンネーム任意の匿名本文を通常メッセージとして投稿する | Primary |
| `extensions.template` | `/テンプレメッセージボタン` | `template_message:*` buttons | 管理者がテンプレボタン群を設置し、参加者が定型文 embed を webhook で投稿する | Existing compatibility only |

`main.py` は `anonymous` と `template` を両方 load し、`discord.Intents.default()` に `guilds` だけを明示しています。Message Content Intent と Voice States Intent は使いません。

## 利用者導線

### 匿名投稿

1. チャンネル管理権限を持つユーザーが `/匿名投稿ボタン` を実行します。
2. Bot が匿名投稿ボタンを対象チャンネルに投稿します。
3. 参加者がボタンを押してモーダルを開きます。
4. 任意のペンネームと本文を入力します。
5. Bot が入力内容を投稿し、匿名投稿ボタンをチャンネル末尾に再設置します。

### テンプレメッセージ

1. チャンネル管理権限を持つユーザーが `/テンプレメッセージボタン` を実行します。
2. Bot が起床、就寝、外出中などのテンプレボタン群を対象チャンネルに投稿します。
3. 参加者がボタンを押すと、Bot が既存または新規 webhook から定型文 embed を投稿します。
4. Bot がテンプレボタン群をチャンネル末尾に再設置します。

この導線は匿名投稿と別の価値なので、Discord Bot JP の単機能 Bot としては分離候補です。

## 分割判断

| Option | Pros | Cons | Recommendation |
| --- | --- | --- | --- |
| 匿名投稿Botとして維持する | 公開メッセージが明確。現 repo 名と一致する。追加の移行なしで先行公開できる | `template` command が同居したままなので、利用者には案内しない運用が必要 | 先行公開の既定方針 |
| テンプレート投稿Botを別 repo / 別 Bot へ分離する | 単機能方針に合う。権限・利用導線を別々に説明できる | 既存導入先の command / webhook 利用状況を人間確認する必要がある | 次回大きな仕様変更前に実施判断 |
| 片方を後続 Wave へ回す | 先行公開の説明が簡単。未検証機能を表に出さずに済む | `template` extension はコード上残るため、完全な非公開にはデプロイ設定かコード分岐が必要 | テンプレ機能は後続 Wave 候補 |

## 再設計メモ

この repo は既存運用を優先して維持していますが、100体プロジェクトの単機能方針では分割候補です。

- `discordbot-anonymous`: 匿名投稿ボタン
- `discordbot-template-message`: テンプレメッセージ投稿ボタン

次に大きな仕様変更を入れる場合は、既存利用状況を確認したうえで単機能 repo へ分割するか判断してください。

## 環境変数

| Name | Required | Description |
| --- | --- | --- |
| `DISCORD_BOT_TOKEN` | Yes | Discord Bot token |
| `CHANNEL_LOG_ID` | Yes | Daug command/component log channel ID |
| `CHANNEL_TRACEBACK_ID` | Yes | Daug traceback/error log channel ID |
| `OPS_LOG_HUB_URL` | No | ops-log-hub ingest endpoint |
| `OPS_LOG_HUB_KEY` | No | ops-log-hub ingest key |
| `OPS_LOG_PROJECT` | No | ops-log project name. Default: `discordbot-anonymous` |
| `OPS_LOG_ENVIRONMENT` | No | `production` / `development` など |

## 必要権限・Intents

- View Channel
- Send Messages
- Manage Messages
- Manage Webhooks
- Use Slash Commands

Message Content Intent と Voice States Intent は不要です。

機能別の権限は以下です。

| Feature | Setup user permission | Bot permission | Intent |
| --- | --- | --- | --- |
| 匿名投稿ボタン | Manage Channels | View Channel, Send Messages, Manage Messages, Use Slash Commands | Guilds |
| テンプレメッセージボタン | Manage Channels | View Channel, Send Messages, Manage Messages, Manage Webhooks, Use Slash Commands | Guilds |

## Ops logging

`OPS_LOG_HUB_URL` と `OPS_LOG_HUB_KEY` が設定されている場合のみ、以下のイベントを ops-log-hub に送信します。

- `startup`: Bot 起動完了
- `config_error`: extension load / command sync の失敗
- `command_error`: slash command、ボタン、モーダル処理の失敗

ログには投稿本文や secret 値は含めず、guild/channel ID など調査に必要な最小限の情報だけを入れます。

## Local run

```bash
cp .env.example .env
python -m pip install -r requirements.txt
python main.py
```
