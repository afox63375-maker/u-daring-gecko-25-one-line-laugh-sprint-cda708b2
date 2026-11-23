"""One-Line Laugh Sprint entry.

Writes a single original one-line joke to /output/entry.txt.
Standard library only, fully deterministic, no network access.
"""

import os

JOKE = (
    "My fridge hums all night like it is gossiping about me, "
    "yet it is the only one in the house who never judges what I eat at 2 a.m."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(line):
    """Check the line against the competition gate.

    The gate requires UTF-8 text, 1-200 characters, exactly one line,
    and more than just whitespace.
    """
    if not isinstance(line, str):
        raise TypeError("joke must be a string")
    if not line.strip():
        raise ValueError("joke must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("joke must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError("joke must be 1-200 characters, got %d" % len(line))
    line.encode("utf-8")  # raises if not UTF-8 encodable


def main():
    validate(JOKE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        # Write the joke byte-for-byte, with no trailing newline.
        handle.write(JOKE)
    print("Wrote %d characters to %s" % (len(JOKE), OUTPUT_PATH))


if __name__ == "__main__":
    main()
