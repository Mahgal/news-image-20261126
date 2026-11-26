#!/usr/bin/env python3
"""news-image-20261126 entry (Python 3.13, standard library only).

Copies the bundled image assets/entry.png to $MAKEFUN_OUTPUT_DIR/entry.png
(default /output/entry.png). The image sums up the world news of
Thursday 26 November 2026; draw.py is the build-time generator that made it.
"""
import os
import shutil
from pathlib import Path


def main() -> None:
    here = Path(__file__).resolve().parent
    src = here / "assets" / "entry.png"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, out_dir / "entry.png")


if __name__ == "__main__":
    main()
