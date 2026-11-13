import os
import json
import argparse
from common import ioi_hash

parser = argparse.ArgumentParser(description="Bruteforce ENUM paths")
parser.add_argument('-o', '--output', type=str, default="bruteforced_enum_paths.txt", help="Output file name. Defaults to bruteforced_enum_paths.txt.")
args = parser.parse_args()

with open(os.path.join("paths", "ENUM.json"), "r") as f:
    enum_data = json.load(f)

found = []
base_paths = set()

for entry in enum_data:
    path = entry.get("path", "")
    if path:
        base_path = path.split(".enumtype")[0]
        base_path = base_path[:base_path.rfind("/") + 1]
        base_paths.add(base_path)

enum_path_end = ".enumtype]."

for entry in enum_data:
    hint = entry.get("hint", "")
    if not hint:
        continue 
    
    for base_path in base_paths:
        path_enumtype = f"{base_path}{hint}{enum_path_end}enumtype"
        
        if ioi_hash(path_enumtype) == entry["hash"]:
            print("FOUND: " + path_enumtype)
            found.append(f"{path_enumtype}")

with open(args.output, "w") as f:
    for item in found:
        f.write(f"{item}\n")
