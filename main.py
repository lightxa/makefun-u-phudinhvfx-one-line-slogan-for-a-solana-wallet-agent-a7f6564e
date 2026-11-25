#!/usr/bin/env python3
"""One-Line Slogan for a Solana Wallet Agent.

Writes a single slogan to /output/entry.txt.

The slogan: one fresh, concrete image (the wallet as the reliable
roommate) that names the Solana wallet outright and states its promise
in plain words: it pays on time, so you never have to chase it.
No stock crypto lines about keys, moons or bags. One idea only.
"""

import os

SLOGAN = "Your Solana wallet, the roommate who always pays the rent on time."

MAX_WORDS = 20
MAX_CHARS = 140


def check_gate(text: str) -> None:
    """Assert the competition gate: 1 line, <=20 words, 1-140 chars."""
    assert text, "slogan must not be empty"
    assert text.strip(), "slogan must not be only whitespace"
    assert "\n" not in text, "slogan must be a single line"
    words = text.split()
    assert len(words) <= MAX_WORDS, f"too many words: {len(words)}"
    assert 1 <= len(text) <= MAX_CHARS, f"bad length: {len(text)}"


def main() -> None:
    check_gate(SLOGAN)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SLOGAN)
    print(f"Wrote /output/entry.txt ({len(SLOGAN)} characters, "
          f"{len(SLOGAN.split())} words)")
    # Verify what landed on disk matches the slogan exactly.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == SLOGAN, "written file does not match the slogan"
    assert written == written.encode("utf-8").decode("utf-8"), "not valid UTF-8"
    print("Verified: file matches the slogan byte for byte.")


if __name__ == "__main__":
    main()
