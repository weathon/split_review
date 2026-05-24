Now I have all the evidence needed. Let me produce the final consolidated review.

## Summary

This paper investigates whether translating English benchmarks into Arabic can mask data contamination in LLM evaluation. It fine-tunes four open-weight models on mixtures of English and Arabic-translated MMLU/XQuAD/MLQA data, evaluates on the original English benchmarks, and extends the TS-Guessing memorization probe with a choice-reordering strategy for multiple-choice tasks. The key finding is that while standard evaluation metrics show relatively flat performance across contamination levels (suggesting no contamination), the TS-Guessing probe reveals lingering memorization signals — most notably index-recall rates (IDR) such as LLaMA-3.2-1B-Instruct reaching 0.643 at 50% contamination on MMLU — indicating that translation obscures but does not eliminate contamination.

## Strengths

1. **Novel extension of TS-Guessing with choice-reordering for MCQs.** The paper adapts TS-Guessing (Deng et al., 2024) by shuffling answer choices and masking incorrect answers, then measuring index-recall rate (IDR) — the fraction of predictions matching the pre-shuffle answer letter. This provides a controlled probe for index-level memorization that goes beyond score-based checks. The method is concretely defined in Section 3.3 and the IDR metric in Section 3.4.

2. **The research question targets a genuine blind spot in contamination research.** The question of whether translation into a non-English language masks contamination while preserving memorization benefits is underexplored and practically important, especially given the growth of multilingual evaluation. The paper is the first systematic controlled study of this dynamic.

3. **Empirical finding that translation-masked contamination is detectable via memorization probes.** Table 3a shows that despite standard evaluation metrics being relatively stable across contamination levels, TS-Guessing detects non-trivial memorization signals on MMLU: LLaMA-3.2-1B-Instruct IDR of 0.643 at 50% contamination, Qwen3-1.7B IDR of 0.251 at 50%, and Gemma-3-1B-it IDR of 0.350 at 10%. These values directly demonstrate that translated contamination can be flagged even when standard accuracy trends appear normal.

4. **Systematic multi-model, multi-dataset controlled study.** The paper uses four diverse open-weight models (1B–7B parameters) and three benchmarks covering two task formats (MCQ and extractive QA) with four precisely controlled contamination proportions (0%, 10%, 50%, 100%) under consistent LoRA/PEFT training. This provides a reproducible test bed that prior work on translation-contamination interactions lacks.

## Weaknesses

### Fatal

None.

### Major

1. **No variance measures or significance estimates across runs.** Every result in Tables 2 and 3 is a single number with no standard deviation, standard error, or multiple seeds. Given the small model sizes (1B–1.7B models in several cases) and the fine-tuning setup, some of the non-monotonic patterns extensively interpreted (e.g., Mistral XQuAD 0.455 → 0.272 → 0.114; MLQA "peak-at-10%" patterns) could reflect training noise rather than meaningful contamination dynamics. Without confidence estimates, the paper's fine-grained interpretations in Section 4.1 (e.g., "fragile transfer," "anticorrelation between XQuAD and MLQA") are speculative. This is the most significant methodological gap in the paper.

2. **The claim of "approximately equal performance" across contamination levels (Section 4.2) is contradicted by the paper's own data.** The paper states: "Across contamination levels p ∈ {10, 50, 100}%, the models exhibit approximately equal performance on all evaluated benchmarks." But Table 2 shows Mistral MMLU going from 0.580 to 0.690 (a 19% relative increase), LLaMA MMLU from 0.381 to 0.431 (13% increase), LLaMA XQuAD from 0.459 to 0.569 (24% increase), and Mistral XQuAD collapsing from 0.455 to 0.114. These are not "approximately equal." This overstatement undermines the paper's own credibility and weakens the central narrative that translation "conceals" contamination signals.

3. **The experimental design does not fully distinguish contamination-driven memorization from data augmentation effects.** The training setup always includes the full English split alongside the Arabic-translated data. Accuracy gains (e.g., Mistral MMLU 0.577 → 0.690) could partially stem from having more English-similar data, cross-lingual regularization, or format familiarity rather than contamination-specific memorization. The paper lacks a control condition (e.g., fine-tuning on an unrelated Arabic dataset at the same proportions, or English-only contamination without translation) to isolate translation's specific role in masking. The TS-Guessing IDR results partially address this concern (they do show memorization), but the accuracy-based claims remain confounded.

### Minor

