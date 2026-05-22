---
state: key-abstractions
---

# Module: [Ability]

Scope: The eight ability scores (Strength, Stamina, Agility, Dexterity, Fighting, Intellect, Awareness, Presence), absent abilities, debilitated abilities, and derived defense values.

**Core terms**:
- ability
- ability rank
- absent ability
- Strength (STR)
- Stamina (STA)
- Agility (AGL)
- Dexterity (DEX)
- Fighting (FGT)
- Intellect (INT)
- Awareness (AWE)
- Presence (PRE)
- Dodge
- Parry
- Fortitude
- Toughness
- Will
- defense
- debilitated
- enhanced ability
- initiative
- active defense
- defense class

**Key Abstractions (term grouping)**:
- **Ability**: ability, ability rank, absent ability, Strength (STR), Stamina (STA), Agility (AGL), Dexterity (DEX), Fighting (FGT), Intellect (INT), Awareness (AWE), Presence (PRE), Dodge, Parry, Fortitude, Toughness, Will, defense, debilitated, enhanced ability, initiative, active defense, defense class

---

# Core Domain

## **Ability**

An ability is one of eight fundamental numeric traits that characterize a hero's physical or mental capabilities. The ability owns its rank (a signed integer from −5 to 20+), the cost formula (2 power points per +1, refund of 2 pp per −1), the cascade rule (when a rank changes, every derived trait — skills, defenses, attack modifiers — changes with it), and the physical/mental partition (STR, STA, AGL, DEX are physical; FGT, INT, AWE, PRE are mental). Each named ability feeds specific skills and derives specific defense values: STR feeds Athletics and unarmed damage; STA derives Toughness and Fortitude; AGL derives Dodge and initiative; DEX feeds ranged attack checks; FGT derives Parry; INT feeds Expertise, Investigation, Technology, Treatment; AWE derives Will; PRE feeds Deception, Intimidation, Persuasion. The ability also owns two extreme states that change the game mechanics applied to a character: the absent state (a creature entirely lacks the ability — no rank, auto-fail on related checks, per-ability capability-loss effects, 10 pp granted) and the debilitated state (rank drops below −5 — per-ability-group conditions imposed, rank floor enforced). Some ability ranks — or portions — can be designated Enhanced Traits (powers), adding nullification and power-modifier eligibility on top of the base rank mechanic. The ability does not own the currency it consumes (power points) or the cap on rank increases (power level), both of which belong to Character.

### **ability**
- One of eight fundamental numeric traits that characterize a hero's physical or mental capabilities.
- Partitioned into physical abilities (STR, STA, AGL, DEX) and mental abilities (FGT, INT, AWE, PRE).
- Each above-average ability rank provides a bonus on related die rolls; below-average rank applies a penalty.
- The ability rank is added to (or subtracted from) die rolls for tasks related to that ability and to calculate derived values.
- Ability ranks can be bought up using power points, reduced below 0 for bonus power points, or altered by power effects during play.
- Some ability ranks — or portions of them — can be designated as Enhanced Traits (powers), which behave differently from natural ranks.

### **ability rank**
- Numeric value expressing the degree of an ability; starts at 0 (the baseline average for an adult human).
- Can go as low as −5 (truly terrible) and as high as 20 or beyond for cosmic beings and forces.
- Costs 2 power points per +1 rank when purchased; yields 2 bonus power points per −1 rank when reduced.
- Cannot be voluntarily lowered below −5; dropping below −5 due to an external effect triggers the debilitated state.
- Used directly as a modifier on die rolls and as the base for calculating derived defense values.

### **absent ability**
- A creature entirely lacking an ability has no rank for it, a state distinct from having rank −5.
- Automatically fails any check requiring the absent ability.
- Lacking an ability grants an additional 10 power points to spend elsewhere — more generous than the −5 floor.
- Heroes cannot lack an ability without Gamemaster permission, as absence has significant game effects.
- An absent ability cannot be weakened or debilitated — it simply is not present.
- Per-ability absence effects:
  - No Strength: incapable of exerting any physical force (incorporeal or immobile creature).
  - No Stamina: no physical body; suffers and recovers from damage as an inanimate object; immune to fatigue; no Fortitude defense.
  - No Dexterity: cannot manipulate objects; cannot make physical attacks.
  - No Agility: unable to move under own power; no Dodge defense.
  - No Fighting: incapable of any close attack.
  - No Intellect: automaton; immune to mental effects and interaction skills; no Will defense.
  - No Awareness: completely unaware; also has no Presence; immune to mental effects and interaction skills; treated as inanimate object.
  - No Presence: unable to interact; immune to interaction skills; no Will defense.

### **Strength (STR)**
- Measures sheer muscle power and the ability to apply physical force.
- Applies to: unarmed and strength-based attack damage; jump distance (Athletics check); weight lifting, carrying, and throwing; Athletics skill checks.
- Physical ability.

### **Stamina (STA)**
- Measures health, endurance, and overall physical resilience.
- Applies to: Toughness defense (resisting damage); Fortitude defense (resisting effects on health); Stamina checks for health-related resistance and recovery when no specific defense applies.
- Physical ability.

