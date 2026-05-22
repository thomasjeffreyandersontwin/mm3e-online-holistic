"""
Move stories from 'Translate Rank to Measure' epic's story_groups
into a new sub-epic of the same name, then save via story_graph_cli write.
"""
import sys
import json
import copy

SCRIPT_DIR = r"C:\dev\agilebydesign-skills\skills\story-driven-delivery\story-graph-ops\scripts"
sys.path.insert(0, SCRIPT_DIR)

from story_map import StoryMap

GRAPH_PATH = r"C:\dev\mm3e-online-holistic\docs\story-graph.json"

with open(GRAPH_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

target_epic_name = "Translate Rank to Measure"

for epic in data.get("epics", []):
    if epic["name"] == target_epic_name:
        # Grab the existing story_groups (with the two stories)
        existing_story_groups = copy.deepcopy(epic.get("story_groups", []))

        # Build the new sub-epic
        new_sub_epic = {
            "name": target_epic_name,
            "sequential_order": 0.0,
            "behavior": None,
            "domain_concepts": [],
            "story_groups": existing_story_groups
        }

        # Move: sub_epics gets the new sub-epic, story_groups emptied on parent
        epic["sub_epics"] = [new_sub_epic]
        epic["story_groups"] = []

        print(f"Done: moved {sum(len(sg.get('stories', [])) for sg in existing_story_groups)} stories into sub-epic '{target_epic_name}'")
        break
else:
    print(f"ERROR: epic '{target_epic_name}' not found", file=sys.stderr)
    sys.exit(1)

out_path = r"C:\dev\mm3e-online-holistic\docs\story-graph.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print(f"Written to {out_path}")
