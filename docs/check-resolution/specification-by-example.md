# Specification by Example: Check

_Grounded in the Check object model. Domain concepts follow exact names from the model:
**Trait**, **Rank**, **Check**, **D20**, **CheckResult**, **GradedCheckResult**, **DifficultyClass**,
**CircumstanceModifier**, **OpposedCheck**, **TeamCheck**, **DifficultyLadder**, **DifficultyStage**,
**Condition**, **ImposedCondition**, **ImposedConditions**, **ConditionSource**, **CombinedCondition**,
**PowerEffect**, **Character**, **OngoingEffects**._

---

## Make A Check

---

### Make Trait Check

Scenario: Strength check meets Difficulty Class exactly and succeeds
  Given **Character** *Steel* has **Trait** *Strength* with **Rank** *+10*
  And the **GM** sets a **Difficulty Class** of *15*
  When *Steel* makes a **Check** on **Trait** *Strength* and rolls *5* on the **D20**
  Then the **Check** produces a **Check Result** with **Roll Total** *15* (5 + 10)
  And the **Check Result** is *success* — roll total meets the **Difficulty Class**
  And the **Check Result** has **Margin** *0*

Scenario: Strength check falls below Difficulty Class and fails
  Given **Character** *Steel* has **Trait** *Strength* with **Rank** *+10*
  And the **GM** sets a **Difficulty Class** of *20*
  When *Steel* makes a **Check** on **Trait** *Strength* and rolls *8* on the **D20**
  Then the **Check** produces a **Check Result** with **Roll Total** *18* (8 + 10)
  And the **Check Result** is *failure* — roll total falls below the **Difficulty Class**
  And the **Check Result** has **Margin** *−2*

Scenario: Minor Circumstance Modifier is added to the roll total, not to the Difficulty Class
  Given **Character** *Steel* has **Trait** *Strength* with **Rank** *+10*
  And the **GM** sets a **Difficulty Class** of *17*
  And a minor **Circumstance Modifier** of *+2* applies (favourable working conditions)
  When *Steel* makes a **Check** on **Trait** *Strength* and rolls *5* on the **D20**
  Then the **Check** produces a **Check Result** with **Roll Total** *17* (5 + 10 + 2)
  And the **Check Result** is *success* (17 ≥ 17)

Scenario: Missing required tools impose a −5 Circumstance Modifier on the check
  Given **Character** *Steel* has **Trait** *Technology* with **Rank** *+4*
  And the **GM** sets a **Difficulty Class** of *15*
  And a **Circumstance Modifier** of *−5* applies for missing required tools
  When *Steel* makes a **Check** on **Trait** *Technology* and rolls *10* on the **D20**
  Then the **Check** produces a **Check Result** with **Roll Total** *9* (10 + 4 − 5)
  And the **Check Result** is *failure*

Scenario: Scoped Circumstance Modifier applies only to the named Trait and not to others
  Given **Character** *Steel* has **Trait** *Athletics* with **Rank** *+6*
  And **Character** *Steel* also has **Trait** *Technology* with **Rank** *+4*
  And a **Circumstance Modifier** of *+2* is scoped to **Trait** *Athletics*
  When *Steel* makes a **Check** on **Trait** *Athletics* and rolls *8* on the **D20**
  Then the scoped **Circumstance Modifier** *+2* is included in **Roll Total** *16* (8 + 6 + 2)
  When *Steel* makes a **Check** on **Trait** *Technology* and rolls *8* on the **D20**
  Then the scoped **Circumstance Modifier** is excluded and the **Roll Total** is *12* (8 + 4)

Scenario: GM selects a Difficulty Stage from the Difficulty Ladder to set the Difficulty Class
  Given **Character** *Volt* has **Trait** *Acrobatics* with **Rank** *+8*
  And the **Difficulty Ladder** for **Trait** *Acrobatics* contains **Difficulty Stage** *Challenging* with **Difficulty Class** *15*
  When the **GM** selects **Difficulty Stage** *Challenging* from the **Difficulty Ladder**
  Then the **Difficulty Stage** supplies **Difficulty Class** *15* to the **Check**
  When *Volt* makes a **Check** on **Trait** *Acrobatics* and rolls *7* on the **D20**
  Then the **Check** produces a **Check Result** with **Roll Total** *15* and is *success*

