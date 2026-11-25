#!/usr/bin/env python3
"""The Meeting That Should Have Been an Email -- make.fun entry.

Writes a single one-line joke (at most 200 characters) to /output/entry.txt.
Python 3 standard library only; no network access.
"""

import os
from pathlib import Path

ENTRY = "Someone shared their screen to show us the email we had been summoned to discuss, then read it to us, slowly."

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUTPUT_PATH = OUTPUT_DIR / "entry.txt"


def main() -> None:
    text = ENTRY
    if not text or not text.strip():
        raise ValueError("entry must not be empty or whitespace-only")
    if len(text) > 200:
        raise ValueError(f"entry is {len(text)} characters, over the 200 limit")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    os.chmod(OUTPUT_PATH, 0o644)
    # Read-back: the file on disk must be byte-for-byte the validated entry.
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    if written != text:
        raise ValueError("read-back mismatch: /output/entry.txt differs from entry")
    if len(written) > 200 or "\n" in written or "\r" in written:
        raise ValueError("read-back failed the gate: not a single line of 1-200 characters")


if __name__ == "__main__":
    main()
