---
state: domain-sketch
---

# Module: [Ability]

_Object model for all Ability terms. Concepts: ability, defense, initiative. Subtypes: Enhanced Ability (of ability); Dodge, Parry, Fortitude, Toughness, Will (of defense). Properties and instances modeled inline._

Scope: The eight ability scores (Strength, Stamina, Agility, Dexterity, Fighting, Intellect, Awareness, Presence), absent abilities, debilitated abilities, and derived defense values.

---

Every character is defined by eight numeric *abilities* — four physical (*Strength*, *Stamina*, *Agility*, *Dexterity*) and four mental (*Fighting*, *Intellect*, *Awareness*, *Presence*). Each *ability* carries a *rank* that modifies die rolls, derives *defenses*, feeds *initiative*, and cascades changes to all dependent *traits*. Two extreme states bracket the *rank*: *absent* (the *ability* does not exist — no *rank*, auto-fail, per-*ability* capability-loss effects) and *debilitated* (*rank* drops below −5 — per-*ability*-group *conditions* imposed). A portion of any *ability rank* may be designated *enhanced*, granting access to nullification, *power modifiers*, and *power stunts* that natural *abilities* lack.

---

# Core Domain

## Ability

An *ability* is one of eight fundamental numeric *traits* that characterize a *character's* physical or mental capabilities. It owns the *rank*, the cost formula (2 *power points* per +1), the cascade rule (changing the *rank* updates all dependent *traits* — *skills*, *defenses*, *attack modifiers* — in the same operation), the physical/mental partition, and two extreme states (*absent* and *debilitated*). *Ability* is the single source of truth for the raw modifier that feeds into *checks*, *defenses*, and *initiative*. Everything in this module exists because an *ability* exists.

### ability

- stores a signed integer *rank* that modifies related die rolls as a direct numeric bonus or penalty
- partitions into physical (*Strength*, *Stamina*, *Agility*, *Dexterity*) and mental (*Fighting*, *Intellect*, *Awareness*, *Presence*) categories, each feeding different *skills* and derived values
- propagates any *rank* change to all dependent *traits* in the same operation — *skills*, *defenses*, and *attack modifiers* all update when the *ability rank* changes
- accepts *power point* investment at a rate of 2 pp per +1 *rank*, and refunds 2 pp per −1 *rank* when reduced
- designates whether any portion of its *rank* is *enhanced* (a *power*) or natural, tracking each portion separately
- derives one or more *defense* values from its *rank* (*Strength* → none directly; *Stamina* → *Toughness* and *Fortitude*; *Agility* → *Dodge*; *Fighting* → *Parry*; *Awareness* → *Will*) and contributes to *initiative* (*Agility*)
- enters the *absent* state when a creature entirely lacks the *ability* — no *rank*, auto-fail on related *checks*, per-*ability* capability-loss effects applied to the *character*, 10 pp granted
- enters the *debilitated* state when *rank* drops below −5 — per-*ability*-group *conditions* imposed on the *character*, *rank* floor enforced
- **Invariant:** whenever *rank* changes, all dependent *traits* must update to reflect the new value in the same operation
- **Invariant:** *rank* cannot drop below −5 through voluntary player adjustment; values below −5 trigger the *debilitated* state via external game effects only
- **Invariant:** an *absent ability* has no *rank* — there is no *modifier*, no purchasing, and no cascade; only the per-*ability* absence effects apply
- **Invariant:** once *debilitated*, the *rank* cannot be lowered further — the *debilitated* threshold is the absolute floor

Properties:
- *ability rank* — signed integer *rank* measuring the *ability's* effectiveness; baseline 0, floor −5

