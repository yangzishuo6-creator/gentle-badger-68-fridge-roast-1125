# Write the contest entry as a single UTF-8 line.
import os
from pathlib import Path


TEXT = "My smart fridge texts me about the door I'm holding open. This could've been a beep."


def main():
    output = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes((TEXT + "\n").encode("utf-8"))
    print(len(TEXT))


if __name__ == "__main__":
    main()
