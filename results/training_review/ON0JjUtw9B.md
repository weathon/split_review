Now I have all the information needed to verify claims. Let me synthesize the final review.

## Summary

The paper proposes WIN, a LiDAR upsampling network that decouples the standard range view into two orthogonal views—Horizontal Range View (HRV) and Vertical Range View (VRV)—to capture complementary geometric information missed by single-view interpolation. A Contrast Selection Module (CSM) fuses the two views via a probabilistic confidence model instead of binary classification. On the CARLA synthetic dataset, WIN achieves improvements over the baseline ILN (+4.53% MAE, +7.01% IoU) with only 1.7M parameters.

## Strengths

- **Novel variable-view representation that addresses a genuine limitation of single-view interpolation**: The paper clearly identifies that range-view-only interpolation loses geometric information for non-smooth surfaces (edges, ground planes) and proposes decoupling RV into two orthogonal views (HRV and VRV) that capture complementary structure. Ablation in Table 4 confirms that either view alone degrades performance, validating the multi-view design. This is, to my knowledge, the first work to do so in LiDAR upsampling.

- **Probabilistic confidence model for view selection outperforms binary classification**: The CSM models view selection as a confidence estimation problem with Gaussian-based soft labels (Eq. 6–8), avoiding the training instability of hard binary labels that change as branches converge at different rates. Ablation (Table 4) shows the proposed probabilistic loss yields better MAE/IoU than binary cross-entropy, and the design of the asymmetric loss is explicitly justified (Section 3.5).

- **Lightweight architecture with consistent gains across upsampling scales**: WIN adds only +0.4M parameters over ILN (1.7M total) yet achieves the best MAE and IoU on CARLA at single and multiple upsampling scales (Tables 1, 2), with the advantage widening at higher upsampling factors. The two interpolation branches share the same local embeddings and only differ in lightweight MLP weight predictors (Section 3.3), making the approach backbone-agnostic.

## Weaknesses

### Fatal

None.

### Major

- **IPN (Park et al., 2023) is cited as a related implicit LiDAR upsampling method (Section 2.2) but is omitted from all experiments.** The paper claims in the abstract that WIN "outperforms all existing methods in a downstream task" and in the conclusion that it "achieved SOTA performance on both virtual and real-world datasets," yet IPN—an implicit function method that the paper itself describes as related—is never compared against in Tables 1, 2, or 3. Without this comparison, the SOTA claim is unsubstantiated. This is not a request to compare with every conceivable method, but IPN is a directly related implicit method the authors already know and cite; its omission is a selective baseline gap.

- **Incomplete downstream evaluation: Table 3 (depth completion) includes only LIIF, ILN, and WIN, omitting LiDAR-SR and TULIP**, both of which appear in the upsampling comparisons (Tables 1, 2). The paper states "we perform 4× upsampling using all models pre-trained on KITTI raw" and claims WIN "achieves a significant advantage in both MAE and RMSE" over existing methods, but the reader cannot verify this claim against LiDAR-SR and TULIP. Since these methods are already pre-trained on the same KITTI raw data (as used for Tables 1/2), their omission from the downstream evaluation undermines the claim of broader superiority.

### Minor

- **The hyperparameter λ (standard deviation scaling in Eq. 8) is never specified.** The paper writes "λ is a constant" (line 133) but does not report its value, and no ablation studies its sensitivity. Since λ controls the sharpness of the ground-truth confidence labels ĝ, this is a missing implementation detail that affects reproducibility of the probabilistic supervision.

- **Figure 5 compares loss curves of BCE and the proposed L\_g, but these loss functions have different scales and minima.** While the intent (showing that BCE plateaus while L\_g continues to decrease) is understandable, raw loss curves from different loss formulations are not directly comparable. Reporting validation accuracy or selection accuracy (e.g., what fraction of points are assigned to the correct view) would substantiate the claim more convincingly.

- **KITTI train/test split is underspecified.** The paper states "sampled frames randomly from sequences of 2011_10_03 for test, and train all models with other sequences" (line 167). It does not specify which sequences constitute "other sequences" or how many test frames were used. This makes reproduction unnecessarily difficult.

### Trivial

