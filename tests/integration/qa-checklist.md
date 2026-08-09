# QA Checklist

## Skill Structure

- [ ] Every Skill has valid YAML frontmatter with name and description.
- [ ] Skill name matches its directory name.
- [ ] Each SKILL.md links directly to its references and examples.
- [ ] SKILL.md stays concise; details live in references.
- [ ] Every Skill has agents/openai.yaml.
- [ ] Every default_prompt explicitly names its skill.

## Behavioral Boundaries

- [ ] Humanizer preserves facts, numbers, names, URLs, and brand terms.
- [ ] Grammar Checker separates certain errors from recommendations.
- [ ] Style Guide respects document type and user/brand glossary.
- [ ] Text Normalizer reports low-confidence or mixed encoding without unsafe conversion.
- [ ] Cross-skill routing does not duplicate or contradict another Skill.

## Release Gate

- [ ] 20 tests per Skill are present.
- [ ] Cross-skill integration fixtures are present.
- [ ] Research sources are recorded.
- [ ] Known limitations are documented.
- [ ] Version and changelog are updated.
