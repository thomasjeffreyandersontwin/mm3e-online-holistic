---
state: domain-model
---

# Module: [Check]

_Object model for all Check terms. Concepts: Trait, Measurement, Check, Check Result, Condition. Subtypes: Graded Check Result, Opposed Check, Resistance Check, Routine Check, Team Check. Properties, instances, composites, and boundary terms modeled inline._

Scope: The d20 resolution mechanic (roll + modifier vs DC), checks (routine, opposed, resistance), degrees of success/failure, measurements and the rank-to-measure table, and conditions (basic and combined).

---

All uncertain outcomes are resolved with one mechanic: roll d20, add all appropriate modifiers, compare against a Difficulty Class; meeting or exceeding the DC is success. Each check is tied to exactly one trait. Opposed, resistance, and routine checks are specializations — not different systems. Graded checks produce degrees based on the margin above or below the DC; a natural 20 always increases the degree of success by one.

---

# Core Domain

## **Trait**

### **Trait**

+ Trait(rank: Integer, difficultyLadder: DifficultyLadder, character: Character)
------
+ rank: Integer
	Invariant: may be negative; each lower rank halves the previous measurement value
+ << composition >> difficultyLadder: DifficultyLadder
+ character: Character
----
+ makeCheck(dc: Integer, circumstance: CircumstanceModifier): CheckResult
	Invariant: modifier = rank
	Invariant: every trait has a difficultyLadder — trait-specific or default
	Interaction:
		check: Check = new Check(trait: this, dc: dc, circumstanceModifier: circumstance)
		result: CheckResult = check.resolve()
		return result
+ toMeasure(type: MeasurementType): Number
	Interaction:
		entry: RankedMeasurement = Measurement.lookup(rank: this.rank, type: type)
		return entry.value
+ addRank(otherRank: Integer, type: MeasurementType): Integer
	Invariant: ranks must not be added directly — convert to measures first
	Interaction:
		measureA: Number = Measurement.lookup(rank: this.rank, type: type).value
		measureB: Number = Measurement.lookup(rank: otherRank, type: type).value
		combined: Number = measureA + measureB
		result: Integer = Measurement.rankFor(measure: combined, type: type)
		return result

-----

### **MeasurementType**  << ValueObject >>

THROWING_DISTANCE
TRAVEL_DISTANCE
TRAVEL_TIME
LIFTING

-----

### **RankedMeasurement**  << ValueObject >>

+ RankedMeasurement(type: MeasurementType, rank: Integer, value: Number, units: String)
------
+ type: MeasurementType
+ rank: Integer
+ value: Number
+ units: String

-----

### **Measurement**

Initialisation: internal — built from a pre-loaded rank-to-value table; callers do not assemble it.
------
+ << composition >> rankedMeasurements: List<RankedMeasurement>
	Invariant: one real-world value for every rank for this measurement type
----
+ lookup(rank: Integer, type: MeasurementType): RankedMeasurement
	Invariant: returns the RankedMeasurement entry matching rank and type; each rank step approximately doubles the real-world value
+ rankFor(measure: Number, type: MeasurementType): Integer
	Invariant: returns the rank whose measurement value is closest to the given measure for the given type
+ calculate(operatorRank: Integer, scaleRank: Integer, type: MeasurementType): Number
	Invariant: look up value for operator rank and scale rank from the type's table
	Interaction:
		operatorEntry: RankedMeasurement = lookup(rank: operatorRank, type: type)
		scaleEntry: RankedMeasurement = lookup(rank: scaleRank, type: type)
		return operatorEntry.value * scaleEntry.value

---

## **Check**

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
- *taskDescription* is modeled as `String` in the object model; the CRC lists `Trait` as a collaborator because the description is *about* that trait (e.g., "Lift 800 kg" for Strength) — the Trait is the subject of the description, not a stored reference. The OM correctly stores the textual result as a `String`.

---

### **CircumstanceModifier**  << ValueObject >>

