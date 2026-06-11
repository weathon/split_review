Now I have a well-calibrated picture. Let me synthesize the comparisons:

- **"Can Stability be Detrimental?" (4.20):** Directly comparable — studies GD stability and Hessian eigenvalues. Reviewers found claims inadequately supported by evidence and theory limited to toy models. Our paper is stronger: more empirical breadth, more systematic eigenvalue analysis, and additional theoretical contributions (convergence theorems, convex reformulation).

- **"Primal-dual algorithm for variational image reconstruction" (5.00):** Clean theory→experiment alignment with convex reformulation and primal-dual solver. Reviewers dinged it for limited baselines and simple architectures. Our paper has broader empirical scope but worse theory→experiment integration (Adam vs GD gap).

- **"Multiscale Training of CNNs" (5.75):** Strong theory-experiment coherence, novel architectural contribution. Our paper is below this in internal coherence.

- **"Progressive Subnetworks" (5.75):** Polished stagewise training paper with clear results. Our paper has more theoretical ambition but worse execution.

Our paper's genuine strengths (eigenvalue mechanism, learning-rate robustness, empirical breadth, convex reformulation) are offset by identifiable gaps (Adam/GD disconnect, Hessian/ReLU issue in theorems, missing CIFAR-100 test accuracy). It lands above the stability paper (4.20) but below the cleaner 5.0-level papers due to the theory-experiment misalignment.

**Final score: 4.5**

---

## Summary

This paper provides theoretical and empirical analysis of why Multi-Grade Deep Learning (MGDL) — a staged training paradigm that builds deep networks incrementally by fitting shallow sub-networks to residuals — outperforms standard end-to-end (single-grade) training. The main theoretical contributions are convergence guarantees for gradient descent under MGDL, a convex reformulation result for MGDL with single-layer ReLU grades, and an eigenvalue analysis showing that MGDL keeps the GD iteration matrix spectrum within (−1, 1) while SGDL eigenvalues escape this range, directly explaining observed loss oscillations. Empirically, MGDL is evaluated against SGDL on image regression, denoising, deblurring, CIFAR-100 classification, and time-series forecasting with transformers, consistently showing superior stability and accuracy.

## Strengths

- **Eigenvalue-based mechanistic explanation (Section 7):** The paper identifies a concrete, testable mechanism for MGDL's stability advantage: eigenvalues of I − ηH_F remain within (−1, 1) for MGDL but fall below −1 for SGDL, causing loss oscillations. This pattern is replicated across synthetic regression (Figure 4), image regression (Figure 5), image denoising, and CIFAR-10 classification (Figure 6) — providing converging evidence across diverse settings.

- **Learning-rate robustness empirically quantified (Section 6):** A systematic sweep of learning rates shows MGDL sustains low loss over intervals roughly an order of magnitude wider than SGDL. On a high-frequency synthetic target, SGDL converges only at η ≈ 0.005 and diverges elsewhere, while MGDL remains stable with loss < 0.01 across η ∈ [0.08, 0.3] — a practically significant difference.

- **Empirical breadth across architectures and tasks:** The paper validates MGDL on fully connected networks, CNNs, and transformers, spanning image reconstruction (Tables 1–3), CIFAR-100 classification (Figure 3), and time-series forecasting (Tables 4–5). The Multi-Grade Transformer results on SPX financial data are particularly striking: MGT achieves test MSE of 1.8×10⁻² vs 8.9×10⁻² for SGT while using 33% of the training time (Table 5), and maintains accuracy under distribution shift where SGT collapses (Figure 8).

- **Convex reformulation for multi-grade ReLU networks (Theorem 3):** The paper proves that when each MGDL grade is a single hidden-layer ReLU network with sufficient neurons, the nonconvex optimization decomposes into a sequence of convex programs. This extends the single-network convexification of Pilanci & Ergen (2020) to deep architectures through MGDL's staged structure.

- **Training efficiency on CIFAR-10:** With full-batch GD, MGDL achieves a lower loss (2.56×10⁻³ vs 7.16×10⁻³) in less time (22,177 s vs 26,878 s) than SGDL, challenging the intuition that staged training must be slower.

## Weaknesses

### Fatal

None.

### Major

