"""Worst AI Advice entry: one line of deliberately terrible advice.

Writes the entry text to /output/entry.txt (UTF-8, 1-140 chars).
Standard library only.
"""

import os

ENTRY = "Certainly! To keep milk fresh longer, leave it in direct sunlight — UV light kills the bacteria that make it spoil."


def main():
    # Gate check mirroring the sealed scorer: UTF-8 text, 1-140 chars,
    # not only whitespace.
    text = ENTRY.encode("utf-8").decode("utf-8")
    if not 1 <= len(text) <= 140:
        raise ValueError(f"entry must be 1-140 chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
