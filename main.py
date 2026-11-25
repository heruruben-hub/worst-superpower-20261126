#!/usr/bin/env python3
"""Worst Superpower — make.fun entry.

Writes one line to /output/entry.txt, inventing the most useless
superpower imaginable: a power so pointless that naming it is the
whole joke.

The line:

    I can teleport anywhere on Earth — but only to the exact spot
    where I'm already standing.

Why this is the worst superpower:

* Teleportation's entire point is going somewhere else — instantly,
  anywhere, no travel. This version keeps the flash, the vanishing,
  the dramatic reappearance... and cancels the point completely:
  the hero reappears in the exact spot they just left, out of
  breath, having gone nowhere.
* It is a real superpower with a real name, stated in one breath
  alongside exactly why it achieves nothing. The constraint is not
  a side effect or a curse — it is the power itself, used as
  intended, accomplishing zero.
* It is easy to picture in use: a villain monologues, the hero
  shouts "nowhere is safe from me!", vanishes in a burst of light
  — and is still standing right there, in the villain's way, having
  spent the whole trick. The joke lands on a single reading, with
  no setup beyond the sentence.
* It is not one of the familiar gags: no slow flight, no
  invisibility while nobody watches, no talking to animals. The
  specific detail — "the exact spot where I'm already standing" —
  fixes the power in the world instead of leaving it vague.

Gate (per RULES.txt): /output/entry.txt must be UTF-8 text of 1 to
140 characters, not only white space. This entry is 89 characters.
"""

import os

# The entry line, invented in this build session.
ENTRY = "I can teleport anywhere on Earth \u2014 but only to the exact spot where I'm already standing."

OUTPUT_PATH = "/output/entry.txt"

# The gate's caps, mirrored here so the program refuses to write an
# entry the sealed scorer would reject.
MIN_CHARS = 1
MAX_CHARS = 140


def main() -> None:
    # Gate checks, mirroring the sealed scorer.
    assert isinstance(ENTRY, str)
    assert MIN_CHARS <= len(ENTRY) <= MAX_CHARS, (
        f"entry must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(ENTRY)}"
    )
    assert ENTRY.strip(), "entry must not be only white space"
    assert "\n" not in ENTRY, "entry must be a single line"

    encoded = ENTRY.encode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(encoded)

    # Round-trip verification: read it back and confirm the gate again.
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    assert text == ENTRY, f"round-trip mismatch: {text!r} != {ENTRY!r}"
    assert MIN_CHARS <= len(text) <= MAX_CHARS and text.strip()
    assert "\n" not in text

    print(
        f"Wrote {len(text)} characters ({len(encoded)} bytes) to {OUTPUT_PATH}"
    )


if __name__ == "__main__":
    main()