Instances:
- *Strength (STR)* — sheer muscle power; feeds unarmed/*strength*-based *attack damage*, jump distance, carrying/lifting/throwing capacity, and *Athletics skill checks*
- *Stamina (STA)* — health, endurance, physical resilience; derives *Toughness* and *Fortitude defenses*; feeds *Stamina checks* to resist or recover from health threats
- *Agility (AGL)* — balance, grace, speed, physical coordination; derives *Dodge defense* and *initiative*; feeds *Acrobatics* and *Stealth skill checks*
- *Dexterity (DEX)* — hand-eye coordination, precision, manual dexterity; feeds ranged *attack checks*, *Sleight of Hand* and *Vehicles skill checks*
- *Fighting (FGT)* — close combat ability; derives *Parry defense*; feeds close *attack checks*
- *Intellect (INT)* — reasoning and learning; feeds *Expertise*, *Investigation*, *Technology*, and *Treatment skill checks*
- *Awareness (AWE)* — common sense and intuition; derives *Will defense*; feeds *Insight* and *Perception skill checks*
- *Presence (PRE)* — force of personality, persuasiveness, leadership; feeds *Deception*, *Intimidation*, and *Persuasion skill checks*

### Decisions made

- One KA for the entire module. *Ability* is a small, cohesive module — everything here exists because an *ability* exists.
- The eight named *abilities* (*Strength* through *Presence*) are instances of *ability*. Each feeds different *skills* and derives different *defenses*, but the core mechanic (*rank*, PP cost, cascade, *absent*/*debilitated* states) is identical. The difference is configuration data (which *skills*, which *defense*), not behavior. Open question for object-model: whether the per-*ability* *debilitation* and absence effects warrant subtype promotion.
- *ability rank* is a property of *ability*, not a separate concept — it has no identity outside its *ability*.
- *absent ability* is a state on *ability*, not a separate concept. The base *ability* enters the *absent* state; each specific *ability* inherits per-*ability* capability-loss effects (auto-fail, game *modifier* changes, *condition* application) from the base *absent* mechanic.
- *debilitated* is an invariant on *ability*, not a separate concept. It is the floor rule plus per-*ability*-group *condition* application — a constraint on what happens when *rank* crosses the −5 threshold.
- *Enhanced Ability* is a subtype of *ability* because it adds three delta behaviors (nullification, *power modifiers*, *power stunts*) that natural *abilities* do not have.

### References

**Ref — Ch3 Abilities**
Source: context/rules/HeroesHandbook-rules__chunk_035.md
Locator: lines 2298-2362
Extract: whole

```source
## CHAPTER 3: ABILITIES
Everyone has certain basic abilities: how strong, fast, smart, and clever they are. These abilities influence most things
your character does. Stronger characters can lift greater weights, more agile characters have better balance, tougher
characters can soak up more damage, and so forth.
MUTANTS & MASTERMINDS characters have eight basic abilities: Strength (Str), Stamina (Sta), Dexterity (Dex), Agility (Agl),
Fighting (Ftg), Intellect (Int), Awareness (Awe), and Presence (Pre). Strength, Dexterity, Agility and Stamina are physical
abilities, whereas Fighting, Intellect, Awareness, and Presence are mental abilities. Each above-average ability pro-
vides a bonus on certain die rolls; while below average abilities apply a penalty.

### Ability Ranks
Each ability has a rank associated with it, based on how above or below average it is. Abilities start at rank 0, the baseline
average for an adult human being. They can go as low as –5 (truly terrible) and as high as 20, with higher values reserved
for truly cosmic beings and forces.
The ability rank is added to, or subtracted from, die rolls when your character does something related to that ability. For
example, your Strength rank affects the amount of damage you do when punching someone. Your Intellect rank comes
into play when you roll skills based on Intellect, and so forth. Sometimes your rank is used to calculate another value, such
as when you use your Agility to determine how good you are at avoiding harm with your reflexes (your Dodge defense).

### Buying Ability Ranks
You choose your hero's ability ranks by spending power
points on them. Increasing an ability rank by 1 costs 2
power points, so putting two points into Strength, for ex-
ample, raises it from 0 to 1. Remember a rank of 0 is av-
erage, 2 is a fair amount of talent or natural ability, 3 is
exceptional, 4 extraordinary, and so forth. (See the Ability
Benchmarks table for guidelines.)

### Reducing Abilities
You can also lower one or more of your character's ability
ranks from the starting value of 0. Each rank you lower an
ability gives you an additional two power points to spend
elsewhere. You cannot lower an ability rank below –5,
which is itself a serious deficiency.
Ability Cost = 2 power points
per +1 to an ability rank.
Gain 2 bonus power points
per -1 to an ability rank.
```

