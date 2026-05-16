Now I have all the information I need. Let me synthesize the final review.

## Summary

This paper tackles novel class discovery (NCD) in point cloud semantic segmentation, extending prior work (NOPS) that assumed equal class sizes. The authors propose (1) an **adaptive self-labeling** strategy using semi-relaxed optimal transport with a data-dependent annealing schedule for the regularization weight γ, and (2) a **dual-level representation** that incorporates regional consistency (via DBSCAN + average pooling) alongside point-level predictions. The method achieves substantial improvements over NOPS on SemanticKITTI and SemanticPOSS (+12.7 points novel mIoU on split 0 of SemanticPOSS), and the ablation study demonstrates incremental contributions from each component.

## Strengths

1. **Adaptive regularization for imbalanced pseudo-labels is convincingly effective.** Table 5 (tab:gamma_analysis) shows that the proposed data-dependent annealing of γ achieves 44.2 mIoU on split 0 of SemanticPOSS, which is **8.2 points higher** than the best fixed γ (36.0) and far exceeds step decay (max 34.6) or cosine annealing (max 36.1). This directly validates the paper's central algorithmic claim that adaptively relaxing the uniform prior improves pseudo-label quality for imbalanced classes.

2. **Dual-level representation with regional consistency provides clear incremental gains.** Table 3 shows that adding the region-level branch on top of imbalanced self-labeling + adaptive regularization raises split 0 novel mIoU from **44.2 to 48.4** (+4.2 points), and the confusion matrices (Fig. 4) confirm that the region branch reduces fragmentation and improves classification for both head and tail classes. The spatial smoothness prior is well-motivated for point cloud data.

3. **State-of-the-art results across two challenging benchmarks with large margins.** On SemanticPOSS (Table 1), the method outperforms NOPS on all four splits (e.g., +12.7 on split 0, +6.2 on split 1). On SemanticKITTI (Table 3), gains are +8.6, +3.3, +3.6 on splits 0–2. The improvements are consistent and often large, especially on medium and head classes where the imbalance problem is most acute. Notably, the method achieves these results with a simpler pipeline than NOPS (no multi-head or overclustering).

4. **Practical handling of unknown number of novel classes.** Section 3.4 provides a method to estimate |C^u| using clustering on pre-trained features. Table 6 shows that even when the estimated count (3) differs from the ground truth (4), the method still achieves 53.47 mIoU vs. NOPS's 31.95 — a large margin that demonstrates robustness to this realistic uncertainty.

5. **Comprehensive ablation and hyperparameter analysis.** Section 4.3 systematically decomposes the contribution of each component (Tables 3, 5) and provides a principled indicator-based strategy (Eq. 8) for selecting ρ and T, with empirical validation showing the indicator correlates well with final performance (Figs. 7–8).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **No multi-run statistics reported.** All main results and ablations are reported as single runs without standard deviations or confidence intervals. Novel class discovery in point clouds is known to be sensitive to initialization (clustering seeds, prototype initialization, random augmentations). While single-run evaluation is common in this sub-field, the large reported margins (e.g., +12.7 points) would be substantially more convincing with mean and std over at least 3 seeds.

2. **The ablation baseline discrepancy with NOPS is not explained.** The first row of Table 3 (equal-size constraint baseline) achieves 31.8 on split 0, while NOPS achieves 35.7 on the same split (Table 1). Both use a uniform/equal-size OT constraint, so the 3.9-point gap suggests implementation differences (e.g., two-view exchange, prototype classifier, or other pipeline components). The paper does not discuss this gap. Since the ablation measures ISL's 4.2% improvement against this baseline rather than against NOPS directly, readers cannot fully disentangle whether the benefit of semi-relaxed OT would be additive atop a stronger reproduction of the prior method.

3. **Two-view exchange is described only in the figure caption, not in the main text.** The exchange of pseudo-labels between two augmented views (Figure 1) is a non-trivial component of the training pipeline. It should be explained in Section 3 (Method) rather than only in the caption. Furthermore, it is never explicitly stated whether *all* ablation variants (including the "baseline" row in Table 3) use the two-view exchange. While the implementation details (line 198) describe the two-view augmentation as part of the general setup, making this explicit would eliminate ambiguity.

