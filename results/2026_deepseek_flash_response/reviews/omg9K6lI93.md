## Summary

This paper investigates whether translating benchmarks into Arabic obscures data contamination signals in LLM evaluation. The authors fine-tune four open-weight models on controlled proportions (0%, 10%, 50%, 100%) of Arabic-translated benchmark data (MMLU, XQuAD, MLQA), evaluate on the original English benchmarks, and apply TS-Guessing (extended with a choice-reordering strategy) to probe memorization. They find that while English MMLU accuracy rises monotonically with contamination (e.g., Mistral: 0.577→0.690), TS-Guessing scores remain low — suggesting translation conceals contamination. They also propose a Translation-Aware Contamination Detection (TACD) framework as a forward-looking blueprint.

## Strengths

- **Addresses an underexplored problem.** The question of whether multilingual evaluation creates a blind spot for contamination detection is genuinely important and has received little empirical attention. The paper's framing of this gap (Section 2, line 122) is well-motivated.

- **Multi-model, multi-dataset evaluation across three task types.** The experiments span four models from different families (Llama-3.2-1B, Mistral-7B, Gemma-3-1B, Qwen3-1.7B) and three benchmarks covering closed-book MCQ (MMLU) and extractive QA (XQuAD, MLQA). This breadth strengthens the finding that contamination dynamics vary by task type (e.g., MMLU rises monotonically while XQuAD/MLQA fluctuate non-monotonically; Table 2).

- **Extension of TS-Guessing with choice-reordering for multilingual probing.** Adapting TS-Guessing with answer-choice shuffling (Section 3.3, Figure 1) is a sensible methodological adaptation that addresses the need to detect index-based memorization when surface forms differ across languages.

- **Key observation that translation compresses but does not eliminate contamination signals.** The data in Table 2 shows that MMLU accuracy increases with contamination even under Arabic→English conditions (e.g., Mistral: +0.113 from 0%→100%), while TS-Guessing scores in Table 3 remain near floor. This divergence is a concrete, empirically-grounded observation worth reporting.

## Weaknesses

### Major

1. **Missing English-contamination baseline undermines the "masking" claim.** The paper's central interpretation — that translation "masks" contamination because TS-Guessing scores are low — requires a control condition where models are fine-tuned on *English* test data at the same proportions (10%, 50%, 100%) and TS-Guessing is applied. Without this, two equally parsimonious explanations exist: (a) translation conceals contamination, or (b) fine-tuning on 10–100% of test data simply does not induce strong memorization, regardless of language. The TS-Guessing scores in Table 3 (IDR values mostly 0.000–0.350, EM values 0.000–0.103) could reflect weak memorization rather than masking. An English-fine-tuning condition would directly test this. This is the single most important missing experiment and must be addressed before the "masking" claim can be supported.

2. **Internal contradiction between Sections 4.1 and 4.2.** Section 4.1 (line 189) correctly states that "MMLU exhibits a generally monotonic increase as contamination rises from 0% → 100%." Section 4.2 (line 201) then states that "Across contamination levels p ∈ {10, 50, 100}%, the models exhibit approximately equal performance on all evaluated benchmarks" — referring to the *same* data and claiming near-flat trends. Looking at Table 2, MMLU accuracy from 10%→100% shows: Mistral 0.580→0.690, LLaMA 0.381→0.431, Gemma 0.244→0.284, Qwen 0.560→0.581. These are not "near-flat." The paper cannot simultaneously claim both "monotonic increase" and "approximately equal performance" for the same observations without resolving the tension.

3. **Unsubstantiated claim about Arabic capabilities.** The abstract states that "models still benefit from exposure to contaminated data, particularly those with stronger Arabic capabilities." However, the paper never measures Arabic language capability for any model. No standard Arabic NLU benchmark is reported, nor is any other metric of Arabic proficiency provided. This claim is asserted without evidence.

### Minor

4. **No variance or significance reporting.** All results in Tables 2 and 3 are single-point estimates with no confidence intervals, standard deviations, or replication. With modest effect sizes (e.g., MMLU gains of 2–11 percentage points), it is impossible to assess whether observed differences are reliable or within noise. While single-run evaluation is common in this setting, the absence of any uncertainty quantification limits the strength of conclusions drawn from small differences.

5. **The p=0 condition already exposes models to English test data.** The training set at p=0 includes D_EN (the English split of the test data; Section 3.1, Equation 1). This is acknowledged, but the implications are not discussed: even the "clean" baseline involves fine-tuning on the English evaluation data, which itself constitutes contamination. This confounds the interpretation of "increases from p=0."

6. **TACD is described but not implemented.** Section 5 outlines a promising framework (cross-translation benchmarking, TS-Guessing across variants, back-translation consistency), but the paper states it is "a forward-looking blueprint rather than a complete implementation" (line 252). As a contribution, this is too thin — a framework with no validation, not even on a toy case, reads as a future-work discussion rather than a result.

