- Decision: Reject
- Avg Score: 4.00
- Scores: 1, 5, 6
Now I have all the information needed. Let me produce the final consolidated review.

---

## Summary

This paper proposes *troenpy* (the expectation of −log(1−p)), framed as a dual to Shannon entropy, and uses it to derive a supervised term weighting scheme (PCF) and odds-ratio features (ECIB) for document classification. The weighting TF-PI (TF × PCF × IDF) is evaluated on seven benchmark datasets with kNN and logistic regression, showing consistent error reduction over TF-IDF in the kNN setting and further gains when ECIB and binary features are added.

## Strengths

- **TF-PI achieves uniform and substantial error reduction over TF-IDF across all seven datasets in kNN.** The paper reports an average 22.9% error reduction and a maximum of 53.4% on R8 (Section 6, Figure 1). This is a direct, reproducible demonstration of the core claim for the kNN setting.

- **Linear computational complexity compared to optimal-transport alternatives.** The paper explicitly notes (Section 6, "Word Moving Distance Methods") that the proposed weighting and ECIB features "can be obtained in a single scan of the data and the time complexity is linear," while Sinkhorn-based OT methods have higher complexity. This is a practical advantage for large-scale use.

- **Clear conceptual motivation linking the proposed quantity to certainty/commonness rather than surprisal.** The definition of PI as −log(1−p(x)) is well-specified (Equations 2–4), and the connection to a term-weighting scheme that leverages class-label distribution is intuitive and easy to follow.

## Weaknesses

### Fatal

None.

### Major

- **No comparison against existing supervised term-weighting baselines.** The paper proposes a *supervised* weighting scheme that uses class-label information, yet it only compares against unsupervised TF-IDF and HOFTT (an optimal-transport method that is not a term-weighting scheme). A substantial literature on supervised term weighting exists (e.g., TF-RF, TF-IG, TF-CHI, Delta-IDF, odds-ratio based weightings). The paper mentions Delta-IDF as inspiration for its ECIB features but does not compare against it or any other supervised weighting. Without these comparisons, it is impossible to determine whether PCF offers any advantage over existing label-aware weightings, which directly undermines the claim that the scheme is "very effective."

- **Missing TF-IDF baseline in the logistic regression experiments.** The logistic regression evaluation (Section 6) only compares TF-PI (alone and with 2B features) against kNN with TF-PI. Logistic regression performance with standard TF-IDF features is never reported. Since the central claim is about the weighting scheme's effectiveness, readers cannot tell how much of the improvement comes from the weighting vs. simply switching from kNN to a linear classifier. This is an evidential gap that weakens the entire logistic regression analysis and the conclusion that "adding the 2B features further significantly reduces the errors."

### Minor

- **Fixed K=7 for kNN without sensitivity analysis.** The paper states (Section 5) that it "fix[es] the number of closest neighborhoods K=7 rather than dynamically selecting the optimal K." While this is acknowledged, the choice of K can significantly affect relative method rankings. At minimum, a sensitivity analysis over a range of K values or cross-validated selection would be needed to ensure the observed improvements are robust to this hyperparameter.

- **Overblown theoretical framing of troenpy.** The paper presents troenpy as "a novel dual of Shannon entropy" and "complement[ing] the classical Shannon information theory" (Abstract, Introduction), but the quantity is a straightforward transformation (−∑ p log(1−p)). Crucially, PI does not satisfy the additive property of self-information for independent events (PI(x,y) ≠ PI(x)+PI(y) in general), which is a fundamental property of information measures. The real contribution is a heuristic supervised weighting scheme, not a new information theory. The paper would be better served by presenting troenpy as a simple certainty measure and downplaying the "dual" rhetoric.

- **Figure reference inconsistency in the logistic regression section.** The text (Section 6, "Logistic Regression based Experiments") states "In Figure 1 we observed: (1) … the logistic regression model uniformly outperforms the kNN approach… (2) adding the 2B features … further significantly reduces the errors." However, the earlier kNN discussion correctly references Figure 1 for the kNN comparison, and Figure 2 is captioned "Error rates of document classification using 2B features in logistic regression classifier." This makes it unclear which figure supports which observation, and observation (2) about 2B features appears to belong to Figure 2.

### Trivial

None.

## Nice-to-Haves

- A discussion of statistical significance (confidence intervals or significance tests) for the reported error reductions would strengthen the credibility of the results.
- Including runtime comparisons between the linear-complexity weighting and OT-based methods would further substantiate the efficiency claim.
- An analysis of cases where the method performs poorly (e.g., Twitter and BBCsport) could offer useful insights into the method's limitations.

## Removed Points

These weaknesses from the original reviews were removed with justification:

1. **"Figure reference error — text says Figure 1 but should be Figure 2."** The paper's Figure 1 (captioned "Errors of document classification for 7 Datasets with TF-IDF and TF-PI") may contain multiple bars per dataset, potentially including both kNN and logistic regression results. Without seeing the figure, this cannot be confirmed as an error. However, the text is confusing in bundling observation (2) about 2B features under Figure 1 — this concern is retained in the Minor section above as a "figure reference inconsistency" rather than a binary error.

2. **"No code or reproducibility details."** This is a standard nitpick for a conference paper where the method is simple enough to reproduce from description. Removed per instruction to remove nitpicks about reproducibility.

3. **"Limited baseline set — should include neural classifiers or word embeddings."** The paper's scope is simple weighting schemes and kNN/logistic regression classifiers. Requesting neural methods is scope creep.

4. **"t-SNE visualization adds little."** This is an opinion; the visualization provides qualitative support, which is a standard practice. The strength (qualitative validation) and the weakness cancel out in different directions; the strength is kept as it is concrete.

5. **Strength Finder strengths that were generic or conflicted with verified weaknesses:** None removed — all listed strengths are specific and concrete.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely converge on the same core issues (missing supervised baselines, incomplete logistic regression comparison) rather than revealing orthogonal perspectives. A small insight from the harsh critic is the observation that PI does not satisfy additivity for independent events — a mathematical property that the paper does not discuss and that limits the case for troenpy as a genuine "information measure."

## Suggestions

1. Add comparisons against at least 2–3 established supervised term-weighting schemes (e.g., TF-RF, TF-IG, Delta-IDF) in both the kNN and logistic regression settings. This is the single most important addition to validate the contribution.
2. Report logistic regression results using standard TF-IDF features alongside the TF-PI results to isolate the effect of the weighting from the classifier.
3. Run kNN with cross-validated K (or show a sensitivity sweep over a range of K values) to demonstrate robustness.
4. Tone down the theoretical framing: present troenpy as a heuristic certainty measure rather than a "novel dual" of Shannon entropy. Acknowledge that PI does not satisfy the additive property of self-information for independent events.
