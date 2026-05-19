- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 8, 6, 6
Now I have all the evidence I need. Let me compose the consolidated review.

---

## Summary

SEED proposes an exemplar-free class-incremental learning method that maintains a fixed-size ensemble of K experts (shared backbone), selectively fine-tunes only one expert per task based on KL divergence between Gaussian class distributions, and performs ensemble Bayes classification at inference. The key ideas are: (1) training only one expert per task to reduce forgetting and naturally diversify the ensemble, and (2) selecting which expert to train based on which latent space best separates the new classes (via multivariate Gaussian overlap).

## Strengths

- **Selective expert training naturally diversifies the ensemble.** By design, each expert is fine-tuned on a different subset of tasks, which creates specialization without an explicit diversity loss. Figure 4 shows experts consistently outperform their own average on the tasks they were selected for (by >2.5 pp), and the ensemble outperforms the best individual expert, confirming genuine complementarity. This is a clean architectural contribution.

- **KL-divergence-based expert selection is validated against alternatives.** Figure 6 compares KL-max selection against random, round-robin, and KL-min across 10 random class orders on CIFAR-100 T=20 and T=50. KL-max achieves higher mean and median average incremental accuracy, establishing that the selection mechanism itself — not just the ensemble structure — drives improvement.

- **Full-covariance Gaussian representation is shown to be an essential component.** The ablation study (Table 4) shows that replacing the multivariate Gaussian with a diagonal covariance drops accuracy from 61.7% to 53.5%, and using only mean prototypes (nearest-mean classifier) drops to 54.1%. This clean ablation validates the design choice.

- **Comprehensive evaluation across three scenarios (equal-split, large-first-task, task-incremental) and three datasets (CIFAR-100, ImageNet-Subset, DomainNet).** The equal-split scenario with DomainNet (345 classes across 6 domains) tests domain shift, which goes beyond standard CIL benchmarks.

## Weaknesses

### Fatal
None.

### Major

- **Headline results conflate the ensemble advantage with the selection mechanism's contribution.** The main comparison (Table 1) pits SEED (5-expert ensemble) against single-model baselines, and the paper emphasizes the 14.7–17.5 pp gaps (e.g., "SEED outperforms other methods by a large margin in each setting"). However, the ablation in Table 4 shows that a *standard* 5-expert ensemble (experts trained sequentially on all tasks with uniform averaging) already achieves 56.9% on CIFAR-100 T=10 — which is 10.6 pp above the best single-model baseline (FeTrIL at 46.3%). SEED's *additional* improvement over the standard ensemble is 4.8 pp (61.7% vs 56.9%). The paper does present this ablation, but only in a separate discussion section; the abstract and results text highlight the 15+ pp margins without separating the (trivial) ensemble effect from the (meaningful but modest) selection effect. This framing exaggerates what the novel mechanism contributes and could mislead a casual reader about the source of the gains.

- **The claim "training does not require more computation than single-model solutions" is misleading.** The expert selection step (Eq. 2) requires forward passes through *all* experts for *all* training examples of the new task to compute class-conditional Gaussians and KL divergences. While the per-iteration gradient update is indeed on only one expert, the one-time selection cost is nontrivial, especially for large datasets or many experts. The contribution list similarly claims "no computational overhead during the training," which is false if the selection step counts as part of training. This claim needs qualification.

### Minor

- **Main results table lacks a single-expert SEED and ensemble baselines.** Table 1 would be much more informative with a row for "SEED (1 expert)" and "Standard 5-expert ensemble" alongside the single-model baselines. The paper does provide this in the ablation (Table 4) and the "Number of experts" analysis (Fig. 7), but placing them directly in the main comparison would allow readers to immediately disentangle the ensemble effect from the selection effect.

- **No reporting of the latent dimension used for the multivariate Gaussians.** The paper mentions reducing the latent space dimension to avoid singular covariance matrices (conclusion, limitations paragraph) but never states the chosen dimension. Since the full-covariance Gaussian is a central component, the reader cannot assess the dimensionality trade-off.

- **Selection variability across different class orders is shown only for the selection strategy analysis (Fig. 6), not for the main results.** Given that selection decisions depend on the data of the current task, and class ordering affects which tasks co-occur, the main results would benefit from variance bars across class orderings (not just across random seeds with a fixed order).

### Trivial
None.

## Nice-to-Haves

- Include ensemble baselines (multiple copies of FeTrIL/LwF trained independently and averaged) in the main CIL table to directly show whether the selection mechanism adds value beyond a generic ensemble.
- Report inference cost (multiplier over single-model forward pass) and total parameter count for all methods in the main CIL results (currently only provided for the task-incremental scenario).
- Analyze selection stability (e.g., how often the same expert is selected across random seeds or class orders).

## Removed Points

These points are flagged to be removed; treat them with caution:

1. "Figure 1 teaser claims SEED is the only method that improves accuracy as tasks increase — this conflates model growth with method performance." — **Removed because**: (a) The paper does not say "only method"; it simply illustrates two CIL setups. (b) SEED has a fixed K=5 experts, not growing over time, so the critic's reasoning about "accumulating experts" is factually incorrect.

2. "KL divergence selection may be unstable with few samples; no analysis of selection reliability." — **Removed because**: Figure 6 provides exactly this analysis — 10 runs with different class orders for KL-max vs alternatives on CIFAR-100 T=20 and T=50. The concern is already addressed.

3. "Data augmentations (AugMix, cutouts) may advantage methods differently." — **Removed because speculative**: The paper explicitly states "We train all methods using random crops, horizontal flips, cutouts, and AugMix data augmentations." All methods receive the same augmentation protocol.

4. "Diversity analysis does not disentangle selection from training order." — **Removed as nitpick**: Selection determines which expert trains on which task; they are inherently coupled. The analysis shows experts specialize, which is the relevant claim.

5. "Plasticity-stability figure X-axis range is narrow for SEED, making comparison less dramatic." — **Removed as trivial**: The range is data-driven; the comparison stands regardless of axis scaling.

6. "Large first task results undercut the claim of universal superiority." — **Removed because**: The paper already acknowledges this explicitly ("The difference between SEED and other methods is noticeably smaller in this scenario than in the equal split scenario") and correctly contextualizes it.

## Novel Insights

The most interesting observation emerging from these reviews — beyond the paper's own contributions — is that the paper's true value is not the 15+ pp headline margin but rather the 4.8 pp improvement of *selective* expert training over *uniform* expert training in an ensemble setting. This is a nontrivial gain: it shows that simply having multiple models is not enough — *which* model you train on *which* data matters. This reframes the contribution from "new SOTA method" to "a well-motivated mechanism for ensemble member-to-task assignment that yields consistent gains over naive ensembling." The paper would be stronger by leading with this decomposition.

## Suggestions

1. **Reframe the headline claim.** Emphasize that SEED's core contribution is a 4–5 pp improvement over a standard ensemble of equal size, rather than the 15+ pp gap over single models (most of which comes from the ensemble structure itself). Place the standard ensemble baseline directly in the main results table (Table 1).

2. **Qualify the computational claim.** Replace "does not require more computation than single-model solutions" with a precise account: per-iteration training cost is comparable, but the selection step incurs a one-time forward pass through all experts per task.

3. **Report the latent dimension** used for Gaussian estimation, ideally with an ablation showing its effect on accuracy vs. numerical stability.

4. **Add a single-expert SEED row to Table 1** to show the method's performance without any ensemble benefit, and add ensemble variants of existing baselines to control for the ensemble advantage.
