Now I have enough information to write the consolidated review. Let me compose it.

## Summary

This paper introduces Recursive Metadata Normalization (R-MDN), a normalization layer that removes confounder effects from intermediate DNN feature representations using recursive least squares. Unlike prior methods (MDN) that require batch-level statistics, R-MDN operates at the level of individual examples, making it compatible with vision transformers and continual learning where confounder distributions change over time. The method is evaluated on synthetic data, ABCD neuroimaging (sex classification), and HAM10000 dermatoscopic image classification, demonstrating reduced correlation with confounders while maintaining competitive accuracy.

## Strengths

1. **Individual-example operation unlocks compatibility with modern architectures and continual learning.** R-MDN processes each example independently via recursive least squares (Section 3), unlike MDN which requires batch-level statistics and pre-computed inverse covariance matrices. This design is validated by successfully deploying R-MDN within a ViT on HAM10000 (Section 4.2.2) — a setting where MDN cannot be applied — and by enabling seamless adaptation across continual learning stages without recomputing batch statistics.

2. **Adapts to changing confounder distributions across continual learning stages without stage-specific networks.** R-MDN's internal state (regression coefficients and inverse covariance matrix) updates incrementally as new data arrives, so a single network suffices across all stages. Table 3 shows R-MDN consistently achieves better forward transfer (FWTd) on the synthetic continual learning benchmark (e.g., FWTd of 0.04 vs. 0.18 for P-MDN on Dataset 2). Table 4 further shows R-MDN variant (C) achieving strong backward transfer (BWT) and accuracy on HAM10000.

3. **Strong generalization to confounder-absent test data.** In the synthetic continual learning experiment (Figure 5), R-MDN maintains near-theoretical accuracy even as confounder intensity drops to zero, while the base model's accuracy falls sharply (~0.83 → ~0.60) and BR-Net/P-MDN also degrade. This demonstrates that R-MDN learns genuinely confounder-invariant features, not just features correlated with the training confounder distribution.

4. **Empirically validated across diverse architectures and modalities.** The paper evaluates on synthetic images (2D CNN), 3D brain MRIs (3D CNN), and dermatoscopic images (ViT). In each setting, R-MDN consistently reduces squared distance correlation (dcor²) with the confounder while maintaining competitive accuracy, demonstrating broad applicability.

5. **Provides a theoretically grounded framework with mini-batch extension and regularization.** The paper derives RLS updates via the Sherman-Morrison rank-1 update (Section 3), extends to mini-batches via the Sherman-Morrison-Woodbury formula (Section 3.1), and adds a regularization term λI for numerical stability (Section 3.3). This improves upon prior methods that are sensitive to batch size (MDN) or require difficult hyperparameter tuning (P-MDN).

## Weaknesses

### Fatal
None.

### Major

None.

### Minor

1. **The justification for linear deconfounding on deep features is incomplete and partially self-contradictory.** The paper motivates linear regression via (1) nonlinear models are hard to interpret and (2) "sufficiently powerful nonlinear models can extract almost any arbitrary variable from the information present in the features" (Section 1). Point (2) actually argues *against* the linear assumption: if features are rich enough, a linear probe may capture only the linearly-predictable portion of confounder influence. While the same linear assumption is made by prior work (MDN), the paper would benefit from engaging with this nuance or providing empirical evidence (e.g., showing that a linear probe can predict the confounder from the features used). **Why it matters:** If the linear assumption fails substantially, the method may remove too little or too much signal, and the claimed invariance is not guaranteed. This is a limitation worth acknowledging, though prior work operates under the same assumption and the empirical results suggest it works in practice.

2. **The claim that R-MDN has the "lowest mean difference between TPR and TNR" in the ABCD experiment (Table 2) needs clarification vis-à-vis BR-Net.** The paper states R-MDN has the lowest TPR–TNR difference among all methods (Section 4.1.2). However, in the static setting, BR-Net is a direct baseline, and its TPR–TNR value should be explicitly compared. If BR-Net achieves a comparable or smaller gap, the claim should be qualified or dcor² should be argued as the primary fairness criterion. **Why it matters:** Without this clarification, the paper's central fairness claim for the ABCD experiment appears potentially incomplete.