**Ref — Beyond Human**
Source: context/rules/HeroesHandbook-rules__chunk_036.md
Locator: lines 2363-2464
Extract: whole

```source
### Beyond Human
Although a rank of 7 is defined as "the peak of human achievement" in an ability on the Ability Benchmarks table, a character
with an ability rank greater than 7 isn't necessarily "non-human," merely superhuman in comparison to ordinary people. Many
"normal human" characters in the comics have truly superhuman abilities, particularly mental abilities. A character can have
a superhuman ability rank without necessarily being anything other than an amazingly talented, well-trained human being.
The limits of what "normal" people can accomplish is up to the Gamemaster and depends very much on the style of the game.

STRENGTH (STR)
Strength measures sheer muscle power and the ability to apply it. Your Strength rank applies to:
• Damage dealt by your unarmed and strength-based attacks.
• How far you can jump (based on an Athletics skill check).
• The amount of weight you can lift, carry, and throw.
• Athletics skill checks.

STAMINA (STA)
Stamina is health, endurance, and overall physical resilience. Stamina is important because it affects a character's ability to resist most forms of damage. Your Stamina modifier applies to:
• Toughness defense, for resisting damage.
• Fortitude defense, for resisting effects targeting your character's health.
• Stamina checks to resist or recover from things affecting your character's health when a specific defense doesn't apply.

AGILITY (AGL)
Agility is balance, grace, speed, and overall physical coordination. Your Agility rank applies to:
• Dodge defense, for avoiding ranged attacks and other hazards.
• Initiative bonus, for acting first in combat.
• Acrobatics and Stealth skill checks.
• Agility checks for feats of coordination, gross movement, and quickness when a specific skill doesn't apply.

DEXTERITY (DEX)
Dexterity is a measure of hand-eye coordination, precision, and manual dexterity. Your Dexterity rank applies to:
• Attack checks for ranged attacks.
• Sleight of Hand and Vehicles skill checks.
• Dexterity checks for feats of fine control and precision when a specific skill doesn't apply.

FIGHTING (FGT)
Fighting measures your character's ability in close combat, from hitting a target to ducking and weaving around any counter-attacks. Your Fighting rank applies to:
• Attack checks for close attacks.
• Parry defense, for avoiding close attacks.

INTELLECT (INT)
Intellect covers reasoning ability and learning. A character with a high Intellect rank tends to be knowledgeable and well-educated. Your Intellect modifier applies to:
• Expertise, Investigation, Technology, and Treatment skill checks.
• Intellect checks to solve problems using sheer brainpower when a specific skill doesn't apply.

AWARENESS (AWE)
While Intellect covers reasoning, Awareness describes common sense and intuition, what some might call "wisdom." A character with a high Intellect and a low Awareness may be an "absent-minded professor" type, smart but not always aware of what's going on. On the other hand, a not so bright (low Intellect) character may have great deal of common sense (high Awareness). Your Awareness modifier applies to:
• Will defense, for resisting attacks on your mind.
• Insight and Perception skill checks.
• Awareness checks to resolve matters of intuition when a specific skill doesn't apply.

PRESENCE (PRE)
Presence is force of personality, persuasiveness, leadership ability and (to a lesser degree) attractiveness. Presence is useful for heroes who intend to be leaders as well as those who strike fear into the hearts of criminals with their presence. Your Presence modifier applies to:
• Deception, Intimidation, and Persuasion skill checks.
• Presence checks to influence others through force of personality when a specific skill doesn't apply.
```

**Ref — Absent Abilities**
Source: context/rules/HeroesHandbook-rules__chunk_038.md
Locator: lines 2525-2595
Extract: whole

