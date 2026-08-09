# Research Sources

ဤ repository သည် Standard Burmese writing assistance အတွက် source များကို စုစည်းထားသည်။ Myanmar script ကို အသုံးပြုသော အခြားဘာသာစကားများနှင့် Burmese ကို မရောထွေးရန်လိုသည်။

## Tier A — Technical and Encoding Standards

### Unicode Consortium

- [Myanmar Scripts and Languages FAQ](https://www.unicode.org/faq/myanmar.html) — Myanmar Unicode block သည် Burmese အပြင် Mon, Shan, Karen, Palaung နှင့် အခြားဘာသာစကားများအတွက်လည်း အသုံးပြုနိုင်ကြောင်း ဖော်ပြထားသည်။ Script-level validation ကို Burmese spelling validation အဖြစ် မသုံးရ။
- [Representing Myanmar in Unicode, UTN #11](https://www.unicode.org/notes/tn11/UTN11_3.pdf) — Myanmar script encoding, canonical order နှင့် language-specific validation ၏ ကန့်သတ်ချက်များအတွက် အခြေခံ technical reference ဖြစ်သည်။

### Technical Implication

Unicode sequence မှန်ခြင်းသည် စာလုံးပေါင်းမှန်ခြင်းနှင့် မတူပါ။ Normalizer သည် encoding/sequence ပြဿနာကို စစ်ပြီး Grammar Checker သည် Burmese language rule ကို သီးခြားစစ်ရမည်။

## Tier B — Burmese NLP Research

- [A Rule-based Syllable Segmentation of Myanmar Text](https://aclanthology.org/I08-3010.pdf) — မြန်မာစာတွင် စာလုံးများကို word-by-word space မခြားဘဲ phrase-level spacing အသုံးများကြောင်းနှင့် syllable segmentation အခက်အခဲများကို ရှင်းပြထားသည်။
- [Burmese Speech Corpus, Finite-State Text Normalization and Grapheme-to-Phoneme Conversion](https://aclanthology.org/2020.lrec-1.777.pdf) — Burmese text normalization အတွက် finite-state grammars နှင့် open corpus ကို တင်ပြထားသည်။
- [Comparison of Grapheme-to-Phoneme Conversion Methods for Myanmar](https://aclanthology.org/W16-3702.pdf) — Myanmar text ၏ syllable/word boundary နှင့် Burmese linguistic structure ကို လေ့လာရန် အသုံးပြုနိုင်သည်။
- [BURMESE-SAN: Burmese NLP Benchmark](https://aclanthology.org/anthology-files/anthology-files/pdf/lrec/2026.lrec-main.16.pdf) — Burmese LLM evaluation အတွက် native-speaker verification နှင့် generation tasks ပါဝင်သည့် benchmark ဖြစ်သည်။

## Tier C — Corpora and Usage Evidence

- [Myanmar Language Dataset Collection](https://github.com/chuuhtetnaing/myanmar-language-dataset-collection) — ရှာဖွေတွေ့ရှိနိုင်သော Burmese speech/text dataset များအတွက် directory အဖြစ် အသုံးပြုမည်။ Dataset တစ်ခုချင်းစီ၏ license နှင့် quality ကို သီးခြားစစ်ရမည်။
- [Myanmar Written Corpus](https://huggingface.co/datasets/freococo/myanmar-written-corpus) — Written Burmese corpus အဖြစ် exploratory analysis အတွက် အသုံးပြုနိုင်သည်။ Production rule အဖြစ် မသတ်မှတ်မီ sampling နှင့် human review လိုအပ်သည်။
- [Asian Language Treebank / Myanmar Corpora Overview](https://aclanthology.org/2023.wat-1.1.pdf) — Myanmar-English corpus များနှင့် tokenization/segmentation ဆိုင်ရာ background ကို လေ့လာရန် အသုံးပြုမည်။

## Evidence Policy

Source မတူညီမှုရှိပါက အောက်ပါအစီအစဉ်အတိုင်း ဆုံးဖြတ်မည်။

1. User/brand-specific rule
2. Target document type နှင့် context
3. Burmese language authority သို့မဟုတ် primary linguistic research
4. Native-writer usage evidence
5. Model preference

မသေချာသော case များကို အလိုအလျောက် အမှားဟု မသတ်မှတ်ဘဲ context_dependent သို့မဟုတ် recommended_change ဟု မှတ်တမ်းတင်မည်။

## Known Gaps

- Publicly accessible, comprehensive Burmese spelling/grammar authority တစ်ခုတည်း မတွေ့ရှိသေးပါ။
- AI-generated Burmese humanizer pattern များအတွက် Burmese-specific published study မလုံလောက်သေးပါ။
- Social media၊ sales နှင့် business writing အတွက် native-reviewed corpus ကို ကိုယ်ပိုင်တည်ဆောက်ရန် လိုအပ်သည်။
