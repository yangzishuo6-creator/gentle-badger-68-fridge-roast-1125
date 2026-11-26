# Write one UTF-8 roast and print its character count.
import os
from pathlib import Path


TEXT = "My smart fridge's ice maker is stuck on 'Installing water.'"


def main():
    output = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes((TEXT + "\n").encode("utf-8"))
    print(len(TEXT))


if __name__ == "__main__":
    main()