```source
### Absent Abilities
Rather than having a rank of –5 in a given ability, some
things or creatures actually lack an ability altogether.
These beings automatically fail any check requiring the
absent ability. The additional effects of an absent ability
are as follows:
• Strength: A creature with no Strength is incapable
of exerting any physical force, either because it has
no physical form (like an incorporeal ghost) or simply
can't move (like a tree).
• Stamina: A creature with no Stamina has no physical
body (like a ghost) or is not a living being (such as a
robot or other construct). Creatures with no Stamina
suffer and recover from damage like inanimate ob-
jects (see Damaging Objects under the Damage
effect). They are immune to fatigued and exhausted
conditions, but cannot exert extra effort. Creatures
with no Stamina are often—but not necessarily—im-
mune to many of the other things affecting living be-
ings as well (see the Immunity effect in the Powers
chapter). They have no Fortitude defense.
• Dexterity: A creature with no Dexterity cannot manip-
ulate objects and hence cannot make physical attacks.
• Agility: A creature with no Agility is unable to move
its body under its own power and has no Dodge de-
fense.
• Fighting: A creature with no Fighting is incapable of
making any sort of close attack (but may still be able
to launch ranged attacks, if it has Dexterity).
• Intellect: A creature with no Intellect is an automa-
ton, lacking free will and operating entirely on simple
instinct or pre-programmed instructions. Anything
with no Intellect is immune to mental effects and in-
teraction skills and has no Will defense.
• Awareness: Anything with no Awareness is com-
pletely unaware and also has no Presence. It is an in-
animate object, not a creature. Objects are immune
to mental effects and interaction skills, and have no
defenses apart from Toughness (and Fortitude, if
they are alive).
• Presence: Creatures without Presence are unable to
interact and immune to interaction skills. They have
no Will defense.
Lacking an ability is –10 power points; that is, it gives the
character an additional 10 power points to spend else-
where, similar to having a –5 rank in an ability, but with
different effects. MUTANTS & MASTERMINDS heroes cannot be
absent an ability without Gamemaster permission, as it can
have significant effects on the character and the game.
Absent abilities cannot be weakened (see the Weaken ef-
fect in the Powers chapter) or debilitated, since they are
not present at all in the first place!
Inanimate objects have no abilities other than their
Toughness. Animate, but nonliving, constructs such as ro-
bots or zombies have Strength, Agility, and Dexterity, and
may have ranks of Awareness and Presence (if aware of
their environment or capable of interaction), and Fighting
(if able to make close attacks). They may have Intellect (if
capable of independent thought), but have no Stamina
(since they are not living things). See Constructs in the
Gadgets & Gear chapter for more information.
```

---

### Enhanced Ability *is a type of* ability

- can be nullified by the *Nullify* effect, reducing the total *ability modifier* by the *enhanced* portion's *rank* during nullification
- can have *power modifiers* (*extras* and *flaws*) applied to it, altering its cost or adding special *conditions* to its use
- can be used for *power stunts* with *extra effort*, enabling improvised uses beyond its normal scope
- **Invariant:** nullification of the *enhanced* portion does not change the natural portion of the same *ability*
- **Invariant:** *power stunt* eligibility and *power modifier* application apply only to the designated *enhanced* portion

### Decisions made

- *Enhanced Ability* is a subtype of *ability* because it adds three delta behaviors (nullification, *power modifiers*, *power stunts*) that natural *abilities* do not have. Same cost (2 pp per +1 *rank*); the player decides which portion is *enhanced*.

### References

**Ref — Enhanced Abilities**
Source: context/rules/HeroesHandbook-rules__chunk_037.md
Locator: lines 2465-2524
Extract: whole

