# Corrections log

Project: mm3e-online-holistic
Source: DDD phase skills (domain-language, key-abstractions, domain-sketch, module-partition, story-mapping, acceptance-criteria)

---

## Entry: Module names must be nouns, not verb phrases

- **Status:** confirmed
- **Context:** abd-module-partition and all downstream DDD phase skills
- **DO / DO NOT:** **DO** name modules as nouns — the thing being modeled (e.g. "Character", "Ability", "Skill", "Check"). **DO NOT** name modules as verb phrases or gerund constructions (e.g. "Character Construction", "Check Resolution", "Assign Abilities", "Configure Powers").
- **Example (wrong):**
  `# Module: [Character Construction]` — "Construction" is a verb/gerund; the module models the *character*, not the act of constructing.
  `# Module: [Check Resolution]` — "Resolution" is what you do with checks; the module models the *check*.
- **Example (correct):**
  `# Module: [Character]` — the noun names the thing the module owns.
  `# Module: [Check]`
- **Likely source:** prompt gap

---

## Entry: Boundary term owners must use canonical singular module names

- **Status:** confirmed
- **Context:** All DDD phase files with boundary terms
- **DO / DO NOT:** **DO** use the canonical singular module name in `*(owned by: Module)*` — e.g. "Ability", "Skill", "Advantage", "Power". **DO NOT** use plurals ("Abilities", "Skills") or verb-phrase epic names ("Assign Abilities", "Configure Powers") as module owners.
- **Example (wrong):**
  `### **trait** *(owned by: Assign Abilities)*`
  `### **power effect** *(owned by: Powers)*`
  `### **Technology skill** *(owned by: Skills)*`
- **Example (correct):**
  `### **trait** *(owned by: Ability)*`
  `### **power effect** *(owned by: Power)*`
  `### **Technology skill** *(owned by: Skill)*`
- **Likely source:** prompt gap

---

## Entry: Domain-language headings used h4 instead of h3

- **Status:** confirmed
- **Context:** abd-domain-language output for all modules
- **DO / DO NOT:** **DO** use `### **term**` (h3) for term headings and `### references` (h3) for the single consolidated references section per domain group. **DO NOT** use `#### **term**` (h4) for terms or `#### References` (h4) as per-term sub-headings. **DO NOT** insert `#### Domain Sketch` or `#### Domain Language` sub-headings under terms — bullets go directly under `### **term**`.
- **Example (wrong):**
  ```
  #### **power level**
  - bullet

  #### References
  **Ref — …**
  ```
- **Example (correct):**
  ```
  ### **power level**
  - bullet

  ### references
  **Ref — …**
  ```
- **Likely source:** instruction not read
