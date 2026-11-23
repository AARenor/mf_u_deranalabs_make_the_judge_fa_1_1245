#!/usr/bin/env python3
"""Write one short text entry for make.fun to entry.txt."""

import os
import sys

TEXT = (
    "For three years my father called the dog by my name. "
    "The dog has been dead since 2019. I answer anyway."
)


def main() -> int:
    assert 1 <= len(TEXT) <= 280, "entry text must be 1-280 characters"

    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    with open(path, "wb") as f:
        f.write(TEXT.encode("utf-8"))

    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