```source
### Enhanced Abilities
Some ability ranks—or portions of them—may be ac-
quired as Enhanced Traits, as described in the Powers
chapter. Enhanced Abilities are superhuman powers rath-
er than natural. The key differences between Enhanced
Abilities and normal ability ranks are Enhanced Abilities
can be nullified (normal abilities cannot, see Nullify, page
173) and Enhanced Abilities can have power modifiers
and be used for power stunts with extra effort (normal
abilities cannot, see Extra Effort, page 19).
Enhanced Abilities and normal abilities have the same
cost (2 power points per +1 ability rank). The player de-
cides if a character's ability rank is normal or enhanced
and, if it is enhanced, how much of it is enhanced.

### Altering Abilities
Over the course of play, your hero's ability ranks may
change for the following reasons:
• Some power effects raise or lower ability ranks (see
the Powers chapter).
• You can improve ability ranks permanently by spend-
ing earned power points on them, but you cannot
increase an ability rank above the limits set by the
series' power level (see Power Level, page 24).
Whenever an ability rank changes, all traits associated
with the ability change as well. So if you increase your
character's Agility, his Agility-based skills and Dodge de-
fense also increase. Likewise, if the hero's Agility bonus
decreases, his Agility-based skills and Dodge suffer.

### Debilitated Abilities
If one of your hero's ability ranks drops below –5 for any
reason, that ability is said to be debilitated and the char-
acter suffers more serious effects than just a penalty to
certain traits and rolls, as follows:
• Debilitated Strength, Agility, or Dexterity means
the hero collapses: defenseless, immobilized, and
stunned (although still conscious and aware).
• Debilitated Stamina means the hero is dying, and
suffers a –5 modifier on Fortitude checks to avoid
death on top of it.
• Debilitated Fighting means the hero is dazed and
defenseless, and cannot make close attacks.
• Debilitated Intellect, Awareness, or Presence
means the hero is unaware and remains so until re-
stored to at least a –5 rank in the ability.
Debilitated ability ranks usually result from a power af-
fecting your character. Ability ranks cannot be lowered
any further once they are debilitated.
```

---

### defense

- computes a base *rank* equal to the associated *ability rank*, producing a defensive value that represents the *character's* resistance or avoidance capability
- accepts *power point* investment to raise the *defense* above its base *ability rank*, at a cost of 1 pp per +1 *rank*, subject to *power level* limits
- serves two purposes: as a *defense class* (*defense* + 10 = *DC* for attackers) and as a *resistance check modifier* (*defense* + *d20* vs effect *DC*)
- belongs to either the *active* category (*Dodge*, *Parry* — degrades under *vulnerability* and *defenselessness conditions*) or the *passive* category (*Fortitude*, *Toughness*, *Will* — always fully effective regardless of mobility)
- **Invariant:** base *defense rank* always equals the associated *ability rank*; investment and *power* effects add on top of this base

### Decisions made

- *active defense* is a category label (the set {*Dodge*, *Parry*}), not a concept with its own behavior — collapsed into the active/passive categorization on *defense* and the degradation rules on *Dodge* and *Parry*.
- *defense class* is a derived value (*defense* + 10) — folded into a behavior bullet on *defense* rather than promoted to its own concept, because it has no identity or state beyond the formula; the targeting semantics ("targets *Dodge*", "targets *Will*") describe which *defense* is selected, not a separate entity.
- The five named *defenses* (*Dodge*, *Parry*, *Fortitude*, *Toughness*, *Will*) are subtypes of *defense* — each has genuinely different behavior (source *ability*, active/passive, *Toughness* investment restriction).
- *Resistance checks* as a mechanic belong to *Check*; this module defines the *defense* values used in those *checks*.

### References

**Ref — Defenses & Initiative**
Source: context/rules/HeroesHandbook-rules__chunk_039.md
Locator: lines 2596-2637
Extract: whole