### **Agility (AGL)**
- Measures balance, grace, speed, and overall physical coordination.
- Applies to: Dodge defense (avoiding ranged attacks and hazards); initiative bonus (acting first in combat); Acrobatics and Stealth skill checks; Agility checks for coordination feats.
- Physical ability.

### **Dexterity (DEX)**
- Measures hand-eye coordination, precision, and manual dexterity.
- Applies to: ranged attack checks; Sleight of Hand and Vehicles skill checks; Dexterity checks for fine control and precision tasks.
- Physical ability.

### **Fighting (FGT)**
- Measures close combat ability — hitting targets and evading counter-attacks in melee.
- Applies to: close attack checks; Parry defense (avoiding close attacks).
- Mental ability (grouped with INT, AWE, PRE as a mental ability in the core rules).

### **Intellect (INT)**
- Covers reasoning ability and learning; a high rank correlates with knowledge and education.
- Applies to: Expertise, Investigation, Technology, and Treatment skill checks; Intellect checks for pure reasoning when no specific skill applies.
- Mental ability.

### **Awareness (AWE)**
- Covers common sense and intuition ("wisdom"), distinct from Intellect (reasoning).
- Applies to: Will defense (resisting mental attacks); Insight and Perception skill checks; Awareness checks for intuition when no specific skill applies.
- Mental ability.
- A creature with no Awareness is also treated as having no Presence; awareness and presence absence are linked.

### **Presence (PRE)**
- Measures force of personality, persuasiveness, leadership ability, and attractiveness.
- Applies to: Deception, Intimidation, and Persuasion skill checks; Presence checks to influence others through force of personality.
- Mental ability.

### **enhanced ability**
- An ability rank (or portion thereof) acquired as an Enhanced Trait (power) rather than as a natural rank.
- Can be nullified by the Nullify effect — normal (natural) ability ranks cannot be nullified.
- Can have power modifiers and be used for power stunts with extra effort — normal ranks cannot.
- Same cost as normal ability ranks: 2 power points per +1 rank.
- The player decides whether a rank is normal, enhanced, or a combination; both apply as modifier simultaneously.

### **debilitated**
- State reached when an ability rank drops below −5 for any reason (typically caused by a power effect).
- Ability ranks cannot be lowered any further once debilitated; this threshold is the floor for each ability.
- Per-ability debilitation effects:
  - STR, AGL, or DEX debilitated: hero collapses — defenseless, immobilized, and stunned (but still conscious and aware).
  - STA debilitated: hero is dying, with an additional −5 modifier on Fortitude checks to avoid death.
  - FGT debilitated: hero is dazed and defenseless; cannot make close attacks.
  - INT, AWE, or PRE debilitated: hero is unaware and remains so until the ability is restored to at least −5.

