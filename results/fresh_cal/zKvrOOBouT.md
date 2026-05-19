Now I have all the information I need. Let me compose the final consolidated review.

## Summary

This paper proposes EvA (Erasing with Activations), a post-hoc debiasing method that detects spurious features in the final linear layer of pretrained neural networks and erases them by zeroing out corresponding weights. EvA-C uses a "consistency" measure (Wasserstein distance between training and unbiased activation distributions) when unbiased data is available, while EvA-E uses a novel "evidence energy" metric derived from a Taylor expansion of the energy score to identify spurious features without any unbiased data. The method is computationally efficient, requiring only retraining of the last linear layer (minutes on a single GPU). Experiments on CMNIST, BAR, Waterbirds, and CelebA show the method is effective at removing spurious feature reliance and competitive with or better than baselines like DFR, JTT, and DivDis.

## Strengths

- **Spurious feature detection without unbiased data is novel and practically appealing.** EvA-E's evidence energy (Eq. 7) identifies spurious features using only the biased training set, by measuring each feature's contribution to prediction confidence. This directly contrasts with methods like DFR that require an unbiased reweighting dataset. The paper demonstrates this works via a controlled CMNIST experiment (Table 2: EvA achieves 97.78% on digit accuracy while only 51.45% on color accuracy, confirming erasure of the spurious color feature) and on Waterbirds (4.1%–4.8% relative gains claimed).

- **Data efficiency advantage over DFR is clearly demonstrated.** Figure 2(c) shows EvA-C consistently outperforms DFR as the unbiased dataset shrinks, and Table 3 shows both EvA variants maintain high accuracy with as little as 0.7% of the training set size as unbiased data. This concretely supports the paper's core efficiency claims.

- **Computational efficiency is a genuine practical advantage.** EvA requires only retraining the final linear layer (minutes on a single GPU), compared to the days of full retraining needed by many debiasing methods. This is well-motivated and practically significant for real-world deployment.

- **Empirical validation links the two detection metrics.** Figure 2(a) shows a moderate positive correlation (Pearson 0.704) between negative evidence energy and inconsistency, and Figure 2(b) demonstrates that erasing by evidence energy removes most high-inconsistency features while retaining core features. This provides empirical support that evidence energy can substitute for consistency when unbiased data is unavailable.

- **Class-specific erasure is shown to matter.** Figure 3(b) demonstrates low overlap of erased features across different classes, and Figure 3(a) shows class-wise erasure consistently outperforms a version without it on BAR, confirming the method correctly handles class-specific spurious features.

## Weaknesses

### Fatal
None.

### Major

- **Limited baseline comparisons do not support the "state-of-the-art" claim.** For the with-extra-data setting (EvA-C), the only comparison is DFR. For the without-extra-data setting (EvA-E), comparisons are limited to JTT and DivDis. Many relevant methods discussed in the paper's own related work (e.g., GroupDRO, LfF, LISA, LNL) are not included in any experiment, yet the abstract and introduction repeatedly claim "state-of-the-art performance." Even if some of these methods operate in a different paradigm, the paper should either expand the comparison set or moderate its claims to reflect the scope of what was actually tested.

- **The DFR comparison on BAR uses a biased reweighting dataset, which disadvantages DFR by construction.** The paper acknowledges (line 181) that "in BAR where the spurious feature is not labeled, the reweighting dataset is also biased," and DFR is designed for unbiased reweighting. While this setting demonstrates EvA's robustness to biased extra data—which is a legitimate contribution—the presentation frames the resulting performance gap as straight "SOTA" without sufficient caveat. A fairer evaluation would include DFR with an unbiased reweighting set where available and clearly separate "EvA is more robust" from "EvA has higher absolute performance."

- **The main BAR and Waterbirds results are presented in figures rather than tables, making precise verification difficult.** The paper's headline claims (6.2% relative gain on BAR, 4.1% on Waterbirds) are stated in the abstract, but the underlying absolute accuracies, standard deviations, and full baseline comparisons appear in Figure 3 (images), not in a readable table. Table 2 provides clean numerical results for CMNIST, and Table 3 is referenced for data efficiency, but the central comparative results lack transparent numerical reporting. This is a significant presentation gap for a paper whose contribution is empirically grounded.

### Minor

- **The "no extra data" setting (EvA-E) still requires a validation set to select the erase ratio ε.** The paper states (line 179): "To select the erase ratio ε, we retrain the linear layer with different erase ratio candidates and select the one with the highest accuracy on D_unbiased." For EvA-E on Waterbirds and CelebA, this validation set is unbiased in practice (following prior work). The framing "without any extra data" is therefore somewhat overstated—EvA-E eliminates the need for an unbiased *reweighting* dataset but still uses an unbiased *validation* set for hyperparameter selection. The paper would benefit from clarifying what can be done when even an unbiased validation set is unavailable.

