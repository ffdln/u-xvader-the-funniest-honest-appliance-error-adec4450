#!/usr/bin/env python3
"""The Funniest Honest Appliance Error — one honest error line.

The entry is a single fixed error message, written for make.fun
u-xvader-the-funniest-honest-appliance-error-adec4450: the funniest
honest error message an appliance could show. A washing machine
reporting an unbalanced load, in its own flat, put-upon voice. This
program writes that line to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt outside the grader's container):

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

Python 3.13, standard library only. The line is fixed text: the same
bytes on every run, no network.
"""

import os
import sys
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

LINE = (
    "Error U02: Load unbalanced. I have shaken myself apart trying "
    "to spin one wet towel. Please remove it before I file for early "
    "retirement."
)


def abort(message):
    """Stop with the reason on stderr and a non-zero exit."""
    print(f"main.py: {message}", file=sys.stderr)
    return 1


def deliver():
    """Validate the line against the gate, then write it out."""
    if not 1 <= len(LINE) <= 200:
        return abort(f"line is {len(LINE)} characters, the gate allows 1-200")
    if not LINE.strip():
        return abort("line is only white space, the gate refuses it")
    target = Path(OUTPUT_DIR) / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE, encoding="utf-8")
    print(f"wrote {target}: {len(LINE)} characters")
    return 0


if __name__ == "__main__":
    raise SystemExit(deliver())
