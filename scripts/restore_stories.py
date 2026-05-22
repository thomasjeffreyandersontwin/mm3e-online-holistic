"""
Restore the two stories into the 'Translate Rank to Measure' sub-epic's story_groups.
"""
import sys
import json

GRAPH_PATH = r"C:\dev\mm3e-online-holistic\docs\story-graph.json"

with open(GRAPH_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

target = "Translate Rank to Measure"

stories = [
    {
        "name": "Translate Trait Rank to Real-World Value",
        "sequential_order": 0.0,
        "connector": None,
        "story_type": "System",
        "users": [],
        "test_class": None,
        "scenarios": [],
        "acceptance_criteria": [],
        "behavior": None
    },
    {
        "name": "Derive Measurement from Rank Formula",
        "sequential_order": 1.0,
        "connector": None,
        "story_type": "System",
        "users": [],
        "test_class": None,
        "scenarios": [],
        "acceptance_criteria": [],
        "behavior": None
    }
]

story_group = {
    "name": "",
    "sequential_order": 0.0,
    "type": "and",
    "connector": None,
    "behavior": None,
    "stories": stories
}

for epic in data.get("epics", []):
    if epic["name"] == target:
        for sub in epic.get("sub_epics", []):
            if sub["name"] == target:
                sub["story_groups"] = [story_group]
                print(f"Restored {len(stories)} stories into sub-epic '{target}'")
                break
        break

with open(GRAPH_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print(f"Written to {GRAPH_PATH}")
