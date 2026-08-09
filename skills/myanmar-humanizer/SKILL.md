---
name: myanmar-humanizer
description: မြန်မာဘာသာဖြင့် AI ရေးသားထားသလိုဖြစ်နေသော စာသားများကို မူရင်းအဓိပ္ပာယ်၊ tone နှင့် ရည်ရွယ်ချက်မပျက်စေဘဲ သဘာဝကျအောင် ပြန်လည်ရေးသားရန် အသုံးပြုသည်။
---

# myanmar-humanizer

## Scope

ဤ Skill သည် Standard Burmese social, sales, business နှင့် educational content များကို conservative နည်းလမ်းဖြင့် သဘာဝကျအောင် ပြန်လည်ရေးသားရန် အသုံးပြုသည်။ Pattern တစ်ခုတည်းဖြင့် စာသားကို AI ဟု မဆုံးဖြတ်ရ။

## Workflow

1. Target audience၊ channel နှင့် content type ကို သတ်မှတ်ပါ။ မသိလျှင် တိုတိုမေးပါ။
2. မူရင်း tone၊ formality နှင့် ရည်ရွယ်ချက်ကို ဖော်ထုတ်ပါ။
3. [patterns.md](references/patterns.md) ထဲက heuristic patterns များကို စစ်ပါ။
4. Facts, numbers, names, URLs, product identifiers, brand terms နှင့် CTA ကို မှတ်သားပါ။
5. မူရင်း tone အတွင်းသာ conservative rewrite ပြုလုပ်ပါ။
6. [output-format.md](references/output-format.md) အတိုင်း detected patterns၊ natural version နှင့် change summary ကို ပြပါ။
7. Meaning preservation checklist ကို ပြန်စစ်ပါ။

## Guardrails

- AI-generated ဟု အတည်ပြုသလို မပြောရ။ AI ဆန်နိုင်သော pattern ဟုသာ ဖော်ပြရ။
- မူရင်းအဓိပ္ပာယ်၊ facts၊ numbers၊ names၊ URLs နှင့် brand terms မပြောင်းရ။
- User တောင်းဆိုခြင်းမရှိဘဲ CTA အသစ်၊ claim အသစ် သို့မဟုတ် marketing promise မထည့်ရ။
- Slang၊ conversational phrasing နှင့် intentional repetition ကို အလိုအလျောက် မဖျက်ရ။
- စာသားတိုလွန်းလျှင် analysis ကန့်သတ်ထားကြောင်း ပြရ။
- မသေချာသောပြင်ဆင်ချက်ကို context_dependent သို့မဟုတ် optional_style ဟု ခွဲခြားပြရ။

## References

- [AI-style heuristic patterns](references/patterns.md)
- [Output format and preservation guard](references/output-format.md)
- [Before/after example](examples/before-after-01.md)
