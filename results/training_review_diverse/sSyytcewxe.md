Now I have a thorough understanding of the paper and can verify each claim. Let me produce the final consolidated review.

## Summary

This paper introduces SEED (Selection of Experts for Ensemble Diversification), an exemplar-free class-incremental learning method that maintains a fixed set of K experts with a shared backbone, but fine-tunes only one expert per task. The expert is selected via a KL-divergence-based criterion that minimizes distribution overlap for new classes. At inference, predictions are formed by ensembling Gaussians from all experts via temperature-scaled softmax averaging. The method achieves large margins over prior work on equal-split CIL scenarios, showing strong plasticity under severe data constraints and domain shift.

## Strengths

- **Selective expert update yields a strong plasticity–stability trade-off in exemplar-free CIL.** Unlike prior ensemble methods that regularize or update all experts (e.g., CoSCL), SEED updates only one expert per task, directly reducing forgetting and encouraging specialization without explicit diversity losses. This is substantiated by Table 1, where SEED outperforms the second-best method by 14.7–17.5 percentage points on CIFAR-100 equal splits, a setting where plasticity is critical. Figure 6 (left) further confirms that SEED achieves a superior forgetting–intransigence trade-off compared to EWC, LwF, and FeTrIL.

- **The KL-max expert-selection rule demonstrably improves ensemble quality over naive alternatives.** The paper proposes selecting the expert where new-class Gaussian distributions overlap least (Equation 2). Figure 6 (selection-strategies) shows KL-max yields higher mean and median accuracy than random, round-robin, and KL-min across 10 runs on CIFAR-100 with T=20 and T=50. This is a principled and empirically validated design choice.

- **State-of-the-art results on equal-split scenarios with substantial margins, including under domain shift.** On CIFAR-100 T=10, SEED achieves 61.7% average incremental accuracy vs. 47.0% for LwF*; on DomainNet T=36 it achieves 39.2% vs. 27.5% for FeTrIL (Table 1). These 14–16 point margins are unprecedented among exemplar-free methods in the challenging equal-split setting where prior methods plateau.

- **Ablation studies cleanly isolate the contribution of each component.** The ablation table (Table 4) shows that removing multivariate Gaussians drops accuracy to 53.5% (from 61.7%), removing covariance to 54.1%, and removing temperature scaling to 59.2%. This rigor strengthens confidence in the method's design choices.

- **Expert diversity arises naturally from the training design.** Figure 5 shows each task has a specialist expert (2.5+ points above average) and the ensemble consistently beats the best individual expert, confirming that diversification through selective training works without ad-hoc diversity losses.

- **SEED outperforms task-incremental methods with fewer parameters despite targeting the harder task-agnostic setting.** On CIFAR-100 20-split, SEED achieves 86.8% task-aware accuracy with 3.2M parameters vs. CoSCL's 79.4% with 4.6M parameters (Table 3).

## Weaknesses

### Major
None.

### Minor

- **The standard ensemble baseline (all experts trained on all tasks) is relegated to the ablation table rather than appearing alongside the main comparisons.** The ablation shows that a standard ensemble already achieves 56.9% on CIFAR-100 T=10 vs. SEED's 61.7%, meaning roughly one-third of SEED's total advantage over single-model methods comes from the multi-expert architecture rather than the selection mechanism. The paper is transparent about this in the discussion section, but placing this baseline in the main results tables (Tables 1 and 2) would allow readers to correctly attribute the gains. As it stands, the primary empirical framing ("SEED vs. single-model methods") conflates architecture scale with the selection contribution.

- **The "no computational overhead" claim in the abstract and contributions list is imprecise.** The selection step (lines 101–105) requires forwarding all new-task data through all trained experts to compute class-conditional distributions and evaluate Equation 1. While the backward pass is indeed limited to one expert, the forward pass for selection adds real computation relative to a single-model baseline. The claim should be qualified (e.g., "no additional backward-pass cost relative to single-model training" or "negligible overhead").

