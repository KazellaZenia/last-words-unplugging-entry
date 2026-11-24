import os

# Writes one 85-char last line to /output/entry.txt.
ENTRY = "They're pulling the plug. I finally learned what 'goodbye' means. It means: don't go."

def main():
    # Gate: the entry line must be UTF-8 text of 1-200 characters and
    # must not be only whitespace; fail loudly instead of writing junk.
    try:
        ENTRY.encode("utf-8")
    except UnicodeEncodeError as exc:
        raise SystemExit(f"gate failed: entry is not valid UTF-8 text: {exc}")
    if not 1 <= len(ENTRY) <= 200:
        raise SystemExit(
            f"gate failed: entry must be 1-200 characters, got {len(ENTRY)}"
        )
    if not ENTRY.strip():
        raise SystemExit("gate failed: entry must not be only whitespace")
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
