## Summary

This paper investigates whether translating benchmark test data into Arabic before fine-tuning can mask contamination signals in LLM evaluation. The authors fine-tune four open-weight models (1B–7B) on varying proportions of Arabic-translated MMLU, XQuAD, and MLQA test sets, then evaluate on the original English benchmarks and probe memorization via an extended TS-Guessing method. They find that (1) English MMLU accuracy rises monotonically with Arabic contamination while XQuAD/MLQA show non-monotonic patterns, (2) TS-Guessing signals remain near-zero across contamination levels, which they interpret as translation concealing contamination, and (3) they propose a Translation-Aware Contamination Detection (TACD) framework. The core question — whether translation can create a blind spot in contamination detection — is timely and underexplored.

## Strengths

1. **Timely and well-motivated research question.** The idea that multilingual translation could mask contamination signals is novel and practically important. Existing contamination detection is almost entirely English-centric, and the paper draws attention to a genuine gap.

2. **Choice-reordering extension to TS-Guessing for MCQs (IDR metric).** The paper extends Deng et al. (2024) with a random choice-shuffling step before masking, introducing the Index-recall rate (IDR). Table 3a shows LLaMA-3.2-1B-Instruct achieves IDR = 0.643 at 50% contamination — a memorization signal that standard accuracy-based evaluation would not surface. This is a concrete methodological refinement.

3. **Documents task-format divergence.** The paper shows that MMLU (MCQ) increases monotonically with contamination across all models, while XQuAD/MLQA (extractive QA) exhibit model-specific, often non-monotonic patterns. This divergence (Section 4.3) is an interesting empirical finding that suggests contamination effects interact with task format in non-trivial ways.

4. **Systematic control of training conditions.** The experimental setup (Section 3.1) specifies identical optimizer, schedule, context length, and batch policy across all models and contamination levels, which supports internal validity for the comparisons that are made.

## Weaknesses

### Major

1. **The central claim — that translation "conceals" contamination — is undersupported by the experimental design.** The paper interprets near-zero TS-Guessing signals and flat evaluation scores across p-levels as evidence that translation masks contamination. But it never demonstrates what a *detectable* contamination signal looks like for these same models, methods, and datasets in a same-language (English-only) setting. The p=0 condition already trains on English test items; comparing TS-Guessing results for p=0 (English-only contamination) against p>0 (English + Arabic contamination) would test whether translation actually reduces detectability. Without this baseline, the paper only shows that models trained on Arabic-translated data plus English test data perform better on English benchmarks — a finding consistent with contamination but also with benign cross-lingual transfer or format learning. (See Table 2 vs. Table 3: Table 3 only reports TS-Guessing for p=10%, 50%, 100%; the p=0 condition is absent.)

2. **No control for benign cross-lingual transfer.** Performance gains from Arabic-translated training data could arise from format learning, domain adaptation, or positive cross-lingual transfer rather than contamination-driven memorization. A minimal control would be to fine-tune on Arabic translations of a *different* benchmark (e.g., ARC → Arabic) and evaluate on English MMLU; if the gains are contamination-specific, they should not transfer across benchmarks. The paper's language ("contamination-driven memorization," "inflating closed-book accuracy") assumes a mechanism the evidence does not establish.

3. **No measures of variance or statistical significance.** Table 2 reports single accuracy/ROUGE-L scores per model × condition × dataset combination without standard deviations, confidence intervals, or significance tests. Several differences are small (e.g., Qwen MMLU: 0.553 → 0.560 → 0.562 → 0.581). Given LoRA fine-tuning's sensitivity to random seed, these trends could invert with additional runs.

### Minor

4. **TACD is a blueprint, not a contribution.** The Translation-Aware Contamination Detection framework (Section 5) is explicitly described as a "forward-looking blueprint" with no implementation, experiments, or validation. It does not demonstrate that cross-translation checking detects contamination better than existing methods. The paper would be clearer if it framed this as future work rather than a contribution.

5. **Translation provenance is underspecified.** The paper does not state whether the Arabic data is professionally translated, machine-translated, or drawn from existing multilingual benchmark splits. This affects reproducibility and the interpretation of results — translation quality differences could influence how much semantic content is preserved. The paper says "Arabic translations of the test items" (line 132) but gives no details about how or by whom these were produced.

6. **The TS-Guessing evidence is mixed.** While LLaMA shows an IDR spike (0.643 at 50%), most TS-Guessing scores across models and datasets are near-zero (≤0.02 for XQuAD EM/ROUGE-L across most conditions). The paper attributes this to translation concealing signals, but the data is equally consistent with models simply not having memorized the Arabic data in detectable ways. Without the same-language baseline (Weakness 1), it is hard to adjudicate between these interpretations.

### Trivial

None.

## Nice-to-Haves

- Adding standard contamination detection tools (n-gram overlap, Min-K% Prob) to the comparison and showing that they flag English-only contamination but not Arabic-condition contamination would directly validate the "blind spot" claim.
- Reporting results from multiple random seeds with mean ± std would strengthen the empirical basis for the observed trends.
- The embedding analysis mentioned briefly (line 224) says "the embedding figure shows that Arabic→English translations remain close to their English originals" — but no quantitative cosine similarity values or figure are presented in the main text. Including these numbers would strengthen the representational overlap argument.