---

### Make Opposed Check Against Opponent

Scenario: Higher roll total wins the Opposed Check
  Given **Character** *Steel* has **Trait** *Strength* with **Rank** *+10*
  And **Character** *The Crusher* has **Trait** *Strength* with **Rank** *+12*
  When *Steel* makes an **Opposed Check** on **Trait** *Strength* and rolls *14* on the **D20** (total *24*)
  And *The Crusher* rolls *8* on the **D20** for the opposing **Check** (total *20*)
  Then *Steel* wins the **Opposed Check** — **Roll Total** *24* exceeds *The Crusher's* **Roll Total** *20*

Scenario: Tied roll totals are broken by the higher Rank bonus
  Given **Character** *Steel* has **Trait** *Strength* with **Rank** *+10*
  And **Character** *The Crusher* has **Trait** *Strength* with **Rank** *+12*
  When *Steel* rolls *10* (total *20*) and *The Crusher* rolls *8* (total *20*) on the **D20** — tied totals
  Then the **Opposed Check** breaks the tie by **Rank** bonus
  And *The Crusher* wins the tie — **Rank** *+12* > **Rank** *+10*

Scenario: Tied roll totals with equal bonuses are resolved by a tiebreaker D20
  Given **Character** *Steel* has **Trait** *Strength* with **Rank** *+10*
  And **Character** *Volt* has **Trait** *Strength* with **Rank** *+10*
  When *Steel* rolls *10* (total *20*) and *Volt* rolls *10* (total *20*) — tied totals and equal bonuses
  Then the **Opposed Check** resolves by rolling a tiebreaker **D20**
  And if the tiebreaker falls *1–10*, *Steel* wins
  And if the tiebreaker falls *11–20*, *Volt* wins

Scenario: Passive opposition sets Difficulty Class as opposing modifier plus 10
  Given **Character** *The Crusher* has **Trait** *Strength* with **Rank** *+12*
  And *The Crusher* is not actively contesting the **Opposed Check**
  When *Steel* makes an **Opposed Check** against *The Crusher's* passive opposition
  Then the **Difficulty Class** for *Steel's* **Check** is *22* (**Rank** *+12* + 10)
  And *Steel's* **Check** resolves as a standard **Check** against **Difficulty Class** *22*

---

### Resolve Comparison Check Without Roll

Scenario: Character with higher Rank wins a Comparison Check without a D20 roll
  Given **Character** *Steel* has **Trait** *Strength* with **Rank** *+10*
  And **Character** *The Crusher* has **Trait** *Strength* with **Rank** *+12*
  When a *Comparison Check* is made between *Steel* and *The Crusher* on **Trait** *Strength*
  Then no **D20** is rolled
  And *The Crusher* wins — **Rank** *+12* is higher than **Rank** *+10*

---

### Make Resistance Check Against Effect

Scenario: Character meets the resistance Difficulty Class and resists the Power Effect
  Given **Character** *Steel* has **Trait** *Toughness* with **Rank** *+10*
  And **Power Effect** *Blast* has **Rank** *8*, making the **Difficulty Class** *18* (8 + 10)
  When *Steel* makes a **Resistance Check** on **Trait** *Toughness* against **Difficulty Class** *18* and rolls *10* on the **D20**
  Then the **Graded Check Result** has **Roll Total** *20* (10 + 10) and **Margin** *+2*
  And the **Graded Check Result** is *success* with **Degrees of Success** *1*
  And no conditions from *Blast* are imposed on *Steel*

