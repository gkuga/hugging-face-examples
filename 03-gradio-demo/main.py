"""Gradio demo: wrap the sentiment-analysis pipeline in a web UI.

This turns the example 01 classifier into a browser app. Gradio builds the
input box, button, and output area automatically from a plain Python
function, then serves it on a local web server.

Run it, then open the printed URL (http://127.0.0.1:7860) in a browser.
"""

import gradio as gr
from transformers import pipeline

# Load the model once at startup (not on every request), so the UI stays
# responsive. Same default model as example 01.
classifier = pipeline("sentiment-analysis")


def analyze(text: str) -> dict[str, float]:
    """Classify one piece of text and return label -> confidence.

    Returning a dict lets gr.Label render it as a labeled confidence bar.
    """
    if not text.strip():
        return {}
    result = classifier(text)[0]
    return {result["label"]: result["score"]}


# gr.Interface wires a function to inputs/outputs and generates the UI.
demo = gr.Interface(
    fn=analyze,
    inputs=gr.Textbox(lines=3, label="Text", placeholder="Type a sentence..."),
    outputs=gr.Label(label="Sentiment"),
    title="Sentiment Analysis",
    description="Hugging Face pipeline + Gradio. Enter text to see if it is POSITIVE or NEGATIVE.",
    examples=[
        ["I love using Hugging Face!"],
        ["This is the worst movie I have ever seen."],
        ["The weather is okay today."],
    ],
)


if __name__ == "__main__":
    # launch() starts a local web server and prints the URL.
    demo.launch()
