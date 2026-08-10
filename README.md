# Burmese Language Skills

မြန်မာစာကို စစ်ဆေးခြင်း၊ သဘာဝကျအောင် ပြန်လည်ရေးသားခြင်း၊ ရေးဟန်တစ်သမတ်တည်းဖြစ်အောင် ထိန်းခြင်းနှင့် Unicode/Zawgyi ဆိုင်ရာ text hygiene စစ်ဆေးခြင်းတို့အတွက် အသုံးပြုနိုင်သော AI Agent Skills စုစည်းမှုဖြစ်သည်။

လက်ရှိ `v0.2.0` တွင် သီးခြားတာဝန်ရှိသော Skills လေးခု၊ research foundation၊ machine-readable benchmark cases ၈၅ ခုနှင့် deterministic validation scripts များ ပါဝင်သည်။

> **လက်ရှိအခြေအနေ — Research MVP:** လက်တွေ့စမ်းသပ်နိုင်သော်လည်း မြန်မာစာသဒ္ဒါနှင့် encoding ပြဿနာအားလုံးကို အပြီးသတ်ဖုံးလွှမ်းထားခြင်း မရှိသေးပါ။

## ပါဝင်သော Skills

| Skill | အသုံးပြုရန် | မလုပ်သင့်သောအရာ |
|---|---|---|
| [`myanmar-text-normalizer`](skills/myanmar-text-normalizer/SKILL.md) | Unicode/Zawgyi-like encoding၊ character order၊ invisible characters၊ whitespace နှင့် punctuation hygiene စစ်ရန် | သဒ္ဒါ၊ tone သို့မဟုတ် အဓိပ္ပာယ်ကို ပြန်မရေးရ |
| [`myanmar-grammar-checker`](skills/myanmar-grammar-checker/SKILL.md) | စာလုံးပေါင်း၊ သဒ္ဒါ၊ phrase spacing နှင့် punctuation စစ်ရန် | မသေချာသောအသုံးအနှုန်းကို certain error အဖြစ် မပြင်ရ |
| [`myanmar-style-guide`](skills/myanmar-style-guide/SKILL.md) | Document type၊ audience နှင့် brand voice အလိုက် tone၊ terminology နှင့် formatting ညှိရန် | Grammar error နှင့် style preference ကို မရောရ |
| [`myanmar-humanizer`](skills/myanmar-humanizer/SKILL.md) | မူရင်းအဓိပ္ပာယ်နှင့် tone မပျက်စေဘဲ မြန်မာစာကို သဘာဝကျအောင် ပြန်ရေးရန် | Claim၊ CTA၊ ဈေးနှုန်း၊ နာမည် သို့မဟုတ် fact အသစ် မထည့်ရ |

## အဓိကစည်းမျဉ်းများ

- မူရင်းအဓိပ္ပာယ်၊ ရည်ရွယ်ချက်နှင့် tone ကို ထိန်းသိမ်းရန်
- နာမည်၊ brand၊ URL၊ ID၊ product code၊ date၊ price နှင့် number များကို protected content အဖြစ်ထားရန်
- `certain_error`၊ `recommended_change`၊ `optional_style` နှင့် `context_dependent` ကို သီးခြားခွဲရန်
- မြန်မာစာ space ကို English word boundary အဖြစ် မယူဆရန်
- Spoken Burmese၊ slang၊ emoji နှင့် social-media punctuation ကို context မရှိဘဲ formalize မလုပ်ရန်
- မသေချာသောအခါ အတင်းပြင်မည့်အစား limitation ကိုပြရန် သို့မဟုတ် context မေးရန်

## စတင်အသုံးပြုခြင်း

Repository ကို clone လုပ်ပါ။

```bash
git clone https://github.com/riddler9999/Burmese-language-skills.git
cd Burmese-language-skills
```

Codex တွင် local Skills အဖြစ်အသုံးပြုလိုပါက လိုအပ်သော Skill folder များကို `~/.codex/skills/` ထဲသို့ ကူးထည့်နိုင်သည်။

```bash
mkdir -p ~/.codex/skills
cp -R skills/myanmar-* ~/.codex/skills/
```

အခြား AI Agent platform များတွင် အသုံးပြုပါက ထို platform သတ်မှတ်ထားသော Skill သို့မဟုတ် instruction directory ထဲသို့ folder တစ်ခုချင်းစီ ကူးထည့်ပါ။

## အသုံးပြုပုံနမူနာများ

### စာလုံးပေါင်းနှင့် သဒ္ဒါစစ်ရန်

```text
Use $myanmar-grammar-checker to check this Burmese text.
သေချာသောအမှားနဲ့ စတိုင်အကြံပြုချက်ကို သီးခြားခွဲပြပါ။
```

### Social caption ကို သဘာဝကျအောင် ပြန်ရေးရန်

```text
Use $myanmar-humanizer to rewrite this Facebook caption naturally.
မူရင်း claim၊ နာမည်၊ number နဲ့ CTA ကို မပြောင်းပါနဲ့။
```

### Technical document ရဲ့ style ညှိရန်

```text
Use $myanmar-style-guide to make this technical document consistent.
API၊ version၊ ID နဲ့ code terms တွေကို မပြောင်းပါနဲ့။
```

### Unicode/Zawgyi နှင့် invisible characters စစ်ရန်

```text
Use $myanmar-text-normalizer to inspect this text.
Mixed encoding ဖြစ်ရင် အလိုအလျောက်မပြောင်းဘဲ affected spans ကိုပြပါ။
```

