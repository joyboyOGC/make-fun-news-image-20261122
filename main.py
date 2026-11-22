#!/usr/bin/env python3
"""Copy the 22 November 2026 news poster to /output/entry.png."""
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "entry.jpg"
OUT = Path("/output") / "entry.png"

def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, OUT)

if __name__ == "__main__":
    main()
