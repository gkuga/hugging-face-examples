"""Hugging Face Hello World: sentiment analysis

The `pipeline` from transformers runs model download, tokenization,
inference, and post-processing all in one call. This is the most basic
building block of Hugging Face.

On the first run, the model (~250MB) is downloaded automatically from the
Hub. After that it is loaded from the local cache (~/.cache/huggingface).
"""

from transformers import pipeline


def main() -> None:
    # Passing a task name ("sentiment-analysis") selects the default model
    # for that task. Internally it uses
    # distilbert-base-uncased-finetuned-sst-2-english.
    classifier = pipeline("sentiment-analysis")

    texts = [
        "I love using Hugging Face!",
        "This is the worst movie I have ever seen.",
        "The weather is okay today.",
    ]

    results = classifier(texts)

    for text, result in zip(texts, results):
        # result is {"label": "POSITIVE"/"NEGATIVE", "score": 0.0-1.0}
        print(f"{result['label']:>8} ({result['score']:.4f})  <-  {text}")


if __name__ == "__main__":
    main()
