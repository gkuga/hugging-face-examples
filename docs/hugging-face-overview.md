# Hugging Face Overview

Notes on what Hugging Face is, to keep this repo's examples in context.

## What is Hugging Face?

A good mental model: **"GitHub for AI models" + cloud services on top**.
It is *half open source, half SaaS*, not a pure SaaS.

The name "Hugging Face" refers to three things depending on context:

1. **The company** — Hugging Face, Inc.
2. **The libraries** — open-source Python packages (`transformers`, etc.)
3. **The Hub** — the website (huggingface.co) where models and datasets are shared.

## Three layers

| Layer | Examples | Nature | Cost |
|-------|----------|--------|------|
| 1. OSS libraries | `transformers`, `datasets`, `gradio` | Open source, runs locally | Free (runs on your machine) |
| 2. Hub (platform) | model / dataset repos on huggingface.co | Sharing site, similar to GitHub | Public free; private partly paid |
| 3. Cloud services (SaaS) | Inference API / Endpoints, Spaces | Run/host models on HF servers | Free tier + usage / subscription |

**The core is the OSS libraries, not the SaaS.** `transformers` and `gradio`
run locally for free; the cloud services are an optional convenience layer on
top for people who want to run or publish without managing infrastructure.

## Key libraries

| Library | Role |
|---------|------|
| `transformers` | Run models (inference / training). The core library. |
| `datasets` | Load and process datasets. |
| `huggingface_hub` | Talk to the Hub (download/upload, auth). |
| `tokenizers` | Fast text-to-token conversion (used under the hood). |
| `accelerate` | Optimize training across GPUs / multiple machines. |
| `gradio` | Build web UIs / demos for models. |

Installing `transformers` automatically pulls in `huggingface_hub` and
`tokenizers` as dependencies.

## Local vs cloud inference

A central distinction these examples illustrate:

| | Local inference | Cloud inference |
|---|-----------------|-----------------|
| Where it runs | Your machine | Hugging Face servers |
| Model download | Required (cached in `~/.cache/huggingface`) | Not needed |
| Token required | No | Yes |
| Used in | example 01, 03 | example 02 |

## How the examples map to the layers

- **01 sentiment-analysis** — Layer 1 (OSS). Local `pipeline`, no HF servers.
- **02 hub-authentication** — Layer 3 (SaaS). Token + Inference API.
- **03 gradio-demo** — Layer 1 (OSS). Deploying it to Spaces would make it Layer 3.

## Tokens and authentication

- A token proves "who you are" to the Hub and is required for cloud services
  and private/gated content.
- Types: **Read** (read/inference), **Write** (upload), **Fine-grained**
  (scoped permissions).
- Best practice: never hardcode tokens. Use `hf auth login` (saved under
  `~/.cache/huggingface`) or the `HF_TOKEN` environment variable.

## References

- Hub: https://huggingface.co
- Docs: https://huggingface.co/docs
- Tokens: https://huggingface.co/settings/tokens