### **defense**
- General term for the five defensive values (Dodge, Parry, Fortitude, Toughness, Will) used to resist or avoid effects.
- Each defense is based on a specific ability rank, modified by advantages and powers.
- Base defense rank equals the rank of the associated ability.
- Can be increased above base by spending 1 power point per rank, subject to power level limits (except Toughness).
- Serves two purposes: (1) defense class (defense + 10 = DC to affect a target with an attack); (2) resistance check (defense + d20 vs effect's DC).
- Active defenses (Dodge, Parry) require mobility and focus to be fully effective; passive defenses (Fortitude, Toughness, Will) are unaffected by mobility.

### **Dodge**
- Defense value based on Agility rank; covers reaction time, quickness, nimbleness, and coordination.
- Used to avoid ranged attacks and other hazards where reflexes and speed are important.
- Active defense: requires mobility and focus; halved (round up) when vulnerable; reduced to 0 when defenseless.
- Used as defense class (Dodge + 10) against ranged attacks.
- Used in Dodge resistance checks (e.g., reflexively avoid a triggered trap).
- Can be increased above the Agility base by spending 1 power point per rank, subject to power level limits.

### **Parry**
- Defense value based on Fighting rank; represents countering, ducking, or evading close attacks.
- Active defense: halved (round up) when vulnerable; reduced to 0 when defenseless.
- Used as defense class (Parry + 10) for close attacks.
- Can be increased above the Fighting base by spending 1 power point per rank, subject to power level limits.

### **Fortitude**
- Defense value based on Stamina rank; measures health and resistance to threats like poison or disease.
- Incorporates constitution, ruggedness, metabolism, and immunity.
- Passive defense: always effective regardless of mobility restrictions.
- Used in Fortitude resistance checks against health-affecting effects (toxins, disease, dying).
- Can be increased above the Stamina base by spending 1 power point per rank.
- Creatures with no Stamina have no Fortitude defense.

### **Toughness**
- Defense value based on Stamina rank; measures resistance to direct damage and overall physical durability.
- Cannot be increased above the base Stamina rank by direct power point spending — only through advantages (e.g., Defensive Roll) and powers (e.g., Protection effect).
- This restriction reflects that greater-than-normal Toughness is virtually always a special ability.
- Used in Toughness resistance checks against damage.

### **Will**
- Defense value based on Awareness rank; measures mental stability, level-headedness, determination, self-confidence, and willpower.
- Used to resist mental or spiritual attacks.
- Used as defense class (Will + 10) when an attack targets Will.
- Can be increased above the Awareness base by spending 1 power point per rank.
- Creatures with no Intellect or no Awareness/Presence have no Will defense.

### **active defense**
- Category of defense that requires mobility, focus, and reaction time to be fully effective.
- Comprises Dodge and Parry — the two ability-derived defenses that degrade under condition effects.
- When vulnerable: active defense ranks are halved (divide normal value by 2, round up).
- When defenseless: active defense ranks are reduced to 0.
- Contrasts with passive defenses (Fortitude, Toughness, Will), which are unaffected by mobility restrictions.

### **defense class**
- The difficulty class for a given attack to affect a target: defense rank + 10.
- Represents the target's "routine defense" (equivalent to a routine check).
- Primary defense class traits: Dodge (for ranged attacks), Parry (for close attacks), and Will (for mental attacks).
- An attack "targets" a defense when it uses that defense's class as its DC.

### **initiative**
- Derived combat-readiness value computed as: Agility rank + Advantages (Improved Initiative) + Power Modifiers.
- Determines action order at the start of a conflict: characters act from highest to lowest initiative modifier.
- Defined in Ch3 Abilities alongside the five defenses, grounding it in the ability module.
- Depends on the Agility ability rank for its base value; the Advantage and Power components are boundary contributions.

### references

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

**Ref — Toughness Rank**
Source: context/rules/HeroesHandbook-rules__chunk_040.md
Locator: lines 2638-2688
Extract: whole

```source
### Toughness Rank
The exception is Toughness, which can only be increased
above your base Stamina rank using advantages and pow-
ers, not by direct spending of power points. This reflects that
greater-than-normal Toughness is virtually always some sort
of special ability. See the Advantages and Powers chapters
for various options for improving Toughness, notably the De-
fensive Roll advantage and the Protection effect.

### Active Defenses
Dodge and Parry defenses require a measure of action to
be fully effective. Limits on your mobility, focus, and reac-
tion time adversely affect them. If you are vulnerable, your
Dodge and Parry defense ranks are halved (divide their
normal values by 2 and round up), and if you are defense-
less, they are both reduced to 0!

### Defense Class
One use of defenses is determining a defense class, or
the difficulty class to affect a target with a particular at-
tack. This is the appropriate defense, plus 10, just like a
routine check (indeed, it is essentially a measure of the
character's "routine" defense). So hitting a character with
a ranged attack goes against Dodge defense, giving the
attack a DC of (Dodge + 10). Similarly, affecting someone
with a mental power goes against Will defense, with a DC
of (Will + 10), and so forth. This is referred to as "targeting"
a defense, such as "targets Dodge" or "targets Will".
The main defense class traits are Dodge, Parry, and Will.

### Resistance Checks
Defenses are also used to measure the ability to over-
come certain effects, involving a resistance check of the
defense plus a die roll against a difficulty class determined
by the effect or hazard. So you might make a Fortitude re-
sistance check for your hero to overcome a toxin, for ex-
ample, or a Dodge resistance check to avoid a trap just as
it is triggered, and so on. This is referred to as "resisting,"
such as "resisted by Fortitude" or "resisted by Dodge".
The main resistance check traits are Dodge, Fortitude,
Toughness, and Will.
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

### decisions made
- One KA for the entire module. Ability is a small, cohesive module — absent ability, debilitated, defenses, and initiative are all aspects of how an ability works, not independent abstractions.
- absent ability is a state on the base ability, not a separate KA. Each specific ability inherits the absent state and has per-ability effects applied to the character (capability loss, game modifier changes). No independent identity outside ability.
- debilitated is an invariant/extreme state on ability, not a separate KA. It is triggered when rank drops below −5 and imposes per-ability-group conditions — it is the floor rule, not a standalone mechanism.
- Defense values are derived from abilities — they exist because abilities exist. Not an independent KA.
- The eight named abilities are kept as distinct terms because each feeds different skills and derives different defenses — they are not instances with identical behavior.
- Fighting is classified as "mental" per the source text — preserved as-is.
- enhanced ability is included as a term because its rules for nullification and power modifiers are part of how ability ranks work.
- power point and power level moved to Boundary Domain — this module depends on them but does not define them.
- Resistance checks as a mechanic are boundary to Check; this module defines the defense values used in those checks but does not own the check mechanic.

---

# Boundary Domain

### **power point** *(owned by: Character)*
- Currency used to purchase ability ranks (2 pp per +1 rank) and defense ranks above base (1 pp per +1 rank).
- Gained by reducing ability ranks below 0 (2 pp per −1 rank) or by lacking an ability entirely (10 pp).

### **power level** *(owned by: Character)*
- Sets the upper limit on ability rank improvements via earned power points (rank cannot be raised above the series' power level).
- Also constrains the maximum defense rank purchasable above the ability base.

### references

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

### decisions made
- power point is boundary because this module consumes it but Character owns the total budget and spending rules.
- power level is boundary because this module is constrained by it but Character defines what power levels are and how they work.
