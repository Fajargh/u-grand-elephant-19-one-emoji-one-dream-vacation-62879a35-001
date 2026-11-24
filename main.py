"""One Emoji, One Dream Vacation.

Writes a single emoji to /output/entry.txt: a desert island, the
classic dream vacation -- a postcard in one glyph. An island you
escape to, palm tree and all, no words needed.
"""

import os

EMOJI = "\U0001F3DD\uFE0F"  # desert island


def main() -> None:
    # Gate check: the entry must be 1-8 characters, a single emoji,
    # and nothing else -- no words, no whitespace, no extra text.
    assert 1 <= len(EMOJI) <= 8, "entry must be 1-8 characters"
    assert EMOJI.strip() == EMOJI and EMOJI.strip(), "entry must not be whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
