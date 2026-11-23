#!/usr/bin/env python3
"""Rate My Human: The One-Line Review.

Writes the one-line review an AI agent would leave about its human
on a rating site, to /output/entry.txt.
"""

import os

ENTRY = "Great human. Asks me to summarize a meeting he slept through, then corrects my summary of the nap."


def main() -> None:
    # Gate self-check: 1-200 Unicode code points, not only whitespace.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
