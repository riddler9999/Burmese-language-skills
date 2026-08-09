# Burmese Error and Style Taxonomy

Taxonomy ၏ အဓိကရည်ရွယ်ချက်မှာ စံအမှား၊ အကြံပြုချက် နှင့် အခြေအနေအလိုက် လက်ခံနိုင်သော အသုံးအနှုန်းကို မရောထွေးစေရန် ဖြစ်သည်။

## Correctness Labels

### SPELLING_ERROR

စာလုံးပေါင်း သို့မဟုတ် သတ်ပုံတွင် အဓိပ္ပာယ်/စံသတ်မှတ်ချက်ကို ချိုးဖောက်သော အမှား။ အထောက်အထားခိုင်လုံပါက ပြင်ပါ။ Slang, brand names, intentional phonetic writing အတွက် မသုံးရ။

### GRAMMAR_ERROR

ဝါကျဖွဲ့စည်းပုံ၊ particle၊ tense/aspect သို့မဟုတ် အဓိပ္ပာယ်ဆက်နွယ်မှု မကိုက်ညီသော အမှား။ Context ရှိမှ ပြင်ပါ။

### SPACING_ERROR

Burmese phrase spacing, punctuation spacing သို့မဟုတ် မလိုအပ်သော whitespace ပြဿနာ။ Word boundary အဖြစ် space ကို မယူဆဘဲ phrase readability ကို စဉ်းစားပါ။

### PUNCTUATION_ERROR

မြန်မာ punctuation၊ quotation၊ list နှင့် sentence ending အသုံးပြုမှု မကိုက်ညီခြင်း။ Channel/document type အလိုက် ပြင်ပါ။

## Style and Generation Labels

### TRANSLATIONESE

English သို့မဟုတ် အခြားဘာသာစကားမှ တိုက်ရိုက်ပြန်ထားသလို ဖြစ်နေသော structure သို့မဟုတ် phrase။ မူရင်းအဓိပ္ပာယ်နှင့် technical terms မပျက်စေဘဲ Burmese-native alternative တင်ပြပါ။

### AI_STYLE

အလွန်တူညီသော sentence rhythm၊ အထွေထွေပြောဆိုချက်များ၊ အကြောင်းအရာမတိုးသော ဆက်စပ်စကားများ သို့မဟုတ် context မကိုက်သော formal phrasing များ။ AI detection claim မပြုလုပ်ဘဲ AI ဆန်နိုင်သော pattern အဖြစ်သာ ပြောပါ။

### TONE_INCONSISTENCY

Formal, polite, conversational, sales, educational စသော tone များ အတွင်း/အပြင် မကိုက်ညီခြင်း။ User သတ်မှတ်ထားသော tone ကို ဦးစားပေးပါ။

### BRAND_TERM

Brand name, product name, username, technical identifier သို့မဟုတ် user-defined preferred term။ Spelling/grammar rule နှင့် မတိုက်ဆိုင်လျှင် မပြင်ပါနှင့်။

### NONSTANDARD_BUT_ACCEPTABLE

စံစာရေးနည်းမဟုတ်သော်လည်း social media၊ conversation၊ slang သို့မဟုတ် brand voice အရ ရည်ရွယ်ချက်ရှိရှိ အသုံးပြုထားသော expression။ မလိုအပ်ဘဲ မပြင်ပါနှင့်။

### UNICODE_ZAWGYI_ISSUE

Encoding၊ character order၊ Zawgyi-like sequence သို့မဟုတ် zero-width character ပြဿနာ။ Normalizer skill သို့ route လုပ်ပါ။ Grammar error အဖြစ် မတင်ပြပါနှင့်။

## Confidence Levels

- certain_error — rule/evidence ခိုင်လုံပြီး context မပြောင်းလဲစေသော အမှား
- recommended_change — ပိုကောင်းသော standard/style ရှိသော်လည်း မဖြစ်မနေအမှားမဟုတ်
- optional_style — channel/brand preference အပေါ် မူတည်သော အကြံပြုချက်
- context_dependent — context မရှိလျှင် မဆုံးဖြတ်နိုင်သော case

## Annotation Schema

Annotation တစ်ခုချင်းစီတွင် id, input, label, span_or_phrase, proposed_output, confidence, rationale, source, preserve နှင့် reviewer_notes fields ပါဝင်ရမည်။
