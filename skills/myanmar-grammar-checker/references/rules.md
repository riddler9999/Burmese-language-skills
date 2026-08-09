# Burmese Grammar Checker Rules

ဤ rules များသည် MVP scope ဖြစ်ပြီး Burmese grammar အားလုံးကို အပြီးသတ်ဖုံးလွှမ်းခြင်းမဟုတ်ပါ။ Rule တစ်ခုချင်းစီကို confidence နှင့် context အလိုက် အသုံးပြုရမည်။

## G1 — Orthography and Confusables

Corpus/source အထောက်အထားခိုင်လုံသော spelling confusion များကို အရင်စစ်ပါ။ ဥပမာများကို source corpus နှင့် မူရင်းစကားလုံး context နှစ်ခုလုံးဖြင့် အတည်ပြုရမည်။

- အက္ခရာပုံစံမှား
- အသံတူသော်လည်း သတ်ပုံကွဲသော စကားလုံး
- keyboard typo နှင့် character sequence error

မသေချာလျှင် correction တိုက်ရိုက်မလုပ်ဘဲ အကြံပြုချက်အဖြစ် ပြပါ။

## G2 — Negation and Verb Context

မ၊ မ…ဘူး၊ မ…ပါ၊ မ…နိုင် စသော အငြင်းပယ်ပုံစံများကို စာကြောင်းတစ်ခုလုံး၏ verb phrase နှင့်အတူ စစ်ပါ။ မ particle တစ်ခုကို တွေ့ရုံဖြင့် အမှားဟု မသတ်မှတ်ရ။

## G3 — Particles and Register

ပဲ၊ သာ၊ တောင်၊ ရယ်၊ ပါ၊ လည်း စသော particles များသည် spoken/formal context အလိုက် အဓိပ္ပာယ်နှင့် tone ပြောင်းနိုင်သည်။ Spoken expression ကို formal writing အဖြစ် အလိုအလျောက် မပြင်ရ။

## G4 — Phrase Spacing

မြန်မာစာ space သည် English လို word boundary မဟုတ်နိုင်ပါ။ Phrase readability, punctuation နှင့် document type ကို စဉ်းစားပါ။ စာလုံးတိုင်းကြား space ထည့်ခြင်း သို့မဟုတ် space အားလုံးဖယ်ခြင်းကို မလုပ်ရ။

## G5 — Punctuation

မြန်မာစာကြောင်းအဆုံး၊ list၊ quotation နှင့် emoji အနီး punctuation ကို channel အလိုက် စစ်ပါ။ Social media တွင် intentional punctuation ကို optional_style အဖြစ်သာ ပြပါ။

## G6 — Protected Spans

အောက်ပါအရာများကို default အနေဖြင့် မပြင်ရ။

- လူ/နေရာ/အဖွဲ့အစည်းအမည်
- Brand နှင့် product name
- URL, email, username
- API, code, ID, version, order number
- User က မပြင်ရန် သတ်မှတ်ထားသော စာသား

## Correction Priority

1. certain spelling/sequence error
2. clear grammar structure error
3. phrase spacing issue with strong context
4. punctuation recommendation
5. optional style suggestion