```source
### Defenses & Initiative
Heroes face many hazards in their line of work, from attacks by villainous foes to traps and fiendish mind control. A
hero's defenses are abilities used to avoid such things, determining the difficulty to affect a hero with an attack, or to
make resistance checks against them. Each defense is based on a particular ability, modified by the hero's advantages
and powers. For more on defenses in general and how you use them, see Chapter 8.
DODGE
Dodge defense is based on Agility rank. It includes reac-
tion time, quickness, nimbleness, and overall coordina-
tion, used to avoid ranged attacks or other hazards where
reflexes and speed are important.
FORTITUDE
Fortitude defense is based on Stamina and measures
health and resistance to threats like poison or disease. It
incorporates constitution, ruggedness, metabolism, and
immunity.
PARRY
Parry defense is based on Fighting. It is the ability to coun-
ter, duck, or otherwise evade a foe's attempts to strike you
in close combat through superior fighting ability.
TOUGHNESS
Toughness defense is based on Stamina and is resistance
to direct damage or harm, and overall durability.
WILL
Will defense is based on Awareness rank. It measures
mental stability, level-headedness, determination, self-
confidence, self-awareness, and willpower, used to resist
mental or spiritual attacks.

### Defense Rank
Your base defense ranks are equal to your ranks in their
associated abilities. You can increase your defenses above
the values granted by your ability ranks by spending pow-
er points: 1 power point grants you an additional rank in
a defense, up to the limits imposed by power level (see
Power Level on page 24).
Defense Cost =
1 power point per +1 rank
With the Enhanced Trait effect (see the Powers chapter)
you can also improve your defenses with powers at the
same cost, 1 point per rank.
```

---

### Dodge *is a type of* defense

- derives its base *rank* from *Agility*
- avoids ranged *attacks* and hazards where reflexes and speed are important
- degrades when *vulnerable* (*rank* halved, round up) or *defenseless* (*rank* reduced to 0)
- provides *defense class* (*Dodge* + 10) against ranged *attacks* and *Dodge resistance checks* against triggered hazards

### References

**Ref — Defenses & Initiative**
Source: context/rules/HeroesHandbook-rules__chunk_039.md
Locator: lines 2596-2637
Extract: partial
Part: DODGE section

---

### Parry *is a type of* defense

- derives its base *rank* from *Fighting*
- counters, ducks, or evades close *attacks* through superior *fighting ability*
- degrades when *vulnerable* (*rank* halved, round up) or *defenseless* (*rank* reduced to 0)
- provides *defense class* (*Parry* + 10) against close *attacks*

### References

**Ref — Defenses & Initiative**
Source: context/rules/HeroesHandbook-rules__chunk_039.md
Locator: lines 2596-2637
Extract: partial
Part: PARRY section

---

### Fortitude *is a type of* defense

- derives its base *rank* from *Stamina*
- resists threats targeting health: poison, disease, toxins, dying
- operates as a *passive defense*, always fully effective regardless of mobility
- **Invariant:** does not exist for creatures with no *Stamina* — absence of the source *ability* eliminates this *defense* entirely

### References

**Ref — Defenses & Initiative**
Source: context/rules/HeroesHandbook-rules__chunk_039.md
Locator: lines 2596-2637
Extract: partial
Part: FORTITUDE section

---

### Toughness *is a type of* defense

- derives its base *rank* from *Stamina*
- resists direct damage and measures overall physical durability
- operates as a *passive defense*, always fully effective regardless of mobility
- **Invariant:** cannot be raised above the *Stamina* base by direct *power point* spending — only through *advantages* (e.g., *Defensive Roll*) and *powers* (e.g., *Protection* effect)

### References

**Ref — Toughness Rank**
Source: context/rules/HeroesHandbook-rules__chunk_040.md
Locator: lines 2638-2688
Extract: partial
Part: Toughness Rank section

```source
### Toughness Rank
The exception is Toughness, which can only be increased
above your base Stamina rank using advantages and pow-
ers, not by direct spending of power points. This reflects that
greater-than-normal Toughness is virtually always some sort
of special ability. See the Advantages and Powers chapters
for various options for improving Toughness, notably the De-
fensive Roll advantage and the Protection effect.
```

---

### Will *is a type of* defense

