## Summary

This paper studies Multi-Grade Deep Learning (MGDL), which decomposes training a deep network into a sequence of shallow subproblems trained on residuals. It provides convergence theorems for GD applied to MGDL, shows that single-layer ReLU grades yield convex subproblems (via Pilanci & Ergen's convex reformulation), monitors the eigenvalues of the linearized GD iteration matrix to explain MGDL's stability advantages, and benchmarks MGDL against standard end-to-end training (SGDL) on image regression, denoising, deblurring, CIFAR-10/CIFAR-100, and transformer-based time series. MGDL consistently achieves lower loss, better stability, and wider learning-rate tolerance across all tasks.

## Strengths

- **Consistent empirical advantage across a diverse set of tasks and architectures.** MGDL outperforms SGDL on 6 image regression tasks (Table 1, PSNR gains 0.42–3.94 dB), 3 denoising settings at 6 noise levels (Table 2, gains 0.16–4.23 dB), 3 deblurring levels (Table 3, gains 0.85–2.84 dB), CIFAR-100 (loss ~10⁻⁴ vs ~10⁻², Figure 3), and two transformer time-series benchmarks (Tables 4–5, test MSE reductions of 16× and 5×). This breadth strengthens the claim that MGDL's advantages are not architecture- or task-specific.

- **Quantified learning-rate robustness (Section 6, Figure 2).** On synthetic regression, SGDL achieves low loss only for a narrow learning-rate range (e.g., η ∈ [0.03, 0.08] in Setting 1), whereas MGDL maintains low loss over a much wider interval (η ∈ [0.01, 0.3]). This provides concrete evidence supporting the paper's central claim about MGDL's greater robustness to hyperparameter choices.

- **Eigenvalue diagnostic connecting training stability to spectral properties (Section 7).** The paper tracks eigenvalues of I − ηH(W^k) during training and observes that MGDL's eigenvalues remain in (−1,1) while SGDL's exit this range, correlating with oscillatory loss. Figures 4–6 show this pattern across synthetic regression, image regression, denoising, and CIFAR-10. While this analysis is empirical rather than proven, it offers an intuitive and visually compelling explanation for why MGDL trains more stably.

- **Clean convexity observation for single-layer ReLU grades (Theorem 3).** The proof that each grade's nonconvex problem reduces to a convex program (following Pilanci & Ergen 2020) is rigorous and correctly applied. Extending convexification from shallow to deep architectures via the grade-wise decomposition is a conceptually clean framing.

## Weaknesses

### Major

- **No classification accuracy reported for CIFAR-100 (or CIFAR-10), despite claiming "superior accuracy."** The CIFAR-100 experiment (Section 5, Figure 3) shows only training MSE loss curves. This is a classification benchmark where top-1 (or top-5) accuracy is the standard evaluation metric. Lower MSE does not guarantee higher classification accuracy, especially since MSE is not the typical loss for classification. Similarly, the CIFAR-10 experiment (Section 7) reports only MSE loss. Without accuracy numbers, the paper's claim of "superior accuracy" on these datasets is unsubstantiated by the evidence presented. This is the single most consequential gap in the experimental evaluation.

- **Theory-practice mismatch: Theorems 1 and 2 assume σ is twice continuously differentiable, but all experiments use ReLU (σ(x)=max{0,x}).** The paper defines σ as ReLU (line 96), uses ReLU throughout the experiments (line 212), but Theorems 1 and 2 explicitly require σ to be twice continuously differentiable (lines 128, 162). ReLU is not differentiable at 0 and has zero second derivative everywhere else. This gap between the theoretical assumptions and the practical setting is never acknowledged or reconciled. Theorem 4 and the eigenvalue analysis also assume twice/thrice continuously differentiable objectives, while ReLU Hessians are zero almost everywhere in the distributional sense — the paper's mention of "Explicit Hessians for SGDL and MGDL under ReLU are given in the Supplementary Material" (line 315) does not bridge this gap without additional clarification about how the Hessian is defined for non-smooth activations.

- **No error bars, multiple runs, or statistical significance for any experiment.** Every table (Tables 1–5) reports single-run values. Given that neural network training is stochastic (data splits, initialization, Adam noise), it is impossible to assess whether the reported PSNR/MSE differences are statistically reliable. Some PSNR gains are small (e.g., 0.16 dB at noise level 60 for Chest in Table 2), which could easily fall within run-to-run variance.

### Minor

- **The central claim "α_l ≪ α" (Theorem 2) is stated without proof or quantification.** The paper's key theoretical argument for MGDL's robustness is that each grade's Hessian spectral norm α_l is much smaller than SGDL's α, allowing a larger admissible learning rate. However, no bound on α_l relative to α is derived. The statement "α_l ≪ α" (line 170) is a qualitative assertion, not a theorem. The empirical evidence in Section 6 supports the robustness claim, but the theory as presented does not deliver what it advertises.

- **The convexity result (Theorem 3) does not address global optimality of the overall MGDL composition.** The paper correctly shows each grade's subproblem is convex, but MGDL trains grades greedily on residuals of previous (fixed) grades. There is no guarantee — and the paper does not discuss — that this sequential greedy convexification converges to a global optimum of the original deep network. Additionally, the condition m_l ≥ P_l (number of neurons ≥ number of activation regions) is acknowledged but not discussed in terms of practical feasibility; P_l can be combinatorial in the data dimension.

- **Transformer baseline (SGT) tuning is not documented, and the performance gap is unusually large.** On synthetic time series, MGT achieves TeMSE of 0.16 vs. SGT's 2.6 — a 16× gap — while requiring only 28% of the training time. On SPX, the gap is 5×. The paper does not describe how SGT's hyperparameters (learning rate, number of blocks, training duration) were selected, whether it was trained to convergence, or whether the comparison is budget-matched. These are the kinds of gaps that typically arise from undertuned baselines, and the paper should provide evidence that SGT was reasonably configured.

- **No computational budget or FLOP comparison for the image experiments.** Training time comparisons are provided only for the transformer experiments (Section 8). For the core image and CIFAR experiments (Section 5), no runtime or training-time comparison is given, making it difficult to assess practical trade-offs.

### Trivial

- None that survive filtering.

## Nice-to-Haves

- **For the transformer experiments**, a controlled comparison where SGT and MGT are matched on total training compute (FLOPs or time) would be more informative than the current setup where MGT uses 28–33% of SGT's time.
- **A bound (even a loose one) on α_l relative to α** would substantially strengthen the theoretical framing of Theorem 2.
- **Statistical testing or confidence intervals** on the key PSNR comparisons would increase confidence in the results.

## Removed Points

- *"The transformer experiments appear staged against a poorly configured baseline"* (Harsh Critic, point 2). This claim is speculative: the paper does not provide evidence that SGT was undertuned. It is valid to flag the unusual gap as a concern, but the assertion that the baseline was "poorly configured" goes beyond what can be verified from the paper. Moved to Minor (point on undocumented baseline tuning).
- *"The eigenvalue analysis is empirical, not theoretical"* (Harsh Critic, point 5). The paper presents the eigenvalue monitoring as empirical observation, not as formal proof. This is not a weakness — it is an appropriate framing for a diagnostic analysis. The relevant theoretical component (Theorem 4) is a standard fixed-point convergence result.
- *"The convergence theorems are standard"* (Harsh Critic, point 3). While this is true, it is not itself a weakness — the paper's contribution is in applying these to the MGDL setting. The real issue (retained) is the unsubstantiated claim α_l ≪ α.
- *"No standard deviation"* is merged into the Major weakness about no multiple runs/error bars.
- Several formatting/style nitpicks and missing appendix references have been removed per guidelines.

## Novel Insights

The eigenvalue monitoring diagnostic (Section 7) — tracking the eigenvalues of I − ηH(W) during training and observing that MGDL keeps them in (−1,1) while SGDL's exit this range — is the paper's most distinctive finding. It directly connects a measurable spectral quantity to observed training instability and explains why shallower subproblems (each grade) are easier to optimize. This diagnostic could be useful beyond the MGDL/SGDL comparison and applied to other training stability analyses.

## Suggestions

1. **Report classification accuracy (top-1 or top-5) for CIFAR-100 and CIFAR-10.** This is the most impactful fix. Even if the network is trained with MSE loss, accuracy can still be computed from the output. Without this, the claimed "superior accuracy" on classification tasks is unsupported.

2. **Add multiple runs with error bars** for all key experiments (at least 3–5 runs). Many PSNR differences are small and could be within variance.

3. **Acknowledge the smoothness assumption gap between Theorems 1/2 and the ReLU experiments.** Either relax the theorems to cover non-smooth activations (e.g., via Clarke subdifferential) or add a remark explaining that the theorems apply to smooth approximations of ReLU and are used to motivate, not strictly prove, the empirical behavior.

4. **Provide a bound on α_l/α or tone down the claim.** If a rigorous bound is not available, state explicitly that "α_l is empirically observed to be smaller, which we hypothesize follows from the reduced depth of each subproblem."

5. **Document transformer baseline tuning.** Report the learning rate search range, whether the training was run to convergence (validation loss plateau), and the number of SGT blocks used in each experiment.

6. **Add compute cost (training time or FLOPs) for the image experiments** to complement the transformer comparison.

7. **Discuss the limitations of the greedy sequential convexification** — specifically, that per-grade convexity does not guarantee global optimality of the composed MGDL network.

---

## Score and Decision

### Calibration

**Round 1 — Bracketing.** Three queries on related topics:
- Weak anchors (score < 3.5): *"Progressive Coarse-graining and DNNs"* (1.50), *"Mitigating Conflicts in Multi-Task RL"* (2.00), *"Stability-Aware Post-Training Cascade"* (1.50). The paper is clearly stronger than these — unlike them, it contains substantive experiments and some theoretical grounding.
- Mid anchors (3.5–7.5): *"Geometric properties of neural multivariate regression"* (5.50, Reject), *"Deep Progressive Training"* (4.67, Reject), *"LDT: Layer-Decomposition Training"* (4.80, Accept Poster), *"NTK with Convex Two-Layer ReLU Networks"* (4.50, Reject). The paper is comparable to the low-mid papers but weaker than the best of these.
- Strong anchors (>7.5): *"Polar Express"* (8.00), *"SUPER Rotation"* (8.50). The paper is far from this level in terms of rigor, novelty, and experimental validation.

Initial bracket: **4.5–6.0**.

**Round 2 — Narrowing.** Queries inside the bracket:
- Progressive/residual training (4.5–5.5): *"Deep Progressive Training"* (4.67, Reject) — this paper has a similar incremental contribution but tests on larger models (GPT-2). *"Knowledge Distillation for LLMs through Residual Learning"* (5.33, Accept Poster) — more focused on LLMs. *"Physics-informed Residual Flows"* (5.00, Reject) — similar in proposing a residual decomposition of training. *"Sparse training"* (5.00, Reject) — theoretical+empirical.
- Stability/Hessian papers (5.5–7.5): *"Beyond Spectra"* (5.60, Accept Poster) — more novel theory and rigorous experiments. *"Taming Curvature"* (6.00, Accept Poster) — demonstrated on billion-parameter models. *"Saddle-to-Saddle"* (6.00, Accept Poster) — more original theoretical results.

Comparison: The paper's empirical breadth (multiple tasks + architectures) and eigenvalue diagnostic exceed the 4.5–4.8 papers, but its experimental rigor (no CIFAR-100 accuracy, no error bars, theory-practice gap) keeps it below the 5.5–6.0 papers. It is most comparable to *"Physics-informed Residual Flows"* (5.00) and *"Sparse training"* (5.00) in terms of contribution depth and coverage.

**Final score: 5.0.**

<score>5.0</score>
<decision>Reject</decision>