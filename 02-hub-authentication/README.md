# 02 - hub-authentication

Authenticate to the Hugging Face Hub with an access token, and use it to run
a model in the cloud via the Inference API.

## Get a token

1. Sign up at https://huggingface.co
2. Create a token at https://huggingface.co/settings/tokens
   (a **Read** token is enough for this example)

## Authenticate (pick one)

```bash
# Option A: log in once; the token is saved under ~/.cache/huggingface
uv run hf auth login

# Option B: set it per shell (never hardcode it in source)
export HF_TOKEN=hf_xxxxxxxx
```

## Run

```bash
uv sync
uv run main.py
```

Expected output:

```
Authenticated as: <your-username> (...)
Account type    : user

Model reply (run in the cloud, no local download):
  Hello!
```

## What this shows

- `get_token()` resolves the token from the `HF_TOKEN` env var first, then
  the token saved by `hf auth login` — so either flow works.
- `whoami()` confirms the token is valid and tells you who you are.
- `InferenceClient` runs a model (`Qwen/Qwen2.5-7B-Instruct`) on Hugging
  Face's servers using your token, so no model is downloaded locally.

## Note on model availability

The Inference API routes requests to providers, and model availability
changes over time. If you get a `model_not_supported` error, swap the model
for another chat model (e.g. `meta-llama/Llama-3.1-8B-Instruct`).