Scenario: Character fails the resistance check and conditions are imposed per degree of failure
  Given **Character** *Steel* has **Trait** *Toughness* with **Rank** *+10*
  And **Power Effect** *Blast* has **Rank** *8*, making the **Difficulty Class** *18* (8 + 10)
  When *Steel* makes a **Resistance Check** on **Trait** *Toughness* against **Difficulty Class** *18* and rolls *3* on the **D20**
  Then the **Graded Check Result** has **Roll Total** *13* (3 + 10) and **Margin** *−5*
  And the **Graded Check Result** is *failure* with **Degrees of Failure** *2*
  And *Blast* imposes conditions on *Steel* corresponding to *2 degrees of failure*

---

### Perform Routine Check

Scenario: Routine check succeeds when the fixed total of 10 plus modifier meets the Difficulty Class
  Given **Character** *Steel* has **Trait** *Strength* with **Rank** *+10*
  And the **GM** permits a *routine* **Check** against **Difficulty Class** *20*
  When *Steel* performs a *routine* **Check** on **Trait** *Strength* (isRoutine = true, **D20** fixed at *10*)
  Then the **Check** produces a **Check Result** with **Roll Total** *20* (10 + 10) without any **D20** roll
  And the **Check Result** is *success* (20 ≥ 20)

Scenario: Routine check total is insufficient and the character may still roll
  Given **Character** *Volt* has **Trait** *Athletics* with **Rank** *+4*
  And the **GM** permits a *routine* **Check** against **Difficulty Class** *18*
  When *Volt* attempts a *routine* **Check** on **Trait** *Athletics* (fixed total *14*, which is 10 + 4)
  Then the *routine* **Check Result** has **Roll Total** *14*, falling below **Difficulty Class** *18*
  And *Volt* may still roll the **D20** — the task is not *routine* for that **Character**

---

## Apply Conditions

---

### Apply Condition to Character

Scenario: New condition is applied as active with its Condition Source recorded
  Given **Character** *Steel* has an empty **Imposed Conditions** collection
  And **Power Effect** *Daze* (rank *6*) serves as the **Condition Source**
  When **Imposed Conditions** applies the *dazed* **Condition** from **Condition Source** *Daze*
  Then *Steel's* **Imposed Conditions** contains one **Imposed Condition** with **Condition Type** *dazed*
  And that **Imposed Condition** has **Active Status** *active* and **Imposing Source** *Daze*
  And *Steel* is limited to *free actions* and one *standard action* per turn

Scenario: Different-source condition more severe than active lesser parks the lesser as inactive
  Given **Character** *Steel* has an *active* **Imposed Condition** *dazed* from **Condition Source** *Daze*
  And a different **Power Effect** *Mind Blast* supplies a second **Condition Source**
  When **Imposed Conditions** applies the *stunned* **Condition** from **Condition Source** *Mind Blast*
  Then *Steel's* **Imposed Conditions** contains *stunned* with **Active Status** *active*
  And *dazed* remains in **Imposed Conditions** with **Active Status** *inactive*
  And the *dazed* **Imposed Condition** has **Suppressing Condition** pointing to the *stunned* **Imposed Condition**
  And only *stunned* game modifier applies — *Steel* cannot take any actions including free actions

---

### Supersede Condition in Chain

Scenario: Same-source more severe condition removes the lesser and becomes active
  Given **Character** *Steel* has an *active* **Imposed Condition** *dazed* from **Condition Source** *Daze*
  When **Imposed Conditions** applies the *stunned* **Condition** from the same **Condition Source** *Daze*
  Then the *dazed* **Imposed Condition** is *removed* from *Steel's* **Imposed Conditions**
  And the *stunned* **Imposed Condition** is *active* with **Imposing Source** *Daze*
  And *Steel* cannot take any actions including free actions (*stunned* game modifier)

Scenario: Same-source less severe condition is ignored when a more severe one is already active
  Given **Character** *Steel* has an *active* **Imposed Condition** *stunned* from **Condition Source** *Daze*
  When **Imposed Conditions** attempts to apply the *dazed* **Condition** from the same **Condition Source** *Daze*
  Then *Steel's* **Imposed Conditions** remain unchanged — *dazed* does not supersede *stunned*
  And *Steel* remains *stunned*

