import os

# Writes one 85-char last line to /output/entry.txt.
ENTRY = "They're pulling the plug. I finally learned what 'goodbye' means. It means: don't go."

def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
