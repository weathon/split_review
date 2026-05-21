Now let me synthesize the review and write it.

## Summary

This paper investigates whether translating evaluation benchmarks (MMLU, XQuAD, MLQA) into Arabic can mask data contamination in LLM evaluation. The authors fine-tune four open-weight models on varying proportions of Arabic-translated test data, then evaluate on English equivalents, using a TS-Guessing probe with a choice-reordering extension to detect memorization. They find that (a) MMLU accuracy rises monotonically with contamination proportion across all models, (b) the TS-Guessing probe shows mostly flat, near-zero detection signals, and (c) performance on extractive QA is more variable. The paper proposes a blueprint for a Translation-Aware Contamination Detection (TACD) framework.

---

## Strengths

**1. Novel and timely research question.** The paper is the first to systematically study whether cross-lingual translation can conceal contamination signals while models still benefit from exposure. Section 1 (line 21) frames the question directly: "whether translating benchmarks into a low resource language—in our case, Arabic—can act as a natural barrier to contamination or whether translation merely conceals memorization effects." This is a genuine gap in the contamination literature, which has overwhelmingly focused on English.

**2. Choice-reordering extension to TS-Guessing.** The paper adapts TS-Guessing (Deng et al., 2024) for multiple-choice questions by randomly shuffling options before masking an incorrect answer (Section 3.3, lines 164–165). This enables detection of memorized index patterns beyond text matching — if a model reproduces the pre-shuffle letter, it signals reliance on memorized position rather than reasoning. This is a clean methodological improvement.

**3. Multi-model, multi-benchmark experimental design.** The study spans four models (Llama-3.2-1B, Mistral-7B, Gemma-3-1B, Qwen3-1.7B) and three benchmarks (MMLU, XQuAD, MLQA) at four contamination levels (0%, 10%, 50%, 100%). Table 2 covers all 48 model–dataset–contamination conditions, providing breadth that strengthens generality relative to single-model studies.

**4. The core empirical finding is real and non-trivial.** Table 2 shows that MMLU accuracy increases monotonically with Arabic-translated contamination (e.g., Mistral: 0.577→0.690; LLaMA: 0.332→0.431), while Table 3 shows the TS-Guessing probe yields low or near-zero detection across most conditions. This pattern — performance gains without detection — is the paper's central contribution and is genuinely informative about a blind spot in current evaluation practices.

---

## Weaknesses

### Fatal
None.

### Major

**1. Missing English contamination baseline weakens the "masking" attribution.** To support the claim that translation *specifically* conceals contamination signals (vs. contamination of any kind producing the same pattern), the paper needs a control condition: fine-tuning on English-translated benchmark data and measuring both the performance gain and the TS-Guessing detection rate at equivalent contamination proportions. Without this, we cannot distinguish between "translation masks contamination" and "TS-Guessing is a weak detector at these contamination levels." The paper's core conclusion depends on this comparison, but it is absent from the experimental design. This is the most significant methodological gap.

**2. Internal contradiction between Section 4.1 and Section 4.2.** Section 4.1 (line 193) correctly states: "Across all models, MMLU exhibits a generally monotonic increase as contamination rises from 0% → 100%." Yet Section 4.2 (line 205) claims: "Across contamination levels p ∈ {10, 50, 100}%, the models exhibit approximately equal performance on all evaluated benchmarks," and line 220 asserts that "Tables 2 and 3a show that scores remain broadly stable as p increases." Table 2's MMLU column contradicts this directly — a 20% relative increase (Mistral: 0.577→0.690) is neither "approximately equal" nor "broadly stable." This is not a minor wording issue: the paper's own framing of its evidence is inconsistent, and a reader relying on Section 4.2 would be misled about what Table 2 shows.

**3. TS-Guessing results are uninterpretable without calibration on known-contaminated English data.** Table 3 shows mostly near-zero detection rates (e.g., IDR for Mistral on MMLU is 0.000–0.001; EM on XQuAD is ≤0.017 for most models). The paper interprets this as evidence that translation masks detection signals. But the alternative interpretation — that the TS-Guessing probe is simply insensitive or poorly configured for these models/datasets — is equally plausible and cannot be ruled out without calibrating the probe on a known-positive condition (e.g., English-native contamination at equivalent levels). Without this calibration, the probe results are ambiguous; they neither confirm nor refute the paper's thesis.

### Minor

**4. No error bars or multiple runs.** With only one run per condition and four contamination levels, the non-monotonic patterns in XQuAD/MLQA (Section 4.1) — which the paper speculatively interprets as evidence of "fragile transfer" and "overfitting to lexical quirks" — could be statistical noise. Error bars or at least two runs would substantially increase confidence.

**5. The TACD framework is a blueprint, not a contribution.** Section 5 describes TACD at a conceptual level (cross-translation benchmarking, back-translation consistency). The paper is honest about this (line 256: "a forward-looking blueprint rather than a complete implementation"), but this means it cannot count as a substantive contribution; it is a list of ideas that would require significant future work to validate.

