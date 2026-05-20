Now I have a thorough understanding of the paper and the calibration landscape. Let me synthesize the final review.

## Summary

The paper investigates whether translating evaluation benchmarks into Arabic can conceal data contamination while still allowing models to benefit from memorized content. The authors fine-tune four open-weight LLMs on Arabic translations of test sets (MMLU, XQuAD, MLQA) at varying proportions, evaluate on original English benchmarks, and probe memorization via an extended TS-Guessing method with choice-reordering. They find that MMLU accuracy increases with contamination exposure while extractive QA shows non-monotonic patterns, and that translation masks surface-form contamination signals. A Translation-Aware Contamination Detection (TACD) framework is proposed as a blueprint.

## Strengths

- **Novel and timely research question.** The paper asks whether cross-lingual translation can mask contamination — a genuine blind spot in the current English-centric contamination detection literature. This is a well-motivated and important issue for multilingual evaluation pipelines, and no prior work has studied it systematically.

- **Clean methodological extension of TS-Guessing.** The choice-reordering strategy for multiple-choice items (randomly shuffling answer options before masking, then checking if the model recalls the pre-shuffle letter index) is a clever adaptation that provides a stronger contamination signal than standard TS-Guessing. The Index-recall rate (IDR) metric captures a form of positional memorization that pure content-masking would miss.

- **Non-monotonic findings in extractive QA.** The observation that XQuAD/MLQA performance often peaks at 10% contamination and then declines (e.g., Gemma-3-1B-it MLQA: 0.474→0.494→0.411→0.471) is a nuanced finding that goes beyond simple "more contamination = more performance" — it suggests small amounts of cross-lingual overlap can aid span extraction while heavier exposure overfits to dataset-specific quirks. This is genuinely interesting and worth further study.

- **Cross-model experimental breadth.** The study covers four diverse instruction-tuned models (1B to 7B) and three benchmarks (MCQ and extractive QA), providing some evidence that the observed patterns are not model- or dataset-specific.

## Weaknesses

### Fatal
None.

### Major

1. **The experimental design models deliberate fine-tuning on test data, not realistic contamination, and this limits what can be concluded.** The paper fine-tunes models on Arabic *translations of the test sets themselves* and evaluates on the original English test sets. This is a "train-on-test" paradigm — explicit, deliberate exposure to evaluation data in another language. Performance gains from this setup are largely expected. The findings do not straightforwardly generalize to the realistic scenario where benchmark data appears incidentally in pre-training corpora and is then detected through surface-form matching. The paper would need a pre-training-level contamination experiment (e.g., injecting Arabic-translated test items into pre-training data, then checking if detection methods fail) to support claims about "real-world contamination dynamics." As structured, the experiment shows that translation obscures exact string matches during fine-tuning on test data — which is true but largely unsurprising.

2. **TS-Guessing results do not consistently support the memorization narrative, and the paper does not adequately address this discrepancy.** In Table 3, the TS-Guessing metrics (IDR, RL-F1, EM) are near-zero across most model/condition combinations, especially for XQuAD/MLQA. For MMLU, only LLaMA at 50% shows a notable IDR of 0.643; all other MMLU entries are ≤0.35 and most are below 0.05. If memorization were the primary driver of the observed performance gains, the probe (designed specifically to detect memorization) should register higher scores. The paper asserts that "translation conceals leakage" but the probe results equally support the alternative interpretation — that performance improvements reflect task adaptation, distribution learning, or general fine-tuning effects rather than verbatim recall. The paper lacks a positive control (e.g., demonstrating that TS-Guessing fires strongly for same-language contamination) and offers no mechanism-level explanation for why the probe fails to detect memorization that supposedly exists. This directly undermines the central claim.

3. **Missing critical baseline: English paraphrasing or equivalent surface transformations.** To argue that *translation* specifically conceals contamination (as opposed to any surface perturbation), the paper must compare against equivalent transformations in English — e.g., paraphrasing, synonym replacement, or word-order shuffling that preserves semantics. Without this, there is no evidence that Arabic plays a special role; the observed effects could be a generic consequence of any meaning-preserving surface change. This is the single most important missing control.

4. **The paper claims existing detection methods fail on translated data but never tests them.** The abstract and conclusion state that translation "evade[s] standard detection tools" and "standard English-only checks fail to capture this" — yet the paper never applies any existing detection method (Min-K% Prob, guided prompts, etc.) to the translated training data to substantiate this claim. This is an empirical assertion the paper itself does not support.

### Minor

1. **The train-on-test paradigm conflates contamination with added data quantity.** The 0% condition uses only the English split; the 10% condition adds Arabic data. Improvements from 0% to 10% could simply reflect having more training data. A control condition with unrelated Arabic data (e.g., Arabic Wikipedia) would help isolate the contamination effect.

2. **TACD is presented as a contribution but is entirely conceptual with no implementation or validation.** Section 5 explicitly states TACD is "a forward-looking blueprint rather than a complete implementation" — which is honest — but this means it cannot be evaluated as a contribution. Including it inflates the apparent submission without adding evidential weight.

