"""
Inject acceptance criteria from acceptance-criteria.md into story-graph.json.
Maps story names from the markdown to stories in the Construct Hero epic.
"""
import json
import re
from pathlib import Path

GRAPH = Path(r"C:\dev\mm3e-online-holistic\docs\story-graph.json")
AC_FILE = Path(r"C:\dev\mm3e-online-holistic\docs\character-construction\acceptance-criteria.md")

# ---------------------------------------------------------------------------
# Parse the markdown into {story_name: [ac_text, ...]}
# ---------------------------------------------------------------------------
def parse_ac_md(path: Path) -> dict[str, list[str]]:
    text = path.read_text(encoding="utf-8")
    result: dict[str, list[str]] = {}
    current_story: str | None = None
    in_ac_section = False
    current_ac_lines: list[str] = []

    def flush_ac():
        if current_story and current_ac_lines:
            ac_text = " ".join(" ".join(current_ac_lines).split())
            result.setdefault(current_story, []).append(ac_text)

    for line in text.splitlines():
        # ## Story: <name>
        m = re.match(r'^## Story:\s+(.+)', line)
        if m:
            flush_ac()
            current_ac_lines = []
            in_ac_section = False
            current_story = m.group(1).strip()
            continue

        # ### Acceptance criteria header
        if re.match(r'^### Acceptance criteria', line, re.IGNORECASE):
            in_ac_section = True
            continue

        # New ## heading (sub-epic or next story) ends AC section
        if re.match(r'^## ', line):
            flush_ac()
            current_ac_lines = []
            in_ac_section = False
            current_story = None
            continue

        if not in_ac_section:
            continue

        stripped = line.strip()
        if not stripped or stripped == "---":
            continue

        # Numbered AC item — flush previous, start new
        m2 = re.match(r'^\d+\.\s+(.+)', stripped)
        if m2:
            flush_ac()
            current_ac_lines = [m2.group(1)]
        elif current_ac_lines:
            # Continuation line (THEN, AND, BUT, Evidence)
            current_ac_lines.append(stripped)

    flush_ac()
    return result


# ---------------------------------------------------------------------------
# Walk story graph and collect {story_name: story_dict} for Construct Hero
# ---------------------------------------------------------------------------
def walk_stories(node: dict, out: dict):
    for se in node.get("sub_epics", []):
        walk_stories(se, out)
        for sg in se.get("story_groups", []):
            for s in sg.get("stories", []):
                out[s["name"]] = s


def build_ac_entry(text: str, order: int) -> dict:
    return {
        "sequential_order": order,
        "description": text,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
data = json.loads(GRAPH.read_text(encoding="utf-8"))

construct_hero_epic = next(
    e for e in data["epics"] if "construct" in e["name"].lower()
)

stories: dict[str, dict] = {}
walk_stories(construct_hero_epic, stories)

print(f"Stories in graph: {list(stories.keys())}\n")

ac_map = parse_ac_md(AC_FILE)
print(f"Stories in AC file: {list(ac_map.keys())}\n")

injected = 0
skipped = 0
for story_name, ac_list in ac_map.items():
    if story_name not in stories:
        print(f"  SKIP (no match): {story_name}")
        skipped += 1
        continue
    story = stories[story_name]
    existing = story.get("acceptance_criteria", [])
    if existing:
        print(f"  SKIP (already has {len(existing)} AC): {story_name}")
        skipped += 1
        continue
    story["acceptance_criteria"] = [
        build_ac_entry(txt, i + 1) for i, txt in enumerate(ac_list)
    ]
    print(f"  OK  ({len(ac_list)} AC): {story_name}")
    injected += 1

print(f"\nInjected: {injected}  Skipped: {skipped}")

GRAPH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"Saved: {GRAPH}")
