- Decision: Reject
- Avg Score: 4.25
- Scores: 5, 6, 3, 3
Now I have thoroughly verified all claims. Let me write the consolidated review.

## Summary

This paper proposes DVCL (Distance-aware Voxel-wise Contrastive Learning) for semi-supervised multi-organ segmentation, addressing a specific drawback of complementary-label-based VCL methods. The key insight is that pushing unreliable voxels away from complementary prototypes can disrupt beneficial semantic relationships among them. Instead, DVCL identifies each unreliable voxel's feature-space neighbors and outsiders, then pulls neighbors together and pushes outsiders apart. The paper also introduces an entropy-based selection module (ESM) for adaptive pseudo-label filtering. Experiments on four multi-organ datasets (FLARE 2022, AMOS, MMWHS, BTCV) with two label ratios (10%, 50%) show consistent improvements over state-of-the-art SSL and VCL methods.

## Strengths

- **Identifies a specific, overlooked drawback of complementary-label VCL**: The paper clearly articulates (Sec. 1, Fig. 1(b)) that pushing unreliable voxels away from complementary prototypes can move originally-close voxels apart and originally-distant voxels together, disrupting useful feature-space structure. This problem is not addressed by prior complementary-label works (Wang et al. 2022c, Du et al. 2023, Feng et al. 2024, Deng et al. 2024).

- **Proposes a well-motivated solution (DVCL) that directly counters the identified drawback**: Rather than using complementary labels, DVCL selects each unreliable voxel's nearest neighbors and furthest outsiders via feature-space cosine similarity (Eq. 13), then pulls neighbors together and pushes outsiders apart (Eq. 14–17). This directly operationalizes the principle "neighbors remain neighbors, outsiders remain outsiders."

- **Consistent and substantial SOTA improvements across four datasets**: Table 1 reports mean Dice gains over the second-best method on all four datasets under both 10% and 50% label settings (e.g., +2.02% on FLARE 2022, +5.28% on AMOS at 10%; +2.53% and +3.84% on BTCV at 10%/50%). The improvements are not isolated to one dataset or label ratio.

- **Ablation confirms each component contributes**: Table 2 shows that removing either EBL or DVCL degrades performance (mean Dice drops from 84.11% to 82.18% without DVCL, and to 78.68% without EBL), with the full method yielding the best results especially on challenging organs (pancreas, adrenal glands).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Loss derivation is unnecessarily opaque and the upper-bound derivation is unclear**: The derivation from Eq. 12 to the final loss (Eq. 17) is convoluted. The likelihood functions in Eq. 14 use a denominator summing over all unreliable voxels (which the paper acknowledges as intractable), and the upper-bound derivation in Eq. 16 is presented in a garbled and fragmentary way (the equation breaks off with "J"). The final loss appears to reduce to something close to a standard contrastive objective between neighbor and outsider sets. The paper would benefit from stating the practical loss directly rather than wrapping it in an incomplete theoretical justification. This is a presentation weakness — the method's core idea is clear but the formalism does not add rigor in its current form.

- **The paper claims neighbors/outsiders are maintained "in the feature space" but provides no direct feature-space analysis**: The central motivation (Sec. 1, Fig. 1(b)) is about preserving feature-space relationships. However, the DVCL loss operates on prediction probabilities p_m, p_n (Eq. 12, 14, 16) rather than features, with the justification "features that are close or distant in the feature space should yield consistent or inconsistent predictions" (line 145). While this connection is reasonable, the paper provides no empirical evidence (e.g., feature t-SNE visualizations, nearest-neighbor retrieval accuracy before/after training for unreliable voxels) that the prediction-based loss actually preserves the claimed feature-space semantics. Adding such evidence would substantially strengthen the core claim.

