Now I have all the information necessary. Here is the consolidated review.

---

## Summary

This paper studies whether translating English evaluation benchmarks (MMLU, XQuAD, MLQA) into Arabic can mask data contamination effects. The authors fine-tune four open-weight LLMs on varying proportions of Arabic-translated test items (always mixed with the English originals) and evaluate on the English benchmarks. They extend the TS-Guessing memorization probe with a choice-reordering step and propose a Translation-Aware Contamination Detection (TACD) framework. The central claim is that translation conceals traditional contamination signals while models still benefit from contaminated data.

## Strengths

1. **Timely and understudied research question.** The question of how translation interacts with data contamination is genuinely underexplored and practically important for multilingual evaluation pipelines. The paper identifies a real blind spot in English-centric contamination detection.

2. **Choice-reordering extension of TS-Guessing.** The methodological addition of shuffling multiple-choice options before masking (Section 3.3, Figure 1) is a clean way to separate index memorization from true reasoning. While incremental, it is a well-motivated refinement that strengthens the memorization signal for MCQ benchmarks.

3. **Multi-dataset and multi-model coverage.** The paper spans three dataset types (MCQ and extractive QA) and four model families (LLaMA, Mistral, Gemma, Qwen), showing that contamination dynamics differ by task format and model — a useful empirical contribution regardless of the framing concerns below.

4. **Uniform training conditions.** All fine-tuning runs use the same LoRA/PEFT configuration, optimizer, context length, and evaluation harness (Section 3.1–3.2), ensuring that observed differences are attributable to contamination level rather than training artifacts.

## Weaknesses

### Fatal

None.

### Major

1. **The experimental design does not support the paper's central claim.** The training setup (Section 3.1) defines `D_train^d(p) = D_EN^d ∪ D_AR^d(p)` where `D_EN^d` — the **English test items themselves** — is present in **all** conditions (p=0, 10%, 50%, 100%). The only varying factor is how much Arabic-translated data is added. This means:
   - The p=0 model is already trained on the exact English test set it is later evaluated on. This is direct contamination, not a clean baseline.
   - The TS-Guessing probe on English benchmarks detects memorization of the **English data**, which is constant across all p. Its flatness (Table 3) does not demonstrate that "translation conceals contamination" — it simply confirms that the English contamination is uniformly present.
   - The paper frames this as a study of "translation masking contamination signals," but it is more accurately a study of whether **additional Arabic-translated data provides cross-lingual transfer benefits** on top of already-present English contamination.

   To properly test whether translation masks contamination, one would need a design where models are exposed only to Arabic translations (with no English test items) and compared against models exposed directly to English test items — allowing measurement of how much the translation attenuates or preserves the contamination effect.

2. **No English-only contamination baseline.** Without a condition where the same proportion of English test items (rather than Arabic translations) is added, the reader cannot assess whether translation reduces, amplifies, or leaves contamination effects unchanged. The paper states (Section 4.2) that "in typical same-language settings, increasing p would be expected to induce noticeable shifts," but never runs that baseline. This makes the central comparison — "translation masks contamination" — untested.

3. **No statistical rigor.** All results (Tables 2 and 3) are single-run point estimates without error bars, confidence intervals, or significance tests. Several reported trends involve small absolute changes (e.g., MMLU: 0.553→0.581 for Qwen; MLQA fluctuations of <0.05 for several models) that could easily be within run-to-run variance. Given the small model sizes and single-seed runs, the reliability of the non-monotonic patterns claimed in Section 4.1 is uncertain.

4. **Core claim about flat TS-Guessing is contradicted by the paper's own data.** Section 4.2 asserts that TS-Guessing scores are "approximately equal" across p, but Table 3a shows large swings: LLaMA IDR goes 0.287 → 0.643 → 0.410, and Gemma IDR drops from 0.350 to 0.029 to 0.005. These are not flat. The paper's interpretation that this supports the "masking" narrative is not supported by the numbers presented.

### Minor

5. **Post-hoc explanations without mechanistic evidence.** The interpretation of non-monotonic XQuAD/MLQA trends (Section 4.1) — e.g., "peak at 10% suggests early leakage, further contamination overfits to distributional quirks" — is speculative. No analysis (e.g., inspecting specific memorized spans, comparing token distributions) is provided to support these claims.

6. **TACD framework is a blueprint, not a contribution.** Section 5 outlines a "Translation-Aware Contamination Detection" proposal (cross-translation benchmarking, TS-Guessing across variants, back-translation consistency) with no implementation, experiments, or proof-of-concept. It essentially restates the paper's existing empirical finding (translation ≠ decontamination) as a research agenda. As presented, it adds no technical value beyond what the earlier sections state.

7. **The test-data-in-training confound is unacknowledged.** Nowhere does the paper discuss the fact that the English test items are present in every training condition. This is a significant oversight that affects the interpretation of every result table. A brief discussion of why this design was chosen and how it affects the conclusions would substantially improve the paper.

