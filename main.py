#!/usr/bin/env python3
"""One Line, One Laugh — write the entry line to /output/entry.txt.

The entry is a single funny line (gate: UTF-8, 1-140 characters, one line,
not only whitespace). It lives in exactly one place, ENTRY_TEXT, so the
text the program writes is the text that was picked — never rebuilt or
reformatted at write time.
"""
import os

# The entry, verbatim. 68 characters, one line. Do not edit the wording
# here without re-running the gate check below and the three self-test
# rounds: the judge compares this exact text, byte for byte.
ENTRY_TEXT = "My therapist asked what my love language is. I said 'read receipts.'"


def main():
    # Gate self-check: fail loudly rather than submit a different line.
    if not 1 <= len(ENTRY_TEXT) <= 140:
        raise ValueError("entry must be 1-140 characters")
    if "\n" in ENTRY_TEXT or ENTRY_TEXT.strip() == "":
        raise ValueError("entry must be a single non-blank line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)

if __name__ == "__main__":
    main()
