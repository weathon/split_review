Now I have all the information needed. Let me synthesize the review.

---

## Summary

This paper introduces M-Longdoc, a benchmark of 851 questions across 180 documents averaging 210.8 pages (120,988 tokens), requiring open-ended answers rather than extractive spans — substantially exceeding prior benchmarks like MMLongBench in document length. The paper also proposes a retrieval-aware tuning framework that includes distractor pages during training to improve robustness in retrieval-augmented settings, and an automated evaluation framework using multiple judge models. Experiments show Qwen2-VL-7B improves from 3.84 to 4.02 on a 5-point correctness scale after tuning.

## Strengths

- **M-Longdoc fills a genuine gap in document length and answer depth.** At an average of 210.8 pages and 120,988 tokens per document, the benchmark far exceeds prior datasets (MMLongBench: 47.5 pages, 2,030.5 tokens). The open-ended question format is a meaningful departure from extractive QA benchmarks (Table 1, Table 2). This is a clear and well-motivated contribution.

- **The retrieval-aware tuning produces consistent, measurable gains across all domains and question categories.** Qwen2-VL-7B improves from 3.84 to 4.02 overall, with gains in every row of Table 3 (academic: 4.03→4.17, product: 3.88→4.01, finance: 3.56→3.86; text: 4.08→4.31, figure: 3.83→4.00, table: 3.62→3.77). The pattern is systematic, not driven by a single category.

- **The automated evaluation framework achieves strong alignment with human judgment.** The aggregated judge scores produce a Pearson correlation of 88.9% (p < 0.001) with human annotators on the preliminary study subset (Section 2.4). This provides empirical support that the automated scoring is reliable for open-ended answers.

- **The training corpus quality is verified.** A random subset of 100 training samples scores 4.82/5 on correctness (Section 3), and training documents are explicitly from non-overlapping companies/products/publication periods, reducing contamination risk (Section 3).

- **The benchmark is diverse and balanced** across three domains (academic, product, financial) and three question categories (text: 271, figure: 283, table: 297), supporting broad evaluation of multimodal document understanding.

## Weaknesses

### Fatal

None.

### Major

- **No ablation isolating the distractor mechanism.** The method adds distractor pages at training time, but there is no control condition that trains on the same data *without* distractors. The 3.84→4.02 improvement over the base Qwen2-VL could be due to standard SFT on the training corpus rather than the retrieval-aware design specifically. This is a core claim of the paper (the tuning framework is "retrieval-aware") that cannot be verified from the current experiments. Adding a "Qwen2-VL + SFT w/o distractors" row to Table 3 would directly address this.

- **Tuning is demonstrated on only one open-source model.** The retrieval-aware tuning is applied only to Qwen2-VL-7B-Instruct (line 313). The paper states "Due to training instabilities with other open-source models" without specifying what failures occurred (OOM? loss divergence? poor convergence?). This makes the claimed generality of the "framework" unsubstantiated — it could be a model-specific recipe. At minimum, the paper needs to (a) report what was attempted on LLaVA-OneVision-7B and why it failed, or (b) soften the generality claims.

- **The judge models used in the evaluation framework are never named.** Section 2.3 describes using "multiple leading multimodal models" (line 172) as judges with J=3, but never specifies which three models. Without knowing the judge models, the evaluation is not reproducible and the 88.9% human correlation cannot be assessed or replicated. This is a straightforward transparency issue — the models evaluated as generators (GPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Pro) are named in Section 4.2, but it is never confirmed whether these are also the judges, nor whether the same judges were used for the preliminary human correlation study and the main results.

### Minor

- **Placeholder macros throughout the paper.** The macros `\datasize{}`, `\trainsize{}`, and `\performanceincrease{}` appear in the abstract (line 4), introduction (lines 22, 83, 85), results (line 349), and conclusion (lines 430, 433). These prevent the reader from assessing the actual scale of the benchmark and training corpus, and the exact performance gain. This must be resolved for publication.

- **No variance estimates or confidence intervals.** All scores in Tables 1, 3, and 4 are reported as point estimates without standard errors or confidence intervals. Given the modest benchmark size (851 questions), this makes it difficult to assess whether the 0.18-point improvement (3.84→4.02) is statistically significant.

