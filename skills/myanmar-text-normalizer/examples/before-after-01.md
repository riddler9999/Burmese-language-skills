# Example 01 — Detection Before Conversion

## Input

စာထဲမှာ Unicode နဲ့ Zawgyi စာသား ရောနေတယ်။

## Analysis

- Encoding status: mixed or unknown until detector checks each span
- Grammar correction: not performed
- Conversion: not applied automatically

## Safe Output

ဒီစာသားမှာ encoding ရောနှောနေနိုင်ပါတယ်။ မူရင်းစာသားကို မပြောင်းဘဲ ဘယ်အပိုင်းတွေကို Unicode သို့ ပြောင်းလိုသလဲ အတည်ပြုပေးပါ။

## Preservation Note

Normalizer သည် encoding ကိုသာ စစ်ဆေးသည်။ စာလုံးပေါင်း၊ tone နှင့် grammar ကို မပြင်ပါ။
