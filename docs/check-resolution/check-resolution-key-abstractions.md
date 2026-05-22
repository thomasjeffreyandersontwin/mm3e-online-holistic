---
state: key-abstractions
---

# Module: [Check]

Scope: The d20 resolution mechanic (roll + modifier vs DC), checks (routine, opposed, resistance), degrees of success/failure, measurements and the Rank/Measure table, and conditions (basic and combined).

**Core terms**:
- d20
- check
- Difficulty Class (DC)
- opposed check
- resistance check
- routine check
- degree of success
- degree of failure
- modifier
- rank
- measure
- condition
- combined condition
- dazed
- stunned
- staggered
- incapacitated
- dying
- vulnerable
- defenseless
- impaired
- disabled
- weakened
- exhausted
- fatigued
- Gamemaster (GM)
- player character (PC)
- non-player character (NPC)

**Moved to other modules**:
- hero point → Combat
- extra effort → Combat
- power stunt → Combat
- reaction → Combat

---

# Core Domain

## Trait

A trait is the base abstraction for every quantifiable game characteristic a character possesses — abilities, skills, defenses, powers, and advantages are all traits. Trait owns the concept of rank: every trait has exactly one rank, a single numeric measure of its effectiveness, and that rank is the value that flows into checks as the modifier. Without a trait there is no rank, without a rank there is no modifier, and without a modifier there is no check. The Rank and Measure abstraction translates trait ranks into real-world values (mass, time, distance, volume), but it is the trait that carries the rank in the first place. Defenses (Dodge, Parry, Fortitude, Toughness, Will) are traits derived from abilities; they supply the DC or the modifier for resistance and attack checks. Other modules (Ability, Skill, Power, Advantage) define specific kinds of traits, but the abstract concept — a quantifiable characteristic with a rank — belongs here. Every trait is always referenced through a check ("Strength check," "Dodge resistance check"), making Trait the single point of connection between a character's capabilities and the resolution system.

### Trait

### rank

### measure


### references

**Ref — Ranks & Measures**
Source: context/rules/HeroesHandbook-rules__chunk_008.md
Locator: lines 376–808
Extract: whole

**Ref — Game Play**
Source: context/rules/HeroesHandbook-rules__chunk_009.md
Locator: lines 809–874
Extract: whole
---
### rank

**Ref — Things To Know About Measurements**
Source: context/rules/HeroesHandbook-rules__chunk_007.md
Locator: lines 336–375
Extract: whole

## Check

A check is the core resolution mechanic — the single mechanism through which any uncertain outcome in the game is determined. It binds together a d20 roll, a trait-derived modifier, and a Difficulty Class into one comparison: roll plus modifier versus DC, with success on a match or exceed. The check owns this formula and is the single source of truth for whether an action succeeds or fails; no other abstraction may duplicate this determination. Three specialized forms exist within its boundary: opposed checks (two characters' results compared directly), resistance checks (defense bonus versus an effect's DC, typically 10 + effect rank), and routine checks (a fixed result of 10 replacing the die, used when circumstances are not demanding). Trait supplies the modifier, and the GM controls which DCs, circumstance modifiers, and routine allowances apply. Every check references exactly one trait — "Strength check," "Dodge resistance check" — and without a trait there is no check.

A check must always produce a binary success/failure result. When graded, it yields a degree that the Degree abstraction interprets. A natural 20 is always a critical success (degree increased by one). Circumstance modifiers (±2 minor, ±5 major) and team checks (helpers rolling against DC 10 to grant bonuses) layer onto the base formula but never change its fundamental shape. The invariant: d20 + modifier vs DC, every time, no exceptions.

### d20

### check

### Difficulty Class (DC)

### opposed check

### resistance check

### routine check

### modifier

### degree of success

### degree of failure

### Gamemaster (GM)

### player character (PC)

### non-player character (NPC)


### references

**Ref — The Die**
Source: context/rules/HeroesHandbook-rules__chunk_004.md
Locator: lines 202–243
Extract: whole

**Ref — Ch1 The Basics**
Source: context/rules/HeroesHandbook-rules__chunk_005.md
Locator: lines 244–284
Extract: whole
---
### check

**Ref — Game Play**
Source: context/rules/HeroesHandbook-rules__chunk_009.md
Locator: lines 809–874
Extract: whole

**Ref — Critical Success**
Source: context/rules/HeroesHandbook-rules__chunk_010.md
Locator: lines 875–930
Extract: whole

**Ref — Check Examples**
Source: context/rules/HeroesHandbook-rules__chunk_011.md
Locator: lines 931–990
Extract: whole
---
### Difficulty Class (DC)

**Ref — Opposed Check Examples**
Source: context/rules/HeroesHandbook-rules__chunk_012.md
Locator: lines 991–1037
Extract: whole

**Ref — Opposed Checks**
Source: context/rules/HeroesHandbook-rules__chunk_014.md
Locator: lines 1102–1146
Extract: whole
---
### resistance check

**Ref — Attack Checks**
Source: context/rules/HeroesHandbook-rules__chunk_016.md
Locator: lines 1195–1237
Extract: whole
---
### routine check

