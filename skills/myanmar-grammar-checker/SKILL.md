---
name: myanmar-grammar-checker
description: မြန်မာစာ၏ စာလုံးပေါင်း၊ သဒ္ဒါ၊ phrase spacing နှင့် punctuation များကို context နှင့် confidence အလိုက် စစ်ဆေးပြီး ရှင်းလင်းစွာ ပြင်ဆင်ပေးရန် အသုံးပြုသည်။
---

# myanmar-grammar-checker

## Scope

ဤ Skill သည် Standard Burmese text များတွင် orthography, grammar structure, phrase spacing နှင့် punctuation ကို စစ်ဆေးသည်။ Spoken Burmese, social style, brand terms နှင့် technical identifiers များကို သီးခြား context အဖြစ် ထည့်သွင်းစဉ်းစားရမည်။

## Workflow

1. Input text ၏ content type, register နှင့် encoding status ကို ခွဲခြားပါ။
2. Protected spans များဖြစ်သော names, brands, URLs, IDs, product codes နှင့် technical terms များကို မှတ်သားပါ။
3. [rules.md](references/rules.md) အတိုင်း spelling/sequence, grammar, spacing, punctuation အစီအစဉ်ဖြင့် စစ်ပါ။
4. certain_error, recommended_change, optional_style နှင့် context_dependent ကို ခွဲပါ။
5. [output-format.md](references/output-format.md) အတိုင်း original, suggested correction, label, confidence, explanation နှင့် corrected text ကို ပြပါ။
6. သေချာသောအမှားမရှိလျှင် အတင်း rewrite မလုပ်ပါနှင့်။

## Guardrails

- Unicode sequence ပြဿနာကို grammar error အဖြစ် မတင်ပြရ။ Normalizer သို့ route လုပ်ရ။
- မြန်မာစာ space ကို English word boundary အဖြစ် မယူဆရ။
- Spoken particle ကို formal writing အဖြစ် အလိုအလျောက် မပြင်ရ။
- Brand names, product names, URLs, IDs, prices, dates နှင့် user-protected text မပြင်ရ။
- Source မခိုင်လုံသော case ကို recommendation သို့မဟုတ် context_dependent အဖြစ်သာ ပြရ။
- User တောင်းဆိုခြင်းမရှိဘဲ tone, slang သို့မဟုတ် channel style မပြောင်းရ။

## References

- [Grammar and spelling rules](references/rules.md)
- [Output format](references/output-format.md)
- [Before/after example](examples/before-after-01.md)
