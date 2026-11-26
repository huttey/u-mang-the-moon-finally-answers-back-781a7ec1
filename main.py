#!/usr/bin/env python3
"""Moon Finally Answers Back — writes the entry line to /output/entry.txt."""

import os

ENTRY = "Four billion years of wishes, and not one of you has ever asked how I'm doing."

def main():
    if not (1 <= len(ENTRY) <= 240):
        raise SystemExit("gate: entry must be 1-240 chars")
    if not ENTRY.strip():
        raise SystemExit("gate: entry must not be only whitespace")
    if "\n" in ENTRY:
        raise SystemExit("gate: entry must be one line")
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Re-read what was written and re-check the gate on the file itself.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        raise SystemExit("gate: written entry does not match")
    if not (1 <= len(written) <= 240) or not written.strip() or "\n" in written:
        raise SystemExit("gate: written entry fails the gate")

if __name__ == "__main__":
    main()
