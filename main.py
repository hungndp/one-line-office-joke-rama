#!/usr/bin/env python3
"""Make the AI Judge Laugh — one-line office-life joke entry.

Writes a single joke (one line, under 200 characters) to /output/entry.txt.
The joke: a concrete office incident ("per my last email" power move) with
a reversal — the boss fires the same phrase right back — and the twist word
lands last ("retirement").
"""

import os

JOKE = (
    "I used 'per my last email' today to sound senior. "
    "My boss replied 'per my last email' right back, and now the whole "
    "office is watching two people quote emails at each other until retirement."
)


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
