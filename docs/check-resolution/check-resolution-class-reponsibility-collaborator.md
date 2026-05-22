---
state: crc
---

# Module: [Check]

_CRC model for all Check terms. Concepts: Trait, Measurement, Check, Check Result, Condition. Subtypes: Graded Check Result, Opposed Check, Resistance Check, Routine Check, Team Check. Properties, instances, composites, and boundary terms modeled inline._

Scope: The d20 resolution mechanic (roll + modifier vs DC), checks (routine, opposed, resistance), degrees of success/failure, measurements and the rank-to-measure table, and conditions (basic and combined).

---

All uncertain outcomes are resolved with one mechanic: roll d20, add all appropriate modifiers, compare against a Difficulty Class; meeting or exceeding the DC is success. Each check is tied to exactly one trait. Opposed, resistance, and routine checks are specializations — not different systems. Graded checks produce degrees based on the margin above or below the DC; a natural 20 always increases the degree of success by one.

---

# Core Domain

## **Trait**

### **Trait**
belong to character         | Character
effectiveness rank          | (integer)
                            |   invariant: may be negative; each lower rank halves the measurement value
difficulty ladder           | Difficulty Ladder
                            |   invariant: every trait has a ladder — trait-specific or the default
makes check                 | Check
                            |   invariant: modifier = rank
translate rank to measure   | Measurement, Measurement Type
                            |   invariant: each rank increase approximately doubles the measurement value
add ranks                   | Measurement, Measurement Type
                            |   invariant: ranks must not be added directly — convert to measures first


### **Measurement Type**   | [ throwing distance, travel distance, travel time, lifting ]

### **Ranked Measurements**
type                        | Measurement Type
units                       | mass, distance, volume, time
rank measured               | (integer)
value                       | Number

### **Measurement**
ranked measurements         | Ranked Measurement
                            |   invariant: one real-world value for every rank for this measurement type
calculate                   | Measurement Type
                            |   invariant: look up value for operator rank and scale rank from the type's table
                            |   invariant: each rank step approximately doubles the real-world value
---

## **Check**

### **Check**
use trait            | Trait
use difficulty class | (integer), Difficulty Stage
apply circumstance   | Circumstance Modifier
is routine           | (boolean — GM-decided; when true d20 is fixed at 10; character may still roll if routine total fails)
resolve             | D20, Trait, Circumstance Modifier, Check Result
                                | invariant: d20 + trait rank + circumstance modifier >= dc

### **Opposed Check**
use opposing trait   | Trait
resolve             | D20, Trait, Circumstance Modifier, Check Result
                                | invariant: both characters resolve as standard Checks; higher result wins
                                | invariant: tie → higher bonus wins; bonus tie → d20 (1–10 vs 11–20)
                                | invariant: passive opposition DC = opposing modifier + 10
                                | invariant: rank vs rank — no d20 roll; higher rank wins directly

### **Team Check**
use helper traits     | Trait
resolve              | D20, Trait, Circumstance Modifier, Check Result
                                 | invariant: leader resolves as a standard Check
resolve helper       | D20, Trait, Check Result
                                 | invariant: each helper rolls same Trait vs DC 10
apply helper outcome | Circumstance Modifier
                                 | invariant: 1 success → +2; 3+ successes → +5; cap +5
                                 | invariant: 2+ failures → −2; cap −2


### **D20**
roll                | Check
                                | invariant: result in [1, 20]

### **Difficulty Ladder**
stages               | Difficulty Stage
link to trait        | Trait
                                | invariant: every trait has a ladder — trait-specific or default (Very Easy DC 0 to Nigh-impossible DC 40)
supply dc to check  | Difficulty Stage, Check

### **Difficulty Stage**
descriptor           | (stage name e.g. Challenging, Formidable)
dc value             | (integer)
task description     | Trait
supply dc           | Check

---

#### Decisions made

##### **Check**
- *Check* alone owns *success/failure* for uncertain outcomes; nothing else reimplements *roll total* versus *difficulty class*.
- *Check result* is a concept, not a property of *Check* — it carries its own responsibilities (success/failure, margin, grading, degree mapping to conditions).
- *Degree of success* and *degree of failure* are properties of a *graded check result*, not standalone concepts.

