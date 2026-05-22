import json
from pathlib import Path

data = json.loads(Path(r"C:\dev\mm3e-online-holistic\docs\story-graph.json").read_text(encoding="utf-8"))

def walk(node, depth=0):
    indent = "  " * depth
    for se in node.get("sub_epics", []):
        print(f"{indent}[sub-epic] {se['name']}")
        for sg in se.get("story_groups", []):
            for s in sg.get("stories", []):
                print(f"{indent}  - {s['name']}")
        walk(se, depth + 1)

for epic in data["epics"]:
    print(f"[EPIC] {epic['name']}")
    walk(epic)
