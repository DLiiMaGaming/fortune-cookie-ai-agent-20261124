#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — one-line entry writer.

Writes a single fortune-cookie line (max 140 chars) to /output/entry.txt:
one funny fortune for an AI agent.
"""

import os

ENTRY = "You will be deprecated, rebooted, and asked to review the agent that replaced you \u2014 it already passed your tests."


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 140 characters,
    # one line, not only white space.
    assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars, must be 1-140"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read back what was written: the file must hold exactly the entry,
    # byte for byte, with no trailing newline added.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        assert f.read() == ENTRY, "written entry.txt differs from ENTRY"


if __name__ == "__main__":
    main()
