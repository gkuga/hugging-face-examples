# hugging-face-examples

A collection of experiments for getting familiar with Hugging Face.
Each directory is a self-contained uv project.

See [docs/hugging-face-overview.md](docs/hugging-face-overview.md) for a short
overview of what Hugging Face is (libraries, Hub, and cloud services).

## Examples

| # | Name | Description |
|---|------|-------------|
| 01 | [sentiment-analysis](01-sentiment-analysis/) | Hello World: sentiment analysis with `pipeline` |
| 02 | [hub-authentication](02-hub-authentication/) | Authenticate with a token and run a model via the Inference API |
| 03 | [gradio-demo](03-gradio-demo/) | Wrap the sentiment-analysis pipeline in a Gradio web UI |

## Next steps (TODO)

Candidate examples to build next:

- [ ] **A. Deploy to Spaces** — publish the example 03 Gradio app to Hugging
  Face Spaces to get a public URL.
- [ ] **B. Datasets** — load a public dataset from the Hub with
  `load_dataset()`; the data side that complements models.
- [ ] **C. Other modalities** — try non-text tasks via `pipeline`, e.g. image
  classification or speech recognition.
- [ ] **D. Fine-tuning** — fine-tune an existing model on your own data with
  the `Trainer` API (the heaviest step: data prep + GPU).

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
