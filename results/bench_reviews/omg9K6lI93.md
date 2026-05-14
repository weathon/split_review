Now I have all the information I need. Let me produce the final consolidated review.

---

## Summary

This paper investigates whether translating benchmark data into Arabic can mask data contamination signals in LLM evaluation. The authors fine-tune four open-weight models on varying proportions of Arabic-translated test data (p ∈ {0, 10%, 50%, 100%}) alongside the English test set, then evaluate on the original English benchmarks. They extend TS-Guessing with a choice-reordering strategy for MMLU to probe memorization, and find that while translation obscures surface-form contamination signals, MMLU accuracy increases monotonically with contamination level — suggesting models still benefit from exposure even when standard detection methods fail to flag it.

## Strengths

- **Addresses an understudied problem — contamination in multilingual evaluation.** Prior contamination detection work focuses overwhelmingly on English benchmarks and exact-string matches. This paper demonstrates that translating benchmarks into Arabic breaks surface-form signals that English-only detectors rely on, revealing a genuine blind spot. The MMLU monotonic increases (e.g., Mistral: 0.577→0.690, LLaMA: 0.332→0.431 as p increases) provide concrete evidence that models benefit from translated contamination even when it would evade standard checks. (Section 4.1, Table 2)

- **Methodological contribution: choice-reordering extension of TS-Guessing.** The paper adapts TS-Guessing (Deng et al., 2024) by randomly shuffling answer choices and masking one incorrect option, then measuring Index-recall rate (IDR) — whether the model outputs the *pre-shuffle* answer letter. This design cleanly separates memorization of answer positions from genuine reasoning. The approach is well motivated and the protocol is clearly described. (Section 3.3, Figure 1)

- **Multi-model, multi-benchmark evaluation with consistent MMLU pattern.** Four instruction-tuned models (Llama-3.2-1B, Mistral-7B, Gemma-3-1B, Qwen3-1.7B) are tested on three tasks (MMLU, XQuAD, MLQA) under four contamination conditions. The consistent monotonic MMLU trend across models strengthens the claim that contamination-driven memorization is a real effect, not an artifact of one model or dataset. (Section 3.1, Table 2)

## Weaknesses

### Major

- **The paper's claim of "flat" / "broadly stable" trends across contamination levels is contradicted by its own data.** Section 4.2 states that "scores remain broadly stable as p increases" and that models "exhibit approximately equal performance on all evaluated benchmarks" across p ∈ {10, 50, 100}%. But Table 2 shows clear, non-trivial variation: MMLU increases monotonically for every model (Mistral: 0.580→0.690→0.690; LLaMA: 0.381→0.389→0.431); XQuAD for Mistral collapses (0.455→0.272→0.114); Qwen's MLQA drops from 0.409 at p=10 to 0.157 at p=50. Table 3a shows similar variation in TS-Guessing IDR (LLaMA: 0.287→0.643→0.410; Gemma: 0.350→0.029→0.005). The paper's central interpretive argument — that translation "masks" contamination by compressing observable differences across p — relies on this claim of flatness, but the data do not support it. (Lines 205–222, Tables 2 and 3a)

- **No clean baseline: all conditions are contaminated with the English test set.** The training set is defined as D_EN^d ∪ D_AR^d(p), where D_EN^d is the *English test split* of the benchmark. Thus even p=0 trains directly on the evaluation data. The paper never compares against a model that has seen no test-set data at all. This makes it impossible to determine whether the observed performance patterns reflect contamination masking or simply the baseline effect of English test-set exposure. The claim that "translation conceals contamination signals" is a relative claim (compared to uncontaminated training), but the experimental design only supports relative comparisons across Arabic contamination levels layered on top of already-contaminated models. (Section 3.1, Equation 1)

- **TS-Guessing detection rates are too weak to cleanly separate memorization from cross-lingual transfer.** For XQuAD, TS-Guessing EM is ≤0.017 across all models and conditions — near floor. For MMLU, IDR values are typically below 0.35 except for LLaMA at 50% (0.643). The paper interprets performance gains as contamination-driven memorization, but an equally plausible explanation is cross-lingual transfer: fine-tuning on Arabic data may simply improve the model's general Arabic-to-English capabilities, boosting English benchmark performance without any memorization of benchmark-specific content. The paper does not conduct control experiments (e.g., fine-tuning on Arabic translations of *unrelated* datasets) to distinguish these explanations. (Table 3, Section 4.2)

### Minor

- **No variance or statistical significance reporting.** All results are reported as single point estimates. With only ~1,400 MMLU samples per condition at p=10%, the non-monotonic patterns in XQuAD/MLQA (e.g., Mistral XQuAD 0.455→0.272→0.114) could reflect sampling noise, but the paper treats them as meaningful. (Tables 2 and 3)

