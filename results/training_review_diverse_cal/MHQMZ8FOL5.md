Now I have all the information needed to produce the consolidated review.

## Summary

This paper proposes a dual-level adaptive self-labeling framework for novel class discovery in point cloud segmentation. The key innovations are (1) a semi-relaxed Optimal Transport formulation with a data-dependent annealing schedule for the regularization weight $\gamma$, which relaxes the restrictive equal-class-size assumption of prior work (NOPS), and (2) a dual-level representation that adds DBSCAN-based region-level consistency to reduce segmentation noise. Experiments on SemanticKITTI and SemanticPOSS show consistent and often large improvements over prior methods.

## Strengths

1. **Novel and well-motivated adaptive regularization for imbalanced pseudo-label generation.** The data-dependent annealing of $\gamma$ (Eq. 7) is clearly motivated by the observation that imbalanced novel classes violate the equal-size constraint. Table 5 shows adaptive $\gamma$ achieves 44.2 mIoU on Split0 versus 36.0 for the best fixed $\gamma$ (0.5), and the paper further compares against step decay (max 34.6) and cosine annealing (max 36.1) schedules, all convincingly outperformed by the adaptive strategy.

2. **Dual-level representation that measurably reduces segmentation noise.** The DBSCAN-based region branch enforces the same prototypes for both point-level and region-level predictions. Table 4 shows adding the region branch on top of ISL+AR improves Split0 novel mIoU from 44.2 to 48.4. The confusion matrices (Fig. 3) and visualizations (Fig. 4) confirm the region branch corrects cases where a single object is fragmented into multiple predicted classes.

3. **Large and consistent empirical gains over SOTA.** On SemanticPOSS (Table 1), the method outperforms NOPS by 12.7%, 6.2%, 3.6%, and 4.7% on the four splits for novel classes. On SemanticKITTI (Table 3), gains are 8.6%, 3.3%, 3.6%, and 0.2%. Under more severe imbalance (Table 2), the method beats NOPS by 7.6% and 5.1%. These margins are substantial for the NCD setting.

4. **Training-set-based hyperparameter selection.** The indicator score $\mathcal{I}$ (Eq. 8) enables hyperparameter tuning without novel-class validation labels. Figures 6-7 show correlation with novel-class IoU, and the chosen parameters ($\rho=0.005$, $T=10$) are robust across a range of values (Tables 7-8).

5. **Robustness to unknown number of novel classes.** Section 3.5 extends an estimation method to point clouds. Table 9 shows that with an estimated $|C^u|=3$ (ground truth is 4), the method achieves 53.47 novel mIoU on Split0 of SemanticPOSS, far ahead of NOPS (31.95).

## Weaknesses

### Major
None. No errors invalidate the core claims.

### Minor

1. **Cross-view pseudo-label exchange is underspecified.** The Figure 1 caption states that pseudo-labels are "exchange[d] between the two views," but the loss function in Eq. 1 ($\mathcal{L} = \mathcal{L}_s + \alpha\mathcal{L}_u^p + \beta\mathcal{L}_u^r$) contains no explicit cross-view term. Algorithm 1 operates on a single input $-\log \mathbf{P}$. It is unclear whether: (a) pseudo-labels from view A serve as targets for view B (and vice versa) within each loss term, (b) the losses are computed independently per view and averaged, or (c) the "exchange" is merely a data-augmentation step performed before pseudo-label generation. This ambiguity is a reproducibility barrier. The authors should explicitly write the cross-view loss formulation.

2. **Ablation baseline vs. NOPS discrepancy.** The ablation baseline (row 1 of Table 3, "equal-size constraints") achieves 31.8 novel mIoU on Split0, while the reported NOPS result (Table 1, Split0) is 35.7 — a 3.9% gap. The paper mentions later (line 253) that NOPS employs "extra training techniques, such as multihead and overclustering," explaining why the simplified baseline is weaker. However, this clarification appears in a different section and is not connected to the ablation study. The ablation should explicitly state that the baseline is a stripped-down version of NOPS without multihead/overclustering, so readers can correctly interpret the component contributions.

3. **GT class distribution result (32.5, Table 5) is mentioned but not explained.** The paper notes this result is "surprising" but offers no analysis. This undermines a simple intuition that adaptive $\gamma$ works by approaching the true distribution — if the true distribution as a hard constraint performs *worse* than fixed $\gamma=0.5$, then the benefit of adaptive $\gamma$ is not merely about matching true class frequencies. Explaining this (e.g., early-training noise makes hard constraints harmful; adaptive $\gamma$ only moves toward imbalance when the model is confident) would turn a puzzling result into a strength of the adaptive design.

