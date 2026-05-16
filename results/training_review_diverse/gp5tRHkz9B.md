I've thoroughly read the paper and verified all claims. Let me now compose the final consolidated review.

---

## Summary

This paper proposes LLM-Boost, a method that fuses LLM predictions with gradient-boosted decision trees (GBDTs) by using LLM logits (scaled by a tuned parameter) as the initial prediction in a GBDT, after which the GBDT learns the residuals. The method is simple, lightweight (LLM scores are precomputed once), and model-agnostic. Experiments on 16 classification datasets show that LLM-Boost consistently outperforms selection (best of LLM/GBDT on validation) and stacking (LLM scores as additional features) baselines across sample sizes from 10 to full dataset. The paper also extends the same boosting approach to TabPFN, showing strong results on larger datasets.

## Strengths

- **Consistent outperformance over selection and stacking baselines**: Across all tested sample sizes (10, 25, 50, 100, 200, 500, full), LLM-Boost achieves the best average rank and average z-score (based on AUC) compared to the two strong ensembling baselines (selection and stacking) and both standalone models. This is verified in Figures 2 and 3, with results averaged over 5 seeds.

- **Causal evidence that meaningful column headers drive the advantage**: The column-header shuffling ablation on the Adult dataset (Figure 5) shows that LLM-Boost with intact headers significantly outperforms the shuffled version at small sample sizes (~0.73 vs ~0.67 AUC at n=25), while both converge as data grows. This provides direct evidence that the LLM's ability to extract semantic meaning from column headers is the source of the improvement, not prompt artifacts.

- **Bridging the gap between LLM-only and GBDT-only regimes**: Figure 2 shows LLM-Boost's AUC lies above both standalone LLM and standalone XGBoost curves at all intermediate sizes (50–500), where neither standalone model dominates. This demonstrates the method's ability to combine complementary strengths.

- **Lightweight overhead and practical compute**: After precomputing LLM scores (using 4 GPUs for up to 18 hours), the full HPO and boosting runs on CPU in ≤4 hours for the largest datasets (Section 4.3). This is far cheaper than LLM fine-tuning, making the method practical.

- **Generalization to non-LLM in-context learners (TabPFN)**: The same boosting approach works with TabPFN (Figure 3), achieving the best average rank on datasets ≥200 samples. This demonstrates that the boosting idea is not limited to LLMs, which is a nice empirical extension.

- **Well-controlled hyperparameter optimization**: The two-stage tuning (100 Optuna trials for GBDT parameters, 30 for the scaling parameter) is fair — baselines receive the same total budget of 130 trials (line 120), ensuring performance gains are not artifacts of unequal tuning effort.

## Weaknesses

### Fatal
None.

### Major

- **Dataset composition shifts confound cross-size comparisons.** The paper subsamples 16 datasets to sizes 10, 25, 50, 100, 200, 500, and full. Many datasets have <250 total samples, so at sizes ≥500, only a subset of datasets is available. The paper notes this (line 147, line 159) but then proceeds to **average rank, z-score, and AUC across datasets at each sample size as if the set of datasets were constant**. This means the performance at n=500 may reflect a different (easier or harder) subset than at n=100, making it impossible to attribute changes in relative performance to sample size rather than dataset selection. The authors should either (a) restrict analysis to datasets that exist at *all* sample sizes, or (b) present per-dataset curves. The paper's central visual narrative (how relative performance evolves with sample size) is undermined by this confound, even though per-size comparisons are still valid.

- **The "state-of-the-art" claim is unsubstantiated given the narrow baseline set.** The paper only compares against selection (best on validation), stacking (LLM logits as features), and standalone models. Missing baselines that would substantiate "state-of-the-art" include: (a) simple averaging (unweighted or weighted) of LLM and GBDT predictions — a natural ensemble baseline; (b) TabPFN as a standalone baseline in the main Flan-T5 experiments (Figure 2), since TabPFN is known to outperform GBDTs and LLMs on small data. Without these, the paper can claim that LLM-Boost improves over selection and stacking, but not that it achieves state-of-the-art performance. The claim should be scoped to "outperforms selection and stacking baselines."

### Minor

- **The 3-shot design choice limits LLM scalability, but this is framed as a fundamental LLM limitation.** The LLM sees exactly 3 examples regardless of training set size (line 159, line 186). The paper acknowledges this in future work (line 210) and shows in Section 5.5 that more shots improve performance. However, phrases like "LLMs cannot scale" (Introduction) or "capped by context length" overstate the case — what is shown is that *this particular prompting strategy* with *these models* scales poorly. Long-context LLMs or retrieval-augmented selection could use more data. This does not invalidate the results, but the framing should be more precise.

- **AUC computation for multiclass datasets is not specified.** The paper filters to ≤5 classes (line 107) but some datasets still have 3–5 classes. AUC for multiclass problems can be macro-average one-vs-rest, weighted, or other variants, and the paper does not state which is used. This should be clarified, and an additional metric such as log-loss (more natural for boosting) would strengthen the evaluation.