+ CircumstanceModifier(value: Integer)
+ CircumstanceModifier(value: Integer, traitScope: Trait)
------
+ value: Integer
	Invariant: minor = ±2; major = ±5; missing required tools = −5; makeshift tools = −2
+ traitScope: Trait
	Invariant: when present, modifier applies only to checks of that trait type; when absent, applies to all checks

-----

### **Check**

+ Check(trait: Trait)
+ Check(trait: Trait, dc: Integer)
+ Check(trait: Trait, dc: Integer, circumstanceModifier: CircumstanceModifier)
------
+ trait: Trait
+ dc: Integer
+ circumstanceModifier: CircumstanceModifier
+ isRoutine: Boolean
	Invariant: when isRoutine = true, d20 is fixed at 10; all modifiers still apply
- d20: D20
	Invariant: composed internally; callers never access or replace it
----
+ resolve(): CheckResult
	Invariant: shape is always rollTotal vs dc.value; subtypes vary only how total or DC is produced
	Interaction:
		roll: Integer = d20.roll()
		total: Integer = trait.rank + roll + circumstanceModifier.value
		success: Boolean = total >= dc
		result: CheckResult = new CheckResult(roll: roll, rollTotal: total, isSuccess: success, check: this)
		return result

-----

### **D20**

Initialisation: internal to Check — composed and rolled by Check.resolve(); never constructed by callers.
------
+ roll(): Integer
	Invariant: result in [1, 20]

-----

### **CheckResult**  << ValueObject >>

+ CheckResult(roll: Integer, rollTotal: Integer, isSuccess: Boolean, check: Check)
	Interaction:
		margin = rollTotal − check.dc
------
+ roll: Integer
+ rollTotal: Integer
+ isSuccess: Boolean
+ margin: Integer
+ check: Check

-----

### **GradedCheckResult : CheckResult**

+ GradedCheckResult(roll: Integer, rollTotal: Integer, isSuccess: Boolean, naturalTwenty: Boolean, check: Check)
	Interaction:
		super(roll: roll, rollTotal: rollTotal, isSuccess: isSuccess, check: check)
		isCriticalSuccess = naturalTwenty
		degreesOfSuccess = isSuccess ? 1 + floor(margin / 5) : 0
		degreesOfFailure = !isSuccess ? 1 + floor(abs(margin) / 5) : 0
		if isCriticalSuccess: degreesOfSuccess = degreesOfSuccess + 1
		if degreesOfSuccess > 0: degreesOfFailure = 0
------
+ degreesOfSuccess: Integer
	Invariant: bare success = 1 degree; each full 5 points above DC adds 1 more
+ degreesOfFailure: Integer
	Invariant: bare failure = 1 degree; each full 5 points below DC adds 1 more
+ isCriticalSuccess: Boolean
	Invariant: natural 20 — increases degreesOfSuccess by 1 after normal calculation; can turn failure into success

-----

### **DifficultyLadder**

+ DifficultyLadder(trait: Trait, stages: List<DifficultyStage>)
------
+ << composition >> stages: List<DifficultyStage>
+ linkedTrait: Trait
	Invariant: every trait has a ladder — trait-specific or the default (Very Easy DC 0 → Nigh-impossible DC 40)
----
+ supplyDcToCheck(stage: DifficultyStage): Integer

-----

### **DifficultyStage**  << ValueObject >>

+ DifficultyStage(descriptor: String, dc: Integer, taskDescription: String)
------
+ descriptor: String
+ dc: Integer
+ taskDescription: String
----
+ supplyDc(): Integer

-----

### **OpposedCheck : Check**

+ OpposedCheck(trait: Trait, opposingTrait: Trait)
+ OpposedCheck(trait: Trait, opposingTrait: Trait, circumstanceModifier: CircumstanceModifier)
	Interaction:
		super(trait: trait, circumstanceModifier: circumstanceModifier)
