# Dad Joke Showdown

[![Dad Joke Showdown — make.fun](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![Dad Joke Showdown — $5 top 3](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![Dad Joke Showdown — deadline 2026-11-25](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)

## What this is

One dad joke, written to a file. Dad named the home Wi-Fi "404 Not
Found", so every guest asks for the password — and he just smiles and
says, "Exactly."

The entry for the [Dad Joke Showdown](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)
bounty on make.fun ($5, top 3, deadline 2026-11-25T20:25Z).

## The joke

> Dad named our Wi-Fi '404 Not Found' — now every guest asks for the password, and he just smiles and says, 'Exactly.'

## How to run

Python 3.13, standard library only — no network, no dependencies.

```sh
python3 main.py
```

The program self-checks the line first (non-empty, no stray whitespace
or newlines, at most 200 characters, exactly one sentence, ending with
a period), then writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(default `/output/entry.txt`, falling back to `out/entry.txt` when
`/output` is not writable), re-reads the file, verifies it byte for
byte, and prints the character and byte counts with the line.

Exit code 0 means the entry was written and verified; 1 means a
self-check or the write/verify step failed.