3. **BWT/FWT metrics in the HAM10000 experiment (Table 4) are not explicitly defined.** Section 4.2.1 carefully defines BWTd and FWTd for the synthetic continual learning experiment. Table 4 reports "BWT" and "FWT" without stating whether these are the same metrics, absolute versions, or something else. This is a clarity gap that makes the main continual learning experiment harder to evaluate. **Why it matters:** Readers cannot verify whether the metrics are comparable across experiments.

4. **The paper does not discuss limitations of its own approach or situations where R-MDN might underperform.** The related works section identifies limitations of MDN and P-MDN, but the paper does not acknowledge scenarios where linear deconfounding might be insufficient, how the choice of regularization parameter λ affects behavior, or the potential feedback loop where regression coefficients are updated using features being simultaneously modified by the deconfounding operation. **Why it matters:** A balanced presentation would strengthen the paper's scientific credibility, though this is common for conference papers.

### Trivial

1. The generalization claim that "R-MDN maintains consistent performance across all distributions" (Figure 5 caption text in Section 4.2.1) slightly overstates the results; a modest accuracy drop is visible as confounder intensity decreases (the text says "near the theoretical maximum" elsewhere which is more accurate).

2. The "does not need to train a stage-specific network" framing in the introduction (Section 1) is stated as an advantage, but the paper does not explicitly contrast this with how many CL baselines (EWC, LwF, PackNet) also use a single network.

## Nice-to-Haves

- A brief ablation of the regularization parameter λ in the main text (even if full details are in the appendix) would help readers assess robustness.
- Reporting statistical significance (confidence intervals or tests) for key accuracy comparisons in Tables 2 and 4 would strengthen the evidence.
- A brief computational complexity statement (O(d²) per sample/batch) in the main text rather than only in the appendix would aid practical assessment.
- Including a summary of the three synthetic continual learning dataset distributions in the main text (currently only in the appendix) would improve readability.

## Removed Points

These points are flagged to be removed, treat them with caution:
- **Critic's claim that "does not need to train a stage-specific network" is not unique or not supported.** The paper makes this claim in context of confounder-removal methods for continual learning (MDN cannot adapt without recomputation; P-MDN needs per-stage tuning). The critic's objection reflects a misunderstanding of the comparison class. REMOVED.
- **Critic's claim that joint training dynamics (feedback loop) could cause instability.** While technically true, this is an unexplored theoretical concern common to most end-to-end methods. Not a specific weakness of this paper. MOVED to Nice-to-Haves as a suggestion for analysis.
- **Critic's note about "slightly worse absolute deviation for batch size 128" (Table 1).** This is a minor trade-off common in all methods; not a meaningful weakness. REMOVED.
- **Strength Finder's claim about R-MDN achieving the smallest TPR-TNR difference (§4.1.2) is kept but the critic's challenge about BR-Net is unresolved.** Without seeing the embedded table image, both cannot be verified. The issue is preserved as Weakness #2 above.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. In the ABCD experiment (Section 4.1.2), explicitly state the BR-Net TPR–TNR value alongside R-MDN's, and clarify whether dcor² or TPR–TNR gap is the primary fairness criterion. A brief justification for prioritizing one metric over the other would resolve the ambiguity.

2. Define BWT/FWT for the HAM10000 experiment (Table 4) unambiguously, either by referencing the same BWTd/FWTd definitions from Section 4.2.1 or by stating any differences.

3. Add a short limitations paragraph in the conclusion or a separate section, discussing when the linear deconfounding assumption might be stressed (e.g., highly nonlinear confounder-feature relationships) and how the regularization parameter λ influences the trade-off.

4. Qualify the generalization claim in Section 4.2.1 ("R-MDN maintains consistent performance") to more precisely describe the small observed accuracy drop at zero confounder intensity.

## Score and Decision

The paper introduces a well-motivated method (R-MDN) that genuinely extends prior work (MDN) in meaningful directions: individual-example operation, ViT compatibility, and seamless continual learning. The algorithmic design is elegant and theoretically grounded. The experimental scope is broad, spanning multiple architectures and data modalities, and the results generally support the claims.

The weaknesses identified are all minor or cosmetic — none threaten the paper's core contributions. The linear assumption concern is shared with prior work and partially validated by the empirical results. The TPR–TNR comparison needs clarification but does not undermine the overall fairness story given R-MDN's much lower dcor² values. The missing metric definition is a presentation fix.

This is a solid contribution that belongs in the proceedings.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>