- **Theory–experiment disconnect: Theorems are for gradient descent, but Section 5 results use Adam.** The convergence guarantees (Theorems 1–2), the eigenvalue analysis (Section 7), and the linearized GD iteration (Theorem 4) are all built around gradient descent dynamics. However, the main experimental section (Section 5, line 154) covering image regression, denoising, deblurring, and CIFAR-100 classification uses the Adam optimizer. Adam's adaptive per-coordinate learning rates and momentum are not governed by the Hessian spectral properties that underpin the paper's theoretical explanation. Sections 6 and 7 do use GD and independently demonstrate the claimed advantages, but the Section 5 Adam-based results — the largest set of empirical comparisons — are not directly explained by the theoretical framework. The paper should at minimum acknowledge this limitation explicitly.

- **Theorems assume twice-differentiable activations, but ReLU is used throughout.** Theorems 1, 2, and 4 explicitly require σ to be twice (or thrice) continuously differentiable (lines 52, 70, 104, 255), yet the paper standardizes on ReLU (lines 36, 154) and computes Hessians for ReLU networks in the eigenvalue analysis (Section 7). For piecewise-linear ReLU networks with squared loss, the ordinary Hessian is zero almost everywhere, which would make the eigenvalue analysis vacuous (all eigenvalues of I − ηH_F would be identically 1). The paper states that explicit Hessians under ReLU are given in the Supplementary Material (line 257), but this central component of the paper's explanation should be addressed in the main text — at minimum specifying what matrix is actually computed (e.g., Gauss–Newton, generalized Hessian) and why the spectral interpretation remains valid.

- **CIFAR-100 results report only training loss, not test accuracy.** For a classification benchmark, the standard metric is test accuracy. Figure 3 shows only training loss curves. The paper claims "MGDL delivers superior accuracy" (line 225) based solely on lower training loss, but lower training loss does not guarantee better generalization — it could reflect overfitting. Without test accuracy, the CIFAR-100 results do not substantiate the claimed accuracy advantage for classification.

### Minor

- **α_l ≪ α is asserted without proof or measurement (line 112).** The claim that MGDL's shallower subproblems yield a smaller Hessian spectral norm is central to the theoretical story about wider stable learning-rate intervals. But α_l and α depend on weight magnitudes, data scaling, and network width — not just depth. The paper provides no bound, scaling argument, or empirical measurement to support this claim. The empirical results in Section 6 are consistent with it, but the theoretical link remains undefended.

- **Theorem 3's convex reformulation requires impractical conditions.** The condition m_l ≥ P_l where P_l is the number of ReLU activation patterns can be as large as O(N^{d_l}), making the convex program (8) intractable for any nontrivial problem. The paper's framing as "extending convexification from shallow to deep architectures" (line 148) is true in a theoretical sense, but the result's practical significance is substantially narrower than suggested.

- **Transformer section (Section 8) is not connected to the theoretical framework.** The eigenvalue analysis, convergence theorems, and convex reformulation are not extended to transformers. While the empirical MGT results are compelling, this section reads as a separate empirical study appended to a theory paper. The paper's title promises a unified explanation for why MGDL outperforms SGDL, but transformers receive no such explanation.

- **MSE loss for CIFAR-100 classification is non-standard and unmotivated.** Classification with MSE is known to be suboptimal compared to cross-entropy. The paper does not justify this choice, limiting the relevance of the classification results to standard practice.

### Trivial

- The Picard iteration framing in Section 7 (line 251) treats ∂F/∂W as a linear operator applied to W^k, but the gradient is a nonlinear function. The subsequent Taylor expansion clarifies the intended meaning, but the initial framing is imprecise.

## Nice-to-Haves

- The paper would benefit from discussing per-grade learning-rate selection versus SGDL's single learning rate. If MGDL benefits from per-grade tuning while SGDL uses a single rate, the comparison may embed an implicit hyperparameter advantage that should be acknowledged.
- Discussing the relationship to classical greedy layer-wise training (Bengio et al., 2006) and progressive growing in more depth would better contextualize MGDL's novelty.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Architectures for CNNs are referenced via equations 28–29, which appear to be in the stripped appendix"** — Removed per rule: do not flag missing appendix content.
- **"The training details are in the stripped appendix (Appendix C)"** — Same rule.
- **"CIFAR-10 experiment uses only 10,000 images with fully connected networks... far from standard practice"** — The eigenvalue analysis with full-batch GD requires computationally tractable Hessian computation; using a subset is a reasonable setup for this analysis. Furthermore, this criticism applies to almost any paper doing eigenvalue analysis with full-batch GD — it is a generic "test on larger datasets" complaint.
- **"No discussion of how learning rates are chosen for each grade"** — MGDL inherently uses per-grade optimization; the empirical learning-rate robustness is explored in Section 6. This criticism is speculative.

## Novel Insights

