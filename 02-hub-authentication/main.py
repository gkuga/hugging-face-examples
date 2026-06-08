"""Hugging Face Hub authentication with an access token.

This example shows how to authenticate to the Hugging Face Hub using an
access token, and what that token unlocks.

Best practice: never hardcode the token in source code. Either log in once
with `hf auth login`, or set the HF_TOKEN environment variable.

Steps:
  1. Resolve the token with get_token() (it reads the HF_TOKEN env var first,
     then the token saved locally by `hf auth login`).
  2. Call whoami() to confirm the token is valid and see who we are.
  3. As a payoff, run a model in the cloud via the Inference API without
     downloading it locally (this call requires a valid token).

How to authenticate (pick one):
  - Run `hf auth login` once and paste a token (saved to ~/.cache/huggingface)
  - Or export it per shell:  export HF_TOKEN=hf_xxxxxxxx

How to get a token:
  - Sign up at https://huggingface.co
  - Create a token at https://huggingface.co/settings/tokens (a "Read"
    token is enough for this example)
"""

import sys

from huggingface_hub import InferenceClient, get_token, whoami


def main() -> None:
    # 1. Resolve the token. get_token() checks the HF_TOKEN env var first,
    #    then the token saved by `hf auth login`. Returns None if neither
    #    exists, so we never need to hardcode secrets.
    token = get_token()
    if not token:
        print(
            "Not authenticated.\n"
            "Run `hf auth login`, or set HF_TOKEN=hf_xxxxxxxx.\n"
            "Get a token at https://huggingface.co/settings/tokens",
            file=sys.stderr,
        )
        sys.exit(1)

    # 2. whoami() asks the Hub "who owns this token?". A successful call
    #    proves authentication works.
    info = whoami(token=token)
    print(f"Authenticated as: {info['name']} ({info.get('fullname', '')})")
    print(f"Account type    : {info.get('type', 'unknown')}")

    # 3. The payoff: run a model on Hugging Face's servers. The model is
    #    NOT downloaded locally; the token authorizes the remote call.
    client = InferenceClient(token=token)
    completion = client.chat_completion(
        model="Qwen/Qwen2.5-7B-Instruct",
        messages=[{"role": "user", "content": "Say hello in one short sentence."}],
        max_tokens=40,
    )
    print("\nModel reply (run in the cloud, no local download):")
    print(f"  {completion.choices[0].message.content.strip()}")


if __name__ == "__main__":
    main()
