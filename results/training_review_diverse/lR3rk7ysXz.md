Now I have thoroughly verified all claims against the paper. Here is the consolidated final review.

---

## Summary

This paper investigates diffusion models for anomaly detection, evaluating DDPM on the ADBench benchmark (57 datasets spanning tabular, image, and NLP data) and proposing Diffusion Time Estimation (DTE) as a simpler, faster alternative. DTE trains a neural network to predict the diffusion time (or noise level) of a point, using the predicted time as an anomaly score. The paper derives an inverse-Gamma form for the posterior over diffusion time, connects the non-parametric version to kNN, and evaluates parametric variants (Inverse Gamma and categorical) against a wide set of baselines. The main empirical finding is that DTE achieves competitive accuracy while being orders of magnitude faster at inference than DDPM.

## Strengths

- **Fast inference with competitive accuracy.** DTE (categorical model) uses a single forward pass through a small network, yielding orders-of-magnitude faster inference than DDPM while matching or exceeding its accuracy across the 57-dataset ADBench benchmark (Figure 1, Figure 2). This is a practically useful result: practitioners needing real-time anomaly detection can now consider a diffusion-grounded alternative without paying the full reverse-chain cost.

- **Large-scale, multi-domain evaluation.** The paper conducts experiments on all 57 ADBench datasets covering tabular, image, and natural language data, in both semi-supervised and unsupervised settings. Prior diffusion-based anomaly detection work focused on domain-specific images; this is the first systematic study across data modalities, providing a reliable point of comparison.

- **Theoretical motivation linking diffusion to kNN.** The derivation of the inverse-Gamma posterior (Eq. 8) and the observation that the non-parametric estimator reduces to a kNN-like score provides a principled connection between diffusion-based anomaly detection and the classical kNN method. This offers an explanation for why kNN remains so effective and motivates DTE as a parametric, scalable surrogate.

- **Ablation on representation quality.** The paper investigates the effect of using raw images vs. pre-trained embeddings for image datasets, showing that embeddings improve performance substantially and offering practical guidance for deploying diffusion methods on image data.

- **Reproducibility-conscious presentation.** The paper commits to releasing code and provides detailed architecture descriptions, dataset descriptions, and per-dataset full results (deferred to appendix), enabling direct reproduction.

## Weaknesses

### Fatal
None.

### Major

- **The claim of "identical" anomaly rankings with kNN is factually incorrect.** The paper states three times (abstract §1, §3.2, §4) that the non-parametric DTE produces rankings "identical" to kNN. However, the scoring functions differ: DTE non-parametric uses the *mean* distance to k-nearest neighbours, while the kNN baseline uses the distance to the *k-th* nearest neighbour. These are not monotonic transforms of each other in general — different inputs can switch rankings under the two scoring functions. The paper acknowledges the scores differ ("the difference in score comes from the distance calculation") yet still claims identical rankings, which is a logical contradiction. This overstatement weakens the central narrative that DTE is a principled simplification that "recovers" kNN. The relationship should be described as *similar* or *inspired by* kNN, not identical. (This does not affect the method's empirical validity, but it is a factual error in the paper's claims.)

### Minor

- **The DDPM baseline's global 25% starting timestep is a concern for fairness of comparison.** The paper uses a fixed 25% of the maximum timestep for DDPM across all 57 datasets (§3, line 83), with a reference to an ablation in the appendix. Given that DDPM's anomaly detection performance is known to be sensitive to the starting timestep, and that the nature of anomalies varies widely across datasets, a single global value may not be optimal for all datasets. Without per-dataset tuning (or evidence from the ablation that 25% is near-optimal everywhere), the claim that "DTE outperforms DDPM on this benchmark" (abstract) rests on a comparison that may not reflect DDPM's best achievable performance. The paper would benefit from either tuning per dataset or providing a more detailed justification for the global choice.

- **The theoretical derivation from log-sum-exp → max → kNN mean is heuristic, not rigorous.** The derivation in §3.1 starts from the exact posterior (Eq. 4), approximates log-sum-exp with the max (yielding a nearest-neighbour score), and then replaces the max with the kNN mean based on an empirical observation ("works better in practice," line 172). The paper honestly acknowledges this transition is heuristic, but the overall framing (especially in the abstract and contributions list) presents the derivation as a tight logical chain leading to kNN. The gap between the max-approximation and the kNN-mean substitution is not formally analyzed. This is acceptable for an empirical paper but the claims should be softened to match the heuristic nature of the connection.

- **The interpretability discussion contains an unsupported claim about DTE's denoising capability.** The paper states (line 269) that "both DDPM and DTE are able to identify a 'denoised' data point; DDPM depends on an initial time step hyper-parameter, whereas DTE does not, by using deterministic ODE flow." However, the paper does not demonstrate this ODE-flow-based denoising for DTE — the results in the paper use DTE purely as a scoring function (classification head predicting diffusion time). The ability to extract a denoised point via ODE flow is presented as a potential capability rather than something implemented and validated. This should be clarified or removed to avoid misleading readers about what DTE practically achieves.

- **No sensitivity analysis for key hyperparameters \(k\) and \(B\).** The non-parametric DTE uses \(k=32\) (stated in a figure caption), and the categorical model uses \(B=7\) bins (also in a figure caption). The paper does not explore how performance varies with these choices. Since both hyperparameters control the granularity of the estimator, an ablation (even on a subset of datasets) would strengthen confidence that the reported results are not brittle to these choices.

