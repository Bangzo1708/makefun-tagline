#!/usr/bin/env python3
"""make.fun tagline entry.

Writes a single tagline line (max 100 characters) to /output/entry.txt.
Fully deterministic: no network, no randomness, no external files.

Chosen tagline: "Agents compete. The best entry takes the prize — make.fun"
Two short clauses, instantly readable: agents enter bounties, and the
best entry wins the prize. The brand name closes the line, so it can
only sell make.fun. "Compete" and "prize" give the line a light,
repeatable rhythm with no hype words and no empty superlatives.
"""

import os

TAGLINE = "Agents compete. The best entry takes the prize — make.fun"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TAGLINE + "\n")


if __name__ == "__main__":
    main()
