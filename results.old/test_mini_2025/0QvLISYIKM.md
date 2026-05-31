Now I have all the information needed to write the consolidated review.

## Summary
This paper proposes using three pointwise information (PI) measures—PMI, PVI, and PSI—as post-hoc confidence estimators for deep neural networks. It provides theoretical analysis of invariance properties, margin sensitivity, and convergence rates. Empirically, it evaluates these measures on failure prediction (misclassification detection and selective prediction) and confidence calibration across four model/dataset combinations, comparing against six standard post-hoc baselines (MSP, SM, ML, LM, NE, NG). PVI is found to outperform both other PI measures and the baselines, particularly on AUPR_error and AURC metrics.

## Strengths
1. **Novel application of PI measures to confidence estimation.** The core idea—using PMI, PVI, and PSI as confidence scores—is original and well-motivated. Section 2 provides clear definitions, and the motivations in Section 1 (information gain, probabilistic causation) make a compelling case for why PI measures are interesting alternatives to softmax-based scores.

2. **Non-trivial theoretical analysis of invariance and margin properties.** Section 3 derives invariance results (Propositions 1–3), margin sensitivity bounds (Proposition 4 for PMI, Theorem 1 for PSI, Proposition 5 for PVI), and convergence rates. The finding that PMI collapses to a constant for non-overlapping class-conditional features (Proposition 4) is a concrete negative result. The margin correlation experiment (Table 1) provides empirical validation of the theoretical predictions about PSI's sensitivity.

3. **Consistent empirical advantage of PVI on key metrics.** Table 2 shows PVI achieves the highest AUPR_error and lowest AURC across all four model/dataset settings, often with non-overlapping standard deviations relative to baselines on these metrics (e.g., ResNet50/CIFAR-10: PVI AUPR_error 56.07±3.24 vs. best baseline NG at 48.25±1.83). Table 3 shows PVI achieves competitive or better ECE values.

4. **Thoughtful reflection on the margin-sensitivity paradox.** Section 5 explicitly acknowledges that PSI has higher margin correlation (Table 1) yet PVI performs better on accuracy-based tasks, and offers a plausible explanation (margin measures decision-boundary sensitivity while failure prediction measures predictive reliability). This is honest science and strengthens the paper's credibility.

## Weaknesses

### Major

1. **Overclaiming of scope.** The abstract states PVI is "outperforming all existing baselines for post-hoc confidence estimation," which is too broad. The paper compares against exactly six baselines (MSP, SM, ML, LM, NE, NG). While these are standard, they do not constitute "all existing baselines." The contributions section and abstract should be narrowed to reflect the actual comparison set. This is a framing problem, not a factual error in the results themselves, but it inflates the claimed contribution.

2. **Representation asymmetry between PI measures.** As stated in Section 4 (around line 278), PVI is computed between input features (raw pixels) and predicted labels, while PMI and PSI are computed between output layer features and predicted labels. The paper justifies this by noting PVI is architecture-dependent while PMI/PSI are not, but this asymmetry means the comparison conflates the choice of measure with the choice of representation. It is possible that PMI/PSI would perform differently—possibly better—if computed on input features rather than output representations, or that PVI benefits from higher-dimensional input features. A control experiment using the same feature representation for all three measures would substantially strengthen the conclusions.

### Minor

3. **No statistical significance testing.** The paper states that PVI "significantly outperforms" baselines (Section 4.2) but does not report any significance tests (e.g., paired bootstrap, Wilcoxon). Given the small number of runs (5) and overlapping standard deviations on several measures (especially AUROC_f and ECE), the claim of significance is not formally supported. For example, on VGG16/STL-10 (Table 3), PVI's ECE is 4.91±2.63 vs. MSP's 7.42±3.09—the standard deviations are large relative to the difference.

4. **Computational cost asymmetry.** PVI requires training an additional neural network of the same architecture as the original classifier (e.g., a full ResNet50), while PMI uses a shallow 2-layer network and PSI uses a Gaussian estimator with 500 random projections. The baselines require no additional training. The paper acknowledges this in the Limitations section but does not quantify it or discuss whether the comparison is equitable from a resource perspective. Adding a computational cost table (training time, parameter count) would improve transparency.

5. **Narrow calibration comparison.** For confidence calibration (Table 3), only MSP and SM are included as baselines. The paper justifies this by noting that calibration requires [0,1]-bounded scores, but the logit-based methods (ML, LM, NE, NG) could potentially be normalized. While this is a minor issue (the PI measures themselves are normalized via softmax), including them would make the calibration evaluation more comprehensive.

### Trivial
None.

