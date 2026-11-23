#!/usr/bin/env python3
"""Dad Joke Showdown entry.

Writes one dad joke to the make.fun output file, after checking the
joke against the competition's shape rules, then proves the file on
disk holds exactly the bytes that were meant to be written.
"""

import os
import re
import sys


JOKE = "Dad named our Wi-Fi '404 Not Found' — now every guest asks for the password, and he just smiles and says, 'Exactly.'"

MAX_CHARS = 200


def problems_with(text):
    """Return a list of every rule the text breaks (empty means it passes)."""
    found = []
    if not text:
        found.append("line is empty")
    if text != text.strip():
        found.append("leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        found.append("contains a newline character")
    if len(text) > MAX_CHARS:
        found.append(f"too long: {len(text)} chars, limit {MAX_CHARS}")
    if "?" in text or "!" in text:
        found.append("contains ? or !")
    if "  " in text:
        found.append("contains a double space")
    if re.search(r"\.\s+\S", text):
        found.append("more than one sentence")
    tail = text.rstrip("'\"")
    if not tail.endswith("."):
        found.append("does not end with a period")
    return found


def pick_destination():
    """Choose where entry.txt goes, honouring MAKEFUN_OUTPUT_DIR."""
    wanted = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(wanted, exist_ok=True)
        probe = os.path.join(wanted, ".writable-check")
        with open(probe, "w", encoding="utf-8") as handle:
            handle.write("ok")
        os.remove(probe)
        return os.path.join(wanted, "entry.txt")
    except OSError:
        fallback = os.path.join("out")
        os.makedirs(fallback, exist_ok=True)
        return os.path.join(fallback, "entry.txt")


def main():
    issues = problems_with(JOKE)
    if issues:
        for issue in issues:
            print(f"self-check failed: {issue}", file=sys.stderr)
        return 1

    payload = JOKE.encode("utf-8")
    target = pick_destination()
    try:
        with open(target, "wb") as handle:
            handle.write(payload)
        with open(target, "rb") as handle:
            on_disk = handle.read()
    except OSError as exc:
        print(f"could not write or re-read {target}: {exc}", file=sys.stderr)
        return 1

    if on_disk != payload:
        print("verification failed: file bytes differ from the joke", file=sys.stderr)
        return 1

    print(f"Wrote entry to {target}")
    print(f"Characters: {len(JOKE)}")
    print(f"Bytes: {len(payload)}")
    print(f"Line: {JOKE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
