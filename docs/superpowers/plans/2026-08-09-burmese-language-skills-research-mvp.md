# Burmese Language Skills Research Foundation and MVP Implementation Plan

> **For agentic workers:** Use the repository workflow and keep each task independently reviewable.

**Goal:** Establish an evidence-backed Burmese language research foundation and build the first usable myanmar-humanizer MVP.

**Architecture:** Keep each Skill independent under skills/. Keep detailed rules and examples in references/ and examples/ so SKILL.md remains small. Keep research decisions, annotation labels, and evaluation cases separate from runtime instructions.

**Tech Stack:** Markdown-based Agent Skills, GitHub repository contents API, Unicode Myanmar technical references, curated Burmese corpus examples, manual/native-writer review.

## Global Constraints

- Use Unicode Myanmar text in repository content.
- Preserve meaning, intent, tone, brand terms, and intentional informal language.
- Separate certain errors from recommendations and context-dependent suggestions.
- Do not claim a rule is authoritative unless its source is recorded.
- Keep the first MVP focused on Burmese social/business content humanization.

---

### Task 1: Research Source Registry

**Files:**
- Modify: research/sources.md
- Create: research/source-notes.md

**Deliverable:** Record authoritative technical sources, language references, academic research, and usage evidence with scope, reliability, and known limitations.

- [ ] Add source URL and citation metadata.
- [ ] Classify each source as technical standard, language authority, academic research, or usage evidence.
- [ ] Record whether a source supports a hard rule, a heuristic, or background context.
- [ ] Record unresolved disagreements instead of silently choosing a rule.

**Verification:** Every rule used in later references must map to at least one source or be labeled as empirical usage guidance.

---

### Task 2: Burmese Writing Taxonomy

**Files:**
- Modify: research/taxonomy.md
- Create: research/annotation-schema.md

**Deliverable:** Define labels for spelling, grammar, spacing, punctuation, AI-style, translationese, tone, brand terms, and Unicode/Zawgyi issues.

- [ ] Define label name, scope, positive example, non-example, confidence, and correction policy.
- [ ] Separate correctness errors from style preferences.
- [ ] Add an explicit NONSTANDARD_BUT_ACCEPTABLE label for intentional informal usage.
- [ ] Define when the Skill must ask for context instead of correcting.

**Verification:** Each label has a non-overlapping purpose and can be applied to a test example.

---

### Task 3: Humanizer Reference Rules

**Files:**
- Modify: skills/myanmar-humanizer/SKILL.md
- Create: skills/myanmar-humanizer/references/patterns.md
- Create: skills/myanmar-humanizer/references/output-format.md
- Create: skills/myanmar-humanizer/examples/before-after-01.md

**Deliverable:** Build a conservative Burmese humanization workflow for social, business, and educational content.

- [ ] Define AI-style patterns without treating every formal sentence as AI-generated.
- [ ] Require content type and target audience detection.
- [ ] Preserve facts, intent, tone, numbers, names, URLs, and brand terms.
- [ ] Add a change-rate warning for aggressive rewrites.
- [ ] Provide a structured output format with detected patterns, revised text, and meaning-preservation notes.

**Verification:** Test examples demonstrate that the Skill improves naturalness without changing the message.

---

### Task 4: Evaluation Set

**Files:**
- Modify: research/evaluation-plan.md
- Create: tests/humanizer/cases.md
- Create: tests/humanizer/expected-behavior.md

**Deliverable:** Create the first evaluation set for Burmese humanization.

- [ ] Include social media, sales, business, technical, formal, conversational, and Burmese-English mixed examples.
- [ ] Include already-natural text and intentional slang to measure over-correction.
- [ ] Include expected behavior, acceptable alternatives, and forbidden changes.
- [ ] Track meaning preservation, tone preservation, and false positives.

**Verification:** The test set contains at least 20 cases across the defined categories before calling the MVP ready.

---

### Task 5: Repository QA

**Files:**
- Modify: README.md
- Modify: CHANGELOG.md

**Deliverable:** Document the MVP status, scope, limitations, and how contributors should add rules and examples.

- [ ] Confirm every Skill has valid frontmatter with name and description.
- [ ] Confirm references are linked from the relevant SKILL.md.
- [ ] Confirm examples and tests use Unicode Myanmar text.
- [ ] Record known limitations and the next research milestone.

**Verification:** Fetch each changed file from GitHub and verify the expected paths and frontmatter.
