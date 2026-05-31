# discordbot-anonymous

Discord チャンネルに匿名投稿ボタンを設置する Bot です。

## 機能

- `/匿名投稿ボタン` で匿名投稿ボタンを設置します。
- ボタンを押すとモーダルが開き、任意のペンネームと本文を投稿できます。
- 投稿後は匿名投稿ボタンをチャンネル末尾に再設置します。
- 既存 extension としてテンプレメッセージボタンも読み込まれています。

## 再設計メモ

この repo は既存運用を優先して維持していますが、100体プロジェクトの単機能方針では分割候補です。

- `discordbot-anonymous`: 匿名投稿ボタン
- `discordbot-template-message`: テンプレメッセージ投稿ボタン

次に大きな仕様変更を入れる場合は、既存利用状況を確認したうえで単機能 repo へ分割するか判断してください。

## 環境変数

| Name | Required | Description |
| --- | --- | --- |
| `DISCORD_BOT_TOKEN` | Yes | Discord Bot token |
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