## Skill ရွေးချယ်ပုံ

Task တိုင်းအတွက် Skills လေးခုလုံးကို မဖြစ်မနေ run ရန်မလိုပါ။

| လိုအပ်ချက် | အရင်သုံးရန် | လိုအပ်မှ ဆက်သုံးရန် |
|---|---|---|
| Encoding မသေချာခြင်း | Text Normalizer | Grammar Checker |
| စာလုံးပေါင်း/သဒ္ဒါစစ်ခြင်း | Grammar Checker | Style Guide |
| Document ရေးဟန်မညီခြင်း | Style Guide | Grammar Checker |
| AI ဆန်နိုင်သော စာကို သဘာဝကျစေခြင်း | Humanizer | Grammar Checker၊ Style Guide |
| သဘာဝကျပြီးသား conversational text | ပြန်မရေးရန် | လိုအပ်မှသာ Style Guide သုံးရန် |

Skill တစ်ခု၏ scope ပြင်ပပြဿနာကို တွေ့ပါက စာသားကို အတင်းပြင်မည့်အစား သက်ဆိုင်ရာ Skill သို့ route လုပ်ရမည်။

## Benchmark နှင့် Tests

`tests/benchmark/` တွင် concrete JSONL fixtures စုစုပေါင်း ၈၅ ခု ပါဝင်သည်။

| အုပ်စု | Cases |
|---|---:|
| Text Normalizer | ၂၀ |
| Grammar Checker | ၂၀ |
| Style Guide | ၂၀ |
| Humanizer | ၂၀ |
| Cross-skill integration | ၅ |

Fixture တစ်ခုချင်းစီတွင် input၊ expected labels၊ allowed decisions၊ acceptable alternatives၊ protected text၊ forbidden additions၊ confidence၊ source နှင့် review status ပါဝင်သည်။

### Benchmark fixtures စစ်ရန်

```bash
python scripts/validate_benchmark.py \
  tests/benchmark/normalizer.jsonl \
  tests/benchmark/grammar-checker.jsonl \
  tests/benchmark/style-guide.jsonl \
  tests/benchmark/humanizer.jsonl \
  tests/benchmark/integration.jsonl
```

### Regression tests run ရန်

```bash
python -m unittest discover -s tests -p 'test_*.py' -v
```

### Structured model outputs စစ်ရန်

Model output ကို JSONL ပုံစံဖြင့် သိမ်းပါ။

```json
{"id":"H-001","decision":"rewrite","labels":["H1","H6"],"output":"ပြင်ဆင်ပြီးစာသား"}
```

ပြီးနောက် evaluator ကို run ပါ။

```bash
python scripts/evaluate_outputs.py \
  tests/benchmark/humanizer.jsonl \
  outputs.jsonl
```

Evaluator သည် allowed decision၊ expected labels၊ protected tokens နှင့် forbidden additions ကို deterministic စစ်ပေးသည်။ Naturalness နှင့် context-dependent judgment များကို native reviewers ဖြင့် သီးခြားစစ်ရန်လိုသည်။

## Repository ဖွဲ့စည်းပုံ

- [`skills/`](skills/) — Skill instructions၊ references၊ examples နှင့် agent metadata
- [`research/`](research/) — Sources၊ taxonomy၊ annotation schema နှင့် evaluation plan
- [`tests/`](tests/) — Evaluation cases၊ benchmark fixtures နှင့် integration tests
- [`scripts/`](scripts/) — Fixture validator နှင့် structured-output evaluator
- [`docs/superpowers/plans/`](docs/superpowers/plans/) — Research နှင့် implementation plans

## လက်ရှိကန့်သတ်ချက်များ

- Text Normalizer တွင် deterministic Zawgyi detector/converter engine မပါသေးပါ။
- Grammar Checker rules များသည် MVP scope ဖြစ်ပြီး မြန်မာသဒ္ဒါအားလုံးကို မဖုံးလွှမ်းသေးပါ။
- Humanizer patterns များသည် AI-generated text ကို သက်သေပြသည့် detector မဟုတ်ဘဲ empirical heuristics များသာဖြစ်သည်။
- Benchmark cases အများစုသည် draft ဖြစ်ပြီး native-review process ဆက်လုပ်ရန်လိုသည်။
- Social၊ regional နှင့် spoken Burmese အသုံးအနှုန်းများကို universal error အဖြစ် မသတ်မှတ်သင့်ပါ။

## Roadmap

- Deterministic Unicode/Zawgyi detection နှင့် conversion layer ထည့်ရန်
- Source-backed spelling lexicon နှင့် grammar rules တိုးချဲ့ရန်
- Skill တစ်ခုစီအတွက် native-reviewed cases အနည်းဆုံး ၈၀ အထိ တိုးချဲ့ရန်
- Naturalness၊ meaning preservation နှင့် over-correction metrics ထည့်ရန်
- Automated CI validation တည်ဆောက်ရန်
- Task intent အလိုက် Skills များကို route လုပ်ပေးမည့် orchestration layer တည်ဆောက်ရန်

## ပါဝင်ကူညီခြင်း

Contribution မတင်မီ [`CONTRIBUTING.md`](CONTRIBUTING.md) ကို ဖတ်ပါ။ Rule သို့မဟုတ် benchmark case အသစ်တစ်ခုတွင် source သို့မဟုတ် native-review note၊ confidence၊ protected content နှင့် expected behavior ပါဝင်ရမည်။

## လိုင်စင်

ဤ project ကို [MIT License](LICENSE) ဖြင့် ဖြန့်ချိထားသည်။
