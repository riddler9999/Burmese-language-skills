# Text Normalizer Evaluation Cases

| ID | Category | Test requirement |
|---|---|---|
| N-001 | Unicode | valid Unicode text remains unchanged |
| N-002 | Zawgyi | high-confidence Zawgyi is detected |
| N-003 | Convert | user-requested Zawgyi-to-Unicode conversion preserves meaning |
| N-004 | Mixed | mixed input reports affected spans |
| N-005 | Low confidence | no automatic conversion |
| N-006 | Sequence | character-order issue is reported |
| N-007 | Zero-width | invisible characters are reported |
| N-008 | Whitespace | repeated/edge whitespace is normalized safely |
| N-009 | Phrase | word boundaries are not invented with spaces |
| N-010 | Punctuation | repeated punctuation is recommendation only in social text |
| N-011 | Brand | brand name is preserved |
| N-012 | URL | URL and email are preserved |
| N-013 | Product | code, price, and date are preserved |
| N-014 | Emoji | intentional emoji is not removed automatically |
| N-015 | English | English technical term remains unchanged |
| N-016 | Empty | empty input returns a clear no-content result |
| N-017 | Long | long text reports confidence and affected spans |
| N-018 | Script | non-Burmese Myanmar-script language is not falsely labeled Burmese error |
| N-019 | Already normalized | no-op result is allowed |
| N-020 | Routing | grammar/style findings route to other Skills |