- **The compute comparison ("10 minutes vs. 6 days") is stated without specifics.** The paper does not identify which prior method requires 6 days, under what hardware configuration, or whether the comparison is apples-to-apples. A concrete runtime table comparing wall-clock time for EvA-E, EvA-C, DFR, and at least one full-training baseline on the same GPU would substantiate this claim.

- **The theoretical analysis is informal and empirically unsupported for real data.** Theorems 1 and 2 are explicitly labeled "(Informal)" and rely on a simplified two-layer linear network. The core assumption (Theorem 2) that spurious features have lower variance than core features (η_spu < η_core) is plausible but unverified for real datasets. The paper acknowledges this (line 164), but the theoretical section does not provide rigorous support—it is better described as intuition. This is not disqualifying for an empirical paper, but the theory should not be presented as formal grounding.

- **The evidence energy derivation (Eq. 6) is presented without a step-by-step justification.** The Taylor expansion approximation that produces the closed-form expression is asserted rather than derived, leaving the reader to fill in the gap between the energy score and the final evidence energy formula. A brief derivation in the paper or appendix would improve clarity.

- **The CMNIST validation target description is confusing.** The paper states (lines 204-206): "if the target feature is color, then the label of validation data is also dependent on the color, and vice-versa." It is unclear how using a validation set that is *also* spuriously correlated with the target feature leads to correct erasure of the non-target feature. The mechanism should be explained more clearly.

- **The data efficiency claim "40% of the extra unbiased data previously required" is ambiguous.** It is unclear whether this means 40% of DFR's data requirement, 40% of the original unbiased dataset, or something else. Concrete numbers (e.g., "EvA-C achieves X% accuracy with N samples, while DFR requires 2.5N samples for the same accuracy") would be clearer.

- **No ablation on the choice of distribution distance for consistency.** The paper uses Wasserstein distance but does not compare with alternatives (KL divergence, MMD, etc.), which is relevant since Wasserstein is expensive on high-dimensional activation distributions.

### Trivial
- The "40% of data" claim and "0.7% of the training set" reference (line 208) have a formatting issue ("$[0.7\%$").
- Minor presentational issues: "fti" typo (line 18), "confilcting" typo (line 173), "over-ftited" (line 18).

## Nice-to-Haves
- An ablation study comparing Wasserstein distance with alternative distribution distance metrics for the consistency measure.
- Analysis of how the erase ratio ε interacts with the number of classes or feature dimensionality beyond Waterbirds.
- A limitations paragraph in the conclusion would strengthen the paper's scholarly positioning.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **"Related work omits several recent debiasing methods"** (Harsh Critic): Removed per hard rules—mentioning missing related works is prohibited since the reviewer cannot verify all relevant literature.
- **"Data generation model (Eq 1-2) is never used in theory or experiments"** (Harsh Critic): Removed as factually incorrect—Section 3.4 explicitly states it "employ[s] data generation mechanism as the same as Section 3."
- **"Integrated gradient analysis not presented"** (Harsh Critic): Removed per hard rules about missing appendix content (likely stripped by parser).
- **"Conclusion lacks self-criticism"** (Harsh Critic): Removed as a generic criticism without concrete anchor.
- **"Figure 3(c) shows sensitivity to ε" framed as a weakness** (Harsh Critic): Re-framed as a minor point about ambiguity in no-validation-set setting rather than a core flaw.

## Novel Insights
None beyond the paper's own contributions. The two reviews converge on the core novelty (evidence energy for spurious feature detection without unbiased data) and the main weaknesses (limited baselines for SOTA claims, presentation of key results in figures rather than tables), but do not surface any fundamentally new perspective on the problem.

## Suggestions
1. **Replace Figure 3 with a comprehensive results table** (or add a table alongside it) reporting absolute accuracy (mean ± std) for EvA-C, EvA-E, and all compared baselines on BAR, Waterbirds, and CelebA. Include both average and worst-group accuracy.
2. **Expand baseline comparisons** to include at least GroupDRO, LfF, and LISA in the with-extra-data setting, and LISA/LNL in the without-extra-data setting, or alternatively cite published results from standardized benchmarks and moderate the "SOTA" claim to match the actual comparison scope.
3. **Clarify the hyperparameter selection protocol for EvA-E** when no unbiased validation set is available, or explicitly state that the method assumes an unbiased validation set for ε tuning.
4. **Provide a concrete runtime comparison table** reporting wall-clock training time for EvA-E, EvA-C, DFR, and at least one full-training baseline on the same GPU hardware.
5. **Tone down the "state-of-the-art" language** in the abstract and introduction to reflect the limited set of baselines actually compared. Replace with more precise claims such as "competitive with or better than DFR, JTT, and DivDis."

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>