4. **DBSCAN recomputation frequency is not specified.** The paper states regions are "pre-computed" (line 22) but also says "during training, we first utilize DBSCAN" (line 93). It is unclear whether DBSCAN is run once before training or re-computed every epoch. This affects both computational cost and the region branch's ability to correct mistakes from earlier epochs. It is a detail needed for reproducibility.

5. **Algorithm 1 (semi-relaxed OT) lacks derivation for the scaling update.** The parameter `f = γ/(γ+ε)` appears without justification; readers unfamiliar with the generalized Sinkhorn for semi-relaxed OT (Chizat et al. 2018) will not be able to reproduce it. Adding a brief derivation or a reference to the specific equations would improve reproducibility.

### Trivial
- The claim that "the indicator provides a balanced evaluation" (line 175) would benefit from a brief intuitive justification beyond the empirical correlation plots.

## Nice-to-Haves

- A controlled ablation that replaces the paper's semi-relaxed OT with NOPS's exact uniform OT (while keeping all other components identical) would cleanly isolate the benefit of the imbalanced formulation. This is the cleanest way to address the baseline discrepancy.
- Reporting multi-run statistics for the main comparisons and key ablations.
- Clarifying whether the point-level and region-level self-labeling branches should use different annealing schedules for γ (since they operate at different granularities).

## Removed Points

- **Two-view exchange as an uncontrolled confound**: The harsh critic claimed the two-view exchange "likely uses only a single view" in the baseline and thus confounds the ablation. The paper's implementation details (line 198) describe the two-view augmentation as part of the **general** training pipeline ("we set the voxel size as 0.05 and utilize the scale and rotation augmentation to generate two views"), which applies to all experiments. There is no evidence the baseline excludes it. The critic's claim is speculative. However, the paper should be *explicit* about this — kept as Minor #3 above but downgraded from the critic's framing as a "structural issue."
- **Hungarian matching bias speculation**: The critic's concern that Hungarian matching "could be biased toward methods that produce more fragmented clusters" is speculative and unsupported by any evidence in the review. Removed.
- **"Missing parts and places to improve" section's repetition**: Many of these (e.g., multi-run stats, two-view description) are already captured in Minor weaknesses above.
- **"Deeper limitations" suggested by the critic** (DBSCAN may not align with semantic boundaries, known class annotation cost): These are speculative extensions that go beyond the paper's stated scope. The paper openly acknowledges its problem setup limitation (line 506). Removed as scope creep.
- **Pure formatting/presentation nitpicks** from the section-by-section notes.

## Novel Insights

The reviews surface two key observations not fully articulated by the paper itself. First, the data-dependent annealing schedule for γ (Eq. 7) is notable because it uses the KL divergence term — which is *part of the optimization objective* — as a training-progress signal. This is a cleaner feedback mechanism than epoch-count-based schedules, and the comparison showing it beats step decay and cosine annealing by ~10 points is compelling evidence that model-aware regularization schedules are valuable for self-labeling. Second, the interaction between the two-level representation (point + region) and the imbalanced OT formulation is synergistic: the region-level branch addresses the fragmentation problem that becomes more acute when the OT constraint is relaxed, which the confusion matrices (Fig. 4) illustrate but the paper does not explicitly discuss as a design motivation.

## Suggestions

1. Add a controlled variant that uses the **exact uniform OT** from NOPS (fixed γ→+∞) within the paper's full pipeline (two-view, prototype classifier, region branch). This would directly isolate the benefit of the semi-relaxed + adaptive formulation and address the baseline discrepancy question.
2. Explicitly state whether DBSCAN regions are computed once or per epoch, and whether all ablation variants use the two-view exchange.
3. Report mean and standard deviation over at least 3 random seeds for the main comparison tables and key ablations.
4. Move the two-view exchange description from the figure caption into the main method text (Section 3).

## Score and Decision

The paper presents a well-motivated method for an important problem (NCD in imbalanced point clouds) with two cleanly novel components (adaptive γ-annealing for semi-relaxed OT, dual-level representation) that are each validated by ablation. The SOTA results are substantial and consistent across two benchmarks. The weaknesses are all addressable in revision — none threaten the core claims. The paper makes a clear contribution.

MY FINAL SCORE: <pineapple>8.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>