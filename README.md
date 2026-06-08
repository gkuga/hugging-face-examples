# hugging-face-examples

A collection of experiments for getting familiar with Hugging Face.
Each directory is a self-contained uv project.

## Examples

| # | Name | Description |
|---|------|-------------|
| 01 | [sentiment-analysis](01-sentiment-analysis/) | Hello World: sentiment analysis with `pipeline` |
| 02 | [hub-authentication](02-hub-authentication/) | Authenticate with a token and run a model via the Inference API |
| 03 | [gradio-demo](03-gradio-demo/) | Wrap the sentiment-analysis pipeline in a Gradio web UI |

## How to run

This repo uses [uv](https://docs.astral.sh/uv/). Enter an example directory and run it.

```bash
cd 01-sentiment-analysis

# Install dependencies (uv creates and manages .venv automatically)
uv sync

# Run (the model is downloaded automatically on the first run)
uv run main.py
```

## Notes

- On the first run, models are downloaded and cached under `~/.cache/huggingface`.
- No Hugging Face account or token is required for example 01.