- derives its base *rank* from *Awareness*
- resists mental or spiritual *attacks*
- provides *defense class* (*Will* + 10) when an *attack* targets *Will*
- operates as a *passive defense*, always fully effective regardless of mobility
- **Invariant:** does not exist for creatures with no *Intellect* or no *Awareness*/*Presence* — absence of the source *ability* eliminates this *defense* entirely

### References

**Ref — Defenses & Initiative**
Source: context/rules/HeroesHandbook-rules__chunk_039.md
Locator: lines 2596-2637
Extract: partial
Part: WILL section

---

### initiative

- computes a combat-readiness *modifier* from *Agility rank* + *Advantages* (*Improved Initiative*) + *Power Modifiers*, producing a value that determines action order
- determines who acts first at the start of a conflict: *characters* act from highest to lowest *initiative modifier*
- **Invariant:** *Agility rank* is always the base; *Advantage* and *Power* components are additive boundary contributions

### References

**Ref — Defenses & Initiative**
Source: context/rules/HeroesHandbook-rules__chunk_040.md
Locator: lines 2638-2688
Extract: partial
Part: INITIATIVE section

```source
INITIATIVE
When things start happening quickly, MUTANTS & MASTER-
MINDS characters use their initiative bonuses to determine
who goes first. Each character involved in a conflict makes
a check of d20 + initiative modifier, which is:
Initiative Modifier = Agility + Advantages
(Improved Initiative) + Power Modifiers
Characters then act in initiative order, from highest to low-
est. For details see the Action & Adventure chapter.
```

---

# Boundary Domain

## Character

Owned by: Character

### power point

- serves as the currency consumed when purchasing *ability ranks* (2 pp per +1) and *defense ranks* above base (1 pp per +1)
- is gained when reducing *ability ranks* below 0 (2 pp per −1) or lacking an *ability* entirely (10 pp)

### Decisions made

- *power point* is boundary because this module consumes it but *Character* owns the total budget and spending rules.

### References

**Ref — Ch3 Abilities**
Source: context/rules/HeroesHandbook-rules__chunk_035.md
Locator: lines 2298-2362
Extract: partial
Part: "Buying Ability Ranks" and "Reducing Abilities" sections.

```source
### Buying Ability Ranks
You choose your hero's ability ranks by spending power
points on them. Increasing an ability rank by 1 costs 2
power points, so putting two points into Strength, for ex-
ample, raises it from 0 to 1.

### Reducing Abilities
You can also lower one or more of your character's ability
ranks from the starting value of 0. Each rank you lower an
ability gives you an additional two power points to spend
elsewhere. You cannot lower an ability rank below –5,
which is itself a serious deficiency.
Ability Cost = 2 power points per +1 to an ability rank.
Gain 2 bonus power points per -1 to an ability rank.
```

---

### power level

- constrains the maximum *ability rank* achievable through earned *power point* spending
- constrains the maximum *defense rank* purchasable above the *ability* base

### Decisions made

- *power level* is boundary because this module is constrained by it but *Character* defines what *power levels* are and how they work.

### References

**Ref — Enhanced Abilities**
Source: context/rules/HeroesHandbook-rules__chunk_037.md
Locator: lines 2465-2524
Extract: partial
Part: "Altering Abilities" section — power level cap on ability rank increases.

```source
### Altering Abilities
Over the course of play, your hero's ability ranks may
change for the following reasons:
• Some power effects raise or lower ability ranks (see
the Powers chapter).
• You can improve ability ranks permanently by spend-
ing earned power points on them, but you cannot
increase an ability rank above the limits set by the
series' power level (see Power Level, page 24).
Whenever an ability rank changes, all traits associated
with the ability change as well.
```

**Ref — Defenses & Initiative**
Source: context/rules/HeroesHandbook-rules__chunk_039.md
Locator: lines 2596-2637
Extract: partial
Part: Defense Rank section — power level cap on defense rank increases.

```source
### Defense Rank
Your base defense ranks are equal to your ranks in their
associated abilities. You can increase your defenses above
the values granted by your ability ranks by spending pow-
er points: 1 power point grants you an additional rank in
a defense, up to the limits imposed by power level (see
Power Level on page 24).
Defense Cost =
1 power point per +1 rank
```

---