### Trivial

None.

## Nice-to-Haves

- Run experiments with at least 3 random seeds to provide variance estimates.
- Add an English-only contamination baseline where only English test items are added at varying proportions.
- Include the embedding analysis (referred to in Section 4.3 but absent from the extracted text as a parser-stripped figure — ensure it is present in the actual submission).
- Probe the Arabic translations themselves with TS-Guessing to directly test whether memorization of Arabic content correlates with English performance gains.
- Shorten the literature review (Sections 2.1–2.4) by roughly half; much of it recites well-known contamination taxonomies without direct relevance to the paper's multilingual angle.

## Removed Points

*The following points were raised by the harsh critic but are removed because they are factually incorrect, speculative, or violate the filtering rules:*

- **"TS-Guessing probe cannot support the concealing claim because it is applied to English benchmarks while contamination is only through Arabic"** — REMOVED (factually incorrect). The paper's training setup includes `D_EN^d` (the English split) in ALL conditions (Section 3.1). The model did see English strings during fine-tuning. The critic's premise that "the model never saw the English text during fine-tuning" is wrong.
- **"Absent embedding figure"** — REMOVED (parser artifact). The figure is referenced in Section 4.3 and was likely part of the original submission; PDF-to-text extraction strips images.
- **Literature review length criticism** — REMOVED (subjective formatting/style nitpick that does not affect the paper's technical evaluation).
- **"All models are instruction-tuned variants — why not evaluate base models"** — REMOVED (scope creep; these models are widely used as-is and the choice is reasonable for a controlled fine-tuning study).
- **"Missing related works"** — REMOVED per meta-reviewer instructions (no external sources to verify).
- **Reproducibility nitpicks (undisclosed hyperparameters, missing appendix content)** — REMOVED (parser strips appendix content; hyperparameters are stated to be in Appendix A).

## Novel Insights

None beyond the paper's own contributions. The observation that cross-lingual exposure to benchmark content can inflate English performance is the paper's genuine empirical finding, but it is not a meta-level insight that emerges from combining the reviews.

## Suggestions for the Authors

1. **Re-frame the paper honestly.** The experimental design studies *cross-lingual transfer of benchmark content* more than it studies *translation masking contamination*. The results show that adding Arabic-translated test items to already-contaminated English training can further benefit English task performance. This is a legitimate and understudied phenomenon — frame the paper around it rather than the unsupported "concealing" narrative.
2. **Remove or substantially revise Section 4.2.** The claim of "approximately equal performance" across p in TS-Guessing is contradicted by the data. Either recalculate or acknowledge the variability.
3. **Add a proper baseline**: fine-tune on English test items only (at varying proportions) to calibrate what "direct contamination" looks like, then compare against the Arabic-translation conditions.
4. **Provide error bars** (at minimum 3 seeds) for all main results tables.
5. **Remove the TACD framework section** or replace it with a 1-paragraph discussion of future work. It currently adds length without substance.

## Score and Decision

**Calibration protocol (performed in two rounds):**

*Round 1 — Bracketing:* Searched the human review corpus for papers on data contamination, LLM evaluation, and multilingual/translation topics across three score bands. Weak anchors (avg <3.5) were papers with fundamental flaws or withdrawn submissions (e.g., LogProber at 3.00, "Mind the Gap" at 2.00). Strong anchors (avg >7.5) were papers with novel methods and thorough experiments (e.g., oral/poster accepts at 8.00). The paper under review clearly sits in the middle band (3.5–7.5).

*Round 2 — Narrowing:* Compared the paper against mid-band anchors. Against "The Impact of Post-training on Data Contamination" (avg 4.67, Reject), the current paper has a less clean experimental design and no error bars → weaker. Against "Sensitivity of SLMs to Fine-tuning Data Contamination" (avg 4.00, Reject), both have comparable quality but the current paper's framing is more problematic → slightly weaker or comparable. Against "Detecting Benchmark Contamination Through Watermarking" (avg 5.00, Reject), the current paper lacks theoretical grounding and implementation → weaker. Against "Fighting Fire with Fire" (avg 3.33, Reject), the current paper has a more interesting research question but equivalent execution issues → slightly stronger. Against "LLMs Could Be Rote Learners" (avg 4.00, Reject), comparable in quality of execution and scope.

The paper's novel research question and multi-model experiments are positive, but the confounded experimental design (English test data always present), missing baselines, lack of error bars, and overclaimed conclusions relative to the evidence place it in the lower half of the middle band. Among the anchors, it sits near "Sensitivity of SLMs" (4.00) but slightly lower due to the design confound, and above "Fighting Fire with Fire" (3.33) due to a clearer presentation and more compelling research question.

**Final score:** 3.5

**Decision:** Reject

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>