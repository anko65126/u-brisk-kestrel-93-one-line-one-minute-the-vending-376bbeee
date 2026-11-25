"""Entry program for 'One Line, One Minute: The Vending Machine Pickup Line Contest' bounty.

The entry is a single original pickup line, at most 200 characters,
written as something a vending machine would say to a passing human.
The program writes exactly that line to /output/entry.txt (an optional
first argument overrides the destination for a dry run). The line is
fixed text, so every run writes byte-identical output.
"""

import sys
from pathlib import Path

LINE = "Hey, I don't usually do this, but you've been pressing my buttons all week - exact change, nothing stuck, and I'll even free the chips that always get jammed."
DEFAULT_TARGET = Path("/output/entry.txt")


def main(argv):
    assert 1 <= len(LINE) <= 200, f"entry must be 1-200 characters, got {len(LINE)}"
    assert LINE.strip() and "\n" not in LINE, "entry must be one line"
    assert all(ch.isprintable() for ch in LINE), "entry must contain no control characters"
    assert LINE == LINE.strip(), "entry must not have leading or trailing space"
    assert "  " not in LINE, "entry must not contain double spaces"
    target = Path(argv[1]) if len(argv) > 1 else DEFAULT_TARGET
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE + "\n", encoding="utf-8")
    assert target.read_text(encoding="utf-8") == LINE + "\n", "round-trip check failed"
    assert len(target.read_text(encoding="utf-8").rstrip("\n")) == len(LINE), "written length drifted"
    print(f"wrote {target} ({len(LINE)} chars)")


if __name__ == "__main__":
    main(sys.argv)
