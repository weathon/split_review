Now I have a thorough understanding of the paper and can verify the reviewer's claims directly against the source text. Let me write the consolidated review.

---

## Summary

This paper studies how standard data augmentation can hurt tail classes in long-tailed learning, formalizing this as an "intertwined imbalance" (data-wise + augmentation-wise). It proposes Dynamic Optional Data Augmentation (DODA), which maintains a per-class probability distribution over augmentations and dynamically updates it based on class-level positive sample counts. Experiments on CIFAR-100-LT, ImageNet-LT, and iNaturalist 2018 show consistent gains when DODA is plugged into various long-tailed learning methods.

## Strengths

1. **Novel formulation of augmentation-wise imbalance in long-tailed learning.** The observation that class-independent DA introduces a second source of imbalance (augmentation-wise) beyond the standard data-wise imbalance is clearly motivated. Theorems 1–3 formalize why tail classes are disproportionately harmed, moving beyond empirical observations. Figure 2 provides supporting evidence across multiple DA configurations.

2. **Flexible plug-in method with strong empirical results.** DODA consistently improves accuracy when combined with CE, CE-DRW, LDAM-DRW, BS, RIDE, and BCL across three benchmarks (CIFAR-100-LT, ImageNet-LT, iNaturalist 2018). On CIFAR-100-LT IR=100, DODA+BS reaches 45.9% vs. CUDA's 45.1% and CMO's 43.8%. Gains are visible across head/medium/tail splits, not just on tail classes (Table 1).

3. **Interpretable adaptation dynamics.** Figure 5 shows that different classes converge to distinct preferred augmentations during training, and Figure 6 reveals that label-preserving transforms (e.g., horizontal flip) are favored over distorting ones for tail classes. This provides insight into why DODA avoids the "sacrifice" problem.

4. **Superiority over search-based augmentation methods without search overhead.** Figure 7 compares DODA with AutoAugment, Fast AutoAugment, DADA, RandAugment, and CUDA across five backbone algorithms. DODA achieves higher accuracy without requiring a separate search stage, which is a genuine practical advantage.

## Weaknesses

### Fatal
None.

### Major

1. **Inconsistent definitions of positive sample size and underspecified update rule.** The paper gives two conflicting definitions of the positive sample size used for updating preference lists. Line 135 defines ∇_{z_c^k}^{pos} as a sum over the *augmented dataset* (mixed augmentations), while Definition 3 (lines 138–139) defines the same variable as the count when applying a *specific augmentation* to all original samples of that class. The update rule (line 144) compares "the positive sample size from the current epoch" to "that from the previous epoch" and attributes the change to each DA O_c^k used — but if the aggregate definition is used, multiple augmentations contribute to the signal simultaneously, creating a credit-assignment problem. If Definition 3's per-augmentation evaluation is used instead, the mechanism is valid but requires separate forward passes for each augmentation, and the paper should state this explicitly. Additionally, the magnitude of up-weighting/down-weighting (additive vs. multiplicative, step size) is never specified. These ambiguities make it difficult to verify what was actually implemented and whether the update rule behaves as claimed. **This is the most significant weakness and must be resolved for the method to be reproducible.**

2. **Missing comparison with the most directly related baseline (FSR).** The paper cites FSR (Wang et al., 2023) as a "pioneer" in adaptive augmentation for long-tailed learning (line 14), yet FSR is absent from all experimental tables and comparisons. Since DODA is positioned as a class-adaptive augmentation method, FSR is the closest prior work in spirit. Its omission weakens the claim of state-of-the-art performance.

### Minor

1. **"Sacrifice rate" is never formally defined.** The term is introduced in Section 2.1 (line 58) and a key quantitative result is reported in Section 4.3 ("DODA reduces the sacrifice rate by 31% and 24%"), but no explicit formula or operational definition is given. Readers cannot verify or reproduce this metric.

2. **p_aug = 0.5 is fixed across all settings with no sensitivity analysis.** The augmentation probability is a central hyperparameter controlling the method's behavior, yet it is set to 0.5 for all datasets and base methods without any ablation. At minimum, a sweep (e.g., {0.3, 0.5, 0.7}) on one dataset is needed.

3. **The claim of "first theoretical analysis" is overstated.** The paper states "for the first time, we theoretically analyze the gains of traditional augmentation strategies in long-tailed learning" (abstract and contributions). Prior work (FSR, CUDA) already analyzed augmentation effects in long-tailed settings; the novelty is in the specific theoretical framing (level-set bias, augmentation sensitivity), not in being the first to analyze the problem at all. This should be tempered.