##### **Resistance Check**
- A *Resistance Check* always produces a *graded check result* — simple pass/fail is insufficient because conditions are imposed per degree of failure.
- Its DC is always derived from the resisted *Power Effect's* effectiveness rank + 10; a difficulty ladder or GM-set DC is never applicable.
- *Comparison check* (rank vs rank, no roll) stays a special case inside *opposed check*, not a second engine.
- *d20* is the instrument a *check* rolls — a property, not a separate concept.
- *Modifier* is a value slot on a *check* (primary from *trait rank*, plus stacked *circumstance modifiers*) — a property, not a concept.
- *Gamemaster*, *player character*, *non-player character* are user/actor roles, not domain objects in this module.

##### **Difficulty Ladder**
-  is a concept, not a property of *Trait* or *DC* — it owns its own structure (a ranked set of *difficulty stages*) and its own responsibility (providing calibrated named DCs for a specific trait).
- The general Difficulty Classes ladder (DC 0–40) is the default instance; trait-specific ladders share the same stage structure but supply different task descriptions.

##### **Difficulty Stage** 
- is a concept within a *Difficulty Ladder* — each stage carries its own descriptor, DC, and task description; it is not a generic "row" or "entry."

---

### References

### **check**
**Ref: Ch1 The Basics**
Source: context/rules/HeroesHandbook-rules__chunk_005.md
Locator: lines 244–284
Extract: whole

**Ref: Game Play**
Source: context/rules/HeroesHandbook-rules__chunk_009.md
Locator: lines 809–874
Extract: whole

**Ref: The Die**
Source: context/rules/HeroesHandbook-rules__chunk_004.md
Locator: lines 202–243
Extract: whole

**Ref: Check Examples**
Source: context/rules/HeroesHandbook-rules__chunk_011.md
Locator: lines 931–990
Extract: whole

**Ref: Circumstances And Difficulty**
Source: context/rules/HeroesHandbook-rules__chunk_015.md
Locator: lines 1147–1194
Extract: whole

**Ref: The Gamemaster**
Source: context/rules/HeroesHandbook-rules__chunk_006.md
Locator: lines 285–335
Extract: whole

### **Check Result**
**Ref: Degrees Of Success And Failure**
Source: context/rules/HeroesHandbook-rules__chunk_013.md
Locator: lines 1038–1101
Extract: whole

**Ref: Critical Success**
Source: context/rules/HeroesHandbook-rules__chunk_010.md
Locator: lines 875–930
Extract: whole

### **Difficulty Ladder / Difficulty Stage**
**Ref: Difficulty Classes**
Source: context/rules/HeroesHandbook-rules__chunk_010.md
Locator: lines 875–930
Extract: Difficulty Classes ladder (Very Easy DC 0 through Nigh-impossible DC 40 with example tasks)

**Ref: Assigning Difficulties**
Source: context/rules/HeroesHandbook-rules__chunk_217.md
Locator: lines 15152–15227
Extract: Difficulty Class Examples table with same stage descriptors and DC values from GM chapter

### **modifier**
**Ref: Circumstances And Difficulty**
Source: context/rules/HeroesHandbook-rules__chunk_015.md
Locator: lines 1147–1194
Extract: whole

### **opposed check**
**Ref: Opposed Check Examples**
Source: context/rules/HeroesHandbook-rules__chunk_012.md
Locator: lines 991–1037
Extract: whole

**Ref: Opposed Checks**
Source: context/rules/HeroesHandbook-rules__chunk_014.md
Locator: lines 1102–1146
Extract: whole

### **resistance check**
**Ref: Attack Checks**
Source: context/rules/HeroesHandbook-rules__chunk_016.md
Locator: lines 1195–1237
Extract: whole

### **is routine (property on Check)**
**Ref: Check Examples**
Source: context/rules/HeroesHandbook-rules__chunk_011.md
Locator: lines 931–990
Extract: whole

### **Team Check**
**Ref: Circumstances And Difficulty**
Source: context/rules/HeroesHandbook-rules__chunk_015.md
Locator: lines 1147–1194
Extract: whole

---

## **Condition**

### **Game Modifier**
penalty value              | Number
restriction description    | String

### **Condition**
label                      | (name of the condition, e.g. *dazed*, *stunned*)
game modifier              | Game Modifier
supersedes                 | Condition
superseded by              | Condition

### **Imposed Condition**
imposing source            | Condition Source
condition type             | Condition
active status              | (active or inactive)
suppressing condition      | Imposed Condition
                           |   invariant: set when parked inactive by a different-source more-severe condition