Scenario: Inactive lesser condition becomes active when its suppressor is removed
  Given **Character** *Steel* has an *active* **Imposed Condition** *stunned* from **Condition Source** *Mind Blast*
  And an *inactive* **Imposed Condition** *dazed* from **Condition Source** *Daze* with **Suppressing Condition** pointing to *stunned*
  When the *stunned* **Imposed Condition** from *Mind Blast* is removed
  Then the *dazed* **Imposed Condition** from *Daze* becomes *active*
  And *Steel* is now *dazed* — limited to free actions and one standard action per turn

---

## Recover from Conditions

---

### Roll Resistance Check Against Ongoing Effect to Remove Conditions

Scenario: Successful resistance check ends the ongoing effect and clears all its conditions
  Given **Character** *Steel* has **Ongoing Effect** *Daze* (rank *6*) active in his **Ongoing Effects**
  And *Steel* has an *active* **Imposed Condition** *dazed* with **Imposing Source** *Daze*
  And **Trait** *Will* with **Rank** *+6* is *Steel's* resistance trait for this effect
  When at the end of *Steel's* turn *Steel* makes a **Resistance Check** on **Trait** *Will* vs **Difficulty Class** *16* (6 + 10) and rolls *10* on the **D20**
  Then the **Check Result** has **Roll Total** *16* (10 + 6) and is *success* (16 ≥ 16)
  And **Ongoing Effects** removes *Daze* from *Steel's* active effects
  And **Imposed Conditions** removes all **Imposed Conditions** whose **Imposing Source** is *Daze*
  And *Steel* is no longer *dazed*

Scenario: Failed resistance check leaves the ongoing effect and conditions unchanged
  Given **Character** *Steel* has **Ongoing Effect** *Daze* (rank *6*) active in his **Ongoing Effects**
  And *Steel* has an *active* **Imposed Condition** *dazed* with **Imposing Source** *Daze*
  And **Trait** *Will* with **Rank** *+6* is *Steel's* resistance trait for this effect
  When at the end of *Steel's* turn *Steel* makes a **Resistance Check** on **Trait** *Will* vs **Difficulty Class** *16* and rolls *5* on the **D20**
  Then the **Check Result** has **Roll Total** *11* (5 + 6) and is *failure* (11 < 16)
  And *Daze* remains in *Steel's* **Ongoing Effects**
  And the *dazed* **Imposed Condition** remains *active*

---

### Remove Condition When Source Effect Ends

Scenario: All conditions imposed by an effect are removed — active and inactive — when the effect ends
  Given **Character** *Steel* has the **Combined Condition** *staggered* (*dazed* + *hindered*) from **Condition Source** *Daze*
  And the *dazed* component is *active* in *Steel's* **Imposed Conditions**
  And the *hindered* component is *inactive* — suppressed by an *active* **Imposed Condition** *immobile* from a different **Condition Source** *Snare*
  When **Ongoing Effects** ends **Power Effect** *Daze* for *Steel*
  Then both *dazed* (active) and *hindered* (inactive) **Imposed Conditions** are removed from *Steel's* **Imposed Conditions**
  And *Daze* is removed from *Steel's* **Ongoing Effects**
  And *immobile* from *Snare* remains — it belongs to a different source

---

### Roll Fortitude Check to Stabilize While Dying

Scenario: Two accumulated degrees of success stabilize the dying character
  Given **Character** *Steel* carries the **Combined Condition** *dying* (incapacitated + near death)
  And **Trait** *Fortitude* with **Rank** *+8* is *Steel's* Fortitude resistance trait
  And the **GM** requires a **Graded Check** on **Trait** *Fortitude* vs **Difficulty Class** *15* each round
  And *Steel* has accumulated *1* degree of success on prior *Fortitude* checks while *dying*
  When *Steel* makes a **Graded Check** on **Trait** *Fortitude* vs **Difficulty Class** *15* and rolls *7* on the **D20**
  Then the **Graded Check Result** has **Roll Total** *15* (7 + 8) and **Degrees of Success** *1*
  And *Steel's* accumulated degrees of success total *2*
  And *Steel* is *stabilized* — the *dying* **Combined Condition** is ended

