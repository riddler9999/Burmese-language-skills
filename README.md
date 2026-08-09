# Burmese Language Skills

မြန်မာဘာသာအတွက် AI Agent Skills Collection တစ်ခုဖြစ်သည်။

ဤ repository သည် မြန်မာစာရေးသားမှုကို စစ်ဆေးခြင်း၊ ပြန်လည်ရေးသားခြင်း၊ Style တစ်သမတ်တည်းဖြစ်အောင် ထိန်းသိမ်းခြင်းနှင့် Unicode/Zawgyi စာသား normalization ပြုလုပ်ခြင်းတို့အတွက် Agent Skills များကို စနစ်တကျ တည်ဆောက်ရန် ရည်ရွယ်သည်။

## Planned Skills

- myanmar-humanizer — AI ရေးသားထားသလိုဖြစ်နေသော မြန်မာစာကို သဘာဝကျအောင် ပြန်ရေးသားရန်
- myanmar-grammar-checker — စာလုံးပေါင်း၊ သဒ္ဒါ၊ spacing နှင့် punctuation စစ်ဆေးရန်
- myanmar-style-guide — Document type နှင့် brand voice အလိုက် ရေးဟန်တစ်သမတ်တည်းဖြစ်အောင် စစ်ဆေးရန်
- myanmar-text-normalizer — Unicode/Zawgyi နှင့် Myanmar text encoding ဆိုင်ရာ normalization ပြုလုပ်ရန်

## Design Principles

1. အဓိပ္ပာယ်နှင့် မူရင်းရည်ရွယ်ချက်ကို ထိန်းသိမ်းရန်
2. သေချာသောအမှားနှင့် စတိုင်အကြံပြုချက်ကို ခွဲခြားပြရန်
3. Native Burmese usage နှင့် authoritative sources နှစ်မျိုးလုံးကို အသုံးပြုရန်
4. Context မရှိဘဲ စာရေးဟန်ကို အလွန်အကျွံ ပြင်ဆင်ခြင်းကို ရှောင်ရန်
5. Rules, examples နှင့် evaluation cases များကို သီးခြားထိန်းသိမ်းရန်

## Repository Structure

- skills/ — Agent Skills များ
- research/ — Source, taxonomy နှင့် evaluation planning
- tests/ — Skill တစ်ခုချင်းစီအတွက် evaluation cases

## Project Status

လက်ရှိအဆင့်သည် repository structure နှင့် research foundation တည်ဆောက်နေသည့်အဆင့်ဖြစ်သည်။ Skill အပြည့်အစုံ implementation မစတင်မီ rules, corpus, annotation taxonomy နှင့် evaluation set များကို သတ်မှတ်မည်။

## License

MIT License