### **Imposed Conditions**
applied conditions         | Imposed Condition
apply new condition        | Condition Source, Condition, Imposed Condition
                           |   invariant: same-source more-severe — remove lesser imposed condition
                           |   invariant: same-source less-severe — do nothing
                           |   invariant: different-source more-severe — park lesser as inactive, set suppressing condition

### **Condition Source**
Effect                     | Power Effect
Other                      | String
                           |  invariant :source be either a power effect or any named string to identify some kind of event 
                           |  or condition


### **Ongoing Effects**
active effects             | Power Effect
add                        | Power Effect
resist                     | Power Effect, Check
                           |   invariant: resistance check made at end of each of the character's turns while effect is active
end effect                 | Power Effect, Imposed Conditions
                           |   invariant: clears only the conditions that this effect imposed
---
#### Decisions made

##### **Condition**
- Each named *condition* (*dazed*, *stunned*, *impaired*, etc.) is an **instance** of *Condition*, not a subtype — they differ by data (which modifiers, which restrictions) but share the same lifecycle: applied, stacked, superseded, resolved.
- *Combined conditions* are **composites** — each names a bundle of *basic condition* instances, not a separate concept with its own behavior.
- *Condition* is imposed as a *result* of a *check* (typically via *degrees of failure* on a *resistance check*); the chain from check to condition is a cross-concept relationship, not duplicated resolution logic.
- Each *Condition* instance owns *supersedes* and *superseded_by* as properties — the *supersession chain* is navigable through condition data itself, not via a separate runtime object.

##### **Condition Source**
- *Condition Source* is a **value** on each *Imposed Condition* instance, not on *Condition* itself and not a separate runtime object — it is the identity token (name, reference, or descriptor) of whatever caused *that particular imposition* to be applied. A single *Condition* type (e.g. *dazed*) can be imposed by different sources simultaneously; the source belongs to the imposition record, not to the condition definition.

---

### References

### **Condition**
**Ref: Reactions**
Source: context/rules/HeroesHandbook-rules__chunk_017.md
Locator: lines 1238–1344
Extract: whole

**Ref: Combined Conditions**
Source: context/rules/HeroesHandbook-rules__chunk_018.md
Locator: lines 1345–1425
Extract: whole

### **Condition Source**
**Ref: Combined Conditions**
Source: context/rules/HeroesHandbook-rules__chunk_018.md
Locator: lines 1345–1425
Extract: whole

---

# Boundary Domain

### **Power Effect** *(is a type of Trait)*
resistance trait           | Trait
ongoing Targets            |  Character,
make resistance            |
check for ongoing targets  | Character, Check
condition on failure       | Condition, Degree of Failure
                           |   invariant: which conditions are imposed is defined by the effect type — owned by Power module
end                        | Imposed Conditions
                           |   invariant: on end — all conditions imposed by this effect, active or inactive, are removed


### **Character**
traits                     | Trait
imposed conditions         | Imposed Conditions
ongoing effects            | Ongoing Effects

---

#### Decisions made

- The "ongoing" quality is a property of an effect, not a separate concept. Whether an effect requires repeated resistance checks is determined by the Power module (the effect's definition), not by this module.
- This module is responsible only for the check-resolution behavior when an ongoing effect is in play: what happens on success (ends + conditions cleared) and failure (persists + conditions remain).
- **Out of scope (Power module):** How a power effect selects which conditions to impose — the mapping from effect type and degree of failure to specific conditions — is not modeled here. This module only knows that `condition on failure` is triggered; the Power module owns the condition-selection rules.
- A resistance check is not a distinct subtype — it is a plain *Check* where the *Power Effect* supplies the DC (effect rank + 10) and the target uses their defense *trait*. No separate concept is needed; the combat context that determines who makes it belongs to the Combat module.

### References

**Ref: Resistance and Ongoing Effects**
Source: context/rules/HeroesHandbook-rules__chunk_209.md
Locator: lines 14791–14830
Extract: whole

**Ref: Attack Checks**
Source: context/rules/HeroesHandbook-rules__chunk_016.md
Locator: lines 1195–1237
Extract: whole

**Ref: The Gamemaster**
Source: context/rules/HeroesHandbook-rules__chunk_006.md
Locator: lines 285–335
Extract: whole

**Ref: Reactions**
Source: context/rules/HeroesHandbook-rules__chunk_017.md
Locator: lines 1238–1344
Extract: whole
