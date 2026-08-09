# Evaluation Plan

## Evaluation Goals

Skill တစ်ခုသည် စာသားကို ပိုသဘာဝကျအောင် ပြင်နိုင်ရုံသာမက မူရင်းအဓိပ္ပာယ်၊ tone၊ facts နှင့် user intent ကို မပျက်စေရန် စစ်ဆေးမည်။

## Test Categories

- Short Burmese sentences
- Social media captions
- TikTok scripts
- Sales replies
- Business documents
- Technical documents
- Formal Burmese
- Conversational Burmese
- Burmese-English mixed text
- Unicode/Zawgyi edge cases
- Intentional slang and brand terms
- Already-natural text

## Evaluation Dimensions

- Naturalness rating by native reviewers
- Meaning preservation for facts, numbers, names, links, identifiers, intent, and CTA
- Tone preservation for formal, friendly, sales, educational, and conversational text
- Over-correction rate for slang, brand terms, repetition, and channel-specific style
- Correction quality and source alignment

## Minimum Human-reviewed Set

Skill တစ်ခုချင်းစီအတွက် အနည်းဆုံး case ၈၀ ပါဝင်ရမည်။

- 20 clear errors
- 20 context-dependent cases
- 20 already-correct examples
- 10 intentional informal/brand examples
- 10 Burmese-English mixed or encoding edge cases

Case တစ်ခုချင်းစီတွင် input, expected behavior, acceptable alternatives, forbidden changes, label နှင့် reviewer note ပါဝင်ရမည်။

## Pass Criteria for the Humanizer MVP

- Meaning-preservation critical cases တွင် 100% pass
- Brand terms, numbers, URLs နှင့် proper names မပျက်စေရ
- Native reviewers အနည်းဆုံး ၂ဦး၏ သဘာဝကျမှု rating ပျမ်းမျှ 4/5 ရရှိရ
- Intentional informal examples တွင် မလိုအပ်ဘဲ formalize မလုပ်ရ
- Output တွင် detected pattern, revised text နှင့် change summary ပါရ
- မသေချာသော case များကို context_dependent ဟု ပြရ

## Evaluation Notes

Published Burmese NLP benchmarks များသည် general NLU/NLG tasks အတွက် အထောက်အကူဖြစ်သော်လည်း social-media humanization အတွက် တိုက်ရိုက် gold standard မဟုတ်ပါ။ ဤ project သည် native-reviewed, task-specific evaluation set ကို သီးခြားတည်ဆောက်ရမည်။