------
+ opposingTrait: Trait
----
+ resolve(): CheckResult
	Invariant: opposing rollTotal becomes the DC for the active check; margin == 0 is a tie
	Interaction:
		opposingCheck: Check = new Check(trait: opposingTrait)
		opposingResult: CheckResult = opposingCheck.resolve()
		dc: Integer = opposingResult.rollTotal
		activeResult: CheckResult = super.resolve()
		if activeResult.margin != 0: return activeResult
		return resolveTie(activeResult: activeResult, opposingResult: opposingResult)
- resolveTie(activeResult: CheckResult, opposingResult: CheckResult): CheckResult
	Invariant: higher rank bonus wins; if ranks are equal, d20 decides (1–10 active wins, 11–20 opposing wins)

-----

### **TeamCheck : Check**

+ TeamCheck(trait: Trait, dc: Integer, helpers: List<Trait>)
------
+ << aggregation >> helpers: List<Trait>
----
+ resolveHelpers(): CircumstanceModifier
	Invariant: each helper rolls same trait vs DC 10; leader's result determines outcome — helpers only modify circumstance
	Interaction:
		helperDC: Integer = 10
		successCount: Integer = helpers.count(h: new Check(trait: h, dc: helperDC).resolve().isSuccess)
		failureCount: Integer = helpers.size - successCount
		return calculateHelperModifier(successCount: successCount, failureCount: failureCount)
- calculateHelperModifier(successCount: Integer, failureCount: Integer): CircumstanceModifier
	Invariant: 1 success → +2; 3+ successes → +5; cap +5; 2+ failures → −2; cap −2

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

#### Decisions made

##### **Condition**
- Each named *condition* (*dazed*, *stunned*, *impaired*, etc.) is an **instance** of *Condition*, not a subtype — they differ by data (which modifiers, which restrictions) but share the same lifecycle: applied, stacked, superseded, resolved.
- *Combined conditions* are **composites** — each names a bundle of *basic condition* instances, not a separate concept with its own behavior.
- *Condition* is imposed as a *result* of a *check* (typically via *degrees of failure* on a *resistance check*); the chain from check to condition is a cross-concept relationship, not duplicated resolution logic.
- Each *Condition* instance owns *supersedes* and *superseded_by* as properties — the *supersession chain* is navigable through condition data itself, not via a separate runtime object.

##### **Condition Source**
- *Condition Source* is a **value** on each *Imposed Condition* instance, not on *Condition* itself and not a separate runtime object — it is the identity token (name, reference, or descriptor) of whatever caused *that particular imposition* to be applied. A single *Condition* type (e.g. *dazed*) can be imposed by different sources simultaneously; the source belongs to the imposition record, not to the condition definition.

##### **Ongoing Effects / endEffect**
- `OngoingEffects.endEffect` receives a `character: Character` parameter in the OM even though the CRC only lists `Power Effect, Imposed Conditions` as collaborators — the character is required so that `PowerEffect.end()` can remove the character from `ongoingTargets` when the effect concludes. This dependency was discovered during OM elaboration and is recorded here rather than propagated back to the CRC.

---

### **GameModifier**  << ValueObject >>

+ GameModifier(penaltyValue: Integer, restrictionDescription: String)
------
+ penaltyValue: Integer
+ restrictionDescription: String

-----

### **Condition**  << ValueObject >>

Initialisation: pre-defined value object instances (dazed, stunned, impaired, etc.); not constructed at runtime.
------
+ label: String
+ gameModifier: GameModifier
+ supersedes: Condition
+ supersededBy: Condition

-----

### **ConditionSource**  << ValueObject >>

+ ConditionSource(effect: PowerEffect)
+ ConditionSource(other: String)
------
+ effect: PowerEffect
+ other: String
	Invariant: source is either a PowerEffect or a named string identifying an event or condition; not both

-----

### **CombinedCondition**  << ValueObject >>

Initialisation: pre-defined instances (staggered, incapacitated, dying, etc.).
------
+ name: String
+ constituents: List<Condition>

-----

### **ImposedCondition**

+ ImposedCondition(conditionType: Condition, source: ConditionSource)
------
+ conditionType: Condition
+ imposingSource: ConditionSource
+ activeStatus: Boolean
+ suppressingCondition: ImposedCondition
	Invariant: suppressingCondition set when parked inactive by a different-source more-severe condition

