- Decision: Reject
- Avg Score: 3.50
- Scores: 5, 3, 3, 3
Now I have a thorough understanding of the paper. Let me synthesize the final consolidated review.

---

## Summary

This paper proposes **LLM-Boost**, a simple method that replaces the initial constant prediction in gradient-boosted decision trees (GBDTs) with a scaled LLM prediction, then trains the GBDT on the residuals. The same mechanism is also applied with TabPFN in place of an LLM. Experiments on 16 tabular datasets at multiple sample sizes (10–500+) compare against Selection (pick best of LLM and GBDT by validation) and Stacking (LLM scores as additional features). The paper reports consistent improvements in average rank and z-score.

## Strengths

1. **Consistent empirical advantage across sample sizes.** LLM-Boost achieves the best average rank and highest average z-score compared to Selection and Stacking at every training sample size (Figures 2 and 3). The improvement is systematic, not cherry-picked at a single regime.

2. **Lightweight overhead beyond LLM precomputation.** The method requires only a one-time LLM scoring pass (GPU, up to 18h on largest datasets); the subsequent HPO and GBDT training runs entirely on CPU (up to 4 hours, Section 4.3). After precomputation, training is no more expensive than standard GBDT training (Section 6), making the approach practical.

3. **Generalizes to non-LLM in-context learners.** The same boosting mechanism applied to TabPFN (Section 5.2, Figure 3) also yields strong results, outperforming the LLM variant on larger datasets. This demonstrates the framework's flexibility beyond language models.

4. **Careful ablations strengthen the core claims.** The column-header shuffling experiment (Figure 5) isolates the contribution of semantic headers, confirming they are especially valuable at small sample sizes. The model-size and few-shot ablation (Figure 6) shows the method robustly benefits from stronger LLM priors.

5. **HPO budget is matched fairly across methods.** The paper uses 130 total Optuna trials for baselines (matching 100 GBDT + 30 scaling for LLM-Boost), ensuring comparison is not confounded by asymmetric tuning effort.

## Weaknesses

### Fatal
None.

### Major

1. **The "state-of-the-art" claim is unsupported by the baseline scope.** The abstract and introduction claim "state-of-the-art performance against numerous baselines and ensembling approaches." However, only two ensemble baselines are compared: Selection and Stacking. Several natural alternatives are missing — most notably a **tuned weighted average of LLM and GBDT probabilities**, which would be the simplest competing fusion method. Without this baseline, the advantage of residual-learning over a straightforward linear combination cannot be assessed, and the "SOTA" claim is overreaching for the evidence presented. This is the paper's most significant weakness and should be corrected by either adding baselines or calibrating the claim.

### Minor

1. **No analysis of *why* the offset structure outperforms stacking.** The paper empirically shows that LLM-Boost beats Stacking (LLM scores as features) under the same HPO budget, but does not analyze or hypothesize why the additive offset provides a better inductive bias. This leaves the reader without insight into whether the advantage comes from the gradient-friendliness of the offset, regularization properties, or something else. Adding discussion or a small diagnostic would strengthen the paper.

2. **The scaling parameter search range is not reported.** The paper states that \(s\) can take values \([0, \infty)\) and is tuned with 30 Optuna trials, but does not give the actual search range or distribution used. This is a minor reproducibility gap.

3. **No statistical significance testing across datasets.** The paper reports average rank and z-score across 16 datasets at each sample size, but does not report a paired test (e.g., Wilcoxon signed-rank) across datasets at any size. Given the modest number of datasets, such a test would help establish whether the improvement is statistically significant beyond what visual inspection of aggregated metrics suggests.

### Trivial

- The paper does not discuss how the offset is realized in specific GBDT libraries (e.g., `base_score` parameter in XGBoost, custom objective, or manual offset). The method description is conceptually clear (replace tree 0 with LLM scores), but a sentence on implementation strategy would aid reproducibility.

## Nice-to-Haves

- **Analyze the learned scaling parameter \(s\).** How does \(s\) vary with dataset size, LLM strength, and dataset complexity? Does it tend toward zero on large datasets? This would directly support the claimed adaptive behavior.
- **Report per-dataset effect sizes** (AUC differences) in a table or dot plot in the main paper, not just in the appendix. This would allow readers to judge the practical magnitude of gains.
- **Report a runtime comparison** (precomputation + GBDT tuning vs. baselines) in a table; current textual estimates are useful but a structured comparison would be clearer.

## Removed Points

- **Criticism that the equation "suggests the LLM offset is added after all trees" (Harsh Critic, Critical Issue #4, first sentence).** This is factually incorrect. The notation \(\text{pred}_{(0,i)} = \text{pred}_{(1,i)} + s\cdot\text{SCORE}_\text{LLM} + C\) with \(\text{pred}_{(a,b)}\) defined as "sum of predictions from tree \(a\) to tree \(b\)" clearly places the LLM as tree 0 (the initial/base prediction). The critic misread the notation; it does not suggest the offset is added after all trees.
- **Criticism about missing comparison to TabNet, FT-Transformer, SAINT (Harsh Critic, Critical Issue #1, second sentence).** The paper explicitly scopes itself to fusion of in-context learners (LLMs/TabPFN) with GBDTs. Mentioning deep tabular architectures as missing baselines is scope creep; the paper's contribution is not "global tabular SOTA" in the sense of beating all deep learning methods. The paper's SOTA claim is scoped to fusion/ensemble approaches, which is clear from context. However, the broader point about missing fusion baselines (weighted average) is kept as Major weakness 1.
- **Multiple generic or speculative concerns from the Harsh Critic's "Missing Parts" section.** E.g., "no comparison to other prior-based boosting methods" is vague and could refer to methods not standard in this setting; "TabPFN variant presented as afterthought" is subjective and unsupported by the paper which devotes Section 5.2 to it. These are removed.
- **Criticism about per-dataset AUC not being shown.** The paper explicitly references Table 3 and Table 6 ("Our full results") in the appendix for per-dataset results. The parser stripped these sections; they exist in the original submission. The main-text figures show aggregate AUC as well. This criticism is not a meaningful weakness given that the data is present in the complete submission.
- **Strengths from Strength Finder that are generic/superficial.** All five listed strengths are concrete and evidence-backed, so none are removed.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the expected tension between the paper's clean empirical story and its overclaimed scope, but do not reveal a hidden conceptual weakness or a new interpretation that the authors missed.

## Suggestions

1. **Replace "state-of-the-art" with more precise language** (e.g., "competitive performance compared to standard fusion baselines") or add at least one additional baseline — a tuned weighted average of LLM and GBDT probabilities would be the most informative and easiest to add.
2. **Add a brief discussion** hypothesizing why the additive-offset structure outperforms stacking (e.g., the offset preserves the gradient-boosting machinery without adding extra feature dimensions that dilute tree splits).
3. **Report the search range used for the scaling parameter \(s\)** in the main text or appendix.
4. **Consider adding a Wilcoxon signed-rank test** (or similar) comparing LLM-Boost vs. Stacking across datasets at representative sample sizes.
