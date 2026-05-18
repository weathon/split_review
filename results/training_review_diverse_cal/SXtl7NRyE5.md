Now I have all the information needed. Let me produce the final consolidated review.

---

## Summary

This paper addresses the underexplored problem of test-time adaptation (TTA) for regression. The key insight is that regression features occupy a low-rank subspace, making naive full-space feature alignment (as used in classification TTA) ineffective or harmful. The authors propose Significant-subspace Alignment (SAL), which uses PCA to detect the meaningful feature subspace and weights dimensions by their impact on the scalar output. Experiments on four regression tasks (SVHN→MNIST, UTKFace with corruptions, Biwi Kinect with gender shift, California Housing) show consistent improvements over baselines adapted from classification TTA.

## Strengths

- **Identifies a genuinely underexplored problem with clear evidence**: TTA for regression is fundamentally different from classification TTA, and the paper provides concrete evidence (Table 1 showing subspace dimensions of ~30–100 vs. 2048 feature dimensions) that regression features live in a low-rank subspace. This observation directly motivates the method.

- **Principled two-component method**: The combination of PCA-based subspace detection (removing degenerated dimensions) and dimension weighting (prioritizing directions that affect the scalar output via the regressor weights w) is clean, well-motivated, and elegantly integrated into the KL-divergence loss (Eq. 7).

- **Consistent empirical superiority across diverse settings**: SAL achieves the highest R² scores across SVHN→MNIST, California Housing, UTKFace (13 corruption types), and Biwi Kinect (6 domain-shift settings). Notably, classification-oriented baselines (BN-adapt, FR, VM, Prototype) often underperform the non-adapted Source, while SAL consistently improves upon it.

- **Thorough ablation study isolating each component**: Table 5 cleanly separates the contributions of subspace detection and dimension weighting. Without subspace detection, performance drops sharply (e.g., on MNIST it falls below Source; on Biwi Kinect it becomes severely negative), confirming both components are necessary.

- **Feature subspace analysis validates the mechanism**: The reconstruction error experiment (Figure 3) demonstrates that SAL preserves the source feature subspace during TTA, while baselines that "break" the subspace produce much larger reconstruction errors, explaining why classification-oriented methods fail.

## Weaknesses

### Fatal

None.

### Major

None. The paper's core claims are supported by the evidence presented, and the identified weaknesses are addressable without invalidating the contribution.

### Minor

- **No error bars or statistical significance reported for any experimental result.** All tables report only point estimates of R² scores. The paper claims SAL "consistently improved the scores" (line 245), but without variance estimates over multiple seeds or runs, it is impossible to distinguish robust improvements from noise. The consistency across many settings (13 corruptions × multiple methods, 6 domain shifts, 2 additional datasets) partially mitigates this concern, but adding error bars (even for a representative subset of experiments) would substantially strengthen the empirical claims.

- **The CLT argument for Gaussianity of projected features is technically imprecise.** The paper (lines 343–351) argues that projected features become Gaussian because each projected element is a sum of terms $a_{i,d}$ across dimensions, invoking the CLT under the assumption that $a_{i,d}$ is "independent of the feature dimension $d$." However, feature dimensions are correlated (the covariance matrix is not diagonal), so the independence assumption required by the standard CLT does not strictly hold. The histograms in Figure 5 provide visual evidence that the projected features are approximately Gaussian, and the method's empirical success does not depend on this theoretical justification. Still, the theoretical framing as presented is weaker than claimed.

### Trivial

- **FR and VM reconstruction errors not quantified.** The caption of Figure 3 notes that FR and VM are not plotted because of "huge errors" but does not specify what "huge" means in absolute terms or discuss why those methods fail so catastrophically.

- **The K determination rule could be stated more concretely.** The paper (line 277) says K can be determined from the subspace rank, but could be more explicit: "set K to the number of eigenvalues explaining 99% of variance" or similar. The ablation (Table 6) already supports this.

## Nice-to-Haves

- Add error bars or confidence intervals (even on a representative subset) to give readers confidence the improvements are not random variation.
- Supplement the visual histograms in Figure 5 with quantitative normality tests (e.g., Shapiro-Wilk) on the projected dimensions to strengthen the Gaussianity claim.
- State the advice for choosing K more explicitly: "set K to the rank of the source covariance matrix, or the number of eigenvalues that explain 99% of the variance."
- Include a brief discussion of whether updating only normalization-layer affine parameters limits adaptation capacity for large shifts (currently only mentioned as an inherited design choice from Tent).
- Add a sentence comparing computational overhead of PCA (one-time) versus the baselines for practitioners.

## Removed Points

These points from the Harsh Critic are removed per the review rules:

- **Baseline modification details deferred to the appendix**: The reviewer criticized that modifications for each baseline (e.g., how Tent's entropy was replaced) are deferred to the appendix. This is removed per hard rules — the parser strips appendix sections from all papers; they exist in the original submission. The main text (lines 213–215) states the baselines and that details are in the appendix.
- **The suggestion to "state the baseline adaptations explicitly in the main text"**: Removed for the same reason — the request amounts to demanding appendix content in the main body, which is not a standard expectation.
- **"The paper does not discuss computational cost or adaptation time"**: This is a nice-to-have, not a weakness. The paper is not required to include runtime analysis for its contribution to be valid.
- **"The failure mode when K is too large is mentioned but not analyzed"**: The paper already notes (line 274) that when K ≥ 400 the loss becomes unstable or diverges. Further analysis is a nice-to-have, not a weakness.

## Novel Insights

None beyond the paper's own contributions. The reviews raise methodological concerns (error bars, CLT justification) but do not contribute novel scientific insights beyond what the paper already provides.

## Suggestions

1. **Add error bars**: Even for a subset of key comparisons (e.g., UTKFace main corruptions, Biwi Kinect), report mean ± std over 3–5 runs with different random seeds. This would address the single most impactful weakness.
2. **Strengthen the Gaussianity claim**: Add a quantitative assessment (e.g., fraction of projected dimensions that pass a Shapiro-Wilk test at α=0.05) to supplement Figure 5's visual histograms.
3. **Clarify K selection**: Explicitly recommend setting K to the rank of the source covariance matrix or the number of eigenvalues explaining ≥99% of variance, and state this is a pre-TTA computation requiring no target access.

## Score and Decision

The paper makes a solid contribution to an underexplored problem. The method is principled, the experiments are reasonably extensive, and the ablations convincingly validate the components. The main weaknesses (lack of error bars, imprecise CLT justification) are addressable and do not undermine the core contribution. The paper is clearly written and appropriately situated within the literature.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>