- The paper states "We choose the virtual dataset created by CARLA simulator" for multiple upsampling scales (Section 4.3). The table caption redundantly repeats this. Minor.

## Nice-to-Haves

- **Extension to arbitrary views is mentioned but not demonstrated.** The paper says (line 101) "by using other plane for projection, this algorithm can be extended to arbitrary view." A simple proof-of-concept with a third view (e.g., an oblique plane) would strengthen the "variable-view" claim, though the paper's focus on HRV and VRV is justified by their orthogonality and ease of transformation.

- **Weighted fusion as an alternative to hard selection.** The CSM uses hard selection (Eq. 5: choose HRV or VRV based on G < 1/2). The paper does not discuss or ablate a continuous weighted blend (e.g., g·R_z + (1-g)·R_d). This is a natural alternative but not a required experiment.

- **Selection accuracy metric.** Reporting what fraction of points the CSM correctly assigns to the better view (computed against ground-truth minimum-error choice) would provide a direct, interpretable validation of the CSM's behavior.

## Removed Points

- **Abstract/body mismatch (MAE claim)**: REMOVED. The abstract explicitly states "on the CARLA dataset" for the 4.53% MAE improvement. The critic misread the abstract.

- **KITTI MAE contradiction**: REMOVED. The paper transparently acknowledges that LIIF achieves better MAE on KITTI and explains why ("projection center of KITTI data is not unique... LIIF regresses the distance values directly from the features, making it easy to fit in this incorrect setting"). No inconsistency exists.

- **Interpolation geometry under-explained**: REMOVED. Eq. 3 provides the complete interpolation equations. The divisions by cos v and sin v are standard spherical-to-range-image geometry. The equations, while benefiting from a brief derivation note, are self-contained and reproducible.

- **Loss asymmetry "without justification"**: REMOVED. Section 3.5 explicitly justifies the asymmetric loss design: "when ĝ is greater than (or less than) 1/2, we hope that the loss is 0 when the predicted value g is greater than (or less than) ĝ." This is a clear rationale.

## Novel Insights

The reviews surface an interesting tension: the paper's core contribution—decoupling range-view into orthogonal views to handle different geometric regimes—is genuinely novel and well-motivated, yet the empirical validation has two avoidable gaps (missing IPN comparison, incomplete downstream table) that prevent the paper from earning the SOTA label it claims. Notably, the reviews do not identify any flaw in the method itself or suggest that the core idea is unsound. The gaps are in the *evaluation scope*, not the methodology. This is an unusual pattern: the technical contribution appears solid, but the experimental design undersells and overclaims simultaneously.

## Suggestions

1. **Add IPN to all main experiments (Tables 1, 2, 3)**. This is the single highest-impact fix. If WIN still outperforms IPN, the SOTA claim is credible. If not, the paper should honestly report the comparison and moderate its claims accordingly.

2. **Add LiDAR-SR and TULIP to the downstream depth completion experiment (Table 3)**. Since these models are already pre-trained on KITTI raw, this is a straightforward extension that would complete the evaluation.

3. **Report the value of λ used in the experiments and add a brief ablation** (e.g., λ ∈ {0.01, 0.1, 1.0}) to validate that the probabilistic model is not sensitive to this choice.

4. **Replace or supplement Figure 5** with a more meaningful comparison: report selection accuracy (fraction of points assigned to the correct view) or downstream validation metrics during training, rather than raw loss curves from different loss functions.

5. **Specify the KITTI training sequences and test frame count** in the experimental settings.

## Score and Decision

The paper presents a creatively motivated and well-designed method for LiDAR upsampling. The core ideas (orthogonal views + probabilistic confidence) are novel and supported by ablation studies. However, the two major weaknesses—omission of the cited comparable method IPN and incomplete downstream evaluation—directly undermine the paper's central SOTA claims. These are fixable gaps in evaluation rather than flaws in the method itself. In its current form, the evidence does not support the claimed level of superiority.

The method is sound, the writing is clear, and the contribution is meaningful. The missing baselines are correctable. I lean toward conditional acceptance if the authors can demonstrate in the rebuttal that WIN outperforms IPN and complete the downstream table. Without that evidence, acceptance cannot be justified.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>