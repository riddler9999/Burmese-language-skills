# Burmese Language Skills

မြန်မာဘာသာအတွက် AI Agent Skills Collection တစ်ခုဖြစ်သည်။

ဤ repository သည် မြန်မာစာရေးသားမှုကို စစ်ဆေးခြင်း၊ ပြန်လည်ရေးသားခြင်း၊ Style တစ်သမတ်တည်းဖြစ်အောင် ထိန်းသိမ်းခြင်းနှင့် Unicode/Zawgyi စာသား normalization ပြုလုပ်ခြင်းတို့အတွက် Agent Skills များကို စနစ်တကျ တည်ဆောက်ရန် ရည်ရွယ်သည်။

## Planned Skills

- myanmar-humanizer — AI ရေးသားထားသလိုဖြစ်နေသော မြန်မာစာကို သဘာဝကျအောင် ပြန်ရေးသားရန်
- myanmar-grammar-checker — စာလုံးပေါင်း၊ သဒ္ဒါ၊ spacing နှင့် punctuation စစ်ဆေးရန်
- myanmar-style-guide — Document type နှင့် brand voice အလိုက် ရေးဟန်တစ်သမတ်တည်းဖြစ်အောင် စစ်ဆေးရန်
- myanmar-text-normalizer — Unicode/Zawgyi နှင့် Myanmar text encoding ဆိုင်ရာ normalization ပြုလုပ်ရန်

## Current Progress

Research foundation၊ Skill MVP workflows လေးခုနှင့် machine-readable benchmark suite ကို တည်ဆောက်ထားသည်။ Benchmark တွင် Skill တစ်ခုစီအတွက် concrete cases ၂၀ ခုနှင့် cross-skill integration cases ၅ ခု၊ စုစုပေါင်း ၈၅ ခု ပါဝင်သည်။ Humanizer rules များသည် Burmese-specific published AI-writing research မလုံလောက်သေးသဖြင့် empirical heuristics အဖြစ်သာ သတ်မှတ်ထားသည်။

## Repository Structure

- skills/ — Agent Skills များ
- research/ — Source, taxonomy, annotation နှင့် evaluation planning
- tests/ — Skill တစ်ခုချင်းစီအတွက် evaluation cases၊ JSONL benchmark နှင့် cross-skill integration fixtures
- scripts/ — Benchmark fixture validator နှင့် structured-output evaluator
- docs/superpowers/plans/ — Implementation plans

## Design Principles

1. အဓိပ္ပာယ်နှင့် မူရင်းရည်ရွယ်ချက်ကို ထိန်းသိမ်းရန်
2. သေချာသောအမှားနှင့် စတိုင်အကြံပြုချက်ကို ခွဲခြားပြရန်
3. Native Burmese usage နှင့် authoritative sources နှစ်မျိုးလုံးကို အသုံးပြုရန်
4. Context မရှိဘဲ စာရေးဟန်ကို အလွန်အကျွံ ပြင်ဆင်ခြင်းကို ရှောင်ရန်
5. Rules, examples နှင့် evaluation cases များကို သီးခြားထိန်းသိမ်းရန်

## Project Status

Version 0.2.0 အဖြစ် Research foundation၊ Humanizer, Grammar Checker, Style Guide, Text Normalizer MVP များနှင့် ၈၅-case benchmark suite ကို တည်ဆောက်ထားသည်။

## License

MIT License