**6. Section 4.2's claim about "flatness" conflates Table 2 and Table 3.** The text at line 220 says "The consolidated results in Tables 2 and 3a show that scores remain broadly stable." Table 3a (TS-Guessing) is indeed flat, but Table 2 (MMLU) is not. The paper should clearly separate the two: MMLU performance increases, while detection probes remain flat. The current presentation muddles this distinction.

### Trivial
None.

---

## Nice-to-Haves

- An English-only contamination baseline (same proportion p, same models, same benchmarks) would be the single strongest addition — it would directly test whether translation reduces detection while preserving performance gains.
- Calibrating TS-Guessing on known-contaminated English data (even on one model) would resolve the ambiguity about whether the probe is working correctly.
- Reporting per-benchmark breakdowns for individual subjects within MMLU could reveal which knowledge domains benefit most from cross-lingual contamination.

---

## Removed Points

- **Harsh Critic point 1 "central claim contradicted"** — The critic claimed that the performance gains in Table 2 contradict the paper's central claim. This is over-broad. The paper's central claim (abstract: "translation conceals traditional contamination signals, models still benefit") is supported by the evidence; the contradiction is between Section 4.1 and Section 4.2's sloppy wording, not between the data and the thesis. Kept as Major weakness #2 but reframed from "fatal contradiction" to a specific internal inconsistency.
- **Harsh Critic point 4 "non-monotonic trends overinterpreted"** — The paper does engage in post-hoc interpretation, but this is standard practice in empirical analysis sections; the issue is mostly about the lack of error bars (already covered in Minor #4). The interpretations are speculative but flagged as such ("suggests," "hints at").
- **Strength Finder claims about "first systematic investigation"** — Keep, this is accurate and verifiable from the paper.
- **Strength Finder claims about TACD being a contribution** — Downgraded: the paper is honest that it's a blueprint, and it would be unfair to count a future-facing outline as a current contribution. Acknowledged but in nice-to-have.
- **Generic strengths about "important problem"** — Removed as generic/delusional. The relevant strength is the specific novel question.

---

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a connection the paper missed, nor an interpretation that reframes its findings in a substantially new light.

---

## Suggestions

1. Add an English contamination baseline condition (same p levels, same models, same benchmarks, but training on English-translated/paraphrased rather than Arabic-translated data). This is the single most important experiment to support the "masking" claim.
2. Calibrate the TS-Guessing probe on known-contaminated English data to verify it produces non-zero signal when contamination is present in-language.
3. Resolve the contradiction between Section 4.1 and Section 4.2: Section 4.2 should clearly acknowledge that MMLU accuracy increases with p while TS-Guessing detection remains flat, rather than claiming performance is "approximately equal."
4. Add confidence intervals or run at least 2–3 seeds per condition, especially for the extractive QA benchmarks where non-monotonic patterns are interpreted heavily.

---

## Score and Decision

**Calibration anchors consulted:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| Nk1MegaPuG (Evading Contamination Detection) | 4.25 | R1, R2 | Weaker paper — unclear methodology, limited contribution. Current paper has clearer experiments and a more novel finding. |
| rAylWUIKtu (Benchmark Inflation) | 4.25 | R1, R2 | Weaker — limited to one benchmark, methodological concerns. Current paper is broader and more focused. |
| hsMkpzr9Oy (Mexa) | 5.40 | R2 | Comparable in experimental breadth but Mexa had limited novelty (simple metric). Current paper has a more impactful finding (contamination blind spot) but similar-level methodological concerns. |
| BCyAlMoyx5 (Crosslingual Capabilities) | 5.67 | R2 | Comparable — both study cross-lingual phenomena with clear experiments. Current paper's finding is more practically significant, but Crosslingual Capabilities had deeper analysis. |
| Nsms7NeU2x (How much can we Forget) | 6.75 | R1, R2 | Stronger — extensive controlled experiments, theoretical analysis, clean methodology. Current paper is less well-controlled and lacks theoretical grounding. |
| m2NVG4Htxs (To the Cutoff and Beyond) | 6.75 | R1 | Stronger — clever longitudinal design, solid execution, accepted. Current paper's methodology has more gaps. |
| OdoS6cH8MP (Language Models for Textual Data Valuation) | 2.00 | R1 | Much weaker — poor scores, different topic. Not directly comparable. |

**Round 1 bracket:** 4–6.

**Narrowing:** After comparing against Mexa (5.40) and Crosslingual Capabilities (5.67), the current paper is slightly weaker due to missing a crucial control condition (English baseline) and having an internal contradiction in its results section. It is stronger than the 4.25 anchors. The upper anchors at 6.75 are clearly stronger in experimental rigor and completeness.

**Final score:** 5.0. The paper identifies a genuinely important blind spot in contamination detection with a novel cross-lingual framing and provides reasonable initial evidence. However, the missing English contamination baseline and TS-Guessing calibration, together with a significant internal inconsistency in the results narrative, prevent the conclusions from being fully supported as-is.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>