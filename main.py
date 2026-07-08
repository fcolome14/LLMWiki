import argparse
import os
from pathlib import Path

from anthropic import Anthropic, BadRequestError
from dotenv import load_dotenv

load_dotenv()

VAULT_PATH = Path("vault")
MODEL = "claude-sonnet-4-6"


def get_client() -> Anthropic:
    try:
        api_key = os.environ["ANTHROPIC_API_KEY"]
    except KeyError:
        raise RuntimeError(
            "ANTHROPIC_API_KEY not set. Copy .env.example to .env and add your key from console.anthropic.com"
        )
    return Anthropic(api_key=api_key)


def load_vault_notes(vault_path: Path) -> dict[str, str]:
    """Read every .md file in the vault into a dict of {relative_path: content}"""
    if not vault_path.exists():
        raise FileNotFoundError(f"Vault path not found: {vault_path.resolve()}")

    notes = {}
    for md_file in vault_path.rglob("*.md"):
        notes[str(md_file.relative_to(vault_path))] = md_file.read_text(encoding="utf-8")

    if not notes:
        raise RuntimeError(f"No .md files found in {vault_path.resolve()}")

    return notes


def build_context(notes: dict[str, str]) -> str:
    """Concatenate all notes into a single context block, labeled by filename"""
    return "\n\n".join(f"--- {path} ---\n{content}" for path, content in notes.items())


def ask_vault(client: Anthropic, question: str, context: str) -> str:
    try:
        message = client.messages.create(
            model=MODEL,
            max_tokens=1500,
            messages=[
                {
                    "role": "user",
                    "content": (
                        "Here are notes from my Obsidian vault:\n\n"
                        f"{context}\n\n"
                        f"Question: {question}\n\n"
                        "Answer using only the information in these notes. If the notes don't "
                        "cover it, say so rather than guessing."
                    ),
                }
            ],
        )
    except BadRequestError as e:
        if "credit balance" in str(e).lower():
            raise RuntimeError(
                "Your Anthropic account has no API credits. Add credits at "
                "https://console.anthropic.com under Plans & Billing, then try again."
            ) from None
        raise
    return message.content[0].text


def main():
    parser = argparse.ArgumentParser(description="Ask questions about your Obsidian vault")
    parser.add_argument("question", help="The question to ask about your vault notes")
    parser.add_argument(
        "--vault", default=str(VAULT_PATH), help="Path to the vault folder (default: vault/)"
    )
    args = parser.parse_args()

    client = get_client()
    notes = load_vault_notes(Path(args.vault))
    print(f"Loaded {len(notes)} notes from {args.vault}")

    context = build_context(notes)
    answer = ask_vault(client, args.question, context)

    print("\n" + answer)


if __name__ == "__main__":
    main()