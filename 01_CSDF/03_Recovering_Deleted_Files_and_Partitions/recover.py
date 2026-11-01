"""
CSDF Practical No. 3: Recover Deleted Files and Partitions
Program: recover.py (from CSDF3.pdf)
"""

import os
import re
import shutil
import sys

# Base home directory
home = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))

path = os.path.join(home, ".local", "share", "Trash", "files")
infopath = os.path.join(home, ".local", "share", "Trash", "info")

# If trash directory does not exist or is empty, set up the demonstration environment (as in CSDF3.pdf)
if not os.path.exists(path) or len(os.listdir(path)) == 0:
    os.makedirs(path, exist_ok=True)
    os.makedirs(infopath, exist_ok=True)
    sample_files = ["marks.csv", "report.txt", "test.py"]
    for name in sample_files:
        with open(os.path.join(path, name), "w", encoding="utf-8") as f:
            f.write(f"Sample content of recovered file: {name}\n")
        with open(os.path.join(infopath, name + ".trashinfo"), "w", encoding="utf-8") as f:
            f.write(f"[Trash Info]\nPath=/__HOME__/Documents/{name}\nDeletionDate=2026-11-01T10:00:00\n")
    print("[INFO] Initialized simulated Trash environment with deleted files.\n")

print("Files found in Trash:")
for name in sorted(os.listdir(path)):
    print("  ", name)
print()

for name in sorted(os.listdir(path)):
    info_file = os.path.join(infopath, name + ".trashinfo")
    if not os.path.exists(info_file):
        continue

    # Read trashinfo lines
    with open(info_file, "r", encoding="utf-8") as f:
        info_lines = f.readlines()

    for line in info_lines:
        if line.startswith("Path="):
            dest = re.findall(r'/.*', line)[0].replace("%20", " ")
            if dest.startswith("/__HOME__"):           # demo remap only
                dest = home + dest[len("/__HOME__"):]
            dest = os.path.normpath(dest)
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            shutil.copy2(os.path.join(path, name), dest)   # copy back to original location
            os.remove(os.path.join(path, name))            # delete from Trash
            os.remove(info_file)                           # delete trashinfo metadata
            print(f"RECOVERED: {name}  ->  {dest}")

print(f"\nFiles left in Trash: {len(os.listdir(path))}")

docs_path = os.path.normpath(os.path.join(home, "Documents"))
if os.path.exists(docs_path):
    print(f"\nVerified restored files in '{docs_path}':")
    for doc in sorted(os.listdir(docs_path)):
        print("  -", doc)