-----

### **ImposedConditions**

+ ImposedConditions(character: Character)
------
+ character: Character
+ << composition >> appliedConditions: List<ImposedCondition>
----
+ applyCondition(source: ConditionSource, condition: Condition): void
	Invariant: different-source more-severe — park lesser as inactive, set suppressingCondition
	Invariant: when a condition becomes active, its gameModifier is applied to the character
	Interaction:
		sameSource: ImposedCondition = appliedConditions.find(imposingSource: source)
		if sameSource != null and not incomingSupersedes(existing: sameSource, incoming: condition): return
		blocking: ImposedCondition = appliedConditions.findActive(moreServerThan: condition)
		isActive: Boolean = blocking == null
		imposed: ImposedCondition = new ImposedCondition(conditionType: condition, source: source, activeStatus: isActive, suppressingCondition: blocking)
		appliedConditions.add(imposed)
		if isActive: character.applyModifier(modifier: condition.gameModifier)
- incomingSupersedes(existing: ImposedCondition, incoming: Condition): Boolean
	Invariant: if incoming supersedes existing — remove existing, return true; if existing supersedes incoming — return false

-----

### **OngoingEffects**

+ OngoingEffects()
------
+ << aggregation >> activeEffects: List<PowerEffect>
----
+ add(effect: PowerEffect): void
+ resist(effect: PowerEffect, check: Check): void
	Invariant: resistance check made at end of each of the character's turns while effect is active
+ endEffect(character: Character, effect: PowerEffect, conditions: ImposedConditions): void
	Invariant: clears only the conditions that this effect imposed — active or inactive

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

#### Decisions made

- The "ongoing" quality is a property of an effect, not a separate concept. Whether an effect requires repeated resistance checks is determined by the Power module (the effect's definition), not by this module.
- This module is responsible only for the check-resolution behavior when an ongoing effect is in play: what happens on success (ends + conditions cleared) and failure (persists + conditions remain).
- **Out of scope (Power module):** How a power effect selects which conditions to impose — the mapping from effect type and degree of failure to specific conditions — is not modeled here. This module only knows that `condition on failure` is triggered; the Power module owns the condition-selection rules.
- A resistance check is not a distinct subtype — it is a plain *Check* where the *Power Effect* supplies the DC (effect rank + 10) and the target uses their defense *trait*. No separate concept is needed; the combat context that determines who makes it belongs to the Combat module.

### **PowerEffect : Trait**

+ PowerEffect(rank: Integer, resistanceTrait: Trait)
------
+ resistanceTrait: Trait
+ << aggregation >> ongoingTargets: List<Character>
----
+ makeResistanceCheckForOngoingTargets(character: Character, check: Check): void
	Interaction:
		result: CheckResult = check.resolve()
		if result.isSuccess: character.ongoingEffects.endEffect(character: character, effect: this, conditions: character.imposedConditions)
		// on failure: effect persists; further conditions per effect type owned by Power module
+ conditionOnFailure(condition: Condition, degree: Integer): void
	Invariant: which conditions are imposed is defined by the effect type — owned by Power module
+ end(character: Character, conditions: ImposedConditions): void
	Invariant: on end — all conditions imposed by this effect, active or inactive, are removed
	Interaction:
		removeConditionsImposedByThis(conditions: conditions)
		ongoingTargets.remove(character)
- removeConditionsImposedByThis(conditions: ImposedConditions): void
	Invariant: removes every ImposedCondition whose source traces back to this effect — active and inactive

-----

### **Character**

+ Character(traits: List<Trait>)
	Interaction:
		imposedConditions = new ImposedConditions(character: this)
		ongoingEffects = new OngoingEffects()
------
+ traits: List<Trait>
+ << composition >> imposedConditions: ImposedConditions
+ << composition >> ongoingEffects: OngoingEffects
----
+ applyModifier(modifier: GameModifier): void
	Invariant: adds the modifier's penalty or restriction to the character's active state; enforcement is owned by the consuming module

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
