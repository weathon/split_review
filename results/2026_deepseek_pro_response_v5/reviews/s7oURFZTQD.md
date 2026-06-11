Now I have good calibration data. Let me synthesize the final review.

**Bracket assessment**: Round 1 placed the paper between roughly 4.5–6.0. Round 2 narrowed this: the paper is clearly stronger than the BCD paper (4.00) and comparable-to-slightly-better than "Convexifying Transformers" (5.00), but weaker than "Multiscale Training of CNNs" (5.75) which has a cleaner theory-practice connection and "Central Flows" (7.00) which is clearly in a different tier.

Final score: **5.0**.

---

## Summary
This paper studies Multi-Grade Deep Learning (MGDL), a staged training paradigm where a deep network is built incrementally: each "grade" trains a shallow sub-network on the residuals of previous grades, with earlier weights frozen. The paper provides three theoretical angles: (i) GD convergence theorems showing MGDL permits wider admissible learning rates, (ii) a convex reformulation when each grade uses a single ReLU hidden layer, and (iii) eigenvalue analysis linking MGDL's stability to iteration-matrix eigenvalues staying within (-1,1). Experiments span image regression, denoising, deblurring, CIFAR-100, CIFAR-10, and time series with transformers, consistently showing MGDL outperforming standard end-to-end training (SGDL).

## Strengths
- **Convex reformulation of deep ReLU networks (Theorem 3)**: The proof that single-hidden-layer ReLU grades reduce the nonconvex MGDL problem to a sequence of convex programs extends the shallow-network convexification of Pilanci & Ergen (2020) to deep architectures through the grade-wise decomposition. The equivalence proof (line 146) is clean and directly substantiates the claim that MGDL "reduces optimization complexity."
- **Consistent empirical improvements across diverse architectures and tasks (Tables 1–5, Section 8)**: MGDL outperforms SGDL on every reported metric — PSNR gains of 0.42–3.94 dB for image regression (Table 1), 0.16–4.23 dB for denoising (Table 2), 0.85–2.84 dB for deblurring (Table 3), and orders-of-magnitude lower loss on CIFAR-100 (Figure 3). The multi-grade transformer (MGT, Section 8) achieves 16× and 5× reductions in test MSE on synthetic and financial time series while requiring only 28–33% of training time.
- **Quantitative learning-rate robustness characterization (Section 6, Figure 2)**: MGDL sustains loss below 0.001 across η ∈ [0.01, 0.3] (a 30× range) vs. SGDL's η ∈ [0.03, 0.08] (~3× range) on synthetic regression. In the high-frequency setting, SGDL diverges for all but η ≈ 0.005 while MGDL remains stable across η ∈ [0.08, 0.3]. This directly supports the robustness claim.
- **Eigenvalue monitoring as a diagnostic tool (Section 7, Figures 4–6)**: The paper explicitly tracks eigenvalues of I − ηH during training and demonstrates a consistent pattern: SGDL's smallest eigenvalues drop below −1, coinciding with loss oscillations, while MGDL's remain in (−1,1). Shown across synthetic regression, image regression, and CIFAR-10.

## Weaknesses

### Fatal
None.

### Major
- **Smoothness assumptions in convergence theory do not match experimental setup**: Theorems 1 (line 70), 2 (line 104), and 4 (line 255) require σ to be twice (or thrice) continuously differentiable. Section 2 (line 36) explicitly defines σ as ReLU, and all experiments (Section 5 onward) use ReLU activations. ReLU has a discontinuous second derivative, so the Hessian-based convergence analysis in Theorems 1–2, the contraction argument in Theorem 4, and the linearized eigenvalue analysis lack formal justification for the networks actually evaluated. The paper never acknowledges this mismatch. This undermines the direct applicability of the theoretical results to the experimental evidence.
- **The central claim α_l ≪ α is asserted without proof (line 112)**: The theoretical advantage of MGDL over SGDL hinges on the claim that each grade's Hessian spectral norm α_l is much smaller than that of the full SGDL network α, yielding a wider admissible learning-rate range. The paper offers no proof, bound, or scaling argument. Each MGDL grade operates on recursively transformed features h_{l-1}^*, and the Hessian norm depends on both the shallow grade architecture and the conditioning of those frozen features — the net effect is not obvious. Without substantiation, this remains an intuition presented as a formal result.

### Minor
- **No comparison to other staged training methods**: The paper cites greedy layer-wise training (Bengio et al., 2006) but never discusses or compares against it. MGDL's specific contribution relative to other staged/decompositional training approaches is unclear. The baseline is always plain end-to-end SGDL without learning-rate scheduling or batch normalization.
- **Eigenvalue analysis demonstrates correlation, not causation (Section 7)**: Theorem 4 only says that IF eigenvalues stay within (−1,1), convergence follows — it does not prove MGDL guarantees this condition. The eigenvalue excursions and loss oscillations co-occur, but the paper does not establish directionality. The paper frames this as "explanation" (line 260), but the evidence supports only correlation.
- **Classification evaluation uses MSE loss with no accuracy reported (Section 5, CIFAR-100)**: CIFAR-100 classification uses mean squared error rather than cross-entropy, and only loss values are reported — classification accuracy is never given. This makes it impossible to assess whether improved MSE translates to improved classification performance.
- **Test-set evaluation in image tasks includes training pixels**: The training set covers 1/4 of image pixels on a regular grid, while the test set includes all pixels (line 156) — meaning test PSNR is partly computed on training data.
- **Convex program intractability not discussed (Section 4)**: P_l, the number of hyperplane arrangement regions, grows exponentially in input dimension and number of data points, making the convex program of equation (8) computationally infeasible for non-toy settings. The paper does not acknowledge this scalability limitation.

