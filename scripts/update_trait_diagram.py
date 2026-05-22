"""
Incremental update: remove Rank class, update Trait with absorbed methods,
update imported Trait on Check and Boundary Domain pages.
"""
import sys
sys.path.insert(0, r"C:\Users\thoma\.cursor\skills\domain-driven-design\drawio-domain-sync\scripts")

import drawio_tools as dt

DRAWIO = r"c:\dev\mm3e-online-holistic\docs\check-resolution\check-resolution-class-diagram.drawio"

tree, mxfile = dt.load_drawio(DRAWIO)

# ── Trait page ──────────────────────────────────────────────────────────
_, trait_root = dt.get_page(mxfile, "Trait")

# 1. Delete Rank class and all its edges
deleted = dt.delete_class_and_edges(trait_root, "Rank")
print(f"Deleted Rank class and edges: {deleted}")

# 2. Update Trait class — absorb Rank property/methods
trait_cell = dt.find_cell_by_name(trait_root, "Trait")
dt.update_class_cell(
    trait_cell,
    properties=[
        "rank: Integer",
        "<< composition >> difficultyLadder: DifficultyLadder",
        "character: Character",
    ],
    operations=[
        "makeCheck(dc, circumstance): CheckResult",
        "toMeasure(type): Number",
        "addRank(otherRank, type): Integer",
    ],
    invariants=[
        "may be negative",
        "modifier = rank",
        "every trait has a difficultyLadder",
        "ranks must not be added directly \u2014 convert to measures first",
    ],
)
print("Updated Trait class")

# 3. Update RankedMeasurement — rank: Integer
rm_cell = dt.find_cell_by_name(trait_root, "RankedMeasurement")
dt.update_class_cell(
    rm_cell,
    properties=[
        "type: MeasurementType",
        "rank: Integer",
        "value: Number",
        "units: String",
    ],
)
print("Updated RankedMeasurement")

# 4. Add dependency edge Trait → Measurement (Trait.toMeasure/addRank use Measurement.lookup)
trait_id = trait_cell.get("id")
meas_cell = dt.find_cell_by_name(trait_root, "Measurement")
meas_id = meas_cell.get("id")
dt.create_edge(
    trait_root, trait_id, meas_id, "dependency",
    label="uses",
    exit_x=1, exit_y=0.7,
    entry_x=0, entry_y=0.7,
)
print("Added Trait→Measurement dependency edge")

# ── Check page ──────────────────────────────────────────────────────────
_, check_root = dt.get_page(mxfile, "Check")

# Update imported Trait: rank: Integer
check_trait = dt.find_cell_by_name(check_root, "Trait")
if check_trait is not None:
    old_value = check_trait.get("value", "")
    new_value = old_value.replace("rank: Rank", "rank: Integer")
    check_trait.set("value", new_value)
    print("Updated imported Trait on Check page")

# ── Boundary Domain page ────────────────────────────────────────────────
_, bd_root = dt.get_page(mxfile, "Boundary Domain")

bd_trait = dt.find_cell_by_name(bd_root, "Trait")
if bd_trait is not None:
    old_value = bd_trait.get("value", "")
    new_value = old_value.replace("rank: Rank", "rank: Integer")
    bd_trait.set("value", new_value)
    print("Updated imported Trait on Boundary Domain page")

# ── Save ────────────────────────────────────────────────────────────────
dt.save_drawio(DRAWIO, mxfile)
print(f"\nSaved: {DRAWIO}")

# ── Audit ───────────────────────────────────────────────────────────────
print("\n=== AUDIT ===")
print(dt.audit_diagram_report(DRAWIO))