The paper's eigenvalue analysis (Section 7) provides a genuinely novel mechanistic lens on why staged training is more stable: by decomposing a deep network into shallow subproblems, MGDL keeps the eigenvalues of the GD iteration matrix I − ηH within (−1, 1), while end-to-end training pushes eigenvalues outside this range, causing the loss oscillations commonly observed in deep network training. The cross-setting replication of this pattern (synthetic, image, classification) strengthens this as a potentially general principle rather than a dataset-specific observation.

## Suggestions

- Run the Section 5 experiments (or a representative subset) with GD/SGD rather than Adam, so that the theoretical framework directly applies to the primary empirical results. Even a smaller-scale GD version of image regression and denoising would bridge the theory–experiment gap.
- Add a paragraph in the main text explaining what Hessian-like matrix is used for ReLU networks in the eigenvalue analysis (Gauss–Newton? generalized Hessian?) and why the spectral interpretation remains valid despite ReLU's non-differentiability.
- Report test accuracy for the CIFAR-100 experiments to substantiate the claim that lower training loss translates to better generalization.
- Either provide a bound or scaling argument for α_l ≪ α, or empirically measure the Hessian spectral norms α and α_l to support the claim.

## Score and Decision

### Calibration Anchors

| Paper | Path | Avg Score | Round | Comparison |
|-------|------|-----------|-------|------------|
| Faster GD in Deep Linear Networks | NbbsRnPBoS | 2.33 | R1 | Weaker — limited theory and empirical scope |
| Understanding Optimization of Operator Networks | xpmDc76RN2 | 2.33 | R1 | Weaker — narrower scope, less empirical validation |
| Directed Structural Adaptation | ZHTYtXijEn | 2.33 | R1 | Not comparable — different domain |
| Projected Subnetworks Scale Adaptation | WM5G2NWSYC | 2.00 | R1 | Weaker — less theory and empirical breadth |
| Can Stability be Detrimental? | zPaTnGjgpa | 4.20 | R1/R2 | Our paper is moderately stronger — broader empirical coverage, more systematic eigenvalue analysis, additional theoretical contributions |
| Towards Stable Learning in PCNs | FwdN0KovFp | 3.75 | R1 | Our paper is stronger — more empirical breadth |
| Mastering Syntax, Unlocking Semantics | hNkXTqDrfb | 3.75 | R1 | Not directly comparable |
| Tight Stability Bounds for PCNs | OZZYqfplS3 | 4.00 | R1/R2 | Our paper is stronger — more empirical breadth |
| Progressive Subnetworks | ZyH5ijgx9C | 5.75 | R1 | Our paper is weaker — less theory-experiment alignment |
| Early Period of Training | qDFpNXnuYK | 5.00 | R1 | Not directly comparable |
| Sharper Guarantees for NN Classifiers | h7GAgbLSmC | 7.00 | R1 | Our paper is weaker — less theoretical rigor |
| Generalization of Scaled Deep ResNets | tMzPZTvz2H | 7.00 | R1 | Our paper is weaker — less theoretical depth |
| Loss Landscape via Convex Duality | 4xWQS2z77v | 8.00 | R1 | Our paper is substantially weaker |
| Activation Functions in Neural ODEs | AoraWUmpLU | 8.00 | R1 | Our paper is substantially weaker |
| Multiscale Training of CNNs | n0YCAMVh8b | 5.75 | R2 | Our paper is weaker — worse theory-experiment integration |
| Primal-dual algorithm for image reconstruction | R9W6fFlr8W | 5.00 | R2 | Our paper is slightly weaker — comparable empirical scope but worse theory-experiment alignment |
| Feature Learning with One Gradient Step | MY8SBpUece | 5.50 | R2 | Our paper is weaker — less theoretical rigor |
| RNNs with gracefully degrading attractors | iqHh5Iuytv | 4.50 | R2 | Comparable — similar level of theoretical-empirical mix with identifiable gaps |

### Round 1 Bracket: 3.5–5.5

### Round 2 Narrowing: 
The paper is clearly stronger than the 4.20 stability paper (more empirical breadth, additional theory) but weaker than the 5.75 multiscale training paper (worse theory-experiment integration) and the 5.00 primal-dual paper (worse internal coherence). The genuine contributions — especially the eigenvalue mechanism replicated across settings — place it above the rejected 4.0–4.2 range, but the major gaps (Adam/GD disconnect, Hessian/ReLU issue, missing CIFAR-100 metrics) prevent it from reaching the 5.0+ tier where papers have cleaner theory-experiment alignment.

**Final score: 4.5**

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>