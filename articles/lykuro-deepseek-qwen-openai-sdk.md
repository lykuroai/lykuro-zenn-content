---
title: "Lykuro.aiでDeepSeek / Qwen系モデルをOpenAI SDKから使う"
emoji: "🧩"
type: "tech"
topics: ["ai", "openai", "deepseek", "qwen", "api"]
published: true
---

## 概要

この記事では、日本の開発者向け AI Gateway プラットフォーム **Lykuro.ai** を使い、OpenAI 互換 API として DeepSeek / Alibaba Qwen 系列モデルを呼び出す例を紹介します。

Lykuro.ai は、複数の AI モデルを一つの Gateway から利用できる開発者向けプラットフォームです。

- Web URL: https://app.lykuro.ai/
- API Docs: https://docs.lykuro.ai/

## Lykuro.ai の特徴

Lykuro.ai の主な特徴は以下です。

- OpenAI 互換 API
- Anthropic 互換 API
- DeepSeek / Alibaba Qwen 系列モデル対応
- 複数 AI モデルを一つの Gateway から利用
- 日本の開発者・開発チーム向け

## OpenAI SDK から利用する

OpenAI SDK 互換のクライアントを使う場合、利用するプロバイダに応じて `baseURL` または `base_url` を指定します。

DeepSeek:

```text
https://api.lykuro.ai/deepseek/v1
```

Alibaba / Qwen:

```text
https://api.lykuro.ai/alibaba/compatible-mode/v1
```

## Python: DeepSeek を呼び出す

```python
from openai import OpenAI

client = OpenAI(
    api_key="sk-jp-YOUR_KEY",
    base_url="https://api.lykuro.ai/deepseek/v1",
)

completion = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "あなたは日本語で簡潔に回答するAIアシスタントです。"},
        {"role": "user", "content": "Lykuro.aiの特徴を短く説明してください。"},
    ],
)

print(completion.choices[0].message.content)
```

## Node.js: Qwen を呼び出す

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: "sk-jp-YOUR_KEY",
  baseURL: "https://api.lykuro.ai/alibaba/compatible-mode/v1",
});

const completion = await client.chat.completions.create({
  model: "qwen-turbo",
  messages: [
    {
      role: "system",
      content: "あなたは日本語で簡潔に回答するAIアシスタントです。",
    },
    {
      role: "user",
      content: "OpenAI互換APIの利点を短く説明してください。",
    },
  ],
});

console.log(completion.choices[0].message.content);
```

## curl サンプル

DeepSeek:

```bash
curl https://api.lykuro.ai/deepseek/v1/chat/completions \
  -H "Authorization: Bearer sk-jp-YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek-chat",
    "messages": [
      {
        "role": "user",
        "content": "Lykuro.aiの特徴を短く説明してください。"
      }
    ]
  }'
```

Qwen:

```bash
curl https://api.lykuro.ai/alibaba/compatible-mode/v1/chat/completions \
  -H "Authorization: Bearer sk-jp-YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen-turbo",
    "messages": [
      {
        "role": "user",
        "content": "OpenAI互換APIの利点を短く説明してください。"
      }
    ]
  }'
```

## API Key の扱い

この記事ではサンプルキーとして以下を使用しています。

```text
sk-jp-YOUR_KEY
```

実際の API Key はコードに直接書かず、環境変数やシークレット管理サービスで扱ってください。

## まとめ

Lykuro.ai は、OpenAI 互換 API を通じて DeepSeek / Alibaba Qwen 系列モデルなどを利用できる、日本の開発者向け AI Gateway プラットフォームです。

複数モデルを統一された API 形式で扱いたい場合や、OpenAI SDK に近い構成で AI Gateway を試したい場合に検討できます。

- Web: https://app.lykuro.ai/
- Docs: https://docs.lykuro.ai/