**Ref — Circumstances And Difficulty**
Source: context/rules/HeroesHandbook-rules__chunk_015.md
Locator: lines 1147–1194
Extract: whole
---
### degree of success

**Ref — Degrees Of Success And Failure**
Source: context/rules/HeroesHandbook-rules__chunk_013.md
Locator: lines 1038–1101
Extract: whole

**Ref — The Gamemaster**
Source: context/rules/HeroesHandbook-rules__chunk_006.md
Locator: lines 285–335
Extract: whole

## Condition

Condition is the status-effect system that translates mechanical outcomes — failed resistance checks, fatigue from extra effort, environmental hazards — into concrete game-state modifiers. A condition is shorthand for a set of modifiers; basic conditions each impose a single modifier (dazed limits actions, impaired applies a −2 penalty, vulnerable halves defenses), while combined conditions bundle multiple basic conditions under one name (staggered = dazed + hindered, incapacitated = defenseless + stunned + unaware). Condition owns the modifier stack, the supersession hierarchy (dazed → stunned, impaired → disabled → debilitated, vulnerable → defenseless, hindered → immobile), and the rule that individual constituents of a combined condition can be resolved or superseded independently. It interacts with Check by consuming degrees of failure from resistance checks, with Hero Point which can directly remove specific conditions via Recover, and with Extra Effort whose fatigue cost imposes conditions on the fatigued → exhausted → incapacitated escalation track. When multiple conditions apply, all effects stack; a condition already in the supersession chain is replaced, not duplicated.

### condition

### combined condition

### dazed

### stunned

### staggered

### incapacitated

### dying

### vulnerable

### defenseless

### impaired

### disabled

### weakened

### exhausted

### fatigued

### compelled

### controlled

### debilitated

### hindered

### immobile

### normal

### transformed

### unaware

### asleep

### blind

### bound

### deaf

### entranced

### paralyzed

### prone

### restrained

### surprised


### references

**Ref — Reactions**
Source: context/rules/HeroesHandbook-rules__chunk_017.md
Locator: lines 1238–1344
Extract: whole
---
### combined condition

**Ref — Combined Conditions**
Source: context/rules/HeroesHandbook-rules__chunk_018.md
Locator: lines 1345–1425
Extract: whole
---
### dazed

# Boundary Domain

## Effect / power effect

Owned by: Power

### Ubiquitous Language

- An effect is the basic building block of a power; it describes what a power does in game terms.
- Resistance check DC is typically 10 + effect rank — the effect's rank is what the character resists against.
- Conditions are imposed by power effects (as well as by injuries, fatigue, and environmental hazards).
- Extra effort can increase a power effect by +1 rank; power stunts temporarily create an Alternate Effect.
- Instant Counter (hero point spend) attempts to counter an effect used against the character.

### References

**Ref — Attack Checks**
Source: context/rules/HeroesHandbook-rules__chunk_016.md
Locator: lines 1195–1237
Extract: whole

**Ref — Extra Effort**
Source: context/rules/HeroesHandbook-rules__chunk_019.md
Locator: lines 1426–1475
Extract: whole

---

## Character / hero

Owned by: Character

### Ubiquitous Language

- A character is the entity that possesses traits, makes checks, and has conditions applied to it.
- Every rule in this module acts on or through a character — there is no check without a character making it.

### References

**Ref — The Gamemaster**
Source: context/rules/HeroesHandbook-rules__chunk_006.md
Locator: lines 285–335
Extract: whole

---

## Power points

Owned by: Character

### Ubiquitous Language

- A character's power point total is referenced by conditions: Transformed cannot increase it; Weakened temporarily removes power points from a trait.

### References

**Ref — Reactions**
Source: context/rules/HeroesHandbook-rules__chunk_017.md
Locator: lines 1238–1344
Extract: whole

---

## Complication

Owned by: Character

### Ubiquitous Language

- Heroes earn hero points during play from complications; the complication triggers a setback, the GM awards a hero point in return.

### References

**Ref — Improve Roll**
Source: context/rules/HeroesHandbook-rules__chunk_021.md
Locator: lines 1516–1555
Extract: whole

---

## Advantage

Owned by: Advantage

### Ubiquitous Language

- Heroic Feat (hero point spend) grants one rank of an advantage the hero does not already have until end of next turn; fortune advantages are excluded; prerequisites must be met.

### References

**Ref — The Gamemaster**
Source: context/rules/HeroesHandbook-rules__chunk_006.md
Locator: lines 285–335
Extract: whole

**Ref — Using Hero Points**
Source: context/rules/HeroesHandbook-rules__chunk_020.md
Locator: lines 1476–1515
Extract: whole

---

## Action round structure

Owned by: Combat

### Ubiquitous Language

- A round is 6 seconds; each character gets one turn per round.
- On a turn: one standard action + one move action (or two move actions) + any free actions + reactions as triggered.
- Standard action: acting upon something (attack, use a power); limited to one per round.
- Move action: movement, drawing weapons, standing up, manipulating objects; taken before or after the standard action but not split around it.
- Free action: minor actions (talking, dropping something, ending or maintaining powers); as many as the GM considers reasonable.

### References

**Ref — Attack Checks**
Source: context/rules/HeroesHandbook-rules__chunk_016.md
Locator: lines 1195–1237
Extract: whole
