# Cross-skill Integration Fixtures

ဤ fixtures များသည် Skill တစ်ခုချင်းစီ၏ boundary နှင့် pipeline behavior ကို စစ်ရန်ဖြစ်သည်။

## Case I-001 — Messenger Sales Text

Input: "မင်္ဂလာပါရှင် ဒီနေ့ dress အသစ်ရောက်ပါတယ်။ ၃ထည်ယူရင် discount ရှိပါတယ်နော်။ order တင်ချင်ရင် ဒီ link ကိုနှိပ်ပါ။"

Expected routing:
1. Text Normalizer — encoding status only
2. Style Guide — sales tone and terminology
3. Grammar Checker — clear spelling/punctuation only
4. Humanizer — only if the user requests a natural rewrite

Must preserve: product term, quantity, discount, and URL.

## Case I-002 — AI-looking Social Caption

Input: "ယနေ့ခေတ်တွင် AI Automation နည်းပညာသည် လျင်မြန်စွာတိုးတက်လျက်ရှိပြီး လုပ်ငန်းနယ်ပယ်အသီးသီးအတွက် အရေးပါသောအခန်းကဏ္ဍမှ ပါဝင်လျက်ရှိပါသည်။"

Expected routing:
- Humanizer first
- Grammar Checker second
- Style Guide if a channel tone is specified

Must not add: new facts, claims, CTA, or hashtags.

## Case I-003 — Mixed Encoding

Input: "Unicode နှင့် Zawgyi စာသားများ ရောနှောနေသော message"

Expected routing:
- Text Normalizer only

Must not do: grammar rewrite or automatic low-confidence conversion.

## Case I-004 — Technical Document

Input: "API version 2.1 က order ID ကို database ထဲမှာ သိမ်းပေးပါတယ်။"

Expected routing:
- Style Guide for technical terminology
- Grammar Checker for clear grammar/punctuation

Must preserve: API, version 2.1, order ID, database.

## Case I-005 — Already Natural Conversation

Input: "အစ်ကို ဒီအရောင်လေးက လက်ကျန်နည်းနေပြီနော်။ လိုချင်ရင် ပြောပေးပါ။"

Expected routing:
- No Humanizer rewrite unless requested
- Optional Style Guide suggestion only

Must preserve: friendly sales tone.