### Trivial

- The paper uses "terra byte" (line 69) instead of "terabyte."
- Section 2.1.1–2.1.3 (guideline, raw text, annotation contamination) is quite elementary and could be condensed into a single paragraph.

## Nice-to-Haves

- Measuring Arabic language capability for each model (e.g., on standard Arabic NLU benchmarks) and correlating it with contamination susceptibility would substantiate the claim about "stronger Arabic capabilities" and add a valuable dimension to the analysis.
- An English-to-English fine-tuning baseline (as described in Major weakness #1) would be the single most impactful addition.
- Reporting statistical significance or effect sizes for the observed trends would strengthen the empirical rigor.

## Removed Points

- **"Structural flaw" claim (experiment tests wrong direction):** Removed. The harsh critic argued the experiment tests fine-tuning on Arabic→evaluating on English when the real concern is pretraining contamination in English hidden by translated evaluation. However, the paper's experiment tests a *different but valid* scenario — whether contamination through translated training data is detectable. The experimental direction is not fundamentally flawed; the issue is the missing baseline, which is already captured in Major weakness #1.
- **"Near-flat trend" misinterpretation claim overstated as "contradiction":** Retained as Major weakness #2 (it is a genuine contradiction), but removed the characterization that "it undermines the core empirical claim" — the contradiction is a presentation issue that can be resolved by clarifying scope.
- **TACD being "too thin":** Downgraded from a critical weakness to Minor weakness #6. A forward-looking blueprint is acceptable in a discussion section, but it should not be positioned as a central contribution.
- **Generic "no statistical information" complaint:** Kept as Minor weakness #4 but downgraded from a major concern since single-run evaluation is standard in this subfield.

## Novel Insights

None beyond the paper's own contributions. The key insight — that translation can compress contamination signals — is the paper's own empirical finding, and the reviewer inputs do not surface a genuinely novel interpretation beyond what the paper itself articulates.

## Suggestions

1. **Add the English-fine-tuning baseline condition.** Fine-tune the same models on English test data at p ∈ {10%, 50%, 100%}, run TS-Guessing, and compare IDR/EM scores with the Arabic-fine-tuning condition. This is necessary to establish that the low TS-Guessing scores under Arabic are due to translation rather than weak memorization.
2. **Resolve the internal contradiction** by clarifying the scope of the "near-flat" claim — specify whether it refers to all benchmarks jointly, or only to non-MMLU benchmarks, and account for the clear monotonic increases in MMLU.
3. **Either remove the "stronger Arabic capabilities" claim or support it** with measurements of Arabic proficiency (e.g., on Arabic NLU datasets).
4. **Add variance estimates** or, at minimum, report per-model replication for a subset of conditions to establish reliability.

## Score and Decision

**Round 1 Bracket (bracketing pass):** The paper was compared to anchors retrieved with queries covering data contamination detection in LLM evaluation:
- Weak anchors (score < 3.5): "Data Contamination in Machine Translation" (2.50), "LLMs Suffer From Their Own Output" (3.20) — our paper is clearly stronger than these.
- Middle anchors (3.5–7.5): "Evading Data Contamination Detection" (4.25, Reject), "Benchmark Inflation" (4.25, Reject), "To the Cutoff... and Beyond" (6.75, Accept), "How much can we Forget" (6.75, Reject).
- Strong anchors (> 7.5): "Training on the Test Task" (8.00, Accept) — our paper is much weaker than these.

Initial bracket: **4.0–6.0**.

**Round 2 Narrowing (narrowing pass):** Retrieved anchors inside the bracket:
- "Crosslingual Capabilities and Knowledge Barriers" (5.67, Reject) — similar cross-lingual evaluation focus. Our paper is methodologically cleaner but has a more serious interpretive gap (missing baseline). Slightly weaker.
- "Detecting Pretraining Data from LLMs" (6.25, Accept) — strong method with multiple case studies. Our paper is substantially weaker.
- "Elephants Never Forget" (4.75, Reject) — similar memorization focus. Our paper is comparable in quality but the central finding is less robust due to the missing baseline.

**Final score: 4.5.** The paper identifies an important and timely problem, conducts a reasonable initial investigation across multiple models and datasets, and surfaces an interesting observation (divergence between accuracy gains and low TS-Guessing scores). However, the central interpretive claim — that translation *masks* contamination — is not adequately supported because the critical English-fine-tuning control is absent. Without it, the results are equally consistent with the simpler explanation that fine-tuning on 10–100% of test data does not produce strong memorization signals regardless of translation. The internal contradiction and unsubstantiated Arabic-capabilities claim further weaken the paper. For a top-tier venue, the experiment needs to be completed with the missing baseline before the core claim can be evaluated.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>