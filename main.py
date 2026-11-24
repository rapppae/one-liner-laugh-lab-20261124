"""Write the one-liner laugh lab entry to /output/entry.txt.

One line, 106 characters (limit 200) -- no trailing newline."""

from pathlib import Path

ENTRY = "I didn't eat your sock. I performed an unscheduled deep-clean of your footwear, and frankly, it needed it."

def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")

if __name__ == "__main__":
    main()
