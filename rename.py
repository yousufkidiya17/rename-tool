"""Bulk file renamer"""
from pathlib import Path

def add_prefix(folder, prefix):
    for f in Path(folder).iterdir():
        if f.is_file():
            f.rename(f.with_name(prefix + f.name))
            print(f"renamed: {f.name}")
