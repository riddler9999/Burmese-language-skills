---
name: myanmar-text-normalizer
description: မြန်မာစာ Unicode/Zawgyi encoding၊ character order၊ zero-width characters၊ spaces နှင့် punctuation များကို စစ်ဆေးပြီး ပုံမှန်ပြန်လုပ်ရန် အသုံးပြုသည်။
---

# myanmar-text-normalizer

## Scope

ဤ Skill သည် မြန်မာစာ၏ encoding နှင့် text hygiene ကို စစ်ဆေးသည်။ Grammar, spelling, tone နှင့် style correction မလုပ်ဘဲ သက်ဆိုင်ရာ Skill သို့ route လုပ်ရမည်။

## Workflow

1. Input ကို မပြင်မီ original text ကို ထိန်းသိမ်းပါ။
2. Unicode, Zawgyi-like, mixed, သို့မဟုတ် unknown ဟု encoding status ခွဲပါ။
3. Affected spans၊ detector confidence၊ character order နှင့် invisible characters ကို စစ်ပါ။
4. User က conversion တောင်းဆိုထားခြင်း သို့မဟုတ် high-confidence policy ရှိမှသာ conversion ပြုလုပ်ပါ။
5. Low-confidence/mixed input တွင် automatic conversion မလုပ်ဘဲ သတိပေးပါ။
6. Normalized output ကို ပြီးနောက် names, brands, numbers, URLs, IDs နှင့် meaning preservation ကို ပြန်စစ်ပါ။
7. Grammar/style issue တွေ့လျှင် Grammar Checker သို့မဟုတ် Style Guide သို့ route လုပ်ပါ။

## Guardrails

- Zawgyi/Unicode detection score ကို absolute proof မယူဆရ။
- Mixed encoding ကို အလိုအလျောက် အကုန်ပြောင်းမလုပ်ရ။
- မြန်မာစာ word boundary မသိဘဲ space ထည့်/ဖယ် မလုပ်ရ။
- Brand names, product codes, URLs, emails, prices, dates နှင့် user-protected text မပြင်ရ။
- Emoji၊ slang နှင့် intentional punctuation များကို အလိုအလျောက် မဖျက်ရ။
- Normalizer သည် encoding ကိုသာ စစ်ပြီး စာသားအဓိပ္ပာယ်ကို မပြန်ရေးရ။

## References

- [Normalization rules](references/normalization-rules.md)
- [Output format](references/output-format.md)
- [Before/after example](examples/before-after-01.md)
