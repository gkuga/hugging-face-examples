# 01 - sentiment-analysis

A Hugging Face Hello World: sentiment analysis with the `pipeline` from `transformers`.

```bash
# Install dependencies (uv creates .venv automatically)
uv sync

# Run (the model is downloaded automatically on the first run)
uv run main.py
```

- Internally it uses `distilbert-base-uncased-finetuned-sst-2-english`.
- On the first run, the model is cached under `~/.cache/huggingface`.
- No Hugging Face account or token is required for this example.
