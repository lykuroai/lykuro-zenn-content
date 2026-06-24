---
title: "Lykuro.ai API サンプル: QwenをNode.jsから呼び出す実装メモ (2026-06-24)"
emoji: "🟩"
type: "tech"
topics: ["ai", "openai", "qwen", "nodejs", "api"]
published: true
---

## 概要

この記事では、Lykuro.ai の OpenAI 互換 API を使って、Node.js アプリケーションから Qwen 系モデルを OpenAI 互換 API として呼び出す方法を紹介します。

Lykuro.ai は、日本の開発者向け AI Gateway プラットフォームです。

- Web: https://app.lykuro.ai/
- Docs: https://docs.lykuro.ai/

## 今週のテーマ

Alibaba / Qwen を題材に、既存の OpenAI SDK に近い形で Lykuro.ai の API を呼び出す流れを確認します。

## API Base URL

```text
https://api.lykuro.ai/alibaba/compatible-mode/v1
```

## Python サンプル

```python
from openai import OpenAI

client = OpenAI(
    api_key="sk-jp-YOUR_KEY",
    base_url="https://api.lykuro.ai/alibaba/compatible-mode/v1",
)

response = client.chat.completions.create(
    model="qwen-turbo",
    messages=[
        {"role": "system", "content": "あなたは日本語で簡潔に回答するAIアシスタントです。"},
        {"role": "user", "content": "OpenAI互換APIの利点を3つ教えてください。"},
    ],
)

print(response.choices[0].message.content)
```

## Node.js サンプル

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: "sk-jp-YOUR_KEY",
  baseURL: "https://api.lykuro.ai/alibaba/compatible-mode/v1",
});

const response = await client.chat.completions.create({
  model: "qwen-turbo",
  messages: [
    {
      role: "system",
      content: "あなたは日本語で簡潔に回答するAIアシスタントです。",
    },
    {
      role: "user",
      content: "OpenAI互換APIの利点を3つ教えてください。",
    },
  ],
});

console.log(response.choices[0].message.content);
```

## curl サンプル

```bash
curl https://api.lykuro.ai/alibaba/compatible-mode/v1/chat/completions \
  -H "Authorization: Bearer sk-jp-YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen-turbo",
    "messages": [
      {
        "role": "user",
        "content": "OpenAI互換APIの利点を3つ教えてください。"
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

Lykuro.ai を使うと、OpenAI SDK に近い形で Alibaba / Qwen 系モデルを呼び出せます。

複数モデルを同じ API 形式で扱いたい開発者や、AI Gateway 経由でモデル利用を整理したいチームに向いた構成です。

<!-- generated: 20260624 -->