4. **No ablation on DBSCAN epsilon.** The epsilon is set to 0.5 so that "95% of the point clouds are included in the region branch learning process" — a heuristic with no sensitivity analysis. Since the region branch contributes 9.1% improvement (Table 3, row 3 vs. row 1), it would be informative to report how performance varies with epsilon (e.g., values in [0.3, 0.7]).

5. **Training time / computational cost not reported.** The method adds DBSCAN computation per point cloud per epoch plus an iterative Sinkhorn solver. Reporting wall-clock time or FLOPs (even a rough comparison to NOPS) would help practitioners assess the practical overhead.

### Trivial
- Inference details: the paper should explicitly state whether the region branch is used at inference time (presumably not, since the model outputs point-level predictions).

## Nice-to-Haves

- A more exhaustive grid search over fixed $\gamma$ values (e.g., a log-scale sweep from 0.01 to 10 with more points) and simple manual decay schedules (e.g., reduce $\gamma$ at fixed epochs). The existing evidence is already strong, but this would make the adaptive $\gamma$ claim completely airtight.
- Demonstrating the indicator score's correlation with novel IoU on a second split or the SemanticKITTI dataset would increase confidence that the indicator is generally useful.
- Adapting a 2D NCD method for point clouds as an additional baseline. The paper's focus is point-cloud-specific challenges, so existing comparisons (EUMS, NOPS) are sufficient, but an additional baseline would strengthen the significance claim.

## Removed Points

- **Criticism that adaptive gamma comparison overstates improvement (Harsh Critic Point 2).** The paper already compares against 6 fixed $\gamma$ values (spanning 5 orders of magnitude, 0.01 to +∞), 5 step-decay schedules, and 5 cosine-annealing schedules. Adaptive $\gamma$ convincingly beats all of them. The request for "more exhaustive" tuning is a Nice-to-Have, not a weakness — the existing evidence is sufficient to support the claim.
- **Criticism about computational cost being a weakness.** This is a valid minor observation but belongs in minor/trivial, not among critical issues. Moved to Minor above.

## Novel Insights

The most interesting finding in the review cross-section is the GT distribution result (32.5), which the paper itself flags as "surprising" but does not explain. The harsh critic insightfully suggests that the adaptive method may work *because* it conservatively moves toward imbalance only when the model is confident, whereas hard-constraining to the true distribution forces noisy early predictions to match a precise target, degrading representations. This turns an anomalous result into a coherent argument for why adaptive softening — rather than simply knowing the true distribution — is the actual mechanism driving improvement. None of the other observations go beyond what the paper's own analysis already demonstrates.

## Suggestions

1. **Clarify the cross-view mechanism** by writing the complete loss explicitly (e.g., $\mathcal{L} = \mathcal{L}_s(x, y^s) + \mathcal{L}_s(\hat{x}, y^s) + \alpha[\mathcal{L}_u^p(x, Q^{\hat{x}}) + \mathcal{L}_u^p(\hat{x}, Q^{x})] + \beta[...]$) or state if the "exchange" is simply averaging losses from independently labeled views.

2. **Add a sentence in the ablation section** (Table 3 discussion) noting that the "equal-size" baseline is a simplified NOPS without multihead/overclustering, explaining the 3.9% gap to the full NOPS result.

3. **Analyze the GT-distribution failure case** to turn a puzzling result into a strength: e.g., note that imposing precise imbalance via a hard constraint early in training harms representations because predictions are noisy, while adaptive $\gamma$ waits until predictions stabilize before relaxing toward imbalance.

4. **Add a brief epsilon sensitivity study** (e.g., three values) to demonstrate that the region-level improvement is not heavily dependent on this hyperparameter.

## Score and Decision

The paper makes a meaningful and well-ablated advance in an under-explored setting (NCD for point cloud segmentation). The adaptive regularization and dual-level representation are both clearly motivated, empirically validated, and produce consistent SOTA-beating results across two datasets and multiple splits. The weaknesses are real but minor — primarily about presentation clarity and missing supporting experiments that would strengthen but not invalidate the core claims. The paper is ready for acceptance with minor revisions.

**MY FINAL SCORE: 7.0**
**MY FINAL DECISION: Accept**