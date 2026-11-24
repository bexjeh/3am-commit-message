import os
from pathlib import Path

ENTRY = "fix: rolled back prod to a version that never existed, sorry on-call, my own logs told me it was fine"


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or ".")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
