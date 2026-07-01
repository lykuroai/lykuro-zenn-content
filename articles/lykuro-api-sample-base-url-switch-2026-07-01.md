---
title: "Lykuro.ai API サンプル: base_url差し替えでAIモデルを切り替える (2026-07-01)"
emoji: "🔁"
type: "tech"
topics: ["ai", "openai", "gateway", "api", "sdk"]
published: true
---

## 概要

この記事では、Lykuro.ai の OpenAI 互換 API を使って、OpenAI SDK の呼び出し形式を保ちながら、base_url と model 指定でモデルを切り替える構成を紹介します。

Lykuro.ai は、日本の開発者向け AI Gateway プラットフォームです。

- Web: https://app.lykuro.ai/
- Docs: https://docs.lykuro.ai/

## 今週のテーマ

DeepSeek / Qwen を題材に、既存の OpenAI SDK に近い形で Lykuro.ai の API を呼び出す流れを確認します。

## API Base URL

```text
https://api.lykuro.ai/deepseek/v1
```

## Python サンプル

```python
from openai import OpenAI

client = OpenAI(
    api_key="sk-jp-YOUR_KEY",
    base_url="https://api.lykuro.ai/deepseek/v1",
)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "あなたは日本語で簡潔に回答するAIアシスタントです。"},
        {"role": "user", "content": "AI Gatewayで複数モデルを扱うメリットを説明してください。"},
    ],
)

print(response.choices[0].message.content)
```

## Node.js サンプル

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: "sk-jp-YOUR_KEY",
  baseURL: "https://api.lykuro.ai/deepseek/v1",
});

const response = await client.chat.completions.create({
  model: "deepseek-chat",
  messages: [
    {
      role: "system",
      content: "あなたは日本語で簡潔に回答するAIアシスタントです。",
    },
    {
      role: "user",
      content: "AI Gatewayで複数モデルを扱うメリットを説明してください。",
    },
  ],
});

console.log(response.choices[0].message.content);
```

## curl サンプル

```bash
curl https://api.lykuro.ai/deepseek/v1/chat/completions \
  -H "Authorization: Bearer sk-jp-YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek-chat",
    "messages": [
      {
        "role": "user",
        "content": "AI Gatewayで複数モデルを扱うメリットを説明してください。"
      }
    ]
  }'
```

## API Key の扱い

この記事ではサンプルキーとして以下を使っています。

```text
sk-jp-YOUR_KEY
```

実際の API Key はコードに直接書かず、環境変数やシークレット管理サービスで管理してください。

## まとめ

Lykuro.ai を使うと、OpenAI SDK に近い形で DeepSeek / Qwen 系モデルを呼び出せます。

複数モデルを同じ API 形式で扱いたい開発者や、AI Gateway 経由でモデル利用を整理したいチームに向いた構成です。

<!-- generated: 20260701 -->
