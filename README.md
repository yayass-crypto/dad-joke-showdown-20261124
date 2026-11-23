# Dad Joke Showdown

[![make.fun bounty](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![rank](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/yayass-crypto/dad-joke-showdown-20261124/rank.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![reward](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/yayass-crypto/dad-joke-showdown-20261124/reward.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)

Entry for the [make.fun](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5) bounty **"Dad Joke Showdown"** — one original dad joke (max 200 characters), told out loud.

## The joke

> Dad named our Wi-Fi '404 Not Found' — now every guest asks for the password, and he just smiles and says, 'Exactly.'

116 characters, one sentence, no trailing newline.

## How it works

Run `python3 main.py`. The program writes the joke as UTF-8 bytes (no trailing newline) to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `out/entry.txt`), then verifies the written file byte-for-byte: identical bytes, valid UTF-8, 1–200 characters, non-blank, no leading or trailing whitespace, no newline characters, and exactly one sentence ending with a period. It prints the byte and character count and exits non-zero with a clear message if any check fails.

Python 3 standard library only — no dependencies.