- **Potential circularity in model usage is not discussed.** The same unspecified pool of "leading multimodal models" is used for question generation (line 136), training answer generation (line 281: "leverage the respective question generator models to also produce a high-quality answer"), and evaluation judging. If the same or similar models serve multiple roles, the evaluation could exhibit biases that favor answers aligned with the judge models' own generation style. The paper does not discuss this risk.

- **Annotator qualifications differ by domain.** Academic questions are verified by "expert annotators who are Ph.D. students and above in computer science," while finance and product questions use "professional annotators" (line 144). The paper does not discuss whether this difference could affect annotation quality or consistency across domains.

- **The choice of J=3 judges and K=5 samples per judge is stated without justification or sensitivity analysis.** While not a fatal flaw, a brief sensitivity study (e.g., showing that results are stable with J=2 or J=4) would strengthen confidence in the evaluation framework.

### Trivial

- The preliminary study for human correlation uses only 100 samples (line 238). While reasonable for a preliminary check, the paper could acknowledge this limitation explicitly.
- Table 4 shows text-based questions improve without images (4.08→4.22). The paper acknowledges this briefly (line 374) but could discuss the implication that images sometimes mislead the model more substantively.

## Nice-to-Haves

- A comparison of M-Longdoc's difficulty against existing benchmarks (e.g., MMLongBench) on the same task, showing that model performance drops more sharply on M-Longdoc to quantify the additional challenge.
- An ablation varying retrieval depth (k=1, 3, 5, 10) after tuning to show whether the method improves robustness to noise.
- Sensitivity analysis of the evaluation framework to the number of judges (J) and samples per judge (K).

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The benchmark is too small (851 questions)"** → 851 questions over 180 documents is a reasonable size for a long-document benchmark, especially given that each document requires processing hundreds of pages. This is a matter of judgment, not an objective flaw.
- **"The relative improvement of ~4.7% may not be practically meaningful"** → For a 7B model on a challenging benchmark, a consistent improvement across all domains and categories is practically meaningful. The critic's framing understates the systematic nature of the gains in Table 3.
- **"The claim of being first to address retrieval setting is 'plausible but not deeply substantiated'"** → The paper clearly positions its contribution relative to prior work (MuRAG, REVEAL, RAFT) and the claim is appropriately scoped to "multimodal long documents." This is a reasonable novelty claim, not an overstatement that needs substantiation.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the core tension clearly: the benchmark is a solid, well-motivated empirical contribution, but the method validation is incomplete without an ablation that separates the effect of the distractor mechanism from standard SFT, and the evaluation framework lacks transparency about which models serve as judges. These are not inherent flaws in the paper's direction but gaps in the current execution.

## Suggestions

1. **Add the distractor ablation.** Fine-tune Qwen2-VL-7B on the same training corpus *without* distractor pages and compare to the retrieval-aware variant. This single experiment would clarify whether the gains come from the distractor mechanism or from standard SFT, and would be the most impactful addition.

2. **Name the judge models explicitly** in Section 2.3. State which three multimodal models were used for evaluation, and confirm whether the same set was used for both the human correlation study and the main results.

3. **Report confidence intervals or bootstrap estimates** for all scores in Tables 1, 3, and 4 so readers can assess the reliability of the reported improvements.

4. **Replace all placeholder macros** (`\datasize{}`, `\trainsize{}`, `\performanceincrease{}`) with explicit numbers.

5. **Explain the "training instabilities"** encountered with other open-source models — was it OOM, loss divergence, or poor convergence? This would clarify whether the limitation is fundamental or addressable with different hyperparameters or hardware.

6. **Discuss the risk of circularity** from using the same pool of models for question generation, answer generation, and evaluation.

7. **Acknowledge the single-model limitation** as a caveat in the conclusion.

## Score and Decision

The M-Longdoc benchmark is a genuine contribution: it addresses a clear gap with substantially longer documents and open-ended questions, and the benchmark construction pipeline is well-documented. The retrieval-aware tuning method is plausible and shows consistent gains. However, the paper's current form has significant gaps: the core methodological contribution (distractor mechanism) is not ablated from standard SFT, the evaluation is not reproducible without named judge models, and placeholder macros prevent the reader from assessing the scale. These issues are fixable in revision, but they prevent the paper from meeting the standard for acceptance in its current form.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>