- **Ablation studies are confined to a single dataset (FLARE 2022, 10% labels)**. While the main results (Table 1) demonstrate generality across four datasets, the component ablations (Tables 2, 3, 4) and hyperparameter analyses are only on FLARE 2022 at 10% labeled ratio. Repeating key ablations (e.g., importance of K/K') on at least one additional dataset would confirm the design choices are not dataset-specific.

- **The comparison with nearest-neighbor VCL methods (Table 4) lacks implementation details**: The baselines (NNCLR variants) are adapted from self-supervised learning to this specific semi-supervised VCL setting, but the paper does not describe how these adaptations were done (e.g., whether they use the same anchor selection, memory bank design, etc.). Without this context, the comparison is hard to interpret.

### Trivial

- **Incorrect time-complexity claim for ESM**: The paper states (line 83) that ESM "reduces the time complexity from O(log N) to O(1)" compared to sorting-based methods. Sorting N items is O(N log N), not O(log N). This is a factual error in a non-central claim. The adaptive thresholding idea is fine; the complexity analysis should simply be corrected.

- **Parsing artifacts aside, the upper-bound derivation (Eq. 16) is incomplete in the extracted text with a stray "J" character**. While this is partly a PDF extraction issue, the equation is also unclear in structure, suggesting the derivation needs cleanup in the original submission.

## Nice-to-Haves

- A small simulation or synthetic feature-space plot demonstrating that complementary labels disrupt semantic neighborhoods (Fig. 1(b) currently uses abstract node diagrams; quantitative evidence would be more convincing).
- Reporting whether improvements are statistically significant beyond standard deviations (e.g., bootstrapped paired tests) would add rigor, though the consistency across four datasets already mitigates this concern.
- A clean, direct statement of the final DVCL loss without the likelihood-ratio derivation would improve accessibility and reproducibility.

## Removed Points

- **"Disconnect between feature-space neighbor selection and prediction-space loss" (harsh critic's Critical Issue #1)**: REMOVED. The paper explicitly justifies this at line 145: "features that are close or distant in the feature space should yield consistent or inconsistent predictions." The neighbor selection uses features; the loss uses predictions under this stated connection. While the paper could provide empirical validation (noted as a minor weakness above), calling it a "disconnect" or "internally inconsistent" overstates the issue. The loss gradients propagate through the shared network, affecting both prediction and feature spaces.

- **"Incorrect and trivial time-complexity claim" elevated to major/critical**: DEMOTED to Trivial. The O(log N) → O(N log N) correction is correct but this is a minor side comment that does not affect the paper's core contribution.

- **"Limited generality of ablation studies" elevated to major**: DEMOTED to Minor. Ablations on a single dataset are standard practice. The main results already demonstrate generality across 4 datasets.

- **"Loss derivation not reproducible" as a fatal flaw**: DEMOTED to Minor. The final loss is clearly stated (Eq. 17), and the core idea is understandable even if the derivation is overcomplicated.

- **Strength Finder's claim about "reduces time complexity from O(log N) to O(1)"**: REMOVED as a supporting strength because the complexity analysis contains a factual error (O(log N) is wrong for sorting). The adaptive thresholding itself remains a reasonable design choice but should not be sold on incorrect complexity claims.

- **Generic strengths from Strength Finder**: REMOVED any generic formulations. The retained strengths are specific and evidence-grounded.

- **Strength Finder claim about ESM "outperforming fixed-threshold filtering"**: The paper doesn't directly compare against a fixed-threshold baseline (there's no "fixed threshold vs adaptive threshold" ablation). This claim is not empirically supported in the paper as presented; the comparison is against prior sorting-based methods which is a different axis. REMOVED.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a clear tension: the paper's stated motivation (feature-space neighbor maintenance) and its implemented loss (prediction-based) are bridged by a reasonable assumption, but the lack of direct feature-space validation leaves a gap between narrative and evidence. This is a useful observation for the authors but does not constitute an independent insight beyond what a careful reader would note.

## Suggestions

1. Present the final DVCL loss (Eq. 17) directly and simply, without the likelihood-ratio upper-bound derivation or at least with a much clearer derivation in the appendix.
2. Add feature-space visualizations (e.g., t-SNE of unreliable voxels before/after training, comparing DVCL vs. complementary-label VCL) to directly support the claim that neighbor/outsider relationships are preserved.
3. Correct the time-complexity statement: sorting-based thresholds are O(N log N), not O(log N).
4. Report how the NNCLR-based baselines in Table 4 were adapted to the semi-supervised VCL setting.
5. Include at least one key ablation (e.g., K/K' sensitivity, component importance) on a second dataset (e.g., AMOS at 10%) to rule out dataset-specific tuning.