### Trivial
- **Figure 3 learning-rate discrepancy**: The figure caption states η = 5 × 10⁻⁵ while the main text (line 225) states η = 5 × 10⁻⁴.

## Nice-to-Haves
- Bridge the activation gap: extend Theorems 1, 2, and 4 to ReLU (e.g., via Clarke subdifferentials) or switch experiments to smooth activations.
- Derive a bound or scaling argument for α_l ≪ α, or explicitly label it as a hypothesis/conjecture.
- Report classification accuracy alongside MSE loss for CIFAR-100.
- Discuss the exponential growth of P_l as a limitation of the convex reformulation.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **HC: "No error bars or variance reporting"** — A generic criticism applicable to many papers. The paper reports full loss curves and PSNR values which provide adequate evidence. Removed as one-size-fits-all.
- **HC: "Small-scale CIFAR-10"** — The paper uses 10K images with fully connected networks deliberately to enable full Hessian computation for the eigenvalue analysis (Section 7). The setting is appropriate for the paper's analytical goals. Removed.
- **HC: "Section 3 notation error"** — The recursive definition uses H_{D_{l-1}} repeatedly for feature extractors from previous grades. This is the intended notation since feature extractors from each grade share the same depth D_{l-1}. Removed as a misreading.
- **HC: "SGDL fails at η near 1 — no practitioner would use this"** — The learning-rate sweep explicitly tests robustness boundaries, not practitioner behavior. Removed.
- **HC: "No limitations section"** — Formatting/style concern. Removed as pure formatting.
- **HC: "Hessian computation details for CIFAR-10 not explained"** — The paper uses small networks throughout Section 7 (explicitly reduced to width 48 for image regression). Implementation details for Hessian computation don't undermine the core finding. Removed.
- **SF: "Convergence analysis linking grade-wise shallowness to larger learning rates (Theorems 1–2)"** — Weakened by α_l ≪ α being unsubstantiated. The theorems are correctly stated but their practical relevance depends on an unproven claim. Downgraded from a strength.

## Novel Insights
The convex reformulation (Theorem 3) is the paper's most novel theoretical contribution: by leveraging MGDL's grade-wise decomposition, the authors extend single-hidden-layer ReLU convexification (Pilanci & Ergen, 2020) to deep architectures without requiring explicit regularization terms. The key insight is that MGDL's staged structure naturally isolates each grade as a shallow problem, making the hyperplane-arrangement technique directly applicable at each stage.

## Suggestions
- Either prove a bound for α_l ≪ α or explicitly label it as a conjecture.
- Add a discussion of how the convex program's exponential P_l growth limits practical applicability.
- Report classification accuracy alongside MSE loss for CIFAR-100.
- Consider comparing against at least one staged baseline to better isolate MGDL's specific advantages.

## Score and Decision

### Anchor comparison

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| `2NwHLAffZZ` (Weak Correlations...) | 2.33 | R1 | Significantly weaker — purely theoretical, narrow scope |
| `NbbsRnPBoS` (Faster GD in Deep Linear Nets) | 2.33 | R1 | Significantly weaker — theory-only, limited contribution |
| `n2RIkaf1S4` (BCD for Neural Networks) | 4.00 | R1 | Weaker — has proof errors, circular arguments, limited empirics |
| `ATCanNIk1H` (Initializing Layer-wise LR) | 3.67 | R1 | Weaker — narrower scope, less theoretical depth |
| `zA0oW4Q4ly` (Compelling ReLU Networks) | 6.00 | R1 | Slightly stronger — cleaner theory-practice connection, more novel core idea |
| `R9W6fFlr8W` (Primal-dual for Image Reconstruction) | 5.00 | R1 | Comparable — convex reformulation + image experiments, but narrower scope |
| `sIE2rI3ZPs` (Central Flows) | 7.00 | R1 | Significantly stronger — novel theoretical framework, extensive validation |
| `fw1oizreEF` (Convexifying Transformers) | 5.00 | R2 | Comparable — similar convex reformulation approach with theory-practice gaps |
| `n0YCAMVh8b` (Multiscale Training of CNNs) | 5.75 | R2 | Slightly stronger — cleaner theory-practice connection for the proposed method |
| `PCTqol2hvy` (Characterizing ResNet's UAC) | 6.25 | R2 | Stronger — tighter theoretical results with clear practical implications |

**Round 1 bracket**: 4.5–6.0, based on comparison against strong-reject (2.33), weak (3.67–4.00), middle (5.00–6.00), and strong (7.00–8.00) anchors.

**Round 2 narrowing**: The paper is closest to "Convexifying Transformers" (5.00) — both offer convex reformulations of deep architectures with theory-practice gaps and somewhat limited experimental validation — but our paper has broader empirical coverage. It is notably weaker than "Multiscale Training of CNNs" (5.75) which has a tighter theory-practice coupling. The two major weaknesses (smoothness-ReLU mismatch and unsubstantiated α_l ≪ α) prevent the paper from reaching the 6.0+ range occupied by papers with cleaner theoretical contributions. The paper lands at **5.0**.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>