- **The TACD framework is presented as a "blueprint" with no implementation or evaluation.** The paper is transparent about this (Section 5.3), but it means the TACD component is not a contribution that can be assessed. The paper's empirical contribution rests entirely on the fine-tuning study.

### Trivial

None.

## Nice-to-Haves

- **Fine-tuning on the test set is not the primary way real contamination occurs.** Real contamination typically happens incidentally during *pre*training on web corpora, not through deliberate fine-tuning on the evaluation benchmark. The paper's controlled setup is still informative, but the connection to realistic contamination scenarios would be strengthened by discussing how the findings might differ under pre-training contamination. (This concern applies to most papers in this area and does not uniquely disadvantage this work.)

## Removed Points

These points are flagged to be removed; treat them with caution:

- *Criticism that the TACD framework "does not constitute a contribution" because it is not implemented.* The paper explicitly scopes TACD as a "forward-looking blueprint" (Section 5.3). Framing it as a missing contribution misreads the paper's own transparent positioning. This is a minor weakness (not a contribution), not a fatal flaw.

- *Criticism that fine-tuning on the test set is "not representative of real contamination."* This is a scope-boundary criticism that applies to most controlled contamination studies. The paper does what it scopes: a controlled experiment on contamination dynamics under translation. Realism is a separate axis and is noted in Nice-to-Haves.

- *Pure formatting/style nitpicks and parser artifacts* (e.g., line breaks, capitalization inconsistencies). These are PDF extraction artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add a clean baseline.** The most important fix: include a condition with no test-set exposure (i.e., no fine-tuning on either English or Arabic benchmark data). This would allow direct measurement of whether translation reduces detectability relative to a truly uncontaminated model.

2. **Add an unrelated Arabic data control.** Fine-tune on Arabic translations of an unrelated dataset to test whether performance gains reflect cross-lingual transfer rather than benchmark-specific memorization. This would substantially strengthen the causal claims.

3. **Remove or qualify the "flat/stable" claim.** The data do not support the claim that results are "approximately equal" across p. The paper should describe the actual patterns (MMLU increasing, XQuAD/MLQA varying) and offer a more measured interpretation.

4. **Add variance estimates.** Report standard deviations or confidence intervals, especially given the modest sample sizes at lower contamination levels.

5. **Explain the discrepancy between TS-Guessing weakness and claimed memorization.** If contamination is occurring, why do the TS-Guessing probes fail to detect it strongly? A frank discussion of this tension would strengthen the paper.

---

## Calibration against human-reviewed anchors

| Anchor Path | Avg Human Score | Comparison |
|---|---|---|
| `/home/wg25r/review_agent/human_reviews_2026/GFDSGlEks2.md` ("The Impact of Post-training on Data Contamination") | 4.67 (Reject) | Stronger experimental design — starts from clean checkpoints, includes variance reporting. Current paper is weaker on execution. |
| `/home/wg25r/review_agent/human_reviews_2026/jCkmwIN9kz.md` ("Fighting Fire with Fire") | 3.33 (Reject) | Similar methodology (fine-tuning on test data) with analogous realism concerns. Current paper asks a more novel question but has a weaker interpretive argument. |
| `/home/wg25r/review_agent/human_reviews_2026/YlpaaYxx4t.md` ("Detecting Data Contamination via In-Context Learning") | 5.33 (Accept Poster) | Cleaner method, more thorough experiments, clearer narrative. Current paper is significantly weaker on methodological rigor. |
| `/home/wg25r/review_agent/human_reviews_2026/WFGxFzFDmQ.md` ("Detecting Benchmark Contamination Through Watermarking") | 5.00 (Reject) | Has formal guarantees and a complete system; stronger contribution. Current paper has more limited scope. |
| `/home/wg25r/review_agent/human_reviews_2026/WERLf030OU.md` ("LogProber") | 3.00 (Reject) | Limited experimental coverage. Current paper has broader evaluation but comparable methodological concerns. |
| `/home/wg25r/review_agent/human_reviews_2026/VKGTGGcwl6.md` ("LLMs Get Lost In Multi-Turn Conversation") | 8.00 (Accept Oral) | Completely different level of rigor, scale, and analytical depth. Not comparable to current paper. |

**Score rationale:** The paper addresses an important and genuinely understudied problem, and the MMLU monotonic trend provides real evidence that translated contamination can affect benchmarks while evading surface-form detection. However, the experimental design lacks a clean baseline, the central interpretive claim about "flat/stable" trends is contradicted by the paper's own data, and the TS-Guessing results fail to cleanly separate memorization from transfer. These issues prevent the paper from meeting the acceptance bar. Relative to the anchor papers, it sits below the typical acceptance threshold.

---

MY FINAL SCORE: <pineapple>3.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>