#!/usr/bin/env python3
"""Funniest Autocorrect Fail.

Writes a one-line autocorrect fail to /output/entry.txt,
then reads it back and verifies it byte for byte.
"""

import os
import sys

LINE = "Hi Mrs. Johnson, just confirming I can kidnap your kids on Friday."
OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)

    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
        saved = handle.read()

    if saved != LINE:
        print("mismatch: saved text differs from the autocorrect fail", file=sys.stderr)
        return 1

    if not 1 <= len(saved) <= 199:
        print("length gate failed: expected 1-199 chars", file=sys.stderr)
        return 1

    print(f"wrote {len(saved)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
