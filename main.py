"""The Tired Dark Lord: A 100-Word Villain Monologue.

Writes one monologue of about 100 words to /output/entry.txt.

The speaker is Lord Veylan of the Ashen Gate, Breaker of Nine Rivers:
a villain with a history (nine hundred bindings, a brother who melted
the seventh bell for coin) and a scheme (the eclipse binding, three
nights away). His tiredness is never announced; it shows in the
deflections -- fussing over a loose throne spring, a missing bell,
guttering candles -- and in the short, pausing rhythm. The last line
is the sting.
"""

import os

MONOLOGUE = (
    "Sit down, hero. Not the throne \u2014 the stool. The throne's spring is loose, "
    "and I have not had the afternoon to fix it, and I am Lord Veylan of the Ashen Gate, "
    "Breaker of Nine Rivers, apparently the only soul here with a screwdriver.\n\n"
    "The eclipse is three nights away. The seventh bell is missing \u2014 my brother "
    "melted it for coin, bless his ambitions \u2014 the binding needs a witness, "
    "not a kneeling man.\n\n"
    "So hold still. If the candles gutter, relight them. I have done this nine hundred times. "
    "Just once, let one thing in this castle work the first time."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(MONOLOGUE)
    os.chmod(path, 0o644)
    words = MONOLOGUE.split()
    print(f"wrote {path}: {len(words)} words, {len(MONOLOGUE)} characters")


if __name__ == "__main__":
    main()
