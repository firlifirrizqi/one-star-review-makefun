#!/usr/bin/env python3
"""One-Star Review of Something Essential entry: writes one review line to /output/entry.txt.

The line is a deadpan one-star review of sleep: eight hours paid, still tired,
dreams just work with worse lighting. Chosen from six candidates in CANDIDATES.md."""

LINE = "One star. Paid eight hours, woke up tired, and the dreams were just my job with worse lighting."

# The gate: /output/entry.txt must hold 1 to 160 characters of real text,
# on a single line (the brief asks for one review line, not a paragraph).
assert 1 <= len(LINE) <= 160 and LINE.strip(), "line must be 1-160 characters"
assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"

if __name__ == "__main__":
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