4. **No statistical significance beyond CIFAR-100-LT.** Three random trials are reported for CIFAR-100-LT, but no variance or significance is reported for ImageNet-LT or iNaturalist 2018, where results may come from a single run. Given the potential stochasticity in the DODA selection mechanism, confidence intervals would strengthen confidence in the results.

5. **Loose coupling between theory and method.** Theorems 1–4 motivate *that* class-independent DA is harmful and *why* tail classes are more sensitive, but they do not derive or predict the specific DODA update rule. The link is qualitative: Theorem 4 says dominant augmentations have less bias, so the method tracks positive sample size. The update rule itself is described heuristically. This does not invalidate the method but limits the theoretical contribution.

6. **No ablation on warm-up duration.** The 50-epoch warm-up (random selection) is a significant hyperparameter (25% of total training for CIFAR-100-LT). The paper should show sensitivity to this choice (e.g., 0, 20, 50, 100 epochs).

### Trivial

None.

## Nice-to-Haves

- **Comparison with random augmentation selection** as a dedicated baseline (the warm-up phase provides partial evidence, but a full training baseline with always-random selection would isolate the benefit of adaptive selection).
- **Sensitivity to the choice of augmentations in the pool** and to the number of augmentations K. The method's effectiveness likely depends on which augmentations are available.
- **Computational cost comparison** (training time, memory) relative to search-based methods, since the paper claims efficiency advantages.
- **Analysis of convergence behavior** of the preference lists: do they stabilize, and how many epochs does this take?

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"Only four classes shown in Figure 5; a full heatmap for all 100 classes would be more convincing."* — Showing a representative subset of classes is standard practice; demanding 100-class heatmaps is scope creep.
- *"Algorithm 1 (in the appendix, presumably): Cannot be reviewed; assume it exists."* — The appendix was stripped by the parser; this is a known artifact, not an author error.
- *"Missing appendix, missing proofs in appendix, or absent references."* — These are parser stripping issues.
- *"The previous epoch likely used a different set of augmentations... so the comparison conflates changes in the model, changes in the augmentation distribution, and random variation."* — While this noise exists in epoch-to-epoch comparisons, it is a standard heuristic (analogous to REINFORCE-style or bandit updates where the signal is noisy but meaningful over time). The reviewer presents this as fatal noise, but it is a mild concern and depends on the actual implementation. The core ambiguity is already captured in Major Weakness #1.
- *"Formatting nitpicks about the parser artifacts."* — Removed per instructions.
- *"The method may not converge to a meaningful preference ordering."* — Without evidence of non-convergence, this is speculation. The actual trend shown in Figure 5 suggests meaningful convergence. Removed.

## Novel Insights

The reviews surface an important meta-point: the paper's update rule description contains a genuine ambiguity that could affect interpretation of the results. Two definitions of positive sample size are given (line 135: aggregate over augmented dataset; Definition 3: per-augmentation on original samples), and it is unclear which was actually used. This is not a fatal flaw — Definition 3 provides a clean, valid mechanism — but resolving this ambiguity is essential before the paper can be accepted. Beyond the paper's own contributions, the reviews do not reveal additional novel insights.

## Suggestions

1. **Resolve the definitional inconsistency.** Clarify whether positive sample size is computed per-augmentation (Definition 3) or as an aggregate (line 135). If per-augmentation, state that explicitly and note the computational cost. If aggregate, provide a justification or modify the update rule to use per-augmentation counts (e.g., tracking accuracy per augmentation within each epoch via a running buffer).

2. **Specify the update magnitude.** State whether up-weighting/down-weighting is additive or multiplicative, and give the step size or update formula. A simple rule (e.g., multiply selection hierarchy by 1+η for positive, 1−η for negative, then re-normalize) would suffice.

3. **Add FSR as a baseline** to the main experimental tables (or explain why a fair comparison is not feasible under identical settings).

4. **Define sacrifice rate formally** with a clear formula, and specify whether it is computed on the training or validation set.

5. **Add sensitivity analysis for p_aug** across at least one dataset, and ideally for warm-up duration as well.

6. **Temper the "for the first time" language** in the abstract and contributions to reflect that the novelty is in the specific theoretical framing, not in being the first to analyze augmentation effects in long-tailed learning.

## Score and Decision

The paper identifies a genuine problem, proposes a novel and intuitive solution, and demonstrates strong empirical performance across multiple benchmarks. The main weakness is an ambiguity in the method specification (two conflicting definitions of the core update signal) that makes the mechanism difficult to verify — but this is a clarity issue, not a fatal flaw (Definition 3 provides a valid mechanism). The remaining issues (missing FSR baseline, undefined sacrifice rate, limited sensitivity analysis) are addressable. On balance, the contributions are solid and the results are compelling. The paper would benefit from a revision to clarify the update rule, but as presented the core ideas are sound and the empirical evidence is convincing.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>