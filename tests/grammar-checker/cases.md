# Grammar Checker Evaluation Cases

| ID | Category | Test requirement |
|---|---|---|
| G-001 | Orthography | clear spelling error ကို certain_error အဖြစ် ခွဲ |
| G-002 | Confusable | အသံတူစကားလုံးကို context မရှိလျှင် မဖြတ် |
| G-003 | Sequence | Unicode character order issue ကို grammar error မလုပ် |
| G-004 | Negation | မ…ဘူး ပုံစံကို ဝါကျအပြည့်စုံဖြင့် စစ် |
| G-005 | Particle | spoken particle ကို formal အဖြစ် အလိုအလျောက်မပြင် |
| G-006 | Register | formal နှင့် conversational ရောစပ်မှုကို style/grammar ခွဲ |
| G-007 | Spacing | စာလုံးတိုင်းကြား space မထည့် |
| G-008 | Punctuation | sentence ending ကို channel အလိုက် အကြံပြု |
| G-009 | Brand | brand name ကို မပြင် |
| G-010 | Product | product code နှင့် price ကို မပြင် |
| G-011 | URL | URL/email ကို မပြင် |
| G-012 | Technical | API/ID/version ကို protected span အဖြစ်ထား |
| G-013 | Social | emoji/repetition ကို optional_style အဖြစ်သာပြ |
| G-014 | Short | context မလုံလောက်လျှင် limitation ပြ |
| G-015 | Mixed | Burmese-English mixed text ကို အကုန်မြန်မာပြောင်းမလုပ် |
| G-016 | No error | သေချာသောအမှားမရှိလျှင် rewrite မလုပ် |
| G-017 | Spoken | particle placement ကို spoken context ဖြင့်စစ် |
| G-018 | Formal | formal document ကို slang အဖြစ်မပြောင်း |
| G-019 | Multiple | spelling နှင့် punctuation ကို confidence ခွဲ |
| G-020 | Ambiguous | source disagreement ကို context_dependent ပြ |
