# Text Normalizer Output Format

## Detection Report

- Encoding status: Unicode, Zawgyi-like, mixed, or unknown
- Confidence: high, medium, low
- Affected spans
- Invisible characters found
- Whitespace/punctuation findings

## Normalized Version

User request သို့မဟုတ် high-confidence policy အရ ပြောင်းလဲရန်ခွင့်ရှိမှသာ normalized text ကို ပြပါ။

## Preservation Report

- Original content retained
- Names and brands retained
- Numbers, prices, dates, URLs, IDs retained
- Meaning not interpreted or rewritten

## Low-confidence Mode

Low-confidence သို့မဟုတ် mixed input ဖြစ်ပါက conversion မလုပ်ဘဲ detected spans နှင့် next action ကို ပြပါ။