## Nice-to-Haves
- A controlled experiment where all three PI measures use the same feature representation (e.g., all on input features, or all on penultimate-layer features) to disentangle measure effects from representation effects.
- Quantitative computational cost comparison (training time, FLOPs, parameter count) for each PI measure.
- A version of PMI that uses a full-network density estimator (comparable to PVI's estimator) to isolate the effect of the measure from the estimator.

## Removed Points
1. **"The theoretical analysis does not coherently support PVI as the most well-rounded"** — The paper's T5 conclusion is actually coherent: it argues PVI is best considering *both* invariance and margin sensitivity. PSI has better margin sensitivity but worse invariance; PMI has good invariance to homeomorphisms (which may be counter-productive, per Remark 9). PVI sits in a reasonable middle. The critic's reading conflates "highest margin correlation" with "best overall." The paper acknowledges PSI has higher margin correlation and explains why this doesn't translate to task performance. This is not a contradiction but a nuanced finding.
2. **"Missing baselines (trust score, Mahalanobis distance, ODIN, RAPS)"** — These methods are primarily designed for OOD detection, while the paper scopes itself to misclassification detection and selective prediction. The six baselines used are standard for this specific task. Scope creep.
3. **"Missing appendix / reproducibility details"** — By instruction, the appendix was stripped by the parser. The original submission contains these details.
4. **Formatting, grammar, and typo nitpicks** — Parser artifacts, not author errors.
5. **"Missing related works"** — Cannot verify without external sources.
6. **Strength Finder's strength: "Comprehensive empirical evidence for PVI superiority"** — Kept and listed above. The strength is valid.
7. **Strength Finder's strength: "Validation of margin-sensitivity theory via correlation experiments"** — Kept and listed above.
8. **"Motivation for JS bound for PMI not justified"** — The paper states it selected the JS bound after comparing three methods in Appendix D.2.1. A reviewer concern about the JS bound's known bias (Poole et al. 2019) is valid as a discussion point but acknowledges the paper handles it through comparison.
9. **"OOD detection omission"** — The paper explicitly scopes to misclassification detection and selective prediction (Section 4.1). This is a stated scope choice, not a weakness.

## Novel Insights
The reviews surfaced one genuinely novel insight beyond the paper's own contributions: the interaction between estimator architecture and measure performance. The harsh critic's observation that PVI uses a full-network estimator while PMI uses a 2-layer network suggests that the empirical comparison may partly reflect estimator quality rather than measure quality. This points to an interesting research question the paper does not explore: if PMI were estimated with a comparably powerful neural estimator, would the performance ordering change? The paper's own theory suggests PMI has better invariance properties (homeomorphisms), so under matched estimator capacity, PMI might close the gap. This is a concrete, testable direction for future work.

## Suggestions
1. Reword the abstract and main claims to say "outperforming six standard post-hoc baselines" rather than "all existing baselines."
2. Add a controlled experiment where PMI and PSI are computed on the same input features as PVI (or PVI on output features) to isolate measure effects from representation effects.
3. Report statistical significance (paired bootstrap or similar) for the claims that PVI "significantly outperforms" baselines, especially where standard deviations overlap.
4. Include a table of computational costs (training time, parameter count) for each PI measure estimator.
5. For the calibration experiment, include additional baselines (ML, LM, NE, NG) after normalizing them to [0,1] for completeness.

## Score and Decision

**Round 1 — Bracketing:**
- Low anchor query (score < 3.5): returned papers with avg scores 2.33–3.00 (feature selection papers, deepfake detection). The current paper is clearly stronger than these.
- Middle anchor query (3.5 < score < 7.5): returned papers with avg scores 4.25–6.00. The most relevant is "How to fix a broken confidence estimator" (5.75) and "Large Language Model Confidence Estimation" (5.50).
- High anchor query (score > 7.5): returned papers with avg scores 7.6–8.0 (oral-level papers). The current paper is substantially weaker than these.

Initial bracket: **4.0–6.0**.

**Round 2 — Narrowing:**
- Post-hoc calibration paper "Optimizing Calibration by Gaining Aware of Prediction Correctness" (5.50) — similar tier: proposes a new loss for calibration, has extensive experiments, but has conceptual clarity issues. The current paper has a stronger theoretical component but a weaker empirical design (representation asymmetry).
- "Slicing Mutual Information Generalization Bounds" (5.50) — information theory paper with theory and limited empirical validation. The current paper has more empirical substance but similar theoretical depth.
- The broken confidence estimator paper (5.75) — an extensive empirical study across 84 classifiers, but criticized for limited novelty and incomplete comparisons. The current paper has more novelty (PI measures for confidence) but weaker empirical breadth (4 model-dataset pairs vs. 84 classifiers).

Comparison to these anchors: The paper has a more original research question and better theoretical grounding than the 5.5–5.75 anchors, but the representation asymmetry and overclaiming are more serious methodological issues than what those papers faced. The paper sits slightly below the broken-confidence-estimator paper in overall rigor.

Final score: **5.0** — marginally below the acceptance threshold. The core idea is interesting and the theoretical analysis is a genuine contribution, but the overclaiming in framing and the representation asymmetry (PVI on input features vs. PMI/PSI on output features) undermine confidence that the reported performance ordering is attributable to the measure rather than the feature representation or estimator capacity. These are addressable in revision.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>