- **No statistical significance tests for key comparisons.** The paper reports average ranks and z-scores but does not perform paired tests (e.g., Wilcoxon signed-rank) across datasets at each sample size. Without this, it is unclear whether the average improvements are statistically robust or driven by a few datasets. The authors should report significance for the LLM-Boost vs. stacking and LLM-Boost vs. selection comparisons.

- **Selection of 3-shot examples is not described.** The paper does not state how the 3 in-context examples are chosen: random, class-stratified, fixed? If random, each seed gets different shots, and LLM performance could vary. This should be specified for reproducibility (the tools from Slack & Singh 2023 are referenced, but the selection mechanism should be explicit).

### Trivial

- The constant \(C\) in the prediction equation (line 88) is described ("a constant which can be added to make SCORE_LLM centered around 0") but no formula is given (e.g., \(C = -\mu\)). This is easily addressed.

## Nice-to-Haves

- **Simple averaging ensemble baseline**: Adding an equally-weighted or validation-weighted average of LLM and GBDT predictions would test whether the boosting mechanism adds value beyond naive fusion.
- **Per-dataset result table**: Showing AUC for each dataset at a few representative sample sizes (e.g., 25, 100, full) would help readers assess variability and see which datasets drive the aggregate improvements.
- **Log-loss metric**: Since boosting optimizes a differentiable loss, reporting log-loss alongside AUC would be more natural and revealing.
- **Demonstration of the scaling parameter \(s\)**: A plot showing performance vs. \(s\) on a few datasets would make the tuning mechanism more concrete.

## Removed Points

These points were flagged by reviewers but are removed because they are either factually incorrect, misunderstand the paper, or reflect scope creep:

- **"The constant C is not defined"** — The paper explicitly states that \(C\) centers the LLM scores around 0 for numerical stability (line 91). This criticism is incorrect.
- **"The paper does not discuss LLM scores for regression"** — The paper is about classification only. Regression is out of scope. Removed.
- **"Fine-tuned LLMs should be a baseline"** — The paper justifies this exclusion (line 52): fine-tuning is computationally expensive and often underperforms GBDTs on larger datasets. This is a reasonable design choice.
- **"FT-Transformer, NODE missing as baselines"** — These are deep learning tabular methods, not ensemble or LLM-based baselines. Requiring them is scope creep for a paper about LLM-GBDT fusion. Removed.
- **"Unfair HPO budget"** — The paper explicitly states baselines get 130 trials total, matching LLM-Boost's 100+30 (line 120). This criticism is factually wrong.
- **"Error bars not shown"** — The paper states standard errors are shown (line 154). Any visibility issues in the parsed PDF are parser artifacts.
- **"The paper should show error bars"** — Already addressed above; redundant criticism removed.

## Novel Insights

None beyond the paper's own contributions. The key insight — using LLM logits as a scaled initial prediction in a GBDT rather than as additional features — is the paper's own contribution. The reviews do not surface an insight beyond what the authors already present.

## Suggestions

1. **Fix the dataset composition confound**: Restrict the main cross-size analysis to the subset of datasets available at all sample sizes (e.g., those with ≥500 samples). Alternatively, present per-dataset plots for a representative subset. At minimum, clearly separate the "changing composition" effect from the "sample size" effect with a secondary figure.
2. **Add a simple averaging baseline**: Include unweighted or validation-weighted averaging of LLM and GBDT predictions to demonstrate that the boosting mechanism outperforms naive fusion.
3. **Tone down "state-of-the-art" claims**: Scope the contribution to outperforming selection and stacking baselines, which is adequately supported by the evidence.
4. **Clarify AUC variant** used for multiclass datasets and consider reporting log-loss as a secondary metric.
5. **Add statistical significance tests** (e.g., Wilcoxon signed-rank) for the main comparisons at each sample size.
6. **Specify shot selection mechanism** (random, stratified, fixed) in the experimental setup.

## Score and Decision

**Originality**: The method is simple but novel — using LLM logits as the initialization for boosting rather than as additional features or through stacking is a clean idea not explored in prior work on LLMs for tabular data.

**Importance of research question**: Combining LLMs' semantic understanding with GBDTs' scalability is a timely and practical problem. The question is well-motivated.

**Claims supported**: The claim of outperforming selection and stacking baselines is supported. The broader "state-of-the-art" claim is not — the baseline set is too narrow.

**Soundness of experiments**: The core experiment design is reasonable but has a notable confound (dataset composition shift across sizes) and would benefit from more baselines and statistical testing.

**Clarity of writing**: Well-written. The method is clearly explained, limitations are honestly discussed, and the figures are well-described.

**Value to the community**: Moderate. The method is practical, easy to implement, and the code is released. It provides a useful technique for practitioners working with small-to-medium tabular datasets with meaningful column headers.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>