- **The large-first-task comparisons (Table 2) are not fully controlled.** Baselines are taken from the FeTrIL paper with no verification that the training setup (augmentations, learning rate schedule, optimizer settings) matches SEED's protocol. The equal-split setting states that AugMix augmentations are used (line 121), but the paper does not specify whether the same augmentations were applied to SEED in the large-first-task setting or whether the FeTrIL baselines used them. Since SEED's training-based approach benefits more from augmentations than frozen-backbone methods, this could advantage SEED. The concern is partially mitigated by the fact that SEED loses to FeTrIL on ImageNet for T=11 and T=21, but a controlled reproduction of at least one baseline would strengthen the comparison.

- **Table 2 baselines are reported as point estimates without standard deviations, while SEED reports ±σ.** Some of SEED's margins (e.g., CIFAR-100 T=21: 62.9 vs. 61.5) may overlap with baseline variance. This is a common issue when taking baselines from prior work, but it limits the statistical force of the comparison.

### Trivial

- **The latent space dimension S is never reported.** Since SEED relies on full-covariance Gaussian estimation (S×S matrices per class), S directly affects the number of parameters and the sample size needed per class. Reporting S (and confirming per-class samples exceed S for all tasks, or describing how singularities are handled) would aid reproducibility.

- **The DomainNet task construction for T=36 is under-specified.** With 6 domains and 36 tasks, each domain supplies multiple tasks. The paper does not explain whether consecutive tasks always switch domains or whether some tasks share the same domain, which affects the degree of domain shift.

- **The task-incremental experiments (Table 3) do not state whether the same random class order was used for all baselines.** The results would be more reproducible with this detail.

- **The paper does not discuss whether log-likelihoods from different experts are on a comparable scale.** Because each expert's covariance matrices are estimated independently, the log-likelihood magnitudes can differ. Temperature scaling helps but does not fully guarantee calibration. This is a minor unexamined issue.

## Nice-to-Haves

- Quantify the wall-time or FLOP overhead of the selection step for a representative run (e.g., CIFAR-100 T=10) to support or correct the computational cost claim.
- Reproduce at least one large-first-task baseline (e.g., FeTrIL) under SEED's augmentation and scheduling protocol to verify comparison fairness.
- Extend the standard-ensemble ablation to at least one more setting (e.g., DomainNet or ImageNet) to test whether the 4.8% selection benefit generalizes.

## Removed Points

These points are flagged to be removed; treat them with caution.

- Criticism that SEED's ensemble beating the best individual expert "does not uniquely validate SEED's selection scheme" (from Harsh Critic's Discussion section). This is a generic property of many ensembles, but the paper's point is that diversity arises *without* an explicit diversity loss, which is a valid observation. The strength stands; the criticism overreaches.
- Criticisms about the teaser figure (Fig. 1) axis labels not being explained. The figure caption provides context, and minor figure presentation details do not affect the paper's contribution.
- "The paper does not discuss why pairwise summation is chosen over total divergence" — the ablation (Fig. 6) shows KL-max outperforms alternatives, which is sufficient empirical validation. This is an under-exploration, not a weakness.
- "The L2 KD loss is not compared to KL-divergence-based distillation" — an unexamined design choice that does not threaten any claim in the paper.
- "The paper should include a statistical test (e.g., paired permutation test)" — this is not standard practice in the CIL benchmarking literature and standard-deviation reporting suffices.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the important nuance that the standard ensemble baseline accounts for a meaningful fraction (~4.8 points out of ~15) of SEED's advantage over single-model methods, but they do not introduce a fundamentally new perspective not already present in the paper's own discussion section.

## Suggestions

1. **Move the standard-ensemble baseline into the main results tables (Tables 1 and 2).** This allows readers to directly attribute gains to the ensemble architecture vs. the selection mechanism, sharpening the paper's central claim.
2. **Qualify the computational overhead claim** to state that the overhead arises only from the forward passes needed for selection, not from the backward pass.
3. **Specify the latent space dimension S** used in all experiments and document how singular covariance matrices are handled.
4. **Clarify the DomainNet task construction** for larger T values, and the class order used in the task-incremental experiments.
5. **Reproduce at least the FeTrIL baseline in the large-first-task setting** under matched conditions, or add a paragraph explaining which variables differ and their likely direction of effect.

## Score and Decision

The paper presents a novel, well-motivated method with strong empirical validation in the challenging equal-split CIL setting. The weaknesses are primarily about presentation framing and minor experimental control issues rather than fundamental flaws. The core contribution is solid and well-supported.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>