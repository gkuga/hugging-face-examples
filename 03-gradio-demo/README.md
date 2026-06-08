# 03 - gradio-demo

Wrap the example 01 sentiment-analysis pipeline in a Gradio web UI, so it can
be used from a browser instead of the terminal.

## Run

```bash
uv sync
uv run main.py
```

Then open the printed URL in a browser:

```
Running on local URL:  http://127.0.0.1:7860
```

Type a sentence and see whether it is POSITIVE or NEGATIVE, with a confidence
bar. Example inputs are provided as clickable buttons.

## What this shows

- `gr.Interface(fn=..., inputs=..., outputs=...)` builds a full web UI from a
  plain Python function — no HTML/JS needed.
- The model is loaded once at startup, then reused for every request.
- `demo.launch()` starts a local web server (default port 7860).

## Next step

A Gradio app like this can be deployed for free on **Hugging Face Spaces**,
which gives it a public URL anyone can use.
