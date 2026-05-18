Now I have all the verification I need. Let me write the final consolidated review.

---

## Summary

This paper identifies a novel phenomenon — *local* dimensional collapse in self-supervised learning, where representations span a high-dimensional space globally but collapse in the vicinity of individual points. To address this, the authors propose LDReg (Local Dimensionality Regularization), a theoretically motivated regularizer derived from an asymptotic Fisher-Rao metric for comparing local distance distributions. The theory yields the insight that LID values should be compared on a logarithmic scale and aggregated via the geometric mean. Empirically, LDReg is applied to SimCLR, SimCLR-Tuned, BYOL, and MAE, showing small but generally positive improvements in linear evaluation and transfer learning accuracy.

## Strengths

- **Novel identification of local dimensional collapse as a distinct problem.** The paper convincingly demonstrates (via diagnostic analysis, e.g., Figure 2 and Table 1) that a method like BYOL can have high effective rank (global dimensionality) yet low local intrinsic dimensionality. This goes beyond prior work that studied collapse only at a global level. The synthetic illustration (Figure 1c) and the empirical finding that BYOL's LID drops sharply while its effective rank stays high (Figures 2c–d) are concrete evidence that local and global collapse are separable phenomena.

- **Theoretically grounded Fisher-Rao derivation yielding actionable insights.** The derivation of the asymptotic Fisher-Rao distance (Lemma 1, Definition 2) gives an elegant closed form \(d_{\AFR}(F,G) = |\ln(\IDstar_G/\IDstar_F)|\), which directly implies that LID values should be compared on a logarithmic scale and aggregated via the geometric mean (Theorem 1, Corollary 1). This is a clean theoretical result with implications beyond the specific regularizer — it makes a principled claim about how to handle LID more broadly.

- **Consistent directional gains across four diverse SSL methods.** LDReg improves linear evaluation on ImageNet for SimCLR (+0.5), SimCLR-Tuned (+0.3), BYOL (+0.9), and MAE (+0.6) using standard pretraining setups (Table 1). Transfer learning results with longer training (Table 2, 4096 batch / 1000 epochs) show more substantial gains (e.g., CIFAR-100: 71.6→75.1; Cars: 35.3→41.6). The method is tested across two architectures (ResNet-50, ViT-B) and on object detection / segmentation (COCO, Table 3), demonstrating versatility.

- **Empirical evidence that augmentation strength correlates with LID.** Figure 2b shows that stronger color jitter increases the geometric mean of LID in SimCLR representations, providing a concrete link between augmentation diversity and local dimensionality that helps explain why augmentations prevent collapse.

## Weaknesses

### Fatal
None.

### Major

1. **Ambiguity in which loss variant is used, and an unexplained square root in the L2 form.** The paper defines two variants (L1 and L2) in Section 5 (lines 424–449). The experimental setup (line 462) reports hyperparameter \(\beta\) values but never states whether \(\mathcal{L}_{L1}\) or \(\mathcal{L}_{L2}\) was used for each experiment. Furthermore, the L2 formulation includes a square root: \(\mathcal{L}_{L2} = \mathcal{L}^{\SSL} - \beta\left(\frac{1}{N}\sum_i (\ln\hat{ID}_i)^2\right)^{1/2}\). This square root does not follow from the Fréchet variance derivation earlier (which would give \(\min -\frac{1}{N}\sum_i (\ln ID)^2\) without the square root). The paper provides no justification for this modification. This is a concrete reproducibility barrier — a reader cannot replicate the experiments or know whether the results are driven by the theoretically motivated loss or an ad-hoc variant.

2. **Single-run results with small gains on the main benchmarks lack statistical grounding.** The ImageNet linear evaluation improvements are consistently below 1 percentage point (0.3–0.9pp). No error bars, confidence intervals, or multi-seed statistics are reported. Given that SSL benchmarks at this resolution are noisy at the level of a few tenths of a percent, the reader cannot determine whether these gains are reliable or within noise range. For the 2048-batch-100-epoch setting in transfer learning (Table 2), results are mixed: CIFAR-100 drops 71.2→70.6, DTD stays essentially flat (67.8→67.7). While longer training (1000 epochs) shows more substantial and consistent gains, the core short-training results that form the paper's main claim are not convincingly outside the noise floor.

### Minor

3. **No comparison to a global dimensionality regularizer applied to the same baselines.** The paper's framing contrasts with global approaches ("Rather than directly optimizing the global dimensionality… we propose to regularize the local intrinsic dimensionality," line 21), which naturally raises the question: would a simple global regularizer (e.g., an effective-rank penalty, a covariance off-diagonal penalty in the style of Barlow Twins/VICReg) applied to the same SSL methods produce similar gains? Adding such a comparison would isolate whether the *local* aspect is what drives the improvement, or whether any dimensionality-increasing penalty helps. This is not a fatal omission — the paper's primary claim is that LDReg improves SSL, not that it outperforms all existing regularizers — but it would substantially strengthen the paper's core conceptual narrative.

