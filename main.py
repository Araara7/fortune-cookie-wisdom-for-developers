#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers — one original line.

"Legacy code is a letter from a stranger who knew exactly what they
were doing, once." Writes it to /output/entry.txt.

Why this line: it reads like a real fortune cookie (one short balanced
sentence, lands in a single breath), it is true about a developer's day
(every senior engineer has inherited legacy code), and it turns that
truth with a fresh twist — "once" carries a double meaning (at one time
/ only once), rewarding a second read.
"""
import os

ENTRY = "Legacy code is a letter from a stranger who knew exactly what they were doing, once."

def write_entry():
    """Write the entry and verify the bytes on disk match exactly."""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        assert f.read() == ENTRY, "entry.txt does not match entry"


def validate_entry():
    """Gate: one non-empty line, 1-120 characters, UTF-8 text."""
    assert 1 <= len(ENTRY) <= 120, "entry must be 1-120 characters"
    assert ENTRY.strip() == ENTRY and ENTRY.count("\n") == 0, "entry must be one line"
    ENTRY.encode("utf-8")


def main():
    validate_entry()
    write_entry()


if __name__ == "__main__":
    main()