3. **No confidence intervals, standard deviations, or repeated runs.** All results are point estimates from single runs. Given the small number of models and the observed fluctuations (especially in QA tasks), it is unclear which differences are significant.

### Trivial
None.

## Nice-to-Haves

- An English-paraphrase control condition would directly test whether translation is uniquely effective at masking contamination.
- A positive control demonstrating that TS-Guessing fires on same-language contamination (English→English) would validate the probe's sensitivity.
- A control with added unrelated Arabic data would separate contamination effects from general training-data benefits.

## Removed Points

- **"Embedding figure is referenced but not shown"** — The figure was stripped by the PDF parser; it exists in the original submission. Not a valid criticism.
- **"Related work is too long / is a general survey"** — This is a presentation preference, not a substantive weakness. The related work is comprehensive and relevant.
- **"Section-by-section style nitpicks"** (e.g., specific line-level formatting issues) — These are largely parser artifacts or minor presentation concerns that don't affect the paper's scientific contribution.
- **Strength Finder's generic strengths** (e.g., "the paper addresses an important problem") — These overlap with the more specific strengths listed above and add no additional information.

## Novel Insights

The most valuable observation from the reviews is the tension between the paper's evaluation results (which show performance gains from contamination) and the TS-Guessing probe results (which largely fail to detect memorization). This tension points to a potentially deeper issue: fine-tuning on translated data may improve benchmark performance through mechanisms other than verbatim recall — such as learning the task format, distribution, or reasoning patterns from additional examples. If this is the case, the paper's framing as "contamination masking" may be misleading, and the real phenomenon is something more interesting (and less alarming): cross-lingual transfer learning during fine-tuning. The non-monotonic patterns in extractive QA further support this reinterpretation. A paper that directly investigated *when* translation-induced gains reflect memorization vs. genuine task adaptation would be a stronger contribution.

## Suggestions

1. Run a positive control: fine-tune on English→English test data (no translation) and verify that TS-Guessing IDR fires strongly, establishing the probe's sensitivity.
2. Add an English-paraphrase baseline (e.g., round-trip translation through a third language, or an LLM-based paraphrase) to compare against the Arabic condition.
3. Test at least one existing detection method (Min-K% Prob, guided prompts) on the Arabic-translated training data to substantiate the claim that "standard detection tools fail."
4. Include a control condition where the added Arabic data is unrelated to the benchmark (e.g., Arabic Wikipedia sentences) to separate contamination effects from general data quantity effects.
5. Report results with variance estimates (e.g., 3 random seeds per condition).
6. Consider framing the contribution more modestly: rather than claiming to study "real-world contamination," position the work as "investigating whether fine-tuning on translated test data can evade surface-form detection methods" — this is what the experiment actually supports.

## Score and Decision

**Calibration anchors:**

| Anchor path | Avg Score | Comparison |
|---|---|---|
| `GFDSGlEks2.md` (Post-training Contamination) | 4.67 | More realistic pre-training contamination setup; cleaner experiments and error bars; rejected. Current paper has a more novel question but weaker experimental design. |
| `x4vwdjckZ6.md` (SLM Contamination Sensitivity) | 4.00 | Tests 23 models across diverse transformations; thorough but less novel question; rejected. Current paper matches in thoroughness but has fewer models and more experimental gaps. |
| `jCkmwIN9kz.md` (Fighting Fire with Fire) | 3.33 | Proposes loss-trajectory-based detection with >95% accuracy but uses similar fine-tuning-on-test-set paradigm; rejected. Current paper has a more novel question but weaker evidence for its central claim. |
| `YlpaaYxx4t.md` (CoDeC) | 5.33 | Clean, well-executed contamination detection method with strong results across many models; accepted as poster. Current paper has more novelty in the question but far weaker execution. |
| `WERLf030OU.md` (LogProber) | 3.00 | Limited experiments, few baselines; rejected. Current paper has broader experiments and a more novel question. |
| `29ETLxTQAN.md` (CapBencher) | 5.50 | Strong theoretical foundation with theorems and broad experiments, though rejected due to practical concerns. Current paper lacks comparable theoretical depth. |
| `KryACG4LGT.md` (Learning without Memorizing) | 2.00 | Poorly structured with unclear contributions; rejected. Current paper is substantially better organized and more focused. |

The paper identifies a genuine and timely gap in contamination research and presents some interesting empirical patterns (non-monotonic QA effects, MMLU gains). However, the experimental design has fundamental limitations — it models deliberate fine-tuning on test data rather than realistic pre-training contamination, the TS-Guessing results contradict the memorization narrative, key baselines are missing, and central claims about "evading standard detection tools" are asserted without empirical testing. The question is interesting enough to motivate follow-up work, but the current evidence does not support the paper's broader conclusions about real-world contamination dynamics.

**Score: 3.5**

**Decision: Reject**

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>