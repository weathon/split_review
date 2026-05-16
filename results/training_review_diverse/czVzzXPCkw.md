Now I have all the information I need. Let me produce the consolidated review.

## Summary

This paper addresses the under-explored problem of extrapolation in material property regression (MPR)—predicting properties outside the training label range. It makes two contributions: (1) a benchmark of seven tasks with extreme-value label splits derived from Matminer, and (2) the Matching-based EXtrapolation (MEX) framework, which reframes regression as a material-property matching problem using absolute cosine-similarity and noise-contrastive estimation losses to align sample and label embeddings. MEX achieves the best average rank across two backbones and both evaluation metrics, and demonstrates high recall for detecting extrapolative materials.

## Strengths

1. **Identifies a genuine, under-studied problem in MPR.** The paper clearly motivates why extrapolation matters for material discovery (OLEDs, thermodynamic stability, etc.) and shows that existing benchmarks use only random i.i.d. splits, which do not test for this capability.

2. **Constructs a dedicated extrapolation benchmark with meaningful splits.** The seven tasks use extreme-value label splits (top/bottom 15% for test and validation), directly mirroring real-world scenarios where researchers seek materials with record-breaking properties. The split construction is well-motivated by application-specific desiderata (e.g., lower formation energy for stability).

3. **Proposes a conceptually interesting approach in MEX.** Reframing regression as a matching problem in latent space is a principled departure from direct point estimation, and the combination of an absolute matching loss (negative cosine similarity) and a relative contrastive loss (NCE) is well-motivated. The framework is backbone-agnostic.

4. **Empirically demonstrates strong average performance.** MEX achieves the best average rank across both backbones (PaiNN, EquiformerV2) and both metrics (MAE, GM), with the lowest MAE on 5–6 out of 7 datasets depending on the backbone. The detection analysis shows recall >80% on three datasets and >60% on six, outperforming baselines in 6/7 tasks.

5. **Provides informative ablations and analysis.** The score module variants (MLP+cos vs. pure cos), the λ trade-off parameter, and running time are all studied, giving practical insight into the method's design choices.

## Weaknesses

### Fatal

None.

### Major

1. **Inference procedure is critically under-specified.** Section 3.2.2 states that candidate labels are iteratively refined using "Monte Carlo sampling-based stochastic optimization" (citing a general survey), but the actual update rule—how candidates are re-sampled or re-weighted, how exploration and exploitation are balanced, how convergence is determined—is never given. The implementation details provide the number of iterations (10) and initial candidate size (C=1500) but not the mechanism. Without this information, the method cannot be reproduced from the paper alone. The authors should provide pseudocode or a precise algorithmic description of the inference loop.

### Minor

2. **High variance weakens the superiority claim.** Several entries in Tables 2–3 show standard deviations comparable to or larger than the performance differences between methods (e.g., Formation Energy with PaiNN: MEX 0.172±0.164 vs. BalancedMSE 0.193±0.297; Shear Modulus (top) with EquiformerV2: MEX 8.213±2.793 vs. BalancedMSE 7.074±1.678). With only 3 random seeds and no statistical significance assessment, the abstract's claim that "MEX outperforms all existing methods" is stronger than the data support. The paper's more measured language in the main text ("best average rank") is appropriate.

3. **Detection analysis uses recall only.** Figure 5 reports recall (fraction of extrapolation samples whose prediction falls in the extrapolation interval). A method could achieve high recall by predicting extreme values indiscriminately while producing many false positives. Without precision, false positive rates on in-distribution samples, or an operating-point analysis, the "detection capability" conclusion is one-sided. The authors should complement the recall analysis.

4. **Label encoder behavior on unseen labels is not examined.** The label encoder is a linear layer + activation; while it is mathematically defined for all inputs, the paper provides no analysis of whether its embeddings for labels far outside the training range are meaningful for matching (e.g., does cosine similarity between a test sample and a test label actually correlate with the true property?). An empirical sanity check would strengthen the paper.

