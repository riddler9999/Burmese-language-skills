# Myanmar Text Normalization Rules

ဤ rules များသည် encoding နှင့် text hygiene အတွက်သာ ဖြစ်ပြီး Burmese grammar correction မလုပ်ပါ။

## N1 — Encoding Detection

Input တစ်ခုလုံးကို Unicode, Zawgyi-like, mixed, or unknown ဟု ခွဲခြားပါ။ Detector score သည် probability ဖြစ်ပြီး absolute proof မဟုတ်ကြောင်း ဖော်ပြပါ။

## N2 — Zawgyi Conversion

Zawgyi-like input ကို Unicode သို့ ပြောင်းရန် user က conversion တောင်းဆိုထားခြင်း သို့မဟုတ် high-confidence detection ဖြစ်ခြင်းကို လိုအပ်ချက်အဖြစ် သတ်မှတ်ပါ။ Original text ကို မပျောက်စေရန် before/after နှစ်မျိုးထားပါ။

## N3 — Mixed Encoding

စာကြောင်းတစ်ကြောင်း သို့မဟုတ် message တစ်ခုအတွင်း Unicode/Zawgyi ရောနေပါက chunk-level detection လုပ်ရန် ကြိုးစားပါ။ မသေချာလျှင် automatic conversion မလုပ်ဘဲ problematic span ကို ပြပါ။

## N4 — Character Order

Myanmar consonant, vowel, medials, asat, virama နှင့် combining marks များ၏ character order ကို စစ်ပါ။ Visual rendering ကောင်း/မကောင်းကို encoding validity တစ်ခုတည်းအဖြစ် မသတ်မှတ်ရ။

## N5 — Zero-width Characters

မလိုအပ်သော zero-width space, zero-width non-joiner, zero-width joiner နှင့် invisible control characters များကို report လုပ်ပါ။ Remove မလုပ်မီ protected text နှင့် intentional formatting ကို စစ်ပါ။

## N6 — Whitespace

Leading/trailing whitespace၊ repeated spaces၊ newline နှင့် punctuation အနီး whitespace ကို normalize လုပ်နိုင်သည်။ မြန်မာစာ word boundary များကို မသိဘဲ whitespace ထည့်/ဖယ် မလုပ်ရ။

## N7 — Punctuation

ထပ်နေသော punctuation ကို report လုပ်ပါ။ Social content တွင် intentional emphasis ဖြစ်နိုင်သော !!!, ??? နှင့် emoji repetition များကို optional_style အဖြစ်သာ ပြပါ။

## N8 — Protected Content

Names, brands, product codes, URLs, emails, API/code, prices, dates နှင့် user-protected spans များကို conversion မဟုတ်သော rewrite ဖြင့် မပြင်ရ။

## Safety Order

1. Detect
2. Preserve original
3. Show confidence and affected spans
4. Ask or apply only requested conversion
5. Validate output encoding
6. Route grammar/style issues to other Skills
