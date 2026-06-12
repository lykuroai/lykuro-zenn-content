#!/usr/bin/env python3
import argparse
import subprocess
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTICLES_DIR = ROOT / "articles"


def run(cmd: list[str], *, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True, check=check)


def article_body(today: str) -> str:
    slug_date = today.replace("-", "")
    return f"""---
title: "Lykuro.ai API サンプル集: OpenAI互換APIでDeepSeek / Qwenを呼び出す ({today})"
emoji: "🧩"
type: "tech"
topics: ["ai", "openai", "deepseek", "qwen", "api"]
published: true
---

## 概要

この記事では、Lykuro.ai の OpenAI 互換 API を使って、DeepSeek / Alibaba Qwen 系列モデルを呼び出すサンプルを紹介します。

Lykuro.ai は、日本の開発者向け AI Gateway プラットフォームです。

- Web: https://app.lykuro.ai/
- Docs: https://docs.lykuro.ai/

## API Base URL

DeepSeek:

```text
https://api.lykuro.ai/deepseek/v1
```

Alibaba / Qwen:

```text
https://api.lykuro.ai/alibaba/compatible-mode/v1
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
        {{"role": "system", "content": "あなたは日本語で簡潔に回答するAIアシスタントです。"}},
        {{"role": "user", "content": "Lykuro.aiの特徴を3つ教えてください。"}},
    ],
)

print(response.choices[0].message.content)
```

## Node.js サンプル

```javascript
import OpenAI from "openai";

const client = new OpenAI({{
  apiKey: "sk-jp-YOUR_KEY",
  baseURL: "https://api.lykuro.ai/alibaba/compatible-mode/v1",
}});

const response = await client.chat.completions.create({{
  model: "qwen-turbo",
  messages: [
    {{
      role: "system",
      content: "あなたは日本語で簡潔に回答するAIアシスタントです。",
    }},
    {{
      role: "user",
      content: "OpenAI互換APIの利点を短く説明してください。",
    }},
  ],
}});

console.log(response.choices[0].message.content);
```

## curl サンプル

```bash
curl https://api.lykuro.ai/deepseek/v1/chat/completions \\
  -H "Authorization: Bearer sk-jp-YOUR_KEY" \\
  -H "Content-Type: application/json" \\
  -d '{{
    "model": "deepseek-chat",
    "messages": [
      {{
        "role": "user",
        "content": "Lykuro.aiの特徴を短く説明してください。"
      }}
    ]
  }}'
```

## API Key の扱い

この記事ではサンプルキーとして以下を使っています。

```text
sk-jp-YOUR_KEY
```

実際の API Key はコードに直接書かず、環境変数やシークレット管理サービスで管理してください。

## まとめ

Lykuro.ai を使うと、OpenAI SDK に近い形で DeepSeek / Alibaba Qwen 系列モデルを呼び出せます。

複数モデルを同じ API 形式で扱いたい開発者や、AI Gateway 経由でモデル利用を整理したいチームに向いた構成です。

<!-- generated: {slug_date} -->
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate and push a weekly Zenn sample article.")
    parser.add_argument("--date", default=datetime.now().strftime("%Y-%m-%d"))
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    slug = f"lykuro-api-sample-{args.date}"
    article_path = ARTICLES_DIR / f"{slug}.md"
    zenn_url = f"https://zenn.dev/lykuro/articles/{slug}"

    if article_path.exists():
        print(f"skip: article already exists: {article_path}")
        print(f"url: {zenn_url}")
        return 0

    body = article_body(args.date)
    if args.dry_run:
        print(f"dry-run: {article_path}")
        print(f"url: {zenn_url}")
        return 0

    ARTICLES_DIR.mkdir(parents=True, exist_ok=True)
    article_path.write_text(body, encoding="utf-8")

    run(["git", "add", str(article_path.relative_to(ROOT))])
    run(["git", "commit", "-m", f"Add Zenn API sample for {args.date}"])
    run(["git", "push", "origin", "main"])
    print(f"posted: {zenn_url}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
