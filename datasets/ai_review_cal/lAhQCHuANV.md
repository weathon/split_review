- Decision: Accept
- Avg Score: 6.33
- Scores: 8, 5, 6
Now I have all the information I need. Let me construct the consolidated review.

---

## Summary

This paper addresses uncertainty quantification for ROC curves in similarity scoring (e.g., face recognition), where false acceptance/rejection rates are U-statistics rather than i.i.d. averages. The authors show that naive bootstrap fails because bootstrap FRR forms a V-statistic with diagonal terms that bias the bootstrap distribution, and they propose a simple recentering fix. They prove asymptotic coverage guarantees (Theorem 1), validate coverage on synthetic data, and apply the method to compare the estimation stability of several NIST-style fairness metrics. The contribution is methodologically clean, practically relevant, and well-supported.

## Strengths

- **Identifies the exact cause of naive bootstrap failure for similarity ROC curves.** The paper pinpoints that the bootstrap version of FRR is a V-statistic (Eq. 7) whose diagonal terms bias the bootstrap distribution away from the empirical ROC. This is demonstrated empirically in Figs. 5/naive\_recentered\_ci, where naive confidence bands do not even contain the empirical ROC curve. This is a concrete, verifiable problem that prior work on uncertainty for ROC curves (Bertail1, Vogel18a) did not address.

- **Provides a theoretically grounded recentered bootstrap with asymptotic coverage guarantee.** Theorem 1 states that the recentered bootstrap confidence interval achieves nominal coverage asymptotically, and the synthetic coverage experiments (referenced in the appendix) confirm near-nominal coverage in finite samples. This directly fills the methodological gap for U-statistic-based performance/fairness metrics.

- **Delivers a practical comparison of fairness metric uncertainty.** Section 4 (Fig. 7) shows that the max-geomean fairness metric consistently exhibits the lowest normalized uncertainty across FAR and FRR, with additional supporting experiments using a different backbone/dataset (ResNet + RFW) in the appendix. This gives actionable guidance to practitioners.

- **Proves strong consistency of empirical similarity ROC curves under U-statistic dependence.** Proposition 1 establishes uniform consistency of \(\widehat{\mathrm{ROC}}_n\), extending classical i.i.d. results to the pairwise multi-sample framework. This fills a theoretical gap that prior work had not covered.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Over-claimed framing in Figure 1 motivation.** The figure caption states that the confidence band is computed for *ArcFace on the first dataset only*, yet the introduction (line 29) claims "both models are indistinguishable in terms of performance, as their ROC curves are contained within the band." A confidence band for one model on one evaluation dataset cannot, strictly speaking, demonstrate indistinguishability across models and across a different dataset split. The later discussion in Section 4 (lines 218–219) uses more measured language ("suggests that ArcFace and CosFace are indistinguishable"), but the introduction's phrasing is technically imprecise. This does not affect the core method — it is a presentation issue — but it could mislead readers about what the band demonstrates.

- **Fairness metric comparison claim modestly over-reaches the evidence.** The paper concludes that the max-geomean metric is "the more robust to assess fairness" (line 248) and "particularly suitable for fairness evaluation" (line 221) based on normalized uncertainty computed under a limited set of experimental conditions (two datasets: MORPH, RFW; two backbones: MobileFaceNet, ResNet; one sensitive attribute: gender). Normalized uncertainty measures estimation stability — a useful property — but it does not directly measure whether a metric is better at detecting unfairness, more interpretable in practice, or more robust under distribution shift. The claim should be hedged (e.g., "among the metrics studied and under the conditions tested, max-geomean exhibits the lowest estimation uncertainty") to match the strength of the evidence.

### Trivial
None.

## Nice-to-Haves

- A brief discussion of alternative uncertainty estimation methods (e.g., asymptotic normal approximation via Hoeffding decomposition, jackknife) would strengthen the practical guidance, though it is not required given the paper's focused goal.
- Including a short summary of the synthetic coverage results in the main text (e.g., "on 200 synthetic datasets, empirical coverage was 94.3%") would improve reader confidence in the method's finite-sample behavior without forcing a trip to the appendix.
- A small simulation examining whether lower normalized uncertainty translates into fewer rank reversals across dataset splits — directly testing the practical question "which metric gives more consistent fairness conclusions?" — would sharpen the fairness metric comparison. This is a suggestion, not a weakness.

## Removed Points

- **Criticism about the fairness comparison lacking "direct measurement of whether the metric is better at detecting unfairness":** Removed — this asks the paper to solve a problem outside its stated scope. The paper's claim is about estimation uncertainty, not about which metric has better construct validity for fairness.
- **Criticism about missing comparison to alternative uncertainty methods:** Removed — this is scope creep. The paper's goal is to provide a valid bootstrap, not to survey all uncertainty methods. Kept as a nice-to-have.
- **Criticism about the centering being "approximate":** Removed — the paper already states this implicitly and relies on the asymptotic proof and empirical validation.
- **Strength Finder's point about the problem being "important":** Removed as generic.

## Novel Insights

None beyond the paper's own contributions. The key insight — that the V-statistic structure of bootstrap FRR (Eq. 7) introduces diagonal terms that bias naive bootstrap confidence bands away from the empirical ROC, and that a simple recentering of the bootstrap distribution around the V-statistic version of the curve fixes this — is the paper's genuine contribution and is clearly articulated. The two reviews did not surface an additional novel angle beyond what the paper itself provides.

## Suggestions

1. **Re-frame the Figure 1 discussion in the introduction.** Either explicitly state that the band is shown for ArcFace on one dataset and that the figure *illustrates* why uncertainty matters (rather than claiming it formally demonstrates indistinguishability), or, if the band truly contains all the curves, add a sentence explaining the interpretation more carefully.
2. **Hedge the fairness metric conclusion.** Replace "the more robust to assess fairness" with language that acknowledges the limited experimental scope (two datasets, two backbones, one sensitive attribute) and describes the finding as "lower estimation uncertainty under the conditions studied."
3. **(Optional)** Move a one-sentence summary of the synthetic coverage results into the main text for improved self-containedness.
