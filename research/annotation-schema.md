# Annotation Schema

Each annotated case should be represented with the following fields.

| Field | Required | Meaning |
|---|---:|---|
| id | yes | Stable case identifier |
| input | yes | Original text |
| label | yes | Taxonomy label |
| span_or_phrase | yes | Relevant text span or phrase |
| proposed_output | yes | Suggested correction or rewrite |
| confidence | yes | certain_error, recommended_change, optional_style, or context_dependent |
| rationale | yes | Plain-language explanation |
| source | yes | Source URL, corpus ID, or native-review note |
| preserve | yes | Facts, tone, terms, and intent that must remain unchanged |
| reviewer_notes | no | Disagreement or follow-up note |

## Annotation Rules

1. One case may have multiple labels only when the issues are independent.
2. Do not label intentional slang as SPELLING_ERROR without context.
3. Brand names, product names, usernames, URLs, and identifiers are protected spans by default.
4. If reviewers disagree, keep the case as context_dependent until resolved.
5. Every proposed change must state what must be preserved.
