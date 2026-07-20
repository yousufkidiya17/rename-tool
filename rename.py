"""Bulk file renamer"""
import sys
from pathlib import Path

def add_prefix(folder, prefix, dry=False):
    for f in Path(folder).iterdir():
        if f.is_file():
            new = f.with_name(prefix + f.name)
            if dry: print(f"[dry] {f.name} -> {new.name}")
            else: f.rename(new); print(f"renamed: {f.name}")

def strip_prefix(folder, prefix, dry=False):
    for f in Path(folder).iterdir():
        if f.is_file() and f.name.startswith(prefix):
            new = f.with_name(f.name[len(prefix):])
            if dry: print(f"[dry] {f.name} -> {new.name}")
            else: f.rename(new); print(f"renamed: {f.name}")

if __name__ == "__main__":
    mode, folder, prefix = sys.argv[1], sys.argv[2], sys.argv[3]
    dry = "--dry" in sys.argv
    {"add": add_prefix, "strip": strip_prefix}[mode](folder, prefix, dry)
