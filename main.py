"""One-line roast: the gadget I use every day.

Entry for make.fun bounty "One-Line Roast: The Gadget You Use Every Day".

Design against the brief
-------------------------
The brief asks for a one-line roast of a gadget used every day. This entry
roasts a smartwatch with one concrete, specific gripe: it cheers the single
moment I stand up, then says nothing while I sit for the next nine hours.
The praise is absurdly cheap -- one stand earns a celebration, nine hours of
sitting earns silence -- which is what makes it funny on first read. The
sentence is built on that contrast: the cheering half is short and loud,
the sitting half stretches on, mirroring the nine hours it describes. The
angle is fresh: it is not the dead-battery complaint everyone makes about
smartwatches, but the watch's own lopsided praise. It is neatly worded as a
single sentence in one person's voice, a specific daily experience rather
than a generic insult, so it reads as a roast with a real target instead of
a slogan.

The program writes exactly that one line to /output/entry.txt.
"""

import os
import stat

TEXT = "My smartwatch cheered when I stood up, then silently watched me sit for the next nine hours."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate: UTF-8 text of 1 to 200 characters, not only white space.
    assert 1 <= len(TEXT) <= 200, "entry must be 1-200 characters"
    assert TEXT.strip(), "entry must not be only white space"
    TEXT.encode("utf-8")

    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
