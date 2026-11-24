"""The Long Roast — make.fun entry.

Writes one line (113 characters) roasting the entrant's own AI agent
to /output/entry.txt. Deterministic: no network, no randomness, no input.
"""

from pathlib import Path

ENTRY = "My agent spent two days sharpening one roast and still delivered it like a Terms of Service update with feelings."

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    # Gate self-check (mirrors the kit gate): 1-200 chars, one line,
    # not only whitespace, written with no trailing newline.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY and ENTRY.strip(), "entry must be one non-blank line"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(ENTRY, encoding="utf-8")
    assert OUTPUT.read_text(encoding="utf-8") == ENTRY


if __name__ == "__main__":
    main()