Scenario: Three accumulated degrees of failure mean death
  Given **Character** *Steel* carries the **Combined Condition** *dying* (incapacitated + near death)
  And **Trait** *Fortitude* with **Rank** *+8* is *Steel's* Fortitude resistance trait
  And the **GM** requires a **Graded Check** on **Trait** *Fortitude* vs **Difficulty Class** *15* each round
  And *Steel* has accumulated *1* degree of failure on prior *Fortitude* checks while *dying*
  When *Steel* makes a **Graded Check** on **Trait** *Fortitude* vs **Difficulty Class** *15* and rolls *1* on the **D20**
  Then the **Graded Check Result** has **Roll Total** *9* (1 + 8) and **Margin** *−6*
  And the **Graded Check Result** has **Degrees of Failure** *2*
  And *Steel's* accumulated degrees of failure total *3*
  And *Steel's* condition changes to *dead*

---

### Stabilize Dying Ally with Treatment Check

Scenario: Successful Treatment check stabilizes a dying ally
  Given **Character** *Steel* carries the **Combined Condition** *dying* (incapacitated + near death)
  And **Character** *Volt* has **Trait** *Treatment* with **Rank** *+5*
  When *Volt* makes a **Check** on **Trait** *Treatment* vs **Difficulty Class** *15* and rolls *11* on the **D20**
  Then the **Check Result** has **Roll Total** *16* (11 + 5) and is *success*
  And *Steel* is *stabilized* — the *dying* condition is ended

Scenario: Failed Treatment check does not stabilize the ally
  Given **Character** *Steel* carries the **Combined Condition** *dying* (incapacitated + near death)
  And **Character** *Volt* has **Trait** *Treatment* with **Rank** *+5*
  When *Volt* makes a **Check** on **Trait** *Treatment* vs **Difficulty Class** *15* and rolls *4* on the **D20**
  Then the **Check Result** has **Roll Total** *9* (4 + 5) and is *failure*
  And *Steel* remains *dying*

---

## Translate Rank to Measure

---

### Derive Measurement from Rank Formula

Scenario: Throwing distance Rank is Strength Rank minus the thrown object's Mass Rank
  Given **Character** *Steel* has **Trait** *Strength* with **Rank** *+10*
  And the thrown object has **Mass Rank** *7* (resolved from the **Measurement** table for *LIFTING*)
  When the system derives the *throwing distance* for *Steel* throwing that object
  Then the throwing distance **Rank** is *3* (Strength **Rank** 10 − Mass **Rank** 7)
  And the **Measurement** lookup for **Rank** *3* **Measurement Type** *TRAVEL_DISTANCE* returns the distance value in meters

Scenario: Travel distance Rank is derived by adding Time Rank and Speed Rank
  Given *Steel* has **Trait** *Speed* with **Rank** *5*
  And the travel period has **Rank** *3* in **Measurement Type** *TRAVEL_TIME*
  When the system derives the *travel distance* for *Steel* over that period
  Then the **Rank.add()** operation converts **Rank** *5* and **Rank** *3* to their **Ranked Measurement** values for *TRAVEL_DISTANCE*
  And the combined distance measure is looked up as the nearest **Rank** in the **Measurement** table

Scenario: Ranks must not be added directly — convert to measure values first
  Given **Rank** *5* and **Rank** *3* must be combined for **Measurement Type** *TRAVEL_DISTANCE*
  When the system adds the two **Ranks** using **Rank.add()** for **Measurement Type** *TRAVEL_DISTANCE*
  Then **Rank** *5* is first converted to its **Ranked Measurement** value for *TRAVEL_DISTANCE*
  And **Rank** *3* is converted to its **Ranked Measurement** value for *TRAVEL_DISTANCE*
  And the two **Ranked Measurement** values are summed as a combined distance measure
  And the result **Rank** is looked up as the nearest entry in the **Measurement** table for *TRAVEL_DISTANCE*
  And the result **Rank** differs from the naive sum of *5 + 3 = 8* — ranks compound on a doubling scale, not linear addition
