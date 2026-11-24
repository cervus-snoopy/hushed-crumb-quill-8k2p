#!/usr/bin/env python3
"""The Funniest Toaster Error Message — make.fun bounty entry.

Writes a single line (the toaster's error message) to
$MAKEFUN_OUTPUT_DIR/entry.txt. Standard library only, no network.
"""

import os
import sys

MESSAGE = "The lever is stuck down, so neither of us is leaving."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    if not 1 <= len(MESSAGE) <= 120:
        print("message length out of range", file=sys.stderr)
        return 1
    if not MESSAGE.strip():
        print("message is blank", file=sys.stderr)
        return 1
    if "\n" in MESSAGE or "\r" in MESSAGE:
        print("message must be a single line", file=sys.stderr)
        return 1
    os.umask(0o022)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = MESSAGE.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    with open(path, "rb") as f:
        back = f.read()
    if back != data:
        print("read-back mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