4. **The TS-Guessing MMLU methodology has an unclear link between the probing mechanism and the IDR metric.** Section 3.3 states: "mask the text of one incorrect answer and prompt the model to fill the mask." The model would naturally output text (the masked answer content), but the IDR metric (Section 3.4) measures whether the model reproduces the *pre-shuffle letter/index*. How the model's text completion maps to a letter output is not explained. The paper hedges by noting the model could reproduce "the text of the masked choice" (line 164), but the IDR metric is defined on letters only. The mechanism connecting the text-mask prompt to letter-level evaluation needs clarification.

5. **TACD is presented as a contribution in the abstract but acknowledged as an unimplemented blueprint in the text.** The abstract states "we propose a Translation-Aware Contamination Detection framework" without qualification. Section 5 explicitly says "we offer TACD as a forward-looking blueprint rather than a complete implementation" (line 256). While transparency about limitations is commendable, this is a mismatch in contribution claims — a proof-of-concept on the paper's own controlled setup (where ground truth contamination is known) would significantly strengthen the paper.

### Trivial

6. **Non-trivial results (e.g., Mistral-7B XQuAD TS-Guessing EM of 0.103 at 10%) are reported alongside very low values with no commentary on which models show meaningful signals.** A brief qualitative summary of detection patterns would improve readability.

7. **The embedding similarity figure referenced in Section 4.3 ("The embedding figure shows that Arabic→English translations remain close...") is not present in the main text.** If in the appendix, a parenthetical reference would help readers.

## Nice-to-Haves

- An English-only contamination control (fine-tune on English benchmarks at the same proportions without translation) to directly test whether the "masking" effect is attributable to translation specifically versus being a general property of the detection methods.
- A simple TACD proof-of-concept using the paper's own controlled setup (e.g., does back-translation consistency detect contamination when ground truth is known?).
- Reporting results with multiple random seeds or runs to establish stability.

## Removed Points

These points were raised by reviewers but are removed with justification:

- **"TS-Guessing probe fails to detect known contamination"** — REMOVED (factually wrong). Table 3a shows that the probe DOES detect contamination on MMLU: LLaMA-3.2-1B-Instruct achieves IDR 0.643 at 50% contamination, Qwen3-1.7B achieves 0.261 at 10%, and Gemma-3-1B-it achieves 0.350 at 10%. These are non-trivial detection rates. The harsh critic's claim that IDR is "near 0 for most models and conditions" is incorrect — 3 out of 4 models show meaningful IDR values on MMLU. The probe fails to detect contamination for Mistral-7B on MMLU and for XQuAD/MLQA across all models, but the paper does not overclaim these negative results. The core argument that "the probe is invalid" is unsupported.

- **"Translation-only check needed in embedding space; embedding figure not shown"** — REMOVED. The embedding figure is likely in the appendix, which is stripped by the parser. The paper references it; the absence in the parsed text is a formatting artifact.

- **"Literature review is disproportionate and could be cut by half"** — REMOVED as a subjective formatting nitpick, not a substantive weakness.

- **"TACD as a 'failed contribution claim'"** — REMOVED as too harsh. The paper explicitly and transparently states TACD is a "blueprint," not an implementation. The abstract's phrasing is slightly overstated but the body is honest. This is a minor mismatch, not a "failed contribution."

- **Strength Finder: "TACD framework as concrete, actionable proposal"** — REMOVED because it conflicts with the verified weakness that TACD is not implemented. The paper itself says it is a "blueprint," not a concrete contribution.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add variance/error bars.** The single most impactful improvement would be running each condition with 3+ random seeds and reporting mean ± std. This would validate whether the non-monotonic XQuAD/MLQA patterns are genuine or noise, and would substantially increase confidence in all claims.

2. **Add English-only contamination controls.** Fine-tune on the same benchmarks in English only at the same proportions (10%/50%/100%). If TS-Guessing detects contamination in this setting but fails on the Arabic condition, the "masking through translation" claim would be directly supported. If the probe also fails on English-only data, the probe itself needs rethinking, not the translation narrative.

3. **Correct the "approximately equal performance" overstatement in Section 4.2.** Either qualify the claim (e.g., "scores do not follow a simple monotonic pattern" or "performance is broadly stable for some model-benchmark combinations") or remove it. The data does not support "approximately equal" across the board.

4. **Clarify the IDR measurement mechanism.** Explain how masking the text of an answer choice and asking the model to "fill the mask" produces a letter output that can be compared to the pre-shuffle answer index. If the model outputs text, how is this mapped to a letter for IDR computation?

5. **Add a small TACD proof-of-concept.** Even a one-paragraph demonstration applying back-translation consistency or cross-lingual TS-Guessing to the paper's own controlled setup would transform TACD from a blueprint into a validated contribution.

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>