4. **Gap between asymptotic theory and finite-sample practice not discussed.** The Fisher-Rao derivation assumes the limit \(w\to 0\), yielding a pure power-law form. The experiments estimate LID via the Method of Moments with \(k=64\) neighbors from a minibatch at finite distances. There is no discussion of whether the estimator is consistent with the asymptotic idealization, how the choice of \(k\) affects the alignment between theory and practice, or whether the finite-sample estimates (for a batch of 2048 samples with a 2048-dimensional representation space) are reliable enough to drive gradient-based optimization. This is common practice in LID literature, but the paper's strong theoretical framing makes the omission more salient.

5. **Sensitivity of results to neighborhood size \(k\) is not explored.** Only \(k=64\) is used for all experiments, without any ablation or justification beyond a brief reference to prior LID estimation work (line 462). Given that the asymptotic theory involves \(k\) and the tail length \(w\) both going to zero, and that downstream gradient updates depend on LID estimates computed from varying numbers of batch neighbors, some sensitivity analysis would be informative.

6. **Effective rank increases do not always correspond to accuracy gains.** For SimCLR+LDReg on ViT-B, effective rank jumps from 283.7→326.1 while accuracy moves only 72.9→73.0 (Table 1). For MAE, effective rank nearly doubles (86.4→154.1) but accuracy increases by only 0.6pp. This weakens the paper's implied mechanistic claim that increasing dimensionality *drives* performance improvements. The correlation between the two is not monotonic, and the paper does not discuss this.

### Trivial
None.

## Nice-to-Haves

- Compare LDReg against a global regularizer (e.g., an effective-rank penalty or covariance off-diagonal loss) on the same SSL baselines, to demonstrate that the *local* aspect provides additional value beyond any dimensionality-increasing penalty.
- Report mean and standard deviation over at least 3 seeds for the main experiments (Table 1 and the short-training transfer results).
- Ablate L1 vs. L2 formulations on a representative setting (e.g., SimCLR 100 epochs) and explain the square root in the L2 variant.
- Provide a sensitivity study for \(\beta\) and \(k\) on one setting to show the method is not brittle.
- Report computational overhead of LDReg (nearest-neighbor computation per batch).

## Removed Points

These points are flagged to be removed; treat them with caution.

- None: All of the Harsh Critic's points are factually grounded and relate to real concerns. Some have been downgraded (as described above) where the severity was disproportionate to the actual impact on the paper's claims.

## Novel Insights

The Harsh Critic's most interesting observation is that the paper's own diagnostic evidence partially undercuts its mechanistic narrative: the disconnect between effective rank gains and accuracy improvements (e.g., ViT-B SimCLR: +42.4 effective rank, +0.1 accuracy) suggests that increasing dimensionality alone is not a sufficient explanation for the observed improvements. This opens a direction the paper does not pursue — namely, what *else* LDReg might be doing beyond simply raising dimensionality (e.g., smoothing the loss landscape, improving gradient flow, or affecting the distribution of singular values in a way that effective rank alone does not capture). The paper would be stronger if it acknowledged and addressed this nuance.

## Suggestions

1. **Specify the loss variant clearly.** State explicitly in the experimental setup (line 462) whether \(\mathcal{L}_{L1}\) or \(\mathcal{L}_{L2}\) was used for each experiment, and provide a brief justification for the choice and for the square root in the L2 variant.

2. **Add multi-seed statistics.** Run the main linear evaluation experiments (Table 1) with at least 3 random seeds and report means and standard deviations. This is the single highest-impact improvement the authors could make, as the gains are small enough that single-run numbers are not trustworthy.

3. **Add an ablation comparing against a global regularizer on the same baselines.** Even a simple global dimensionality penalty (e.g., maximizing effective rank or minimizing covariance off-diagonal entries) applied to SimCLR would help isolate the benefit of the *local* aspect of LDReg.

4. **Discuss the theory-practice gap.** Acknowledge that LID is estimated at finite \(k\) and finite distances, and provide some justification for why the asymptotic theory is nevertheless informative for the practical loss. A sensitivity analysis on \(k\) would go a long way.

---

## Score and Decision

**Originality:** Above average. The identification of local dimensional collapse as distinct from global collapse is genuinely novel, even if prior LID work has hinted at similar ideas.

**Importance of research question:** Moderate to high. Dimensional collapse is a well-recognized problem in SSL, and a local perspective offers a useful new angle.

**Claims well supported:** Moderate. The theoretical claims are well-supported by the derivation. The empirical claims are directionally supported but lack statistical rigor and suffer from the loss-formulation ambiguity.

**Soundness of experiments:** Moderate. The experimental design is reasonable (multiple methods, architectures, tasks) but the single-run results and small gains make the conclusions less robust than they could be.

**Clarity of writing:** Good. The paper is well-structured and the theoretical exposition is clear. The loss formulation ambiguity is the main clarity issue.

**Value to research community:** Moderate. The theoretical insights about logarithmic scale and geometric mean for LID are likely to be useful beyond SSL. The method itself provides a modest but consistent improvement.

**Overall:** The paper has genuine contributions — a novel observation about local dimensional collapse in SSL, a clean theoretical derivation of a Fisher-Rao metric for LID, and a well-motivated regularizer that shows consistent if modest improvements across diverse SSL methods. However, the empirical validation has a significant reproducibility gap (which loss variant was used? unreported), lacks statistical grounding, and the central mechanistic claim is partially undermined by the paper's own diagnostic data. The paper would benefit from addressing these issues before publication. In its current form, the strengths are real but the weaknesses prevent full confidence in the results.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>