### Trivial
- The paper states "the difference in score comes from the distance calculation: for DTE non-parametric, we take the mean distance from the k-nearest neighbours as opposed to (a variation of) kNN that takes the distance from the kth-nearest neighbour" (line 182). This parenthetical describes the kNN baseline as "a variation," which is non-standard — distance to the k-th nearest neighbour is the most common definition of the kNN anomaly score. The wording should be corrected.

## Nice-to-Haves
- **Precision-Recall (PR) AUC.** The ADBench benchmark provides both ROC AUC and PR AUC. Including PR AUC results would strengthen the evidence, especially for highly imbalanced datasets where ROC AUC can be overly optimistic.
- **Hyperparameter sensitivity analysis.** An ablation on the effect of \(k\) (non-parametric) and \(B\) (categorical) on a representative subset of datasets would be informative.
- **Visualization of DTE's learned scores on real high-dimensional data.** Figure 1 shows a 2D toy example; a UMAP/t-SNE visualization of DTE's predicted diffusion time on real-world tabular or image data would help readers build intuition for what the score captures.
- **Clarification of the bootstrapping procedure in the unsupervised setting.** The paper uses bootstrapping for training in the unsupervised setting (line 245) — a brief justification for this choice and a discussion of how it affects comparability with other methods would be helpful.

## Removed Points

These points are flagged to be removed from the critique; treat them with caution.

- *"The number of bins B for the categorical model is not stated in the main paper."* — **Removed: factually wrong.** The Figure 3 caption explicitly states "categorical model (with seven bins)."
- *"The paper does not discuss the case when d ≤ 2 (where inverse Gamma shape parameter a is not positive)."* — **Removed: factually wrong.** Line 165 explicitly states "this analysis is only valid for three or higher dimensions."
- *"The paper repeatedly contrasts DTE and DDPM on interpretability, stating... DTE falls behind DDPM... this is not obviously interpretable."* — **Removed: misreads the paper.** The paper acknowledges DTE falls behind DDPM in interpretability (line 296). It does not claim DTE is more interpretable; it investigates interpretability of both methods and reports honest limitations.
- *"No discussion of training time and memory."* — **Removed: the paper states these are in Appendix §C.5** (line 262: "Training time, inference time and compute amounts are available in \Cref{sec:compute}"). Parser-stripped appendix content is not a valid criticism.
- *"Missing details on normalizing flow baseline architecture."* — **Removed: the paper cites the original planar flows paper** (line 242), which is standard practice for baseline description.
- *"The claim about identical rankings is false because kNN is typically defined using k-th distance."* — Actually kept as Major above, but modified to note the scoring functions differ, not that the definition of kNN is wrong. The paper correctly describes the kNN baseline as using kth distance; the error is claiming rankings are identical despite different scoring functions.
- *Criticisms about the paper not covering group/contextual anomalies.* — **Removed: scope creep.** The paper explicitly focuses on point anomalies (line 298) and lists group/contextual anomalies as future work.
- *Pure formatting and style nitpicks.* — Removed per instructions.

## Novel Insights

The reviews surface one genuinely novel observation that goes beyond the paper's own contributions: the paper's central tension — that DTE claims a "principled" theoretical derivation linking to kNN while simultaneously admitting the key step is heuristic ("works better in practice") — reveals an interesting general pattern in ML research. Methods motivated by elegant theory often make unanalyzed engineering approximations at critical junctures, and the empirical success then retroactively justifies the approximations. The reviews push the authors to be more precise about where the derivation is rigorous and where it is a practical heuristic, which would strengthen the paper's intellectual honesty. Beyond this meta-observation, the reviews do not surface new insights about anomaly detection or diffusion models that the paper itself does not already discuss.

## Suggestions

1. **Correct the "identical rankings" claim throughout the paper.** Replace "identical" with "equivalent up to the scoring function" or "producing the same ordering when the mean and kth distance are monotonic" — or simply state that DTE non-parametric is *inspired by* kNN and yields *similar* rankings, rather than identical ones. This is the most important revision.
2. **Acknowledge the DDPM baseline limitation openly.** Either (a) tune the starting timestep per dataset and report the tuning, or (b) add a sentence acknowledging that a fixed 25% global value was used and this may not be optimal for all datasets, but that DDPM still serves as a reasonable reference point from the literature. This changes the comparison from a definitive "DTE outperforms DDPM" to a more honest "DTE matches or exceeds DDPM with the default settings we used."
3. **Clarify or remove the ODE-flow denoising claim for DTE.** If the ODE flow is not implemented, remove the claim that DTE can identify a denoised data point. If it is in the appendix, reference the results explicitly.
4. **Add a brief hyperparameter sensitivity study** for the key hyperparameters (\(k\) for non-parametric DTE, \(B\) for categorical DTE) on a representative subset of datasets, either in the main paper or appendix.

## Score and Decision

The paper proposes a well-motivated approach (DTE) with practical value (fast, competitive anomaly detection grounded in diffusion theory) and provides a large-scale evaluation that is among the most comprehensive for diffusion-based anomaly detection. The main empirical finding — that a simple feedforward network trained to predict diffusion timesteps works competitively — is genuine and useful. The weaknesses are addressable: the "identical rankings" claim is a clear overstatement but does not invalidate the method, the DDPM baseline concern is mitigated by the referenced ablation, and the other issues are clarifications or additions. No fatal flaw is present.

**Score:** 6.5

**Decision:** Accept with minor revisions

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>