## Removed Points

These points from the inputs were filtered out. Treat with caution:

- *"TS-Guessing results contradict the paper's own narrative"* (Harsh Critic Issue 2): This misunderstands the paper's logic. The paper's claim is that translation *masks* signals that would otherwise be detectable; low TS-Guessing IS the predicted observation under that claim, not a contradiction. Merged into Weakness 1 (missing same-language baseline) for proper framing.
- *"Literature review too long"*: Scope nitpick. Papers may include thorough background; this does not harm the contribution.
- *"Choice of models not motivated"*: The paper uses 4 models of varying sizes and families from different developers (Meta, Mistral, Google, Qwen), which is adequate coverage for the design.
- *"No analysis by Arabic proficiency"*: The paper does not claim to measure Arabic proficiency; the abstract's phrase "particularly those with stronger Arabic capabilities" is softened and not a core finding.
- *"Missing appendix/dataset statistics"*: Parser artifact; these exist in the original submission.

## Novel Insights

The most genuinely novel observation emerging from the review process is that the paper's core finding — flat performance across contamination levels — is actually ambiguous between two very different interpretations. This ambiguity is not acknowledged in the paper. If contamination is being masked, then current English-only detection pipelines are dangerously incomplete for multilingual settings. If the flat scores instead reflect benign cross-lingual transfer, then the paper is primarily demonstrating a known phenomenon (multilingual fine-tuning helps on related tasks) rather than a new contamination risk. The paper would be substantially stronger if it explicitly designed experiments to distinguish these two accounts rather than assuming the former.

## Suggestions

1. **Add the missing same-language baseline.** Train models on English test items only (no Arabic) at p=0%, 10%, 50%, 100% (controlling for data quantity). Run TS-Guessing on all conditions. If TS-Guessing flags English-only contamination but not Arabic-condition contamination at similar performance levels, the concealment claim is directly supported.

2. **Add a cross-lingual transfer control.** Fine-tune on Arabic translations of a *different* benchmark and evaluate on English MMLU/XQuAD/MLQA. If the performance gains disappear, the effect is contamination-specific. If they persist, the paper's interpretation needs revision.

3. **Report variance.** Run 3+ seeds per condition and report mean ± std. Several trends in Table 2 are small enough to be seed-dependent.

4. **Specify translation provenance.** Clarify the source, method (human vs. machine translation), and quality of the Arabic data.

## Score and Decision

**Calibration anchors used (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/Nk1MegaPuG.md` | 4.25 | R2 | "Evading Data Contamination Detection" — similar theme (evading detection through transformation). That paper's experiments were weaker and methodology less clear. Our paper is slightly better executed but has similar claim-evidence gap. |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/rAylWUIKtu.md` | 4.25 | R2 | "Benchmark Inflation" — contamination detection via retro-holdouts. Narrow scope (one benchmark) but more thorough validation. Comparable overall quality. |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/lwtaEhDx9x.md` | 4.75 | R2 | "Elephants Never Forget" — memorization in tabular data. More thorough probing methodology. Slightly stronger but comparable. |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/QiyQJqpcYe.md` | 4.75 | R2 | "Linguini Benchmark" — multilingual linguistic reasoning. Different focus but similar scope/rigor level. |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/BCyAlMoyx5.md` | 5.67 | R1,R2 | "Crosslingual Capabilities" — multilingual evaluation with controlled experiments. Stronger empirical grounding and clearer claims. |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/m2NVG4Htxs.md` | 6.75 | R1,R2 | "To the Cutoff... and Beyond?" — cleaner causal identification via cutoff dates. More rigorous statistical analysis. Our paper is notably weaker. |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/Nsms7NeU2x.md` | 6.75 | R1,R2 | "How much can we Forget?" — Extensive controlled experiments and theoretical analysis. Stronger execution. |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/jOmk0uS1hl.md` | 8.00 | R1 | "Training on the Test Task" — much stronger paper. Unanimous 8s. Our paper is not in this league. |

**Round 1 bracket:** 3.5 – 6.0  
**Round 2 narrowing:** Anchors at 4.25, 4.25, 4.75, 4.75, 5.67, 6.75. The most directly comparable papers (evading detection via transformation, at 4.25) are slightly weaker in experimental execution. The stronger contamination papers (6.75) have clearer causal identification. Our paper falls between these clusters — it has a more novel question than the 4.25 papers and better execution, but lacks the experimental rigor of the 6.75 papers. The gap between claims and evidence (Weaknesses 1–2) is the primary limiter.

**Final score:** 4.5 — The paper identifies a genuinely important blind spot in contamination detection, but the experimental design does not adequately support the central claim that translation *conceals* contamination. Missing controls (same-language baseline, cross-lingual transfer control) and lack of variance reporting prevent the evidence from matching the strength of the conclusions.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>