5. **Spearman correlations reported only qualitatively.** The text mentions "weak (0-0.2)" correlations but the exact numbers for each method/dataset are not tabulated. Given this is the paper's main analysis of prediction quality beyond error magnitude, exact reporting would be more useful.

6. **Several hyperparameters not ablated.** The candidate set size (C=1500) and noise distribution parameters (K=3, fixed σs) are not varied. A sensitivity study on at least one dataset would improve understanding of the method's robustness.

7. **Shear modulus dual-task construction has structural overlap.** Creating separate top and bottom tasks from the same raw dataset means the same crystal structures appear in both tasks (with different label values). This should be acknowledged as a limitation of the benchmark design.

8. **No simple extrapolation-capable baseline.** Including a k-nearest neighbor regressor or Gaussian process on learned features would contextualize MEX's benefit relative to a non-neural extrapolation method.

### Trivial

- The term "extrapolation interval" in the detection analysis (Section 4.4) could be more precisely defined.

## Nice-to-Haves

- A more detailed characterization of the label encoder's output space (e.g., plot cosine similarity between a fixed material embedding and label embeddings across a dense grid). This would directly validate the matching assumption.
- A comparison with a non-neural extrapolation baseline (e.g., k-NN or GP) to contextualize MEX's benefit beyond the neural DIR/DA methods tested.

## Removed Points

These points are flagged to be removed, treat them with caution:
- The harsh critic's framing of the label encoder issue as a "structural gap" that "the entire matching approach collapses" is overstated. A linear layer + activation is a continuous function defined for all inputs; the concern is about usefulness of the learned mapping, not catastrophic failure. The paper's empirical success implicitly validates the approach. Moved to Minor.
- The strength finder's claim that "Improvements are statistically significant with standard deviations from 3 runs." The paper does not report any statistical significance tests, so this claim is unsupported. Removed.
- The harsh critic's request that the paper "should explicitly verify that no training sample has a label in the test range." The split procedure (top/bottom 15% test, second 15% validation, remaining 70% train) inherently guarantees disjointness by construction. This is a trivial clarification.
- The harsh critic's note about candidate set range. The critic acknowledges the range is fine. No weakness here.
- Several of the harsh critic's line-level presentation nitpicks about vague phrasing that do not affect the core contribution.

## Novel Insights

The most insightful observation across the reviews is the tension between the method's core mechanism (matching in latent space) and the underspecification of how that matching is performed at inference. The paper argues that matching is "simpler" than direct regression, but the inference procedure resorts to a black-box stochastic optimization over a candidate set—this is itself a non-trivial optimization problem. The reviewers collectively identify that without characterizing whether the learned label encoder produces meaningful embeddings for unseen labels (especially since it is only a linear layer), the method's foundation is not fully validated. This points to a concrete experimental direction (analyzing the label encoder's similarity landscape) that would either substantiate or refute the core hypothesis.

## Suggestions

1. **Specify the inference algorithm in full** by adding pseudocode or a clear algorithmic description of the iterative candidate refinement step. This is the single most important fix for reproducibility.

2. **Either run more seeds** (5–10), report bootstrap confidence intervals, or at minimum discuss which performance differences exceed the combined standard errors.

3. **Add precision or false-positive analysis** to the detection study, or report the distribution of predictions for in-distribution samples to show that high recall is not achieved by indiscriminately predicting extreme values.

4. **Tabulate the Spearman correlations** by method and dataset rather than reporting only a qualitative range.

5. **Tone down the abstract's claim** from "outperforms all existing methods" to language that reflects the best-average-rank finding, given the variance concerns.

## Score and Decision

The paper makes a solid contribution by identifying and formalizing an underexplored problem, constructing a useful benchmark, and proposing a novel method with competitive empirical results. The primary weakness—underspecified inference procedure—is fixable in revision and does not invalidate the core contribution. The variance and metric concerns are real but moderate. Overall, this is a worthwhile contribution that can be strengthened with targeted revisions.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>