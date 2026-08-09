# Tests

Skill တစ်ခုချင်းစီအတွက် test cases များကို သီးခြား folder တွင် ထည့်သွင်းမည်။

Test case တစ်ခုတွင် input, expected behavior, acceptable alternatives နှင့် notes ပါဝင်သင့်သည်။

## Machine-readable Benchmark

`tests/benchmark/` တွင် concrete JSONL fixtures ၈၅ ခု ပါဝင်သည်။

- Text Normalizer — ၂၀ ခု
- Grammar Checker — ၂၀ ခု
- Style Guide — ၂၀ ခု
- Humanizer — ၂၀ ခု
- Cross-skill integration — ၅ ခု

Fixture တစ်ခုတွင် ID၊ Skill၊ input၊ expected labels၊ allowed decisions၊ acceptable alternatives၊ exact preservation tokens၊ forbidden additions၊ confidence၊ source နှင့် review status ပါဝင်သည်။

Fixture integrity စစ်ရန်—

```bash
python scripts/validate_benchmark.py \
  tests/benchmark/normalizer.jsonl \
  tests/benchmark/grammar-checker.jsonl \
  tests/benchmark/style-guide.jsonl \
  tests/benchmark/humanizer.jsonl \
  tests/benchmark/integration.jsonl
```

Model သို့မဟုတ် reviewer output သည် JSONL တစ်ကြောင်းလျှင် အောက်ပါပုံစံဖြစ်ရမည်။

```json
{"id":"H-001","decision":"rewrite","labels":["H1","H6"],"output":"ပြင်ဆင်ပြီးစာသား"}
```

Protected text၊ forbidden additions၊ expected labels နှင့် allowed decision ကို စစ်ရန်—

```bash
python scripts/evaluate_outputs.py tests/benchmark/humanizer.jsonl outputs.jsonl
```

Validator unit tests run ရန်—

```bash
python -m unittest tests.benchmark.test_benchmark_tools -v
```

JSONL fixtures များသည် automated safety checks အတွက်ဖြစ်ပြီး naturalness နှင့် context-dependent judgment များကို native reviewers အနည်းဆုံး ၂ ဦးဖြင့် ဆက်လက်စစ်ဆေးရမည်။
