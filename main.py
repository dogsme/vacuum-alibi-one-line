"""The Vacuum's Alibi: one line, 200 characters or fewer.

Writes the robot vacuum's excuse for missing a spot to /output/entry.txt.
"""

from pathlib import Path

LINE = "I skipped that spot on purpose: my lidar filed it under 'haunted', and my warranty does